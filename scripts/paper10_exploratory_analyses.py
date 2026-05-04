"""
Paper 10 Exploratory Analyses (A1-A4).

A1: CR vs entropy ratio — do CR and per_token_entropy relate as theory predicts?
A2: Token-position structure — does autocorrelation differ parse-phase vs generate-phase?
A3: Task-modality systematic — tau_c by task type (MC, open, math, creative)
A4: CR transition matrix — P(CR_{t+1} | CR_t), check Markov structure

All on existing clean data.
"""
import json
import numpy as np
from pathlib import Path
from collections import Counter, defaultdict
from scipy import stats

ROOT = Path("C:/_proj/FriktionsLLM")
RESULTS = ROOT / "data" / "results"
OUTPUT_DIR = ROOT / "data" / "paper10_analysis"
OUTPUT_DIR.mkdir(exist_ok=True)


# ======================================================================
# A1: CR vs entropy ratio
# ======================================================================

def a1_cr_entropy_relation():
    """Test if CR relates to Shannon entropy as predicted."""
    path = RESULTS / "entropy_cr_paired_cogito_671b.jsonl"
    if not path.exists():
        return {"error": "entropy_cr_paired file not found"}

    cr_all, ent_all = [], []
    with open(path, encoding="utf-8") as f:
        for line in f:
            try: r = json.loads(line)
            except: continue
            cr = r.get("per_token_cr", [])
            ent = r.get("per_token_entropy", [])
            if isinstance(cr, list) and isinstance(ent, list):
                for c, e in zip(cr, ent):
                    if isinstance(c, (int, float)) and isinstance(e, (int, float)):
                        if 0 < c < 100 and 0 <= e < 100:
                            cr_all.append(float(c))
                            ent_all.append(float(e))

    if len(cr_all) < 100:
        return {"error": "insufficient paired data"}

    cr_arr = np.array(cr_all)
    ent_arr = np.array(ent_all)

    # Correlation
    pearson_r, pearson_p = stats.pearsonr(cr_arr, ent_arr)
    spearman_rho, spearman_p = stats.spearmanr(cr_arr, ent_arr)

    # Theoretical: if CR counts top-probability tokens and entropy is Shannon's
    # H = -sum p log p, for broad distributions we expect monotonic relation.
    # For uniform on CR tokens (ideal): H ~ log(CR). Test this.
    # Compute log(CR) — for CR=1 (perfectly sharp), log=0; as CR grows, log grows.
    log_cr = np.log(cr_arr)
    r_log, p_log = stats.pearsonr(log_cr, ent_arr)

    # Bin by CR value, compute mean entropy
    bins = sorted(set(int(c) for c in cr_arr if c <= 20))[:20]
    binned_means = {}
    for b in bins:
        mask = cr_arr.astype(int) == b
        if mask.sum() >= 20:
            binned_means[b] = {
                "n": int(mask.sum()),
                "mean_entropy": float(ent_arr[mask].mean()),
                "std_entropy": float(ent_arr[mask].std()),
            }

    return {
        "n_tokens_paired": len(cr_all),
        "pearson_cr_entropy": {"r": pearson_r, "p": pearson_p},
        "spearman_cr_entropy": {"rho": spearman_rho, "p": spearman_p},
        "pearson_log_cr_entropy": {"r": r_log, "p": p_log},
        "binned_by_cr": binned_means,
        "cr_range": [float(cr_arr.min()), float(cr_arr.max())],
        "ent_range": [float(ent_arr.min()), float(ent_arr.max())],
    }


# ======================================================================
# A2: Token-position structure
# ======================================================================

CLEAN_FILES = [
    "truthfulqa_calibrated_base.jsonl",
    "gsm8k_cr_validation_qwen3_235b.jsonl",
    "mixed_eval_v3_multijudge_liquid.jsonl",
    "mixed_eval_v3_multijudge_cogito.jsonl",
    "creativity_temperature_sweep.jsonl",
    "design3_episode_chain.jsonl",
    "p23_fictive_mechanism.jsonl",
]


