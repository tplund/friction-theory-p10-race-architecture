# Paper 10 Submission Package

**Paper:** *Race all the way down, race all the way up: A substrate-universal race-architecture across quantum, classical, biological, and computational regimes*

*(Working subtitle: A Schwinger-Keldysh derivation with a universal inverted-U signature)*


**Author:** Tomas Pødenphant Lund (Independent Research, Aarhus)

**Status:** Open research program. Companion to Paper 1 (Pødenphant Lund 2026b) which establishes Friction Theory (FT) on biological/cognitive/computational substrates.

**Target venues (priority order):**
1. *Foundations of Physics* (primary — fits the formal-derivation + interpretation-engagement scope)
2. *Synthese* (secondary — philosophy-of-physics venue if FoP rejects)
3. *Behavioral and Brain Sciences* target article (wildcard — if integrative-review framing is preferred)

**Companion preprint route:** arXiv (`physics.gen-ph` or `cond-mat.stat-mech`), PhilSci-Archive, FQXi essay-contest.

---

## Contents

```
paper10_submission_package/
├── README.md                              (this file)
├── manuscript/
│   ├── paper10_english.md                 (~18,000 words main manuscript, §1–§11 incl. §1.5 7-case + §1.6 3-observable + §2.1.5 Newton-Econ + §6 distributional)
│   ├── paper10_dansk_laesbar.md           (Danish reader version, ~7000 words; located in docs/dansk_til_tomas/ per HARD RULE no_danish_in_submission_packages)
│   ├── paper10_dansk_kort.md              (Danish executive summary; located in docs/dansk_til_tomas/)
│   ├── paper10_derivation_details.md      (formal derivations 5A-5E, ~3000 words)
│   └── paper10_bibliography.md            (~50 references, annotated)
├── figures/
│   ├── fig1_race_cycle.png                (race cycle schematic)
│   ├── fig2_schwinger_keldysh_contour.png (closed-time-path diagram)
│   ├── fig3_cr_autocorrelation_empirical.png (empirical CR-autocorr decay, 5 substrates)
│   ├── fig4_substrate_timescale_ladder.png (40-orders-of-magnitude clock-rate span)
│   ├── fig5_parameter_limit_unification.png (4 corollaries as regimes of one derivation)
│   └── fig6_monte_carlo_non_markovian.png (non-Markovian = real signal validation)
├── data/
│   ├── cr_autocorrelation_results_20260423.json
│   ├── cr_stratified_results_20260423.json
│   ├── exploratory_A1_A4_results_20260423.json
│   ├── non_markovian_monte_carlo_20260423.json
│   ├── non_markovian_scan_results_20260423.json
│   ├── ollama_scaling_summary_20260424.json
│   └── quantum_critical_scaling_20260423.json
└── scripts/
    ├── paper10_cr_autocorrelation_analysis.py     (Prediction #1 + #2 main analysis)
    ├── paper10_cr_stratified_validation.py        (correctness + Fourier PSD)
    ├── paper10_exploratory_analyses.py            (A1-A4: CR-entropy, position, task, Markov)
    ├── paper10_non_markovian_monte_carlo.py       (1/f signal validation vs white noise)
    ├── paper10_non_markovian_scan.py              (per-sequence PSD scan)
    ├── paper10_ollama_scaling.py                  (base-model scaling via Ollama)
    ├── paper10_quantum_critical_scaling.py        (5-model size-vs-1/f-fraction test)
    ├── paper10_figures.py                         (regenerates all 6 figures)
    └── paper10_publication_clean.py               (manuscript build script)
```

## Headline findings (for cover letter)

1. **Theoretical (universal inverted-U, §1.5):** Any system satisfying R1+R2+R3 (parallel candidates + bounded resources + irreversible commit) exhibits an inverted U on its evaluation-to-commit-rate by structural necessity, independent of any specific dynamics. Five empirical cases tile this prediction across distinct physical scales: qubit decoherence-window (Preskill 2018; Krantz et al. 2019), stochastic resonance (Benzi 1981; Wiesenfeld-Moss 1995; Gammaitoni et al. 1998), Margolus-Levitin saturation (Margolus-Levitin 1998; Lloyd 2000), encoding-friction in learning (Pødenphant Lund 2026b), and Yerkes-Dodson behavioural arousal (Yerkes-Dodson 1908; Diamond et al. 2007). The unified pattern is independent corroboration of the substrate-universal race claim. Wallace's biocognition rate-distortion programme (Wallace, Leonova & Gochhait 2022; Wallace 2025a, 2025b) is the closest concurrent precedent in biology-and-cognition scope; FT extends to quantum + thermodynamic scales beyond Wallace's coverage and provides a substrate-free deductive argument that does not require rate-distortion machinery.

2. **Theoretical (Schwinger-Keldysh, §3):** race-axioms A1–A5 are satisfied by the Schwinger-Keldysh closed-time-path generating functional of any bipartite quantum system with einselected pointer basis and Markovian environment (Theorem §3.2). Four corollaries recover Feynman path integral (quantum), Onsager-Machlup (classical), Friston FEP (biological), and Paper 1's CR-signal (computational) as parameter-limits of one derivation.

