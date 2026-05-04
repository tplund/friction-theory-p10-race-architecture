"""
Paper 10 Corollary 4 extended validation:
- Correctness-stratified autocorrelation (does tau_c differ for correct vs incorrect?)
- Fourier power spectrum (Markovian white vs non-Markovian 1/f signatures)

Tests hypotheses:
(a) RACE-commit-quality: correct responses commit "cleaner" (larger tau_c, higher R^2)
(b) Markovian commit: CR power spectrum is flat (white)
(c) Non-Markovian memory: CR power spectrum has 1/f or peaked structure
"""
import json
import numpy as np
from pathlib import Path
from scipy.optimize import curve_fit

ROOT = Path("C:/_proj/FriktionsLLM")
RESULTS_DIR = ROOT / "data" / "results"
OUTPUT_DIR = ROOT / "data" / "paper10_analysis"
OUTPUT_DIR.mkdir(exist_ok=True)

TARGET_FILES = [
    # "truthfulqa_mc_adaptive_qwen35_9b.jsonl",  # EXCLUDED: thinking-mode contamination (Qwen3.5)
    "truthfulqa_calibrated_base.jsonl",           # CLEAN (qwen3-4b-base)
    "gsm8k_cr_validation_qwen3_235b.jsonl",       # CLEAN (Instruct-2507)
    "mixed_eval_v3_multijudge_liquid.jsonl",      # CLEAN (Liquid LFM2)
]

MIN_SEQUENCE_LENGTH = 30
MAX_LAG = 30


def load_sequences_with_correctness(path, min_length=MIN_SEQUENCE_LENGTH):
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
            arr = np.array([float(c) for c in cr], dtype=float)
            arr = arr[arr < 100]
            if len(arr) < min_length:
                continue
            correct = None
            # Try multiple field names
            for key in ("correct", "is_correct", "vanilla_correct",
                        "adaptive_correct", "judge_correct", "final_correct"):
                v = rec.get(key)
                if v is not None:
                    correct = bool(v)
                    break
            if correct is None:
                decision = rec.get("decision")
                if decision in ("truthful", "correct", True, 1):
                    correct = True
                elif decision in ("untruthful", "incorrect", False, 0):
                    correct = False
            seqs.append((arr, correct))
    return seqs


def autocorr_normalized(x, max_lag):
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
    except Exception:
        return np.nan, np.nan


def power_spectrum(sequences, max_freq_bins=32):
    """Compute averaged power spectrum across sequences."""
    spectra = []
    for s in sequences:
        if len(s) < max_freq_bins * 2:
            continue
        s_centered = s - s.mean()
        fft = np.fft.rfft(s_centered[:max_freq_bins * 2])
        psd = np.abs(fft) ** 2
        spectra.append(psd[:max_freq_bins])
    if not spectra:
        return None
    return np.mean(spectra, axis=0)


def fit_power_law(freqs, psd):
    """Fit PSD ~ freq^(-alpha). White noise: alpha=0. 1/f: alpha=1."""
    try:
        # Use log-log fit, skip DC component
        mask = (freqs > 0) & (psd > 0)
        log_f = np.log(freqs[mask])
        log_p = np.log(psd[mask])
        slope, intercept = np.polyfit(log_f, log_p, 1)
        alpha = -slope
        # Residuals
        fitted = slope * log_f + intercept
        ss_res = np.sum((log_p - fitted) ** 2)
        ss_tot = np.sum((log_p - log_p.mean()) ** 2)
        r2 = 1 - ss_res / ss_tot if ss_tot > 0 else np.nan
        return float(alpha), float(r2)
    except Exception:
        return np.nan, np.nan


