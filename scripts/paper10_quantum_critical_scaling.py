"""
Paper 10: Quantum-critical scaling test.

Hypothesis: LLMs operate near a quantum critical point in parameter space.
If true, the 1% non-Markovian (1/f) subpopulation found in `paper10_non_markovian_scan.py`
should scale systematically with model size.

Test: compute fraction of reliable-1/f sequences across LLM substrates of
different parameter counts. If fraction scales with model size (or some other
systematic model property), quantum-critical hypothesis is supported. If flat,
hypothesis is falsified.
"""
import json
import numpy as np
from pathlib import Path
from collections import Counter

ROOT = Path("C:/_proj/FriktionsLLM")
RESULTS = ROOT / "data" / "results"
OUTPUT_DIR = ROOT / "data" / "paper10_analysis"

# Datasets with verified clean data + known model size
DATASETS = [
    ("design3_episode_chain.jsonl", "qwen2.5-0.5b-instruct", 0.5),
    ("truthfulqa_calibrated_base.jsonl", "qwen3-4b-base", 4.0),
    ("p23_fictive_mechanism.jsonl", "qwen3-8b", 8.0),
    ("mixed_eval_v3_multijudge_liquid.jsonl", "LiquidAI-LFM2-24B", 24.0),
    ("gsm8k_cr_validation_qwen3_235b.jsonl", "Qwen3-235B-Instruct-2507", 235.0),
    ("mixed_eval_v3_multijudge_cogito.jsonl", "Cogito-671B", 671.0),
]

MIN_LEN = 64
MAX_FREQ_BINS = 32


def load_sequences(path, min_length=MIN_LEN):
    seqs = []
    with open(path, encoding="utf-8", errors="replace") as f:
        for line in f:
            try: r = json.loads(line)
            except: continue
            cr = r.get("per_token_cr")
            if not isinstance(cr, list) or len(cr) < min_length:
                continue
            arr = np.array([float(c) for c in cr], dtype=float)
            arr = arr[arr < 100]
            if len(arr) < min_length:
                continue
            seqs.append(arr)
    return seqs


def per_sequence_alpha(seq, max_freq_bins=MAX_FREQ_BINS):
    if len(seq) < max_freq_bins * 2:
        return None
    s = seq - seq.mean()
    fft = np.fft.rfft(s[:max_freq_bins * 2])
    psd = np.abs(fft) ** 2
    psd = psd[:max_freq_bins]
    freqs = np.arange(len(psd)) / (len(psd) * 2)
    mask = (freqs > 0) & (psd > 0)
    if mask.sum() < 5: return None
    log_f = np.log(freqs[mask])
    log_p = np.log(psd[mask])
    try:
        slope, intercept = np.polyfit(log_f, log_p, 1)
        alpha = -slope
        fitted = slope * log_f + intercept
        ss_res = np.sum((log_p - fitted) ** 2)
        ss_tot = np.sum((log_p - log_p.mean()) ** 2)
        r2 = 1 - ss_res / ss_tot if ss_tot > 0 else np.nan
        return float(alpha), float(r2)
    except Exception:
        return None


def classify(alpha):
    if abs(alpha) < 0.2: return "white"
    elif 0.5 <= alpha < 1.5: return "1f"
    elif alpha >= 1.5: return "brown"
    elif alpha < -0.2: return "anticorr"
    else: return "weak"


def analyze(path):
    seqs = load_sequences(path)
    if len(seqs) < 50:
        return None
    alphas_reliable = []
    n_all = 0
    n_reliable = 0
    for s in seqs:
        result = per_sequence_alpha(s)
        if result is None: continue
        n_all += 1
        a, r2 = result
        if r2 > 0.3:
            n_reliable += 1
            alphas_reliable.append(a)
    cats = Counter(classify(a) for a in alphas_reliable)
    n_1f = cats.get("1f", 0)
    return {
        "n_total_seq": len(seqs),
        "n_with_fit": n_all,
        "n_reliable": n_reliable,
        "n_1f": n_1f,
        "frac_reliable": n_reliable / max(len(seqs), 1),
        "frac_1f_of_total": n_1f / max(len(seqs), 1),
        "frac_1f_of_reliable": n_1f / max(n_reliable, 1),
        "mean_alpha_reliable": float(np.mean(alphas_reliable)) if alphas_reliable else None,
        "categories": dict(cats),
    }