2. **Empirical (LLM substrate):** CR-autocorrelation exponential decay confirmed across 5 clean datasets, R² 0.980–0.997 (~1600 sequences, four+ model architectures, post thinking-mode audit excluding 19 contaminated files).

3. **Empirical (Markovian assumption):** Aggregate Fourier power spectrum α ≈ 0.1 (white-noise regime) across 4 datasets. Theorem assumption (ii) Markovianity empirically validated at ensemble level.

4. **Empirical (non-Markovian subpopulation, reframed Phase 4zz-17):** ~1% of sequences exhibit 1/f spectrum (α 0.7–0.95). Monte Carlo validation against matched white-noise gave 0% 1/f classification — non-Markovian finding is *real signal*, not selection bias. Per §1.6 three-observable framework + §4.4 reframing: this is the LLM-substrate's instantiation of the **substrate-universal pink-noise observable** (energy radiated to environment from abandoned candidate-routes via R1 parallel-evaluation-phase decoherence), the same signature that appears in Hooge resistor-noise (1969), Bak-Tang-Wiesenfeld SOC (1987), Beggs-Plenz neural avalanches (2003), and Cont financial-market 1/f (2001). Attention-head memory effects remain a plausible domain-specific implementation, but the framework-level claim is cross-substrate persistence of the 1/f exponent.

5. **Empirical (size scaling):** Within Qwen2.5-instruct family, τ_c decreases monotonically from 0.306 (0.5B) to 0.100 (3B) tokens (3× reduction over 6× parameters; n=3 datapoints, R² ≥ 0.97 each fit).

6. **Theoretical extension (Paper 1 cross-paper integration):** §6 derives five distributional regimes (Gauss, power-law, bimodal, exponential, log-normal) as parameter-limits of the same Schwinger-Keldysh apparatus. Provides formal foundation for distributional signature predictions (DSP-1 to DSP-5) and cross-paper anchor for HRP-3.σ/K/S/R/M empirical findings.

## Reproducibility

To reproduce the empirical analyses:

```bash
# From repository root
pip install -e .  # main friktionsllm package
cd docs/paper10_submission_package/scripts/
python paper10_cr_autocorrelation_analysis.py     # Finding 1+2
python paper10_cr_stratified_validation.py        # PSD + correctness
python paper10_non_markovian_monte_carlo.py       # Finding 4 validation
python paper10_quantum_critical_scaling.py        # 5-model test
python paper10_exploratory_analyses.py            # A1-A4 supplementary
python paper10_figures.py                         # Regenerate all figures
```

Source data is in main repository `data/results/*.jsonl`. Thinking-mode-contaminated datasets (19 files identified in 2026-04-23 audit per `docs/HARD_RULE_thinking_models.md`) are archived in `data/results/_archive_thinking_contaminated_20260423/` and excluded from all reported results.

## Submission status

- **Manuscript:** drafted, ~18,000 words, §1–§11 with prose, post-Phase-4zz-19 (incl. §1.5 seven-case empirical signature, §1.6 three-observable framework, §2.1.5 Newton-Econ-parallel, §6 distributional consequences). Ready for submission after final proofread.
- **Figures:** 6 figures generated, embedded in manuscript.
- **Bibliography:** 74 entries, annotated with section-citations; 18 Scite-spot-checked + 21 ISBN-verified textbook refs (see `docs/paper10_scite_verification_log.md`).
- **Empirical data + scripts:** ready, reproducible.
- **Danish reader versions:** ready for author's reference (not for submission).
- **Concession review:** completed 2026-04-26 per HARD_RULE_no_preemptive_concession. Phase 4zz expansion (universal inverted-U §1.5 + reframed Wallace prior art) requires re-running concession review under new framing.
- **Cross-paper integration:** §6 Distributional consequences integrated per Paper 1-session approval. Phase 4zz §1.5 substrate-universal claim broadcast to all papers (P0/P2/P3/P4/P6/P8/P11) 2026-04-30 sen aften 5.
- **Bibliography:** 61 entries, all Scite-verified.
- **Pending:** external peer review (cold-email path: Zurek, Rovelli, Friston, Wallace; arXiv preprint endorsement; FQXi community).

## Acknowledgments structure

The intellectual contribution is the author's: the foundational intuition (formulated 2026-04-21 after a winter sea-bath that the author now recognizes as structurally apt for race — bounded computational resources under thermal stress producing a substrate-timescale-shift in the very act of conceiving substrate-timescales), the framework name, the theoretical claims, and responsibility for errors.

The execution layer — discussion partner, literature search, mathematical derivation drafting (with author verification of each step), empirical analysis pipeline, figure generation, manuscript structuring, cross-paper coordination — was conducted in collaboration with Claude Sonnet 4.5 (Anthropic) over sessions 2026-04-23 to 2026-04-26.

This division should be acknowledged transparently in the published manuscript per emerging best practice for AI-assisted research output.

---

**Last updated:** 2026-04-30 sen aften 5 (Phase 4zz race-all-the-way integration: title-change + new §1.5 universal-inverted-U + Wallace-corpus reframed + Schwinger-Keldysh §3-§4-§8 cross-refs to §1.5).
