# Paper 10 — Zenodo Deposit Metadata

**Workflow** (per Tomas-direktiv 2026-05-03): **Zenodo først**, så Arxiv. Files på Zenodo linker direkte til GitHub-repo (ingen separate file-upload til Zenodo). Zenodo-DOI cross-refereret i Arxiv-submission når den uploades.

---

## Zenodo deposit form — copy-paste ready

### Files

**Option A (recommended)**: Upload kun PDF (genereret fra `build/paper10_english.docx` via Word → Save as PDF). Code/data linker via "Related identifiers" til GitHub-repo.

**Option B**: Upload PDF + companion files (`paper10_derivation_details.md`, `paper10_bibliography.md`, `ARXIV_SUBMISSION_GUIDE.md`).

### Upload type

```
Publication → Preprint
```

### Basic information

**DOI**: Reserve a DOI now (Zenodo will assign on publish). Format: `10.5281/zenodo.{XXXXXXXX}` (sequential — likely ~20015XXX given P0/P1/P2/P3 are 19462500/20012655/20013491/20014122).

**Publication date**: 2026-05-03

**Title**:
```
Race all the way down, race all the way up: A substrate-universal race-architecture across quantum, classical, biological, and computational regimes
```

**Authors**:
```
Pødenphant Lund, Tomas
Affiliation: Independent Research, Aarhus, Denmark
ORCID: (insert if available — strongly recommended for citation tracking)
```

**Description / Abstract** (HTML allowed; plain text below ~1700 chars):

```
Scope note: Friction Theory (FT, Pødenphant Lund 2026b) formalizes bounded probabilistic computation systems satisfying the race-axioms. FT's established scope covers biological, cognitive, and computational substrates (Papers 1–6). This paper investigates whether FT's mathematical structure scales to physics-scope substrates (quantum measurement, classical mechanics, thermodynamics).

We argue that "decision" in resource-bounded probabilistic systems is not a mental or agentive primitive but a substrate-universal structural phenomenon: the resolution of competing processes racing toward commit under a finite-time budget. Any system satisfying R1 (parallel candidates) + R2 (bounded resources) + R3 (irreversible commit) exhibits an inverted U on its evaluation-to-commit rate — too low yields no information processing, too high yields noise-dominated commit, and only the intermediate rate maximizes information throughput. Seven apparently independent phenomena — qubit decoherence-window, Ohm-Drude electron transport, chemistry/biochemistry molecular kinetics, stochastic resonance, Margolus-Levitin saturation, encoding-friction in learning, and Yerkes-Dodson — are manifestations of this single structural necessity across substrate scales spanning forty orders of magnitude in characteristic timescale.

We refine R1-R3 to a five-axiom formulation A1-A5 appropriate for Schwinger-Keldysh derivation, and demonstrate that A1-A5 are satisfied by the closed-time-path generating functional of any bipartite quantum system with einselected pointer basis and Markovian environment. As corollaries we recover the Feynman path integral, Onsager-Machlup stochastic dynamics, the Friston free energy principle, and a CR-signal in large language models as parameter-regimes of one underlying derivation. Time emerges from commit-sequences. We engage interference, linearity-nonlinearity, and reversibility honestly: the framework relocates rather than solves the measurement problem.
```

**Version**: `v1.0` (eller `2026-05-03` hvis dato-baseret versioning foretrækkes)

**Language**: `English (eng)`

### Keywords (Zenodo accepts free-text keywords)

```
race architecture
Schwinger-Keldysh formalism
substrate-universal dynamics
inverted-U signature
decoherence and einselection
Friston free energy principle
large language models
Onsager-Machlup
stochastic resonance
Yerkes-Dodson
friction theory
quantum measurement
substrate timescale
race-model tradition
```

### Additional notes (optional)

```
Subtitle: A Schwinger-Keldysh derivation with a universal inverted-U signature.

Companion to Pødenphant Lund 2026b (Paper 1, Friction Theory master). Target peer-review venue: Foundations of Physics (primary), Synthese (secondary), Behavioral and Brain Sciences (fallback).

Code, data, analysis scripts, and supplementary materials available at GitHub: https://github.com/tplund/friction-theory-p10-race-architecture (will be made public on submission).

Companion documents (derivation appendix, bibliography, arXiv submission guide) available in the same repository.
```

### Funding / Grants

```
None (independent research)
```

### Related identifiers / Alternative identifiers

