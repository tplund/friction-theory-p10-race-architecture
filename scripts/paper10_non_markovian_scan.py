"""
Paper 10: Non-Markovian subpopulation scan.

Aggregate power spectrum across all sequences shows alpha ~ 0.1 (white noise, Markovian).
But aggregate may hide subpopulation with non-Markovian (colored) spectra.

This script computes per-sequence PSD and alpha-fit, then looks at distribution
of alpha values. If a subpopulation of sequences has alpha > 0.5 (1/f-like),
non-Markovian memory exists in some subset of computation substrates.

Relevant for: theorem assumption (ii) Markovianity. If subpopulation is small,
aggregate Markovian approximation is defensible. If large, non-Markovian extension
is needed.
"""
import json
import numpy as np
from pathlib import Path
from collections import Counter

ROOT = Path("C:/_proj/FriktionsLLM")
RESULTS_DIR = ROOT / "data" / "results"
OUTPUT_DIR = ROOT / "data" / "paper10_analysis"
OUTPUT_DIR.mkdir(exist_ok=True)

# Clean datasets only (post thinking-mode audit)
TARGET_FILES = [
    "truthfulqa_calibrated_base.jsonl",
    "gsm8k_cr_validation_qwen3_235b.jsonl",
    "mixed_eval_v3_multijudge_liquid.jsonl",
    "temp_sweep_logprobs_full.jsonl",
    "creativity_temperature_sweep.jsonl",
]

MIN_SEQUENCE_LENGTH = 64  # need enough for PSD fit


def load_sequences(path, min_length=MIN_SEQUENCE_LENGTH):
    seqs = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            try:
                r = json.loads(line)
            except json.JSONDecodeError:
                continue
            cr = r.get("per_token_cr")
            if not isinstance(cr, list) or len(cr) < min_length:
                continue
            arr = np.array([float(c) for c in cr], dtype=float)
            arr = arr[arr < 100]  # filter saturation
            if len(arr) < min_length:
                continue
            seqs.append(arr)
    return seqs


def per_sequence_alpha(seq, max_freq_bins=32):
    """Compute PSD and fit power-law alpha for a single sequence."""
    if len(seq) < max_freq_bins * 2:
        return None
    s = seq - seq.mean()
    fft = np.fft.rfft(s[:max_freq_bins * 2])
    psd = np.abs(fft) ** 2
    psd = psd[:max_freq_bins]
    freqs = np.arange(len(psd)) / (len(psd) * 2)
    # Skip DC
    mask = (freqs > 0) & (psd > 0)
    if mask.sum() < 5:
        return None
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


def classify_alpha(alpha):
    if alpha is None:
        return "unfit"
    if abs(alpha) < 0.2:
        return "white (Markovian)"
    elif 0.2 <= alpha < 0.5:
        return "weak-pink"
    elif 0.5 <= alpha < 1.5:
        return "1/f (non-Markovian memory)"
    elif alpha >= 1.5:
        return "brown (strong memory)"
    else:
        return "anti-correlated"


def analyze_file(path):
    seqs = load_sequences(path)
    if not seqs:
        return None

    alphas = []
    r2s = []
    for s in seqs:
        result = per_sequence_alpha(s)
        if result is not None:
            a, r2 = result
            alphas.append(a)
            r2s.append(r2)

    if not alphas:
        return None

    alphas_arr = np.array(alphas)
    r2s_arr = np.array(r2s)

    # Filter to reliable fits only (R^2 > 0.3)
    reliable = r2s_arr > 0.3
    alphas_reliable = alphas_arr[reliable]

    categories = Counter(classify_alpha(a) for a in alphas_reliable)
    n_reliable = reliable.sum()

    return {
        "file": path.name,
        "n_sequences": len(seqs),
        "n_with_fit": len(alphas),
        "n_reliable_r2_gt_0.3": int(n_reliable),
        "mean_alpha": float(np.mean(alphas_reliable)) if n_reliable > 0 else None,
        "median_alpha": float(np.median(alphas_reliable)) if n_reliable > 0 else None,
        "std_alpha": float(np.std(alphas_reliable)) if n_reliable > 0 else None,
        "p25_alpha": float(np.percentile(alphas_reliable, 25)) if n_reliable > 0 else None,
        "p75_alpha": float(np.percentile(alphas_reliable, 75)) if n_reliable > 0 else None,
        "categories": dict(categories),
        "frac_non_markovian": float(
            sum(v for k, v in categories.items() if "non-Markovian" in k or "memory" in k) / n_reliable
        ) if n_reliable > 0 else None,
    }


def main():
    print("=" * 70)
    print("Paper 10: Non-Markovian subpopulation scan")
    print("Per-sequence PSD alpha-distribution")
    print("=" * 70)

    results = []
    for fname in TARGET_FILES:
        path = RESULTS_DIR / fname
        if not path.exists():
            continue
        print(f"\n[PROCESS] {fname}")
        r = analyze_file(path)
        if r is None:
            print("  insufficient data")
            continue

        print(f"  n_sequences: {r['n_sequences']}, reliable fits: {r['n_reliable_r2_gt_0.3']}")
        if r["mean_alpha"] is None:
            print(f"  no reliable fits — PSD too noisy for per-sequence power-law fit")
        else:
            print(f"  alpha distribution: mean={r['mean_alpha']:.3f} median={r['median_alpha']:.3f} std={r['std_alpha']:.3f}")
            print(f"  IQR: [{r['p25_alpha']:.3f}, {r['p75_alpha']:.3f}]")
            print(f"  categories: {r['categories']}")
            print(f"  fraction non-Markovian (alpha >= 0.5): {r['frac_non_markovian']:.3f}")
        results.append(r)

    output_path = OUTPUT_DIR / "non_markovian_scan_results_20260423.json"
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved: {output_path}")

    # Overall summary
    print("\n" + "=" * 70)
    print("Overall summary:")
    print("=" * 70)
    total_reliable = sum(r["n_reliable_r2_gt_0.3"] for r in results)
    total_non_mark = sum(
        int(r["frac_non_markovian"] * r["n_reliable_r2_gt_0.3"])
        for r in results if r["frac_non_markovian"] is not None
    )
    print(f"Total sequences with reliable PSD fit: {total_reliable}")
    print(f"Of which non-Markovian (alpha >= 0.5): {total_non_mark} ({100*total_non_mark/total_reliable:.1f}%)" if total_reliable else "")


if __name__ == "__main__":
    main()
