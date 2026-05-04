"""
Paper 10 Corollary 4 empirical validation: CR-autocorrelation analysis.

Tests whether LLM CR temporal autocorrelation follows exponential decay
predicted by Schwinger-Keldysh mapping (docs/paper10_derivation_sketch_v1.md §5B).

Target predictions:
1. Autocorrelation C_CR(tau) decays as exp(-Gamma*tau) with single timescale
2. CR magnitude scales with softmax temperature T
"""
import json
import numpy as np
from pathlib import Path
from scipy.optimize import curve_fit
from collections import defaultdict

ROOT = Path("C:/_proj/FriktionsLLM")
RESULTS_DIR = ROOT / "data" / "results"
OUTPUT_DIR = ROOT / "data" / "paper10_analysis"
OUTPUT_DIR.mkdir(exist_ok=True)

# Files with long per_token_cr sequences, representing multiple models
# Thinking-mode status per Paper 1 §9.1c rule:
# - Qwen3.5-9B: CONTAMINATED (763 median tokens but response "A" = hidden reasoning)
# - Qwen3-235B-Instruct-2507: CLEAN (Instruct-2507 variant has thinking off per CLAUDE.md)
# - qwen3-4b-base: CLEAN (base model = direct-answer)
# - LiquidAI LFM2: CLEAN (not thinking-model family)
# - temp_sweep/creativity_sweep: model unknown but 400-token-cap suggests direct-answer

TARGET_FILES = [
    "temp_sweep_logprobs_full.jsonl",             # CLEAN (probable)
    # "truthfulqa_mc_adaptive_qwen35_9b.jsonl",   # EXCLUDED: thinking-mode contamination
    "truthfulqa_calibrated_base.jsonl",           # CLEAN (qwen3-4b-base)
    "gsm8k_cr_validation_qwen3_235b.jsonl",       # CLEAN (Instruct-2507, thinking-off)
    "combined_friction_cogito_671b.jsonl",
    "creativity_temperature_sweep.jsonl",         # CLEAN (probable)
    "mixed_eval_v3_multijudge_liquid.jsonl",      # CLEAN (LiquidAI, not thinking)
]

MIN_SEQUENCE_LENGTH = 30
MAX_LAG = 30


def load_sequences(path, min_length=MIN_SEQUENCE_LENGTH):
    """Load per_token_cr sequences from JSONL file with optional metadata."""
    seqs = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            cr = rec.get("per_token_cr")
            if not isinstance(cr, list) or len(cr) < min_length:
                continue
            cr_arr = np.array([float(c) for c in cr], dtype=float)
            # Filter saturation (CR values >= 100 likely indicate saturation cap)
            cr_arr_filtered = cr_arr[cr_arr < 100]
            if len(cr_arr_filtered) < MIN_SEQUENCE_LENGTH:
                continue
            meta = {
                "temperature": rec.get("temperature") or rec.get("temp"),
                "model": rec.get("model"),
                "correct": rec.get("correct") or rec.get("is_correct"),
                "category": rec.get("category"),
                "length": len(cr_arr_filtered),
                "has_saturation": bool((cr_arr >= 100).any()),
            }
            seqs.append((cr_arr_filtered, meta))
    return seqs


def autocorr_normalized(x, max_lag):
    """Compute normalized autocorrelation, C(tau)/C(0)."""
    x = x - x.mean()
    var = np.var(x)
    if var == 0:
        return np.ones(max_lag) * np.nan
    result = np.zeros(max_lag)
    for lag in range(max_lag):
        if lag == 0:
            result[lag] = var
        else:
            result[lag] = np.mean(x[: len(x) - lag] * x[lag:])
    return result / result[0]


def fit_exp_decay(taus, corr):
    """Fit C(tau) = exp(-Gamma*tau). Returns (Gamma, R^2)."""
    try:
        mask = ~np.isnan(corr)
        taus_m = taus[mask]
        corr_m = corr[mask]
        if len(corr_m) < 5:
            return np.nan, np.nan
        popt, _ = curve_fit(
            lambda t, G: np.exp(-G * t),
            taus_m, corr_m, p0=[0.1], bounds=(0, 10.0), maxfev=5000,
        )
        Gamma = float(popt[0])
        fitted = np.exp(-Gamma * taus_m)
        ss_res = np.sum((corr_m - fitted) ** 2)
        ss_tot = np.sum((corr_m - corr_m.mean()) ** 2)
        r2 = 1 - ss_res / ss_tot if ss_tot > 0 else np.nan
        return Gamma, float(r2)
    except Exception as e:
        return np.nan, np.nan


