# Paper 10 — arXiv Submission Guide

**Status:** Manuscript er final efter pre-submission cleanup pas (race-rename, case-reordering, race-model tradition cite, særstatus-fjernelse) per 2026-05-02. Alle indholdsmæssige loose-ends resolved. Klar til preprint submission.

---

## arXiv form-felter (copy-paste klar)

### Title
```
Race all the way down, race all the way up: A substrate-universal race-architecture across quantum, classical, biological, and computational regimes
```

(Subtitle "A Schwinger-Keldysh derivation with a universal inverted-U signature" kan inkluderes i abstract eller som fodnote — arXiv har ikke separat subtitle-felt.)

### Authors
```
Tomas Pødenphant Lund
```

Affiliation: Independent Research, Aarhus, Denmark
Email: tomas.lund@frictiontheory.org

### Abstract (arXiv har 1920-tegns grænse — denne er ~1700 tegn)

```
We argue that "decision" in resource-bounded probabilistic systems is not a mental or agentive primitive but a substrate-universal structural phenomenon: the resolution of competing processes racing toward commit under a finite-time budget. Any system satisfying R1 (parallel candidates) + R2 (bounded resources) + R3 (irreversible commit) exhibits an inverted U on its evaluation-to-commit rate — too low yields no information processing, too high yields noise-dominated commit, and only the intermediate rate maximizes information throughput. Seven apparently independent phenomena — qubit decoherence-window, Ohm-Drude electron transport, chemistry/biochemistry molecular kinetics, stochastic resonance, Margolus-Levitin saturation, encoding-friction in learning, and Yerkes-Dodson — are manifestations of this single structural necessity across substrate scales spanning forty orders of magnitude in characteristic timescale. We refine R1-R3 to a five-axiom formulation A1-A5 appropriate for Schwinger-Keldysh derivation, and demonstrate that A1-A5 are satisfied by the closed-time-path generating functional of any bipartite quantum system with einselected pointer basis and Markovian environment. As corollaries we recover the Feynman path integral, Onsager-Machlup stochastic dynamics, the Friston free energy principle, and a CR-signal in large language models as parameter-regimes of one underlying derivation. Time emerges from commit-sequences. We engage interference, linearity-nonlinearity, and reversibility honestly: the framework relocates rather than solves the measurement problem.
```

### Categories (arXiv subject classifications)

**Primary**: `cond-mat.stat-mech` (Statistical Mechanics)
- *Rationale*: Schwinger-Keldysh formalism, Onsager-Machlup, Freidlin-Wentzell large deviations, 1/f noise universality, fluctuation-dissipation are all stat-mech subject matter. This is the most specific category and gives the right reviewer pool.

**Cross-list**:
1. `quant-ph` (Quantum Physics) — envariance Born-rule derivation, Zurek einselection, decoherence, three-hard-problems engagement
2. `physics.gen-ph` (General Physics) — substrate-universal claim across physics/cognition/computation, foundations engagement
3. `q-bio.NC` (Neurons and Cognition) — Friston FEP corollary, Yerkes-Dodson case #7, race-model tradition (Vickers/Ratcliff)
4. `cs.CL` (Computation and Language) — LLM CR-signal as case #6 + Corollary 4 empirical anchor
5. `nlin.AO` (Adaptation and Self-Organizing Systems) — substrate-universality of inverted-U, Belousov-Zhabotinsky chemical oscillators

(arXiv tillader 1 primary + max 3-5 cross-lists per submission — pick top 3 cross-lists based on which audiences you most want to reach.)

### Keywords (5-10, comma-separated)

```
race architecture, Schwinger-Keldysh formalism, substrate-universal dynamics, inverted-U signature, decoherence and einselection, Friston free energy principle, large language models, Onsager-Machlup, stochastic resonance, Yerkes-Dodson
```

### MSC Classification (mathematical subject codes — optional but useful)

- **Primary**: `82C70` (Transport processes in time-dependent statistical mechanics)
- **Secondary**: `81P05` (General foundations of quantum theory), `92B20` (Neural networks, biological / artificial), `81S22` (Open quantum systems / quantum master equations)

### PACS Classification (physics subject codes — optional)

- `05.30.-d` (Quantum statistical mechanics)
- `03.65.Yz` (Decoherence; open systems; quantum statistical methods)
- `05.40.-a` (Fluctuation phenomena, random processes, noise, and Brownian motion)
- `87.19.lo` (Information theory in cognition and behavior)

### Comments field (arXiv form)

```
24 pages excluding bibliography, 6 figures, 27,000 words including derivation appendix and bibliography. Companion to Pødenphant Lund 2026b (Paper 1, Friction Theory master). Target venue: Foundations of Physics.
```

### License

**Recommended**: `CC BY 4.0` (Creative Commons Attribution 4.0 International)
- Allows reuse with attribution; standard open-access license; compatible with most journals
- arXiv form: select "arXiv.org perpetual, non-exclusive license" + "CC BY 4.0" if asked

### Data and code availability statement (for arXiv comments or end-of-paper)

```
Code and data: https://github.com/tplund/friction-theory-p10-race-architecture (currently private; will be made public on submission)
```

---

## Format conversion (for arXiv upload)

arXiv accepts: LaTeX source (preferred), PDF only, or HTML.

### Option A: PDF only (simplest, acceptable for arXiv)

If you have pandoc installed:
```bash
cd docs/paper10_submission_package/manuscript/
pandoc paper10_english.md -o paper10_english.pdf \
  --pdf-engine=xelatex \
  --variable mainfont="Times New Roman" \
  --variable fontsize=11pt \
  --variable geometry=margin=1in \
  --variable linkcolor=blue \
  --toc --number-sections \
  --resource-path=../figures
```

