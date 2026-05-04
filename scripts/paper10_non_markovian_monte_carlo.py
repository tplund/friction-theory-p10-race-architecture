"""
Paper 10: Monte Carlo validation of non-Markovian subpopulation finding.

Earlier finding: of 16 sequences with reliable per-sequence PSD fit (R^2 > 0.3),
15 classified as 1/f (alpha 0.7-0.95). Suggests non-Markovian memory
in subpopulation. But could be selection bias: R^2 > 0.3 threshold may
favor sequences with underlying 1/f structure.

Monte Carlo test: generate synthetic white-noise (alpha = 0) sequences
matching real data length distribution. Run same PSD pipeline. Count
reliable fits + their alpha classifications.

If synthetic white noise produces 1/f classifications at same rate
(~94%) when passing R^2 > 0.3 → selection bias dominates.
If synthetic produces mostly "white" classifications → real non-Markovian
signal in 1% of real data.
"""
import json
import numpy as np
from pathlib import Path
from collections import Counter

ROOT = Path("C:/_proj/FriktionsLLM")
RESULTS_DIR = ROOT / "data" / "results"
OUTPUT_DIR = ROOT / "data" / "paper10_analysis"
OUTPUT_DIR.mkdir(exist_ok=True)

CLEAN_FILES = [
    "truthfulqa_calibrated_base.jsonl",
    "gsm8k_cr_validation_qwen3_235b.jsonl",
    "mixed_eval_v3_multijudge_liquid.jsonl",
    "temp_sweep_logprobs_full.jsonl",
    "creativity_temperature_sweep.jsonl",
]

MIN_LEN = 64
MAX_FREQ_BINS = 32
N_MONTE_CARLO = 3


def per_sequence_alpha(seq, max_freq_bins=MAX_FREQ_BINS):
    if len(seq) < max_freq_bins * 2:
        return None
    s = seq - seq.mean()
    fft = np.fft.rfft(s[:max_freq_bins * 2])
    psd = np.abs(fft) ** 2
    psd = psd[:max_freq_bins]
    freqs = np.arange(len(psd)) / (len(psd) * 2)
    mask = (freqs > 0) & (psd > 0)
    if mask.sum() < 5:
        return None
    log_f = np.log(freqs[mask])
    log_p = np.log(psd[mask])
    try:
        slope, _ = np.polyfit(log_f, log_p, 1)
        alpha = -slope
        fitted = np.polyval([slope, np.mean(log_p) - slope * np.mean(log_f)], log_f)
        ss_res = np.sum((log_p - fitted) ** 2)
        ss_tot = np.sum((log_p - log_p.mean()) ** 2)
        r2 = 1 - ss_res / ss_tot if ss_tot > 0 else np.nan
        return float(alpha), float(r2)
    except Exception:
        return None


def classify_alpha(a):
    if abs(a) < 0.2:
        return "white"
    elif 0.2 <= a < 0.5:
        return "weak-pink"
    elif 0.5 <= a < 1.5:
        return "1/f (non-Markovian)"
    elif a >= 1.5:
        return "brown"
    else:
        return "anti-correlated"


def collect_real_sequence_metadata():
    """Get length distribution and mean/std from real data."""
    lengths = []
    stats = []
    for fname in CLEAN_FILES:
        path = RESULTS_DIR / fname
        if not path.exists():
            continue
        with open(path, encoding="utf-8") as f:
            for line in f:
                try:
                    r = json.loads(line)
                except:
                    continue
                cr = r.get("per_token_cr")
                if not isinstance(cr, list) or len(cr) < MIN_LEN:
                    continue
                arr = np.array([float(c) for c in cr], dtype=float)
                arr = arr[arr < 100]
                if len(arr) < MIN_LEN:
                    continue
                lengths.append(len(arr))
                stats.append((float(arr.mean()), float(arr.std())))
    return lengths, stats


def run_monte_carlo(lengths, stats, rng):
    """Generate synthetic white-noise sequences matching real length/stats distribution.
    Return (n_reliable, category_counts, alpha_list)."""
    n_reliable = 0
    categories = Counter()
    all_alphas = []
    for L, (mean_cr, std_cr) in zip(lengths, stats):
        # White noise with matched mean/std
        syn = rng.normal(loc=mean_cr, scale=max(std_cr, 0.01), size=L)
        result = per_sequence_alpha(syn)
        if result is None:
            continue
        alpha, r2 = result
        if r2 > 0.3:
            n_reliable += 1
            categories[classify_alpha(alpha)] += 1
            all_alphas.append(alpha)
    return n_reliable, categories, all_alphas