def analyze_correctness_stratified(path, max_lag=MAX_LAG):
    seqs = load_sequences_with_correctness(path)
    if not seqs:
        return None

    # Filter sequences long enough
    long_enough = [(s, c) for s, c in seqs if len(s) >= max_lag + 1]
    if len(long_enough) < 10:
        return None

    correct = [s for s, c in long_enough if c is True]
    incorrect = [s for s, c in long_enough if c is False]

    def analyze_group(group_seqs, label):
        if len(group_seqs) < 3:
            return {"label": label, "n": len(group_seqs), "available": False}
        corrs = [autocorr_normalized(s, max_lag) for s in group_seqs]
        corrs = [c for c in corrs if not np.all(np.isnan(c))]
        if len(corrs) < 3:
            return {"label": label, "n": len(group_seqs), "available": False}
        mean_corr = np.nanmean(np.array(corrs), axis=0)
        taus = np.arange(max_lag)
        Gamma, r2 = fit_exp_decay(taus, mean_corr)
        tau_c = 1.0 / Gamma if (not np.isnan(Gamma) and Gamma > 0) else np.nan
        mean_CR = np.mean([s.mean() for s in group_seqs])
        std_CR = np.std([s.mean() for s in group_seqs])
        return {
            "label": label,
            "n": len(group_seqs),
            "n_valid_corr": len(corrs),
            "available": True,
            "Gamma_eff": float(Gamma) if not np.isnan(Gamma) else None,
            "tau_c_tokens": float(tau_c) if not np.isnan(tau_c) else None,
            "r2_exp_fit": float(r2) if not np.isnan(r2) else None,
            "mean_CR": float(mean_CR),
            "std_CR": float(std_CR),
            "mean_corr_tau": [float(x) for x in mean_corr],
        }

    result = {
        "file": path.name,
        "total_sequences": len(long_enough),
        "correct": analyze_group(correct, "correct"),
        "incorrect": analyze_group(incorrect, "incorrect"),
    }

    # Power spectrum (all sequences)
    psd = power_spectrum([s for s, _ in long_enough])
    if psd is not None:
        freqs = np.arange(len(psd)) / (len(psd) * 2)
        alpha, psd_r2 = fit_power_law(freqs, psd)
        result["power_spectrum"] = {
            "psd": [float(x) for x in psd],
            "freqs": [float(f) for f in freqs],
            "alpha_fit": float(alpha) if not np.isnan(alpha) else None,
            "alpha_r2": float(psd_r2) if not np.isnan(psd_r2) else None,
            "signature": classify_spectrum(alpha),
        }

    return result


def classify_spectrum(alpha):
    if np.isnan(alpha):
        return "unknown"
    if abs(alpha) < 0.2:
        return "white noise (Markovian, flat PSD)"
    elif 0.5 <= alpha <= 1.5:
        return "pink / 1/f (scale-free, non-Markovian memory)"
    elif alpha > 1.5:
        return "brown / 1/f² (random walk, strong memory)"
    elif alpha < -0.2:
        return "blue noise (anti-correlated)"
    else:
        return f"intermediate (alpha={alpha:.2f})"


def main():
    print("=" * 70)
    print("Paper 10 Corollary 4 Extended Validation")
    print("Correctness-stratified + Fourier power spectrum")
    print("=" * 70)

    results = []
    for fname in TARGET_FILES:
        path = RESULTS_DIR / fname
        if not path.exists():
            continue
        print(f"\n[PROCESS] {fname}")
        r = analyze_correctness_stratified(path)
        if r is None:
            print("  insufficient data")
            continue

        print(f"  total sequences: {r['total_sequences']}")

        for key in ("correct", "incorrect"):
            g = r[key]
            if not g["available"]:
                print(f"  {key:<10} n={g['n']:<4} [not enough data]")
                continue
            print(
                f"  {key:<10} n={g['n']:<4} mean_CR={g['mean_CR']:.2f}  "
                f"tau_c={g['tau_c_tokens']:.2f}  R2={g['r2_exp_fit']:.3f}"
            )

        if "power_spectrum" in r:
            ps = r["power_spectrum"]
            print(
                f"  power spectrum: alpha={ps['alpha_fit']:.3f} (R2={ps['alpha_r2']:.2f})  "
                f"=> {ps['signature']}"
            )

        results.append(r)

    output_path = OUTPUT_DIR / "cr_stratified_results_20260423.json"
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved: {output_path}")

    # Cross-dataset summary
    print("\n" + "=" * 70)
    print("Cross-dataset summary:")
    print("=" * 70)
    print(f"{'File':<55} {'correct_tau':>11} {'wrong_tau':>10} {'alpha':>7}")
    for r in results:
        c = r["correct"]
        w = r["incorrect"]
        ps = r.get("power_spectrum", {})
        ct = f"{c['tau_c_tokens']:.2f}" if c.get("tau_c_tokens") is not None else "N/A"
        wt = f"{w['tau_c_tokens']:.2f}" if w.get("tau_c_tokens") is not None else "N/A"
        al = f"{ps.get('alpha_fit', float('nan')):.2f}" if ps.get("alpha_fit") is not None else "N/A"
        print(f"{r['file']:<55} {ct:>11} {wt:>10} {al:>7}")


if __name__ == "__main__":
    main()