If pandoc is not installed: install via `winget install JohnMacFarlane.Pandoc` (or download from pandoc.org), then run the above.

Upload the resulting PDF to arXiv submission form.

### Option B: LaTeX source (preferred by arXiv reviewers)

```bash
cd docs/paper10_submission_package/manuscript/
pandoc paper10_english.md -o paper10_english.tex \
  --standalone \
  --variable documentclass=article \
  --variable fontsize=11pt \
  --variable geometry=margin=1in \
  --resource-path=../figures
```

Then create a tar archive with:
- `paper10_english.tex`
- `figures/*.png` (6 figures)
- Optional: `paper10_bibliography.bib` (if you convert bibliography to BibTeX)

Upload tar archive to arXiv.

**Build status (2026-05-02 22:06):**
- `build/paper10_english.docx` — ✅ regenereret med dagens cleanup pas. Klar til at åbne i Word.
- `build/paper10_english.html` — ✅ regenereret, self-contained med embedded figures + MathJax. Klar til at åbne i browser.
- `build/paper10_english.tex` — ✅ regenereret. Klar til upload til arXiv (foretrukken format).
- `build/paper10_english.pdf` — ❌ slettet (gammel stale version fra 1. maj). Generer ny PDF via:
  - **Letteste vej**: Åbn `paper10_english.docx` i Word → File → Save as → PDF
  - **Alternativ**: Åbn `paper10_english.html` i browser → Print → Save as PDF
  - **arXiv-foretrukken**: Installer MiKTeX (~200 MB), så kan pandoc generere PDF direkte med `--pdf-engine=xelatex` (eller upload `.tex` source direkte til arXiv som accepterer det og genererer PDF selv).

### Option C: Submit master Markdown directly to arXiv

arXiv does not accept raw `.md` files. You must convert to PDF or LaTeX first.

---

## Pre-submission checklist

- [x] Master manuscript final (`paper10_english.md`, 18,442 words)
- [x] Bibliography clean (`paper10_bibliography.md`, 73 entries, all DOI-verified or textbook-confirmed)
- [x] Derivation appendix clean (`paper10_derivation_details.md`, 5,099 words, EN, no version-history)
- [x] Figures present (6 PNG files in `figures/`)
- [x] race-rename complete (no "RACE" caps anywhere)
- [x] Cases ordered by substrate-speed (#1 quantum → #7 behavior)
- [x] Race-model tradition acknowledgment in §2.2 (Vickers, Ratcliff, Logan, Smith-Ratcliff, Usher-McClelland, Brown-Heathcote, Cisek-Kalaska, Gold-Shadlen)
- [x] No internal session-narrative annotations (datoer, "Phase 4zz", commit hashes)
- [x] GitHub repo URL inserted in Reproducibility section: https://github.com/tplund/friction-theory-p10-race-architecture
- [ ] **YOU**: Push submission-package contents to GitHub repo (Monday when rate-limit refreshes)
- [ ] **YOU**: Switch repo to public on submission day
- [x] DOCX/HTML/TeX regenereret 2026-05-02 22:06 (build/)
- [ ] **YOU**: Generer PDF fra DOCX (Word → Save as PDF) eller upload .tex direkte til arXiv
- [ ] **YOU**: Submit to arXiv with form-fields above

---

## Companion documents to upload alongside (arXiv "ancillary files")

arXiv allows uploading "ancillary files" (data, code, supplementary) alongside the main paper. For Paper 10:

- `paper10_derivation_details.md` (derivation appendix)
- `paper10_bibliography.md` (annotated bibliography)
- Optional: data JSON files from `data/` (currently 7 files, ~1MB total)

Or simply point at the GitHub repo URL in the Reproducibility section (already done).

---

## After arXiv acceptance

1. **Update CROSS_PAPER_DASHBOARD.md** with arXiv DOI + URL
2. **Update Paper 10 master Reproducibility section** with arXiv URL (besides GitHub)
3. **Push GitHub repo to public** (currently private)
4. **Email outreach** per `paper10_outreach_emails_draft_2026_04_30.md` (Zurek, Rovelli, Friston, Wallace)
5. **Submit to Foundations of Physics** as primary target venue

---

## Quick-reference: All arXiv form fields

| Field | Value |
|---|---|
| Title | Race all the way down, race all the way up: A substrate-universal race-architecture across quantum, classical, biological, and computational regimes |
| Authors | Tomas Pødenphant Lund |
| Abstract | (1700 chars, see above) |
| Primary category | cond-mat.stat-mech |
| Cross-lists | quant-ph, physics.gen-ph, q-bio.NC (+optionally cs.CL, nlin.AO) |
| Keywords | race architecture, Schwinger-Keldysh formalism, substrate-universal dynamics, inverted-U signature, decoherence and einselection, Friston free energy principle, large language models, Onsager-Machlup, stochastic resonance, Yerkes-Dodson |
| MSC | 82C70 (primary), 81P05, 92B20, 81S22 |
| PACS | 05.30.-d, 03.65.Yz, 05.40.-a, 87.19.lo |
| Comments | 24 pages excluding bibliography, 6 figures, 27,000 words including derivation appendix and bibliography. Companion to Pødenphant Lund 2026b (Paper 1, Friction Theory master). Target venue: Foundations of Physics. |
| License | CC BY 4.0 |
| Reproducibility URL | https://github.com/tplund/friction-theory-p10-race-architecture |

---

*Submission guide written 2026-05-02 as part of Paper 10 final pre-submission pas.*