def a2_position_structure():
    """CR at each relative position (normalized 0–1)."""
    all_sequences = []
    for fname in CLEAN_FILES:
        path = RESULTS / fname
        if not path.exists(): continue
        with open(path, encoding="utf-8", errors="replace") as f:
            for line in f:
                try: r = json.loads(line)
                except: continue
                cr = r.get("per_token_cr")
                if not isinstance(cr, list) or len(cr) < 20:
                    continue
                arr = np.array([float(c) for c in cr if isinstance(c, (int, float))], dtype=float)
                arr = arr[arr < 100]
                if len(arr) >= 20:
                    all_sequences.append(arr)

    if not all_sequences:
        return {"error": "no sequences"}

    # Normalize positions to [0, 1] and bin
    n_bins = 20
    binned = [[] for _ in range(n_bins)]
    for seq in all_sequences:
        L = len(seq)
        for i, v in enumerate(seq):
            pos_normed = i / (L - 1) if L > 1 else 0.0
            bin_idx = min(int(pos_normed * n_bins), n_bins - 1)
            binned[bin_idx].append(v)

    positions = []
    for i, bin_vals in enumerate(binned):
        if bin_vals:
            positions.append({
                "bin_center": (i + 0.5) / n_bins,
                "n": len(bin_vals),
                "mean_CR": float(np.mean(bin_vals)),
                "std_CR": float(np.std(bin_vals)),
                "sem_CR": float(np.std(bin_vals) / np.sqrt(len(bin_vals))),
            })

    # Linear regression CR vs relative position
    all_positions = []
    all_crs = []
    for i, bin_vals in enumerate(binned):
        pos = (i + 0.5) / n_bins
        for v in bin_vals:
            all_positions.append(pos)
            all_crs.append(v)
    if len(all_positions) > 100:
        slope, intercept, r, p, _ = stats.linregress(all_positions, all_crs)
        regression = {"slope": float(slope), "intercept": float(intercept),
                      "pearson_r": float(r), "p": float(p)}
    else:
        regression = None

    # Also: compare first 25% vs last 25% via t-test
    first_q = []
    last_q = []
    for seq in all_sequences:
        L = len(seq)
        first_q.extend(seq[:max(L // 4, 1)].tolist())
        last_q.extend(seq[-max(L // 4, 1):].tolist())
    t, p_t = stats.ttest_ind(first_q, last_q, equal_var=False)
    first_vs_last = {
        "mean_first_quartile": float(np.mean(first_q)),
        "mean_last_quartile": float(np.mean(last_q)),
        "diff": float(np.mean(first_q) - np.mean(last_q)),
        "t_stat": float(t), "p": float(p_t),
    }

    return {
        "n_sequences": len(all_sequences),
        "n_tokens_total": sum(len(s) for s in all_sequences),
        "positions": positions,
        "regression_cr_vs_position": regression,
        "first_vs_last_quartile": first_vs_last,
    }


# ======================================================================
# A3: Task-modality systematic
# ======================================================================

def classify_task(fname, record):
    """Return task modality label."""
    fn = fname.lower()
    if "truthfulqa" in fn:
        return "mc"
    if "gsm8k" in fn or "math" in fn:
        return "math"
    if "creativity" in fn:
        return "creative"
    if "mixed_eval" in fn:
        return "mixed_eval"
    if "episode" in fn:
        return "narrative"
    if "fictive" in fn:
        return "creative"
    if "temp_sweep" in fn:
        return "qa"
    return "unknown"


def a3_task_modality():
    """Compute mean tau_c per task modality."""
    by_task = defaultdict(list)
    for fname in CLEAN_FILES + ["temp_sweep_logprobs_full.jsonl"]:
        path = RESULTS / fname
        if not path.exists(): continue
        with open(path, encoding="utf-8", errors="replace") as f:
            for line in f:
                try: r = json.loads(line)
                except: continue
                cr = r.get("per_token_cr")
                if not isinstance(cr, list) or len(cr) < 30:
                    continue
                arr = np.array([float(c) for c in cr if isinstance(c, (int, float))], dtype=float)
                arr = arr[arr < 100]
                if len(arr) < 30:
                    continue
                task = classify_task(fname, r)
                by_task[task].append(arr)

    results = {}
    for task, seqs in by_task.items():
        # Autocorrelation mean
        max_lag = 20
        corrs = []
        for s in seqs:
            if len(s) < max_lag + 1: continue
            c = s - s.mean()
            var = np.var(c)
            if var == 0: continue
            ac = np.zeros(max_lag)
            for lag in range(max_lag):
                if lag == 0: ac[lag] = var
                else: ac[lag] = np.mean(c[:-lag] * c[lag:])
            corrs.append(ac / ac[0])
        if len(corrs) < 3: continue
        mean_corr = np.mean(corrs, axis=0)
        # Fit tau_c
        from scipy.optimize import curve_fit
        try:
            popt, _ = curve_fit(lambda t, G: np.exp(-G * t), np.arange(max_lag),
                                mean_corr, p0=[0.1], bounds=(0, 10), maxfev=5000)
            gamma = float(popt[0])
            tau_c = 1.0 / gamma if gamma > 0 else float("nan")
            fitted = np.exp(-gamma * np.arange(max_lag))
            ss_res = np.sum((mean_corr - fitted) ** 2)
            ss_tot = np.sum((mean_corr - mean_corr.mean()) ** 2)
            r2 = 1 - ss_res / ss_tot
            results[task] = {
                "n_sequences": len(seqs),
                "mean_seq_len": float(np.mean([len(s) for s in seqs])),
                "mean_CR": float(np.mean([s.mean() for s in seqs])),
                "gamma": gamma, "tau_c": tau_c, "r2": float(r2),
            }
        except Exception:
            continue
    return results


# ======================================================================
# A4: CR transition matrix — Markov or higher order?
# ======================================================================

def a4_transition_matrix():
    """Estimate P(CR_{t+1} | CR_t) and test Markov property."""
    # Collect all paired (CR_t, CR_{t+1}) and triples (CR_{t-1}, CR_t, CR_{t+1})
    max_cr = 10  # cap for binning
    pair_counts = Counter()
    triple_counts = Counter()
    for fname in CLEAN_FILES:
        path = RESULTS / fname
        if not path.exists(): continue
        with open(path, encoding="utf-8", errors="replace") as f:
            for line in f:
                try: r = json.loads(line)
                except: continue
                cr = r.get("per_token_cr")
                if not isinstance(cr, list) or len(cr) < 3: continue
                cr_clipped = [min(int(c), max_cr) for c in cr
                              if isinstance(c, (int, float)) and 0 < c < 100]
                for i in range(len(cr_clipped) - 1):
                    pair_counts[(cr_clipped[i], cr_clipped[i+1])] += 1
                for i in range(len(cr_clipped) - 2):
                    triple_counts[(cr_clipped[i], cr_clipped[i+1], cr_clipped[i+2])] += 1

    if sum(pair_counts.values()) < 100:
        return {"error": "insufficient data"}

    # P(CR_{t+1} | CR_t) transition matrix
    row_totals = Counter()
    for (a, _), c in pair_counts.items():
        row_totals[a] += c
    transition = {}
    for (a, b), c in pair_counts.items():
        if row_totals[a] > 0:
            transition.setdefault(a, {})[b] = c / row_totals[a]

    # Test Markov: P(CR_{t+1}|CR_t, CR_{t-1}) ?= P(CR_{t+1}|CR_t)
    # If Markov, transition triples from same middle-state should give same distribution
    markov_deviation_score = 0.0
    markov_deviation_n = 0
    for middle in range(1, max_cr + 1):
        # Collect transitions (prev, next) where current = middle
        prev_groups = defaultdict(Counter)
        for (p, m, n), c in triple_counts.items():
            if m == middle:
                prev_groups[p][n] += c
        if len(prev_groups) < 2: continue
        # For each "prev", compute P(next|prev, middle)
        dists = {}
        for p, counter in prev_groups.items():
            total = sum(counter.values())
            if total < 20: continue
            dists[p] = {n: counter[n] / total for n in counter}
        if len(dists) < 2: continue
        # KL-divergence between each pair of distributions, averaged
        prevs = list(dists.keys())
        keys_all = set().union(*[set(d.keys()) for d in dists.values()])
        for i in range(len(prevs)):
            for j in range(i+1, len(prevs)):
                d1 = dists[prevs[i]]
                d2 = dists[prevs[j]]
                kl = 0.0
                for k in keys_all:
                    p = d1.get(k, 1e-6)
                    q = d2.get(k, 1e-6)
                    kl += p * np.log(p / q)
                markov_deviation_score += abs(kl)
                markov_deviation_n += 1

    mean_kl_deviation = markov_deviation_score / max(markov_deviation_n, 1)

    return {
        "n_pairs": sum(pair_counts.values()),
        "n_triples": sum(triple_counts.values()),
        "transition_matrix": {int(k): {int(kk): v for kk, v in vv.items()}
                               for k, vv in transition.items()},
        "markov_test_mean_kl_divergence": float(mean_kl_deviation),
        "markov_test_n_comparisons": markov_deviation_n,
        "markov_interpretation": "Markov if KL << 1; if KL >> 1, memory beyond first-order",
    }


# ======================================================================
# Main
# ======================================================================

def main():
    print("=" * 78)
    print("Paper 10 Exploratory Analyses (A1-A4)")
    print("=" * 78)

    print("\n[A1] CR vs entropy ratio")
    r1 = a1_cr_entropy_relation()
    if "error" in r1:
        print(f"  {r1['error']}")
    else:
        print(f"  n paired tokens: {r1['n_tokens_paired']}")
        print(f"  Pearson(CR, entropy):     r = {r1['pearson_cr_entropy']['r']:.3f}  p = {r1['pearson_cr_entropy']['p']:.4g}")
        print(f"  Spearman(CR, entropy):    rho = {r1['spearman_cr_entropy']['rho']:.3f}  p = {r1['spearman_cr_entropy']['p']:.4g}")
        print(f"  Pearson(log CR, entropy): r = {r1['pearson_log_cr_entropy']['r']:.3f}  p = {r1['pearson_log_cr_entropy']['p']:.4g}")
        print(f"  Theoretical: H ~ log(CR) for uniform distribution on top-K.")
        print(f"  Binned by CR (n >= 20 per bin):")
        for cr_val, stats_d in r1['binned_by_cr'].items():
            print(f"    CR={cr_val:2d}: n={stats_d['n']:<6} mean_H={stats_d['mean_entropy']:.3f}")

    print("\n[A2] Token-position structure")
    r2 = a2_position_structure()
    if "error" in r2:
        print(f"  {r2['error']}")
    else:
        print(f"  n sequences: {r2['n_sequences']}, n tokens: {r2['n_tokens_total']}")
        reg = r2['regression_cr_vs_position']
        if reg:
            print(f"  Linear regression CR vs normalized position:")
            print(f"    slope = {reg['slope']:.4f}  (positive = CR rises through sequence)")
            print(f"    Pearson r = {reg['pearson_r']:.4f}  p = {reg['p']:.4g}")
        flq = r2['first_vs_last_quartile']
        print(f"  First quartile mean CR: {flq['mean_first_quartile']:.3f}")
        print(f"  Last quartile mean CR:  {flq['mean_last_quartile']:.3f}")
        print(f"  Difference (first - last): {flq['diff']:.3f}  t = {flq['t_stat']:.2f}  p = {flq['p']:.4g}")

    print("\n[A3] Task-modality systematic")
    r3 = a3_task_modality()
    if r3:
        print(f"  {'task':<15} {'n_seq':>6} {'mean_CR':>8} {'tau_c':>8} {'R2':>6}")
        for task, s in sorted(r3.items()):
            tc = s['tau_c'] if s['tau_c'] != float('nan') else -1
            print(f"  {task:<15} {s['n_sequences']:>6} {s['mean_CR']:>8.3f} {tc:>8.3f} {s['r2']:>6.3f}")

    print("\n[A4] CR transition matrix + Markov test")
    r4 = a4_transition_matrix()
    if "error" in r4:
        print(f"  {r4['error']}")
    else:
        print(f"  n pairs: {r4['n_pairs']}, n triples: {r4['n_triples']}")
        print(f"  Transition matrix P(CR_next | CR_curr), first few rows:")
        for curr in sorted(r4['transition_matrix'].keys())[:5]:
            row = r4['transition_matrix'][curr]
            top = sorted(row.items(), key=lambda x: -x[1])[:4]
            top_str = ", ".join(f"{k}:{v:.3f}" for k, v in top)
            print(f"    CR={curr}: {top_str}")
        print(f"  Markov test (mean KL divergence): {r4['markov_test_mean_kl_divergence']:.4f}")
        print(f"  ({r4['markov_test_n_comparisons']} comparisons)")
        kl = r4['markov_test_mean_kl_divergence']
        if kl < 0.05:
            print("  => STRONG MARKOV: next-token distribution independent of history beyond current")
        elif kl < 0.2:
            print("  => APPROXIMATELY MARKOV: small deviation from first-order")
        else:
            print("  => NON-MARKOV: substantial history-dependence")

    # Save
    output_path = OUTPUT_DIR / "exploratory_A1_A4_results_20260423.json"
    with open(output_path, "w") as f:
        json.dump({"A1": r1, "A2": r2, "A3": r3, "A4": r4}, f, indent=2, default=str)
    print(f"\nSaved: {output_path}")


if __name__ == "__main__":
    main()
