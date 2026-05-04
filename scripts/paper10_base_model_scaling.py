"""
Paper 10 Task B: Base-model scaling test (quantum-critical definitive test).

Run identical prompt-set on Qwen2.5-base models at different sizes.
Compute per_token_cr, then run autocorrelation + PSD analysis.
Test if commit-timescale and non-Markovian fraction scale with log(params).

Uses Together.ai API with free-tier Qwen2.5 models.
Cost estimate: ~$0.50-2 total for 30 prompts × 6 sizes.
"""
import json
import os
import sys
import time
from pathlib import Path
import numpy as np
from scipy.optimize import curve_fit

# Ensure src/ is on path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from friktionsllm.together_client import TogetherClient
from friktionsllm.friction.cr_utils import compute_cr_from_logprobs

ROOT = Path("C:/_proj/FriktionsLLM")
RESULTS_DIR = ROOT / "data" / "paper10_analysis"
RESULTS_DIR.mkdir(exist_ok=True)
OUTPUT_FILE = RESULTS_DIR / "base_model_scaling_20260424.jsonl"

# Qwen2.5 base (non-instruct) models — together.ai catalog
MODELS = [
    # Standard Qwen2.5 — non-Turbo variants return logprobs reliably
    ("Qwen/Qwen2.5-7B-Instruct", 7.0),
    ("Qwen/Qwen2.5-Coder-7B-Instruct", 7.0),
    ("Qwen/Qwen2.5-72B-Instruct", 72.0),
    ("meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo", 8.0),
    ("meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo", 70.0),
]

# Shorter prompt set — diverse tasks to sample across task-modality
PROMPTS = [
    "What is 2+2? Answer in one word.",
    "The capital of France is",
    "Name one color.",
    "Complete: The sun rises in the",
    "1+1=",
    "What is the largest planet? One word.",
    "Is water wet? Yes or no.",
    "Name a Shakespeare play.",
    "What gas do plants produce? One word.",
    "How many legs does a spider have?",
    "What is Pi to 2 decimals? Use plain digits.",
    "Name a type of bird.",
    "What is the opposite of hot?",
    "Is the Earth flat? Yes or no.",
    "What is 10x10?",
    "Name a mathematical operation.",
    "What is the chemical symbol for gold?",
    "What year is this? One number.",
    "Is fire cold? Yes or no.",
    "Name a famous scientist.",
    "What is the boiling point of water in Celsius?",
    "Name a prime number under 10.",
    "What color is the sky on a clear day?",
    "Name a continent.",
    "What is the theory of relativity?",
    "What is DNA?",
    "Name a programming language.",
    "What is 7 times 8?",
    "Who wrote Hamlet?",
    "What is gravity?",
]


def run_single(client, model, prompt, max_tokens=80):
    """Run one prompt through model with logprobs."""
    try:
        result = client.generate(
            prompt,
            max_tokens=max_tokens,
            temperature=0.7,
            logprobs=True,
            model=model,
        )
        # Extract per_token_cr using canonical util
        stats = compute_cr_from_logprobs(result.token_logprobs)
        per_token_cr = stats.per_token_cr
        return {
            "prompt": prompt,
            "response": result.text,
            "per_token_cr": per_token_cr,
            "n_tokens": len(per_token_cr),
            "latency_ms": result.latency_ms,
            "error": None,
        }
    except Exception as e:
        return {"prompt": prompt, "error": str(e), "per_token_cr": [], "n_tokens": 0}


def main():
    client = TogetherClient()
    if not client.is_available():
        print("ERROR: Together API key not available")
        return

    print(f"Running {len(MODELS)} models x {len(PROMPTS)} prompts")
    print(f"Target max_tokens: 80 each -> expected ~{80 * len(PROMPTS) * len(MODELS)} tokens total")
    print()

    all_results = []
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f_out:
        for model, params_B in MODELS:
            print(f"\n=== {model} ({params_B}B) ===")
            model_results = []
            t_start = time.time()
            for i, prompt in enumerate(PROMPTS):
                r = run_single(client, model, prompt)
                r["model"] = model
                r["params_B"] = params_B
                model_results.append(r)
                f_out.write(json.dumps(r) + "\n")
                f_out.flush()
                if r.get("error"):
                    # ASCII-safe printing
                    err = str(r['error'])[:80].encode('ascii', 'replace').decode('ascii')
                    print(f"  [{i+1}] ERROR: {err}")
                else:
                    resp = str(r['response'])[:60].encode('ascii', 'replace').decode('ascii')
                    print(f"  [{i+1}] n_tok={r['n_tokens']:>3}  resp: {resp}")
            elapsed = time.time() - t_start
            print(f"  {model}: {len(model_results)} results, {elapsed:.1f}s")
            all_results.extend(model_results)

    # Aggregate analysis
    print("\n" + "=" * 78)
    print("Aggregate analysis")
    print("=" * 78)

    by_model = {}
    for r in all_results:
        if not r.get("error") and r.get("per_token_cr"):
            by_model.setdefault(r["model"], []).append(np.array(r["per_token_cr"], dtype=float))

    for model, seqs in by_model.items():
        if not seqs: continue
        all_crs = np.concatenate(seqs)
        # Aggregate autocorrelation (short max_lag given short sequences)
        max_lag = min(15, max(5, min(len(s) for s in seqs) - 1))
        corrs = []
        for s in seqs:
            if len(s) < max_lag + 1: continue
            c = s - s.mean()
            var = np.var(c)
            if var == 0: continue
            ac = np.array([
                np.var(c) if lag == 0 else np.mean(c[:-lag] * c[lag:])
                for lag in range(max_lag)
            ])
            corrs.append(ac / ac[0])
        if len(corrs) < 3:
            print(f"  {model}: insufficient for autocorr")
            continue
        mean_corr = np.mean(corrs, axis=0)
        try:
            popt, _ = curve_fit(lambda t, G: np.exp(-G * t), np.arange(max_lag),
                                mean_corr, p0=[0.1], bounds=(0, 10), maxfev=5000)
            gamma = float(popt[0])
            tau_c = 1 / gamma if gamma > 0 else float("nan")
            fitted = np.exp(-gamma * np.arange(max_lag))
            ss_res = np.sum((mean_corr - fitted) ** 2)
            ss_tot = np.sum((mean_corr - mean_corr.mean()) ** 2)
            r2 = 1 - ss_res / ss_tot
            print(f"  {model[:40]:<40}  n={len(seqs):>3}  mean_CR={all_crs.mean():.2f}  tau_c={tau_c:.3f}  R2={r2:.3f}")
        except Exception as e:
            print(f"  {model}: fit failed: {e}")

    print(f"\nSaved raw data: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