def main():
    print("=" * 70)
    print("Paper 10: Monte Carlo validation of non-Markovian subpopulation")
    print("=" * 70)

    lengths, stats = collect_real_sequence_metadata()
    print(f"\nReal data: {len(lengths)} sequences with length >= {MIN_LEN}")
    print(f"Length range: [{min(lengths)}, {max(lengths)}], median {np.median(lengths):.0f}")
    print(f"Mean-CR range: [{min(s[0] for s in stats):.2f}, {max(s[0] for s in stats):.2f}]")

    print(f"\nRunning {N_MONTE_CARLO} independent Monte Carlo trials of matched white noise...")

    mc_results = []
    for trial in range(N_MONTE_CARLO):
        rng = np.random.default_rng(seed=42 + trial)
        n_rel, cats, alphas = run_monte_carlo(lengths, stats, rng)
        mc_results.append({
            "trial": trial,
            "n_reliable": n_rel,
            "categories": dict(cats),
            "frac_1f": cats.get("1/f (non-Markovian)", 0) / max(n_rel, 1),
            "mean_alpha": float(np.mean(alphas)) if alphas else None,
            "median_alpha": float(np.median(alphas)) if alphas else None,
        })
        print(f"\n  Trial {trial} (seed={42+trial}):")
        print(f"    reliable fits (R^2 > 0.3): {n_rel}/{len(lengths)} ({100*n_rel/len(lengths):.2f}%)")
        print(f"    category counts: {dict(cats)}")
        print(f"    fraction classified 1/f: {mc_results[-1]['frac_1f']:.3f}")
        if alphas:
            print(f"    alpha: mean={np.mean(alphas):.3f}, median={np.median(alphas):.3f}")

    # Compare to observed
    print("\n" + "=" * 70)
    print("Comparison to observed:")
    print("=" * 70)
    print(f"REAL data: 16/{len(lengths)} reliable fits ({100*16/len(lengths):.2f}%)")
    print("REAL data: 15/16 classified 1/f (non-Markovian), 1/16 anti-correlated")
    print("REAL data: fraction 1/f among reliable = 0.938")
    print()
    print("Monte Carlo (white noise):")
    for r in mc_results:
        ma = r["mean_alpha"] if r["mean_alpha"] is not None else 0.0
        print(
            f"  Trial {r['trial']}: {r['n_reliable']} reliable, "
            f"{r['frac_1f']:.3f} classified 1/f, mean alpha = {ma:.3f}"
        )

    # Save
    output_path = OUTPUT_DIR / "non_markovian_monte_carlo_20260423.json"
    with open(output_path, "w") as f:
        json.dump({
            "n_sequences": len(lengths),
            "observed": {"n_reliable": 16, "n_1f": 15, "frac_1f": 0.938},
            "monte_carlo": mc_results,
        }, f, indent=2)
    print(f"\nSaved: {output_path}")

    # Interpretation
    mean_mc_frac = np.mean([r["frac_1f"] for r in mc_results])
    mean_mc_n_reliable = np.mean([r["n_reliable"] for r in mc_results])
    print("\n" + "=" * 70)
    print("Interpretation:")
    print("=" * 70)
    print(f"Monte Carlo mean reliable: {mean_mc_n_reliable:.1f} vs observed 16")
    print(f"Monte Carlo mean fraction 1/f: {mean_mc_frac:.3f} vs observed 0.938")
    print()
    if mean_mc_frac > 0.5:
        print("=> SELECTION BIAS DOMINATES: white noise PSDs passing R^2 > 0.3")
        print("   threshold tend to look 1/f-like due to random downward-sloping fits.")
        print("   Non-Markovian subpopulation finding in real data is LIKELY ARTIFACT.")
    elif mean_mc_frac < 0.2:
        print("=> REAL SIGNAL: white noise does not produce 1/f classifications")
        print("   at the observed rate. Non-Markovian subpopulation finding is")
        print("   SUPPORTED in real data.")
    else:
        print("=> AMBIGUOUS: Monte Carlo produces intermediate rate. Need more data")
        print("   or better fit diagnostics.")


if __name__ == "__main__":
    main()
