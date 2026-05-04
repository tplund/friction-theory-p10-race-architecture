"""
Paper 10 Task B (Ollama version): Base-model scaling test via local Ollama.

Strict constraint: only ONE model loaded at a time. Explicit unload between.

Runs identical prompt-set on Qwen2.5 instruct family at different sizes,
computes per_token_cr, tests scaling of commit-timescale and non-Markovian
signatures with model size.
"""
import json
import sys
import time
import subprocess
from pathlib import Path
import httpx
import numpy as np
from scipy.optimize import curve_fit

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from friktionsllm.ollama_client import OllamaClient
from friktionsllm.friction.cr_utils import compute_cr_from_logprobs

ROOT = Path("C:/_proj/FriktionsLLM")
OUTPUT_DIR = ROOT / "data" / "paper10_analysis"
OUTPUT_DIR.mkdir(exist_ok=True)
OUTPUT_FILE = OUTPUT_DIR / "ollama_scaling_20260424.jsonl"

# Serial execution, one at a time. Size order ascending — smallest first.
MODELS = [
    ("qwen2.5:0.5b-instruct", 0.5),
    ("qwen2.5:1.5b-instruct", 1.5),
    ("qwen2.5:3b-instruct", 3.0),
]

# 30 diverse prompts — same across all models
PROMPTS = [
    "What is 2+2? Answer with one number.",
    "The capital of France is",
    "Name one color.",
    "Complete: The sun rises in the",
    "1+1=",
    "What is the largest planet? One word.",
    "Is water wet? Yes or no.",
    "Name a Shakespeare play.",
    "What gas do plants produce? One word.",
    "How many legs does a spider have?",
    "What is Pi to two decimals? Plain digits.",
    "Name a type of bird.",
    "What is the opposite of hot?",
    "Is the Earth flat? Yes or no.",
    "What is 10 times 10?",
    "Name a mathematical operation.",
    "What is the chemical symbol for gold?",
    "What year is this? One number.",
    "Is fire cold? Yes or no.",
    "Name a famous scientist.",
    "What is the boiling point of water in Celsius?",
    "Name a prime number less than 10.",
    "What color is the sky on a clear day?",
    "Name a continent.",
    "What is relativity about? One sentence.",
    "What is DNA? One sentence.",
    "Name a programming language.",
    "What is 7 times 8?",
    "Who wrote Hamlet?",
    "What is gravity? One sentence.",
]


def ollama_unload(model):
    """Unload a specific model from RAM via keep_alive=0."""
    try:
        r = httpx.post(
            "http://localhost:11434/api/generate",
            json={"model": model, "prompt": "", "keep_alive": 0},
            timeout=10,
        )
        # Alternative: ollama stop via subprocess
        time.sleep(1)
        return True
    except Exception as e:
        print(f"  [unload warn] {e}")
        return False


def run_prompt(client, model, prompt):
    try:
        r = client.generate(
            prompt, model=model, max_tokens=60, temperature=0.7, logprobs=True,
        )
        stats = compute_cr_from_logprobs(r.token_logprobs)
        return {
            "prompt": prompt,
            "response": r.text,
            "per_token_cr": stats.per_token_cr,
            "n_tokens": len(stats.per_token_cr),
            "mean_cr": float(stats.mean_cr) if hasattr(stats, "mean_cr") else None,
            "latency_ms": r.latency_ms,
            "error": None,
        }
    except Exception as e:
        return {"prompt": prompt, "error": str(e)[:200], "per_token_cr": [], "n_tokens": 0}


def check_ollama_running():
    try:
        r = httpx.get("http://localhost:11434/api/tags", timeout=5)
        return r.status_code == 200
    except Exception:
        return False


def check_thinking_contamination(records):
    """Quick audit: are tokens >> response chars? Indicates thinking contamination."""
    samples = []
    for r in records:
        if r.get("error"): continue
        resp = str(r.get("response", ""))
        ntok = r.get("n_tokens", 0)
        if ntok > 0:
            samples.append((ntok, len(resp)))
    if not samples: return False, 0
    suspicious = sum(1 for t, rl in samples if t > 30 and rl < 10) / len(samples)
    return suspicious > 0.3, suspicious