| Identifier | Relation | Description |
|---|---|---|
| `https://github.com/tplund/friction-theory-p10-race-architecture` | `isSupplementedBy` | Code, data, analysis scripts |
| `10.5281/zenodo.19462500` | `isPartOf` | Paper 0 (BFT — Behavioural Friction Theory) |
| `10.5281/zenodo.20012655` | `isContinuationOf` | Paper 1 (FT master — substrate-universal extension foundation) |
| `10.5281/zenodo.20013491` | `compiles` | Paper 2 (capacity scaling — companion empirical work) |
| `10.5281/zenodo.20014122` | `compiles` | Paper 3 (friction-guided inference — CR-signal source) |

(After Arxiv submission: also add Arxiv DOI as `isPreviousVersionOf`.)

### Contributors (optional, separate from authors)

```
Claude (Anthropic, 2025–2026) — Other (Research Assistant)
Role: Discussion partner, literature search, mathematical derivation drafting, empirical analysis, figure generation, manuscript structuring. The theoretical claims, foundational intuition (formulated by the author after a winter sea-bath, 2026-04-21), framework name, and responsibility for any errors are those of the author.
```

(Tomas's call whether to include — many academics prefer to leave AI-tool acknowledgment in the paper Acknowledgments section only, not as Zenodo Contributor.)

### References (optional — Zenodo can list cited works)

Skip for Zenodo deposit (bibliography is in the manuscript itself; duplicate-listing in Zenodo's Reference field adds maintenance burden without citation benefit).

### Communities (optional)

Search Zenodo communities for relevant ones; possible candidates:
- `Foundations of Physics`
- `Open Quantum Science`
- (any cognitive-science or AI-research community Tomas is part of)

### Subjects (optional, controlled vocabulary)

Use arXiv subject classifications as loose guidance:
- Statistical Mechanics (cond-mat.stat-mech)
- Quantum Physics (quant-ph)
- General Physics (physics.gen-ph)
- Neurons and Cognition (q-bio.NC)
- Computation and Language (cs.CL)

### License

```
Creative Commons Attribution 4.0 International (CC BY 4.0)
```

### Access right

```
Open Access
```

### Embargo

```
None
```

---

## Zenodo-metadata reuses arXiv-metadata 1:1

Most fields above are identical to those in `ARXIV_SUBMISSION_GUIDE.md`. Workflow:

1. **Today (Zenodo)**: Upload PDF to Zenodo with metadata above → get DOI like `10.5281/zenodo.{20015XXX}`
2. **Later (Arxiv)**: Upload `.tex` source (or PDF) to Arxiv with categories from `ARXIV_SUBMISSION_GUIDE.md` → get arXiv-id
3. **After both exist**: Add Arxiv-id as Related Identifier on Zenodo deposit (relation: `isPreviousVersionOf` or `isIdenticalTo` depending on whether content differs)

---

## After Zenodo deposit — update master + bibliography

When Zenodo DOI is assigned, update:

1. **`paper10_english.md` Reproducibility section** (line 904):
   ```
   Replace: https://github.com/tplund/friction-theory-p10-race-architecture
   With: https://github.com/tplund/friction-theory-p10-race-architecture (Zenodo DOI: 10.5281/zenodo.{YYY})
   ```

2. **`paper10_bibliography.md`**: When this paper is referenced as Pødenphant Lund 2026k or similar, add Zenodo DOI to its self-entry.

3. **`CROSS_PAPER_DASHBOARD.md`**: Add Paper 10 Zenodo DOI to other papers' bibliography entries that reference Paper 10.

---

## Quick-reference summary

| Field | Value |
|---|---|
| Upload type | Publication → Preprint |
| Title | Race all the way down, race all the way up: A substrate-universal race-architecture across quantum, classical, biological, and computational regimes |
| Authors | Pødenphant Lund, Tomas (Independent Research, Aarhus) |
| Publication date | 2026-05-03 |
| Version | v1.0 |
| Language | English |
| License | CC BY 4.0 |
| Access right | Open Access |
| Keywords | race architecture, Schwinger-Keldysh formalism, substrate-universal dynamics, inverted-U signature, decoherence and einselection, Friston free energy principle, large language models, Onsager-Machlup, stochastic resonance, Yerkes-Dodson, friction theory, quantum measurement, substrate timescale, race-model tradition |
| Funding | None (independent research) |
| Files | PDF only (rest linker til GitHub via Related Identifiers) |
| GitHub | https://github.com/tplund/friction-theory-p10-race-architecture |
| Related: P0 | 10.5281/zenodo.19462500 (isPartOf) |
| Related: P1 | 10.5281/zenodo.20012655 (isContinuationOf) |
| Related: P2 | 10.5281/zenodo.20013491 (compiles) |
| Related: P3 | 10.5281/zenodo.20014122 (compiles) |

---

*Zenodo metadata-fil skrevet 2026-05-03 som del af submission-prep. Cross-reference: `ARXIV_SUBMISSION_GUIDE.md` (samme metadata bruges for Arxiv-submission senere).*
