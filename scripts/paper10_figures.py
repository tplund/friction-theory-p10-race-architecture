"""
Paper 10 figures: generate PNG figures for skeleton + preprint.

Figures produced:
  fig1_race_cycle.png — RACE cycle schematic (evaluation -> competition -> commit)
  fig2_schwinger_keldysh_contour.png — closed-time-path contour
  fig3_cr_autocorrelation_empirical.png — empirical CR autocorrelation exp decay
  fig4_substrate_timescale_ladder.png — photon to civilization timescale span
  fig5_parameter_limit_unification.png — 4 corollaries as regimes of SK
  fig6_monte_carlo_non_markovian.png — real vs white-noise comparison
"""
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

ROOT = Path("C:/_proj/FriktionsLLM")
FIG_DIR = ROOT / "docs" / "figures" / "paper10"
FIG_DIR.mkdir(parents=True, exist_ok=True)
ANALYSIS_DIR = ROOT / "data" / "paper10_analysis"

plt.rcParams.update({
    "font.size": 11,
    "axes.labelsize": 12,
    "axes.titlesize": 13,
    "figure.dpi": 120,
})


def fig1_race_cycle():
    """RACE cycle schematic."""
    fig, ax = plt.subplots(figsize=(9, 4))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4)
    ax.axis("off")

    # Phase 1: Evaluation
    ax.add_patch(mpatches.FancyBboxPatch(
        (0.3, 1.3), 2.5, 1.4, boxstyle="round,pad=0.05",
        facecolor="#cfe8ff", edgecolor="#1f77b4", linewidth=2
    ))
    ax.text(1.55, 2.4, "Evaluation", ha="center", fontweight="bold", fontsize=12)
    ax.text(1.55, 1.9, "parallel candidates", ha="center", style="italic", fontsize=10)
    ax.text(1.55, 1.55, "path integral / ensemble", ha="center", fontsize=9, color="#555")
    ax.text(1.55, 0.9, "A1, A2", ha="center", fontsize=9, color="#888")

    # Phase 2: Competition
    ax.add_patch(mpatches.FancyBboxPatch(
        (3.8, 1.3), 2.5, 1.4, boxstyle="round,pad=0.05",
        facecolor="#ffe5b4", edgecolor="#d6862d", linewidth=2
    ))
    ax.text(5.05, 2.4, "Competition", ha="center", fontweight="bold", fontsize=12)
    ax.text(5.05, 1.9, "interference / selection", ha="center", style="italic", fontsize=10)
    ax.text(5.05, 1.55, "under finite-time budget", ha="center", fontsize=9, color="#555")
    ax.text(5.05, 0.9, "A3", ha="center", fontsize=9, color="#888")

    # Phase 3: Commit
    ax.add_patch(mpatches.FancyBboxPatch(
        (7.3, 1.3), 2.5, 1.4, boxstyle="round,pad=0.05",
        facecolor="#c8e6c9", edgecolor="#2ca02c", linewidth=2
    ))
    ax.text(8.55, 2.4, "Commit", ha="center", fontweight="bold", fontsize=12)
    ax.text(8.55, 1.9, "pointer state selected", ha="center", style="italic", fontsize=10)
    ax.text(8.55, 1.55, "irreversibly", ha="center", fontsize=9, color="#555")
    ax.text(8.55, 0.9, "A4, A5", ha="center", fontsize=9, color="#888")

    # Arrows
    ax.annotate("", xy=(3.7, 2), xytext=(2.9, 2),
                arrowprops=dict(arrowstyle="->", lw=2, color="#333"))
    ax.annotate("", xy=(7.2, 2), xytext=(6.4, 2),
                arrowprops=dict(arrowstyle="->", lw=2, color="#333"))

    ax.text(5, 3.5, "RACE: Parallel Evaluation, Competition, Commit",
            ha="center", fontsize=14, fontweight="bold")
    ax.text(5, 0.3, "Substrate-agnostic; each phase manifests differently by substrate",
            ha="center", fontsize=10, style="italic", color="#555")

    plt.tight_layout()
    out = FIG_DIR / "fig1_race_cycle.png"
    plt.savefig(out, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  saved {out.name}")


def fig2_schwinger_keldysh_contour():
    """Closed-time-path contour figure."""
    fig, ax = plt.subplots(figsize=(8, 4.5))

    # Forward branch
    t_fwd = np.linspace(0, 8, 100)
    y_fwd = np.full_like(t_fwd, 0.4)
    ax.plot(t_fwd, y_fwd, "b-", lw=2.5, label="$C_+$ (forward branch)")
    ax.annotate("", xy=(4.2, 0.4), xytext=(3.8, 0.4),
                arrowprops=dict(arrowstyle="->", lw=2.5, color="blue"))

    # Turnaround
    theta = np.linspace(-np.pi/2, np.pi/2, 30)
    x_turn = 8 + 0.3*np.cos(theta)
    y_turn = 0.2 + 0.2*np.sin(theta)
    ax.plot(x_turn, y_turn, "purple", lw=2.5)

    # Backward branch
    t_bwd = np.linspace(8, 0, 100)
    y_bwd = np.full_like(t_bwd, 0.0)
    ax.plot(t_bwd, y_bwd, "r-", lw=2.5, label="$C_-$ (backward branch)")
    ax.annotate("", xy=(3.8, 0.0), xytext=(4.2, 0.0),
                arrowprops=dict(arrowstyle="->", lw=2.5, color="red"))

    # Time axis
    ax.annotate("", xy=(8.5, -0.7), xytext=(-0.3, -0.7),
                arrowprops=dict(arrowstyle="->", lw=1))
    ax.text(8.3, -0.9, "real time $t$", ha="right", fontsize=11)

    # Markers
    ax.plot([0, 0], [-0.05, 0.45], "k-", lw=1)
    ax.text(0, -0.25, "$t_0$", ha="center", fontsize=11)
    ax.text(8.0, -0.25, "$t_\\mathrm{max}$", ha="center", fontsize=11)

    # Field labels
    ax.text(4, 0.55, "$\\phi_+$", ha="center", fontsize=14, color="blue")
    ax.text(4, -0.12, "$\\phi_-$", ha="center", fontsize=14, color="red")

    # Caption-like text
    ax.text(4, 1.1,
            "$Z[J_+, J_-] = \\int \\mathcal{D}\\phi_+ \\mathcal{D}\\phi_-\\, e^{iS[\\phi_+]/\\hbar - iS[\\phi_-]/\\hbar + iS_\\mathrm{IF}[\\phi_+,\\phi_-]}$",
            ha="center", fontsize=12)

    ax.set_xlim(-0.5, 9.5)
    ax.set_ylim(-1.2, 1.5)
    ax.axis("off")
    ax.legend(loc="lower left", fontsize=10)
    ax.set_title("Schwinger-Keldysh Closed-Time-Path Contour", fontsize=13)

    plt.tight_layout()
    out = FIG_DIR / "fig2_schwinger_keldysh_contour.png"
    plt.savefig(out, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  saved {out.name}")


def fig3_cr_autocorrelation():
    """Empirical CR-autocorrelation decay across 5 clean datasets."""
    path = ANALYSIS_DIR / "cr_autocorrelation_results_20260423.json"
    if not path.exists():
        print(f"  SKIP fig3: missing {path}")
        return
    with open(path) as f:
        data = json.load(f)

    fig, ax = plt.subplots(figsize=(8, 5.5))

    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
    labels = {
        "temp_sweep_logprobs_full.jsonl": "Temp-sweep (unknown)",
        "truthfulqa_calibrated_base.jsonl": "qwen3-4b-base",
        "gsm8k_cr_validation_qwen3_235b.jsonl": "Qwen3-235B-Instruct-2507",
        "creativity_temperature_sweep.jsonl": "Creativity-sweep (unknown)",
        "mixed_eval_v3_multijudge_liquid.jsonl": "LiquidAI LFM2",
    }

    for i, rec in enumerate(data):
        fname = rec["file"]
        if fname not in labels:
            continue
        mc = np.array(rec["mean_corr_tau"])
        taus = np.arange(len(mc))
        gamma = rec["Gamma_eff"]
        tau_c = rec["tau_c_tokens"]
        r2 = rec["r2_exp_fit"]
        # Observed
        ax.plot(taus, mc, "o-", color=colors[i % len(colors)], markersize=5,
                label=f"{labels[fname]}  ($\\tau_c$={tau_c:.2f}, R²={r2:.3f})")
        # Fit
        fitted = np.exp(-gamma * taus)
        ax.plot(taus, fitted, "--", color=colors[i % len(colors)], alpha=0.5, lw=1)

    ax.set_xlabel("Lag $\\tau$ (tokens)", fontsize=12)
    ax.set_ylabel("Autocorrelation $C_\\mathrm{CR}(\\tau)/C_\\mathrm{CR}(0)$", fontsize=12)
    ax.set_title("Empirical CR-autocorrelation decay across 5 clean LLM substrates",
                 fontsize=12)
    ax.legend(loc="upper right", fontsize=9)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 29)
    ax.set_ylim(-0.1, 1.05)
    ax.axhline(0, color="gray", lw=0.5)

    plt.tight_layout()
    out = FIG_DIR / "fig3_cr_autocorrelation_empirical.png"
    plt.savefig(out, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  saved {out.name}")


def fig4_substrate_timescale_ladder():
    """Substrate-timescale ladder from photon to civilization."""
    fig, ax = plt.subplots(figsize=(9, 5))

    substrates = [
        ("Photon ($\\tau=0$)", 1e-25, "null proper time"),
        ("Electron", 1e-23, "decoherence"),
        ("Atomic/molecular", 1e-15, "thermal decoherence"),
        ("Microsecond chemistry", 1e-6, ""),
        ("LLM token (forward pass)", 1e-1, "compute substrate"),
        ("Neural spike", 1e-2, "biological commit"),
        ("Cognitive decision", 1e0, "perceptual commit"),
        ("Behavioural choice", 1e2, ""),
        ("Lifetime trajectory", 1e9, "biographical commit"),
        ("Civilizational path", 1e16, "cultural commit"),
    ]

    log_times = [np.log10(t) if t > 0 else -26 for _, t, _ in substrates]
    names = [s[0] for s in substrates]
    notes = [s[2] for s in substrates]

    y_pos = np.arange(len(substrates))
    colors_grad = plt.cm.viridis(np.linspace(0.1, 0.9, len(substrates)))
    ax.barh(y_pos, log_times, color=colors_grad, edgecolor="black", alpha=0.8)

    for i, (name, note) in enumerate(zip(names, notes)):
        offset = log_times[i] + 0.5
        ax.text(offset, i, note, va="center", fontsize=9, color="#555")

    ax.set_yticks(y_pos)
    ax.set_yticklabels(names)
    ax.set_xlabel("$\\log_{10}(\\tau_c)$  [seconds]", fontsize=12)
    ax.set_title("Substrate-timescale ladder: $\\tau_c$ spans ~40 orders of magnitude",
                 fontsize=12)
    ax.axvline(0, color="red", lw=1, linestyle=":", alpha=0.7)
    ax.text(0.2, len(substrates) - 0.5, "1 s", color="red", fontsize=9)
    ax.grid(True, alpha=0.3, axis="x")

    plt.tight_layout()
    out = FIG_DIR / "fig4_substrate_timescale_ladder.png"
    plt.savefig(out, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  saved {out.name}")


def fig5_parameter_limit_unification():
    """4 corollaries as parameter regimes of Schwinger-Keldysh."""
    fig, ax = plt.subplots(figsize=(9, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis("off")

    # Central box: SK
    ax.add_patch(mpatches.FancyBboxPatch(
        (3.5, 2.8), 3, 1.4, boxstyle="round,pad=0.1",
        facecolor="#ffd1dc", edgecolor="black", linewidth=2.5
    ))
    ax.text(5, 3.75, "Schwinger-Keldysh\ngenerating functional", ha="center",
            fontweight="bold", fontsize=11)
    ax.text(5, 3.1, "$Z[J_+, J_-]$, axioms A1-A5", ha="center", fontsize=9, color="#555")

    # Four corollaries
    corollaries = [
        (1.0, 5.3, "Corollary 1\nQuantum regime", "#a8d8ea", "$\\hbar$ finite, $D \\to 0$",
         "Feynman path integral"),
        (8.9, 5.3, "Corollary 3\nBiological regime", "#c8e6c9", "Markov blanket + thermal",
         "Friston FEP $F[q]$"),
        (1.0, 1.5, "Corollary 2\nClassical stochastic", "#ffe5b4", "$\\hbar \\to 0$, $D$ finite",
         "Onsager-Machlup\n+ Freidlin-Wentzell"),
        (8.9, 1.5, "Corollary 4\nComputational (LLM)", "#e1bee7", "discrete-time sampling",
         "CR signal =\nKeldysh threshold-\nfunctional"),
    ]
    for x, y, name, color, cond, result in corollaries:
        ax.add_patch(mpatches.FancyBboxPatch(
            (x-1.2, y-0.7), 2.4, 1.4, boxstyle="round,pad=0.1",
            facecolor=color, edgecolor="black", linewidth=1.5
        ))
        ax.text(x, y+0.4, name, ha="center", fontweight="bold", fontsize=10)
        ax.text(x, y+0.05, cond, ha="center", fontsize=8, color="#555", style="italic")
        ax.text(x, y-0.45, result, ha="center", fontsize=8, color="#333")

    # Arrows from center to corners
    for (x, y, _, _, _, _) in corollaries:
        ax.annotate("", xy=(x + (0.9 if x < 5 else -0.9), y - 0.3 if y > 3.5 else y + 0.3),
                    xytext=(5 + (-1.3 if x < 5 else 1.3), 3.5 + (0.4 if y > 3.5 else -0.4)),
                    arrowprops=dict(arrowstyle="->", lw=1.5, color="#333"))

    ax.text(5, 6.5, "Parameter-limit unification: 4 disparate frameworks as regimes of one derivation",
            ha="center", fontsize=12, fontweight="bold")
    ax.text(5, 0.3, "$\\hbar$, $D$, $T$, substrate-structure parametre differentierer regimer",
            ha="center", fontsize=10, style="italic", color="#555")

    plt.tight_layout()
    out = FIG_DIR / "fig5_parameter_limit_unification.png"
    plt.savefig(out, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  saved {out.name}")


def fig6_monte_carlo_non_markovian():
    """Monte Carlo validation: real data non-Markovian vs white noise."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5))

    path_mc = ANALYSIS_DIR / "non_markovian_monte_carlo_20260423.json"
    if not path_mc.exists():
        print(f"  SKIP fig6: missing {path_mc}")
        return
    with open(path_mc) as f:
        mc_data = json.load(f)

    # Left: reliable fits count
    real_n_reliable = mc_data["observed"]["n_reliable"]
    mc_reliables = [t["n_reliable"] for t in mc_data["monte_carlo"]]
    categories = ["Real LLM CR", "MC white noise\n(trial 1)",
                  "MC (trial 2)", "MC (trial 3)"]
    values = [real_n_reliable] + mc_reliables
    colors = ["#d62728", "#bbbbbb", "#bbbbbb", "#bbbbbb"]
    ax1.bar(categories, values, color=colors, edgecolor="black")
    for i, v in enumerate(values):
        ax1.text(i, v + 0.3, str(v), ha="center", fontsize=10, fontweight="bold")
    ax1.set_ylabel("Reliable per-sequence PSD fits (R² > 0.3)", fontsize=11)
    ax1.set_title("Real data has ~7× more structured sequences than white noise",
                  fontsize=11)
    ax1.tick_params(axis="x", labelsize=9)

    # Right: fraction 1/f classified
    real_frac = mc_data["observed"]["frac_1f"]
    mc_fracs = [t["frac_1f"] for t in mc_data["monte_carlo"]]
    vals2 = [real_frac] + mc_fracs
    ax2.bar(categories, vals2, color=colors, edgecolor="black")
    for i, v in enumerate(vals2):
        ax2.text(i, v + 0.02, f"{v:.3f}", ha="center", fontsize=10, fontweight="bold")
    ax2.set_ylabel("Fraction classified 1/f (non-Markovian)", fontsize=11)
    ax2.set_title("Real 1/f rate ≈ 94%; white noise 0%",
                  fontsize=11)
    ax2.set_ylim(0, 1.1)
    ax2.axhline(0.938, color="red", lw=1, linestyle=":", alpha=0.5)
    ax2.tick_params(axis="x", labelsize=9)

    fig.suptitle("Non-Markovian subpopulation finding: SIGNAL, not selection bias",
                 fontsize=13, fontweight="bold", y=1.02)

    plt.tight_layout()
    out = FIG_DIR / "fig6_monte_carlo_non_markovian.png"
    plt.savefig(out, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  saved {out.name}")


def main():
    print("Generating Paper 10 figures...")
    print(f"Output dir: {FIG_DIR}")
    print()

    fig1_race_cycle()
    fig2_schwinger_keldysh_contour()
    fig3_cr_autocorrelation()
    fig4_substrate_timescale_ladder()
    fig5_parameter_limit_unification()
    fig6_monte_carlo_non_markovian()

    print()
    print(f"All figures generated in {FIG_DIR}")


if __name__ == "__main__":
    main()