def analyze_file(path, max_lag=MAX_LAG):
    seqs_with_meta = load_sequences(path)
    if not seqs_with_meta:
        return None

    # Filter to sequences long enough
    valid = [(s, m) for s, m in seqs_with_meta if len(s) >= max_lag + 1]
    if len(valid) < 3:
        return None

    # Compute autocorrelation per sequence
    corrs = []
    for seq, _ in valid:
        ac = autocorr_normalized(seq, max_lag)
        if not np.all(np.isnan(ac)):
            corrs.append(ac)

    if len(corrs) < 3:
        return None

    corrs_arr = np.array(corrs)
    mean_corr = np.nanmean(corrs_arr, axis=0)
    sem_corr = np.nanstd(corrs_arr, axis=0) / np.sqrt(len(corrs))

    taus = np.arange(max_lag)
    Gamma, r2 = fit_exp_decay(taus, mean_corr)
    tau_c = 1.0 / Gamma if (not np.isnan(Gamma) and Gamma > 0) else np.nan

    # Per-sequence stats
    cr_means = [s.mean() for s, _ in valid]
    cr_stds = [s.std() for s, _ in valid]

    # Temperature-grouped stats (for prediction #2)
    temp_groups = defaultdict(list)
    for s, m in valid:
        t = m.get("temperature")
        if t is not None:
            temp_groups[round(float(t), 2)].append(s.mean())

    temp_scaling = None
    if len(temp_groups) >= 2:
        temp_scaling = {
            float(T): {
                "n": len(vals),
                "mean_cr": float(np.mean(vals)),
                "sem_cr": float(np.std(vals) / np.sqrt(len(vals))),
            }
            for T, vals in sorted(temp_groups.items())
        }

    return {
        "file": path.name,
        "n_sequences_used": len(valid),
        "n_sequences_valid_corr": len(corrs),
        "mean_sequence_length": float(np.mean([len(s) for s, _ in valid])),
        "Gamma_eff": float(Gamma) if not np.isnan(Gamma) else None,
        "tau_c_tokens": float(tau_c) if not np.isnan(tau_c) else None,
        "r2_exp_fit": float(r2) if not np.isnan(r2) else None,
        "mean_cr_across_sequences": float(np.mean(cr_means)),
        "std_cr_across_sequences": float(np.std(cr_means)),
        "mean_corr_tau": [float(x) for x in mean_corr],
        "sem_corr_tau": [float(x) for x in sem_corr],
        "temperature_scaling": temp_scaling,
    }


def main():
    results = []
    print("=" * 70)
    print("Paper 10 Corollary 4 Empirical Validation")
    print("CR-autocorrelation analysis")
    print("=" * 70)

    for fname in TARGET_FILES:
        path = RESULTS_DIR / fname
        if not path.exists():
            print(f"[SKIP] {fname} not found")
            continue

        print(f"\n[PROCESS] {fname}")
        r = analyze_file(path)
        if r is None:
            print(f"  insufficient data")
            continue

        print(f"  n_sequences: {r['n_sequences_used']} (used for autocorr: {r['n_sequences_valid_corr']})")
        print(f"  mean sequence length: {r['mean_sequence_length']:.1f} tokens")
        print(f"  mean CR across sequences: {r['mean_cr_across_sequences']:.3f} (std {r['std_cr_across_sequences']:.3f})")
        if r['Gamma_eff'] is not None:
            print(f"  Gamma_eff: {r['Gamma_eff']:.4f} / token")
            print(f"  tau_c: {r['tau_c_tokens']:.2f} tokens")
            print(f"  R² for exp fit: {r['r2_exp_fit']:.3f}")

        if r['temperature_scaling']:
            print(f"  temperature scaling ({len(r['temperature_scaling'])} T values):")
            for T, stats in r['temperature_scaling'].items():
                print(f"    T={T}: n={stats['n']}, mean_CR={stats['mean_cr']:.3f} ± {stats['sem_cr']:.3f}")

        results.append(r)

    # Save results
    output_path = OUTPUT_DIR / "cr_autocorrelation_results_20260423.json"
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)

    print("\n" + "=" * 70)
    print(f"Saved: {output_path}")
    print("=" * 70)

    # Summary table
    print("\nSummary — exponential fit quality:")
    print(f"{'File':<55} {'tau_c':>8} {'R²':>6}")
    for r in results:
        tc = f"{r['tau_c_tokens']:.1f}" if r['tau_c_tokens'] else "N/A"
        r2 = f"{r['r2_exp_fit']:.2f}" if r['r2_exp_fit'] else "N/A"
        print(f"{r['file']:<55} {tc:>8} {r2:>6}")

    # Temperature scaling verification
    print("\nTemperature-scaling verification (prediction #2):")
    for r in results:
        if r['temperature_scaling']:
            print(f"\n  {r['file']}:")
            ts = r['temperature_scaling']
            Ts = sorted(ts.keys())
            crs = [ts[T]['mean_cr'] for T in Ts]
            monotonic = all(crs[i] <= crs[i+1] for i in range(len(crs)-1))
            reverse_mono = all(crs[i] >= crs[i+1] for i in range(len(crs)-1))
            tag = "monotonic INCREASING" if monotonic else ("monotonic DECREASING" if reverse_mono else "non-monotonic")
            print(f"    T range: {min(Ts):.2f} -> {max(Ts):.2f}")
            print(f"    CR range: {min(crs):.2f} -> {max(crs):.2f}")
            print(f"    Signature: {tag}")


if __name__ == "__main__":
    main()
