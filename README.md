# Race all the way down, race all the way up — data & code (Paper 10)

Reproducibility release for **Pødenphant Lund, T. (2026). *Race all the way down, race all the way up: A unifying vocabulary for bounded-commit dynamics across quantum, classical, biological, and computational substrates*. Zenodo.** https://doi.org/10.5281/zenodo.20014567

This repository holds the per-token log-probability datasets, the analysis scripts, the saved analysis outputs, and the figure-generation code behind the empirical sections of the paper.

## What the empirical part of the paper claims

The paper is a vocabulary-and-synthesis proposal rather than a new-physics paper, and its empirical component is correspondingly narrow. Language-model token generation is used as a **tractable substrate** in which bounded-commit dynamics can be measured directly, where the physical substrates the paper also organises (quantum decoherence, chemical kinetics, neural accumulation) cannot currently be instrumented at the relevant timescale.

The measured quantity is **Competing Routes (CR)**: per generated token, the count of candidate next-tokens above a probability threshold in the pre-commit softmax distribution. CR is introduced in Paper 1 and used here as a structural analogue of an equal-time Keldysh (distribution-width) observable, under assumptions stated explicitly in §4.3. Two results are reported: CR autocorrelation decays **exponentially** across substrates (R² 0.980–0.997) with a commit-timescale τ_c that varies by substrate, and a small non-Markovian sub-population departs from that decay, validated against a Monte Carlo null.

## Layout

```
scripts/                                   analysis + figure code (plain Python, no local package)
  paper10_cr_autocorrelation_analysis.py   §4.3 main result: exponential CR-autocorrelation decay, per-substrate tau_c
  paper10_non_markovian_monte_carlo.py     Monte Carlo null for the non-Markovian sub-population
  paper10_non_markovian_scan.py            scan identifying that sub-population
  paper10_cr_stratified_validation.py      protocol validation: PSD + stratification by correctness
  paper10_quantum_critical_scaling.py      cross-model scaling check
  paper10_base_model_scaling.py            base-vs-instruct comparison
  paper10_ollama_scaling.py                local-substrate scaling run
  paper10_exploratory_analyses.py          supplementary A1-A4 analyses
  paper10_figures.py                       regenerates the figures in figures/
data/
  results/*.jsonl                          the six per-token logprob datasets the analyses read
  paper10_analysis/*.json                  saved analysis outputs (the reference values quoted in the paper)
figures/                                   the six figures as they appear in the paper
manuscript/
  paper10_english.md                       the manuscript master
  paper10_bibliography.md                  annotated reference list
  paper10_derivation_details.md            derivation appendix: the CR-Keldysh substrate-mapping (§4.3)
                                           and the Onsager-Machlup classical-stochastic regime (§4.2)
```

## Reproduce

```bash
pip install -r requirements.txt
python scripts/paper10_cr_autocorrelation_analysis.py    # §4.3 exponential decay + per-substrate tau_c
python scripts/paper10_non_markovian_monte_carlo.py      # Monte Carlo null
python scripts/paper10_cr_stratified_validation.py       # protocol validation
python scripts/paper10_figures.py                        # regenerate figures/
```

Scripts resolve their paths relative to the repository root, so they run from a clone with no configuration. Each writes into `data/paper10_analysis/`, overwriting the saved copy — diff against the committed version to confirm a reproduction.

## Which datasets are included, and why

All reported results come from runs with **thinking-mode disabled** (`/no_think` on the Qwen3 family; thinking-disabled variants elsewhere), so that CR is measured on answer tokens rather than on a mixed reasoning/answer stream. Thinking-mode traces follow a different token distribution and are not comparable to direct-answer traces. Datasets identified as thinking-contaminated in an April 2026 audit were excluded from every reported result and are not included here; the six datasets in `data/results/` are the clean set the paper uses.

## Scope and limits

CR has a documented ceiling: it does not discriminate confident-right from confident-wrong (Paper 1 §9.1b). The paper treats it as a *component* of a Keldysh-like observable, not a complete one. The substrate-mapping in §4.3 is a structural correspondence under explicit assumptions (Gaussian approximation, discretization, Markovian modes), not a strict parameter-limit reduction; the derivation appendix in `manuscript/` sets these out in full.

## Licence

Code and data released under [CC BY 4.0](LICENSE).