def main():
    print("=" * 78)
    print("Paper 10: Quantum-critical scaling test")
    print("Hypothesis: 1% non-Markovian fraction scales with model size")
    print("=" * 78)

    results = []
    for fname, model_name, params_B in DATASETS:
        path = RESULTS / fname
        if not path.exists():
            print(f"\n[SKIP] {fname} missing")
            continue
        print(f"\n[PROCESS] {model_name} ({params_B}B params)")
        r = analyze(path)
        if r is None:
            print("  insufficient data")
            continue
        r["file"] = fname
        r["model"] = model_name
        r["params_B"] = params_B
        r["log_params"] = float(np.log10(params_B))

        print(f"  n_total: {r['n_total_seq']}  reliable: {r['n_reliable']}  1/f: {r['n_1f']}")
        print(f"  frac_reliable: {r['frac_reliable']:.4f}")
        print(f"  frac_1f_of_total: {r['frac_1f_of_total']:.4f}")
        if r['mean_alpha_reliable'] is not None:
            print(f"  mean_alpha_reliable: {r['mean_alpha_reliable']:.3f}")
        print(f"  categories: {r['categories']}")
        results.append(r)

    # Save
    output_path = OUTPUT_DIR / "quantum_critical_scaling_20260423.json"
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved: {output_path}")

    # Statistical test: does frac_1f scale with log(params)?
    if len(results) >= 3:
        from scipy import stats
        log_p = np.array([r["log_params"] for r in results])
        frac_1f_total = np.array([r["frac_1f_of_total"] for r in results])
        frac_1f_reliable = np.array([r["frac_1f_of_reliable"] for r in results])
        frac_reliable = np.array([r["frac_reliable"] for r in results])
        mean_alphas = np.array([r.get("mean_alpha_reliable") or 0 for r in results])

        print("\n" + "=" * 78)
        print("Scaling analysis")
        print("=" * 78)

        for name, y in [
            ("frac_1f_of_total vs log(params)", frac_1f_total),
            ("frac_1f_of_reliable vs log(params)", frac_1f_reliable),
            ("frac_reliable vs log(params)", frac_reliable),
            ("mean_alpha_reliable vs log(params)", mean_alphas),
        ]:
            if np.all(y == 0): continue
            rho, p = stats.spearmanr(log_p, y)
            pearson_r, pearson_p = stats.pearsonr(log_p, y)
            print(f"\n  {name}:")
            print(f"    Spearman rho = {rho:.3f}  (p = {p:.4f})")
            print(f"    Pearson  r   = {pearson_r:.3f}  (p = {pearson_p:.4f})")

        # Print table
        print("\n  Summary table:")
        print(f"    {'model':<32} {'params':>8} {'n_tot':>6} {'n_rel':>6} {'n_1f':>6} {'frac_1f':>10} {'mean_a':>8}")
        for r in sorted(results, key=lambda x: x["params_B"]):
            ma = r.get("mean_alpha_reliable") or float('nan')
            print(f"    {r['model']:<32} {r['params_B']:>7.1f}B {r['n_total_seq']:>6} {r['n_reliable']:>6} {r['n_1f']:>6} {r['frac_1f_of_total']:>10.4f} {ma:>8.3f}")

    print("\n" + "=" * 78)
    print("Interpretation")
    print("=" * 78)
    # Based on direction + significance of frac_1f_of_total trend
    from scipy import stats
    if len(results) >= 3:
        log_p = np.array([r["log_params"] for r in results])
        frac = np.array([r["frac_1f_of_total"] for r in results])
        rho, p = stats.spearmanr(log_p, frac)
        if p < 0.05:
            direction = "INCREASES" if rho > 0 else "DECREASES"
            print(f"  CONCLUSION: 1/f fraction systematically {direction} with model size")
            print(f"  (Spearman rho = {rho:.3f}, p = {p:.4f})")
            print(f"  => quantum-critical-scaling hypothesis SUPPORTED")
        else:
            print(f"  CONCLUSION: No significant scaling of 1/f fraction with model size")
            print(f"  (Spearman rho = {rho:.3f}, p = {p:.4f})")
            print(f"  => quantum-critical-scaling hypothesis NOT SUPPORTED at n={len(results)}")
            print(f"     (may need more datasets, or hypothesis is wrong)")


if __name__ == "__main__":
    main()