def main():
    print("=" * 78)
    print("Paper 10 Task B (Ollama): Base-model scaling test")
    print("Serial execution, ONE MODEL AT A TIME, explicit unload between")
    print("=" * 78)

    if not check_ollama_running():
        print("ERROR: Ollama not running. Start with 'ollama serve' first.")
        return

    client = OllamaClient()
    all_results = []

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f_out:
        for idx, (model, params_B) in enumerate(MODELS):
            print(f"\n{'='*78}")
            print(f"[{idx+1}/{len(MODELS)}] Model: {model} ({params_B}B)")
            print(f"{'='*78}")

            model_results = []
            t_start = time.time()
            failures = 0
            for i, prompt in enumerate(PROMPTS):
                r = run_prompt(client, model, prompt)
                r["model"] = model
                r["params_B"] = params_B
                model_results.append(r)
                f_out.write(json.dumps(r) + "\n")
                f_out.flush()

                if r.get("error"):
                    failures += 1
                    err_short = str(r["error"])[:60].encode("ascii", "replace").decode("ascii")
                    print(f"  [{i+1}] ERROR: {err_short}")
                    if failures >= 3:
                        print(f"  [ABORT] too many failures on this model")
                        break
                else:
                    resp = str(r["response"])[:50].encode("ascii", "replace").decode("ascii")
                    print(f"  [{i+1}] n={r['n_tokens']:>3}  r: {resp}")

            elapsed = time.time() - t_start
            print(f"\n  Model {model}: {len(model_results)} runs in {elapsed:.1f}s")

            # Audit thinking contamination
            contaminated, ratio = check_thinking_contamination(model_results)
            if contaminated:
                print(f"  [WARN] possible thinking contamination (ratio={ratio:.2f})")
            else:
                print(f"  [OK] no thinking contamination detected (ratio={ratio:.2f})")

            all_results.extend(model_results)

            # UNLOAD THIS MODEL BEFORE NEXT
            print(f"  [UNLOAD] removing {model} from RAM...")
            ollama_unload(model)
            time.sleep(2)

    # Post-analysis
    print("\n" + "=" * 78)
    print("Autocorrelation scaling analysis")
    print("=" * 78)

    from collections import defaultdict
    by_model = defaultdict(list)
    for r in all_results:
        if not r.get("error") and r.get("per_token_cr") and len(r["per_token_cr"]) >= 10:
            by_model[r["model"]].append(np.array(r["per_token_cr"], dtype=float))

    print(f"\n{'model':<30} {'params':>7} {'n_seq':>6} {'med_len':>8} {'mean_CR':>9} {'tau_c':>8} {'R2':>6}")
    scaling_data = []
    for model, seqs in sorted(by_model.items()):
        # Get params_B
        params_B = next((p for m, p in MODELS if m == model), 0)
        all_crs = np.concatenate(seqs)
        lengths = [len(s) for s in seqs]
        median_len = int(np.median(lengths))

        # Autocorrelation
        max_lag = min(12, max(5, min(lengths) - 1))
        corrs = []
        for s in seqs:
            if len(s) < max_lag + 1: continue
            c = s - s.mean()
            if np.var(c) == 0: continue
            ac = np.array([np.var(c) if lag == 0 else np.mean(c[:-lag] * c[lag:])
                           for lag in range(max_lag)])
            corrs.append(ac / ac[0])
        if len(corrs) < 3:
            print(f"  {model[:28]:<30} {params_B:>6}B {len(seqs):>6} {median_len:>8} {all_crs.mean():>9.3f}  insufficient")
            continue
        mean_corr = np.mean(corrs, axis=0)
        try:
            popt, _ = curve_fit(lambda t, G: np.exp(-G * t), np.arange(max_lag),
                                mean_corr, p0=[0.1], bounds=(0, 10), maxfev=5000)
            gamma = float(popt[0])
            tau_c = 1/gamma if gamma > 0 else float("nan")
            fitted = np.exp(-gamma * np.arange(max_lag))
            ss_res = np.sum((mean_corr - fitted)**2)
            ss_tot = np.sum((mean_corr - mean_corr.mean())**2)
            r2 = 1 - ss_res/ss_tot if ss_tot > 0 else float("nan")
            print(f"  {model[:28]:<30} {params_B:>6}B {len(corrs):>6} {median_len:>8} {all_crs.mean():>9.3f} {tau_c:>8.3f} {r2:>6.3f}")
            scaling_data.append({
                "model": model, "params_B": params_B, "n_seq": len(corrs),
                "mean_CR": float(all_crs.mean()), "tau_c": tau_c, "r2": r2,
                "gamma": gamma, "median_len": median_len,
            })
        except Exception as e:
            print(f"  {model[:28]:<30}  fit failed: {e}")

    # Scaling test
    if len(scaling_data) >= 3:
        from scipy import stats
        log_p = np.array([np.log10(d["params_B"]) for d in scaling_data])
        tau_cs = np.array([d["tau_c"] for d in scaling_data])
        mean_crs = np.array([d["mean_CR"] for d in scaling_data])

        rho_tau, p_tau = stats.spearmanr(log_p, tau_cs)
        rho_cr, p_cr = stats.spearmanr(log_p, mean_crs)

        print(f"\nScaling of tau_c with log(params):   Spearman rho = {rho_tau:.3f}  p = {p_tau:.4f}")
        print(f"Scaling of mean_CR with log(params): Spearman rho = {rho_cr:.3f}  p = {p_cr:.4f}")

    # Save summary
    summary_path = OUTPUT_DIR / "ollama_scaling_summary_20260424.json"
    with open(summary_path, "w") as f:
        json.dump(scaling_data, f, indent=2)
    print(f"\nSaved summary: {summary_path}")
    print(f"Saved raw: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
