# Paper 10 — Hostile review prompts for ChatGPT / Gemini

**Status**: Round 1 complete (prompt 1 sent to both ChatGPT and Gemini 2026-05-21). Round 2 prompts below incorporate Round 1 findings so the LLMs can build on what's already been caught instead of repeating it.

**Master file** (give to LLM before any prompt):
- Path: `C:\_proj\FriktionsLLM\docs\paper10_submission_package\manuscript\paper10_english.md`
- Public URL: https://github.com/tplund/friction-theory-p10-race-architecture
- DOCX version: `C:\_proj\FriktionsLLM\docs\paper10_submission_package\build\p10_v21_post_hostile_review.docx`

---

## Background context to give the LLM (paste before any Round 2 prompt)

```
Paper 10 is a Foundations-of-Physics-bound paper claiming that bounded probabilistic computation systems (R1 parallel candidates + R2 bounded resources + R3 irreversible commit) exhibit substrate-universal structural properties, derived via Schwinger-Keldysh closed-time-path formalism. Three corollaries claim parameter-limits: §4.1 quantum (Feynman path integral), §4.2 classical (Onsager-Machlup), §4.3 computational (LLM CR-signal).

Version history:
- v1 (Zenodo 10.5281/zenodo.20014568, 2026-05-03): claimed R1+R2+R3 → universal inverted-U
- v2 (2026-05-21, internal): weakened per Wallace counterexample (Erlang-2 kernel → bimodal/U-shape via Lambert-W branch geometry); FEP-as-Corollary-3 removed
- v2.1 (2026-05-21, in repo): post-hostile-review fixes — R1 tightened to require non-trivial competitive interference; falsification criterion range-conditional; §4 split into Corollaries (§4.1+§4.2 strict parameter-limits) + substrate-mapping (§4.3 structural correspondence under Gaussian-approximation); §4.2 Onsager-Machlup sharpened with Kramers-rate commit; case #2 Drude demoted to bounded-resources analogy; Dutta-Horn reconciliation §1.6 + §3 Markovian assumption

Round 1 findings (already identified, do NOT repeat — build on these):

From ChatGPT (2026-05-21):
- Theorem "Race-Schwinger-Keldysh Equivalence" overclaimed; needs renaming to "Conditional representation theorem"
- A4 bundles decoherence + Born rule + outcome selection; needs splitting
- A5 Landauer claim too strong; weaken to "lower bound for logically irreversible recording/reset, not for every commit event"
- GR vs GK inconsistency in CR mapping — equal-time Keldysh GK is correct for distribution-width
- Empirical numbers inconsistent across master + derivation appendix (5 vs 6 datasets, 1600 vs 3200 sequences, R² 0.980-0.997 vs 0.901-0.997, τc ranges)
- Public package metadata (README, ZENODO_METADATA.md, GitHub headline) still v1 language
- §5E Noether/Higgs crackpot-adjacent — recommend remove or quarantine
- §9.3 Higgs-mass M-L test recommend remove
- "Time emerges from commit-sequences" too strong for abstract

From Gemini (2026-05-21):
- A3 conflates Margolus-Levitin (kinematic, isolated unitary) with Γ = Im(Σ^R) (dynamic, open-system dissipation) — category error
- 1/f reconciliation requires specific 1/τ-distributed environmental modes, not general Markovian superposition; "universal" 1/f overstates
- Falsifiability of "interior structure" too weak; almost no real curve is strictly monotone
- Born rule derivation via envariance is unnecessary baggage that imports contested literature

Author is implementing v2.2 fixes for these in parallel. Your job in Round 2 is to find FURTHER substantive issues that Round 1 did not catch, or to do deeper technical dives on specific paper sections.
```

---

## Prompt 2 — §3 Schwinger-Keldysh derivation deep stress test

```
[Background context above]

Now focus narrowly on §3 of Paper 10 (Schwinger-Keldysh derivation). The Theorem in §3.2 claims that any bipartite quantum system with (i) einselection, (ii) Markovianity, (iii) thermal initial state satisfies all five race-axioms A1-A5 via the closed-time-path generating functional. The proof sketch is 8 steps in §3.3. The companion derivation sketch (Section 5A-5E in C:\_proj\FriktionsLLM\docs\paper10_submission_package\manuscript\paper10_derivation_details.md) unpacks the proof in more detail.

YOUR TASK: Identify NEW technical problems in §3 that go beyond Round 1's findings (theorem renaming, A4 bundling, A5 Landauer overreach, GR vs GK, M-L vs Γ).

Specifically:

1. **Step-by-step audit of §3.3 proof sketch**: Walk through each of the 8 steps. For each step:
   - Is the derivation rigorous, or does it rely on "well-known" / "standard" claims without explicit citation?
   - Are there hidden assumptions that should be made explicit?
   - Does the step preserve the axiom-mapping consistently (e.g., if a step establishes A3, is it the same A3 used elsewhere in the paper)?

2. **Companion §5A-5E derivations**: Are these rigorous unpackings or hand-wavy filler? Particularly:
   - §5A envariance derivation of Born-rule (already noted as contested; identify NEW technical issues)
   - §5B CR-to-Keldysh mapping (already noted as overclaim; identify specific mathematical gaps)
   - §5D Onsager-Machlup derivation (does it cleanly derive OM from CTP, or is it asserted equivalence?)
   - §5E Noether reformulation (already flagged for removal; if it stays, identify technical issues)

3. **Foundations of Physics journal style**: This is the target venue. Their reviewers expect:
   - Explicit assumptions stated upfront
   - All claims derivable or cited
   - Notation defined before use
   - Distinguishing genuine derivations from structural mappings

   What would a Foundations of Physics referee specifically reject in §3 + §5?

4. **Limits and edge cases**: What substrates ARE strictly covered by §3 theorem after all assumptions? What's the actual derivation domain in physics terms (specific energy/temperature/coupling ranges)? Is this domain explicit in the paper?

Output: substantive new findings only. Do not repeat Round 1.
```

---

## Prompt 3 — §4 corollaries and substrate-mapping strictness

```
[Background context above]

Focus narrowly on §4 of Paper 10 (parameter-limit corollaries + substrate-mapping). Three sub-sections:
- §4.1: Quantum regime (Feynman path integral, Corollary 1)
- §4.2: Classical stochastic (Onsager-Machlup + Kramers-rate barrier crossings, Corollary 2)
- §4.3: Computational substrate-mapping (LLM CR-signal as structural correspondence, NOT strict parameter-limit per v2.1 demotion)

Round 1 already established:
- §4.3 should NOT be called "Corollary 3" — demoted to substrate-mapping (done in v2.1)
- §4.2 Onsager-Machlup → Kramers-rate commit clarification (done in v2.1)
- Case #2 Drude is bounded-resources analogy, not strict R1+R2+R3 (done in v2.1)

YOUR TASK: Identify NEW issues with §4.

1. **§4.1 (Quantum)**: Is the D→0 parameter-limit derivation rigorous? Does the paper explicitly show that the Feynman path integral emerges from CTP in this limit, or assert it? Are there subtleties about which path-integral measure is recovered?

2. **§4.2 (Classical)**: The ℏ→0, D-finite limit via Keldysh rotation → MSR → Onsager-Machlup. Is this chain of derivations actually shown in the paper, or only sketched/asserted? §4.2 now claims commit is via Kramers-rate barrier crossings — does the Kramers derivation appear anywhere, or is it cited only?

3. **§4.3 (Substrate-mapping)**: Even as demoted to "structural correspondence", the LLM CR-signal mapping requires:
   - Gaussian approximation on softmax (when valid? when not?)
   - Discretization assumption (what happens at finite token-step?)
   - Markovian-modes inheritance (does softmax-sampling actually satisfy this?)
   
   Are these assumptions adequately defended, or is the mapping still "trust me it works"?

4. **The figure 5 unification diagram**: The figure visualises three "regimes of one derivation". With v2.1's demotion of §4.3 to substrate-mapping, does this figure still claim too much? Should the figure be revised?

5. **Cross-corollary consistency**: If §4.1 quantum uses einselection commit, §4.2 classical uses Kramers-rate barrier crossings, and §4.3 uses softmax-sampling — are these three commit mechanisms actually instances of the same A4 axiom, or are they separate commit-mechanism families dressed up under a single axiom name?

Output: substantive new findings. Do not repeat Round 1.
```

---

## Prompt 4 — Seven empirical cases audit (R1+R2+R3 + kernel-shape consistency)

```
[Background context above]

Focus on §1.5 of Paper 10 — the seven empirical cases. Cases are (in v2.1 ordering):
1. Quantum decoherence-window
2. Ohm-Drude electron transport (caveat: demoted to bounded-resources analogy in v2.1)
3. Chemistry / biochemistry molecular kinetics
4. Stochastic resonance
5. Margolus-Levitin saturation
6. Encoding-friction in learning
7. Yerkes-Dodson arousal-performance

Round 1 already noted:
- Case 2 Drude doesn't satisfy strict R1 — demoted (done in v2.1)
- Case 4 SR is boundary case, noise-amplification rather than strict race
- Case 5 ML is a bound, not a commit-mechanism
- Marcus inverted region is on driving-force axis, not rate-parameter axis

YOUR TASK: Identify NEW issues with the seven cases.

1. **Each case audited for ALL three R1+R2+R3 (strict) tests**:
   - Case 1 Quantum decoherence-window: R1 ✓ (coherent superposition), R2 ✓ (energy + decoherence rate), R3 ✓ (pointer-basis selection). Solid.
   - Case 3 Chemistry / biochemistry: 
     - R1: parallel reaction pathways. Strict competitive interference? In Marcus theory yes; in simple single-product enzyme catalysis maybe not. Is this distinction made?
     - R2: thermal energy + diffusion + concentration. Always satisfied?
     - R3: irreversible bond-formation. But reversible reactions exist; when does R3 fail in chemistry?
   - Case 6 Encoding-friction (learning): does this case actually correspond to LLM-substrate (covered in §4.3) or biological-substrate (Paper 1 §6)? The §1.5 case-#6 entry says "LLM + biological"; in §4 it's only LLM. Inconsistency?
   - Case 7 Yerkes-Dodson: biological-substrate. Is the R1+R2+R3 mapping for Y-D explicit anywhere, or just asserted?

2. **Kernel-shape claim audit**: §1.5 v2 says all seven cases share "monotone-survival kernels" → inverted-U. Quick check:
   - Case 1: exponential decoherence — monotone-survival ✓
   - Case 2: drift-velocity bounded — monotone-survival but R1 questionable
   - Case 3: Arrhenius/Eyring exponential — monotone-survival, but BZ-oscillator is limit-cycle (NOT monotone-survival; internal kernel-tension in the chemistry case itself)
   - Case 4: SR depends on noise model
   - Case 5: ML bound — kernel?
   - Case 6: LLM softmax / biological learning — kernel?
   - Case 7: Y-D empirical — kernel?
   
   Is "all seven share monotone-survival kernels" actually verified case-by-case, or hypothesis-level?

3. **Forty orders of magnitude claim**: The paper repeatedly says "substrate scales spanning forty orders of magnitude". Trace this claim: which timescales for each case? Is the 40-OOM range actually documented, or rhetorical?

4. **Are there cases that should NOT be in the list?**: After v2.1 demotion of Drude, should others also be demoted? Specifically Case 4 SR (R1 forced) and Case 5 ML (R3 not really a mechanism). Six clean cases > seven mixed cases.

5. **Are there cases that SHOULD be in the list but aren't?**: What R1+R2+R3-strict substrates are well-documented in physics/biology literature that the paper misses?

Output: substantive new findings. Do not repeat Round 1.
```

---

## Prompt 5 — Internal tensions, scope-discipline, and Foundations of Physics readiness

```
[Background context above]

Final round. Read the whole paper (or as much as fits in your context window) as a single document. Find INTERNAL TENSIONS between sections that survive Round 1 and v2.1 fixes.

Round 1 caught:
- Markov assumption (§3) vs 1/f universal (§1.6) — partial reconciliation via Dutta-Horn in v2.1, but Gemini noted this still overstates universality
- Strong abstract vs §1.3 scope-disclaimer — softened in v2.1
- Empirical numbers inconsistency across files
- §5E Noether/Higgs crackpot-adjacent

YOUR TASK: Identify NEW internal tensions / scope-discipline issues.

1. **Abstract vs body audit**: Does the abstract still overstate the body? After v2.1 fixes, does the abstract reflect:
   - Range-conditional falsification
   - §4.3 as substrate-mapping (not Corollary 3)
   - Drude demoted to analogy
   - Kernel-conditional shape claim
   - Open-research scope-disclaimer
   
   List specific abstract sentences that still pull harder than body supports.

2. **§1.3 scope-disclaimer vs §4 corollaries**: §1.3 says "open research, not established FT content"; §4 develops formal corollaries. Are these still in tension? Could §1.3 be sharper about what IS and ISN'T established?

3. **§5 (Time emerges from race) and v2.1 corollary downgrade**: §5 makes claims about substrate-clock-rate that depend on the broader corollary structure. With §4.3 demoted, do §5's claims still hold? Particularly §5.2.5 (energy configuration as primary substrate parameter) which uses M-L and Landauer.

4. **§6 (Distributional consequences DSP-1-5)**: These are corollaries of the formal apparatus. After §4.3 demotion + Drude demotion, which DSPs still rest on §3 theorem and which rest on extended/analogical reasoning?

5. **§8 (race across QM-interpretations)**: Configuration-space realism, Many-Worlds, Bohmian, Copenhagen. Does this section's interpretation-agnosticism survive v2.1's tightened scope? Should §8 be reduced?

6. **§9 (Implications)**: AGI discourse, emergent time, cosmology, empirical program. With v2.1's narrower scope, are these implications still warranted, or are some of them now scope-overreach?

7. **§11 (Discussion)**: Does the discussion accurately reflect what has been ESTABLISHED vs what is CONJECTURED vs what is OPEN RESEARCH? Foundations of Physics expects clear bracketing.

8. **For Foundations of Physics referee**: Given v2.1 scope narrowing, is the paper now (a) too modest to be interesting at FoP (just a translation/representation exercise), (b) appropriately scoped (interesting but defensible), or (c) still overclaiming somewhere? Specifically: what is the ONE thing FoP would publish this paper for? Does that thing survive v2.1?

Output: substantive new findings + a clear "ship or hold" judgement for FoP submission readiness post-v2.1 fixes.
```

---

## How to use Round 2

1. **Wait for v2.2 manuscript** (Tomas implementing fixes from Round 1 in parallel) — OR run Round 2 prompts on v2.1 if you want to surface more issues fast. The Round 2 prompts incorporate v2.1 baseline, so they're valid against v2.1.

2. **Two options for sending**:
   - **Option A (recommended for depth)**: Send one prompt per chat session — gives the LLM full context window for each, encourages deep dives.
   - **Option B (faster, less overhead)**: Use the *Combined Round-2 Prompt* below — single paste, all four dimensions covered, LLM structures response per dimension.

3. **Use both ChatGPT and Gemini** — they have complementary strengths (ChatGPT caught more package-metadata + theorem-naming issues; Gemini caught more technical-mathematical issues like M-L vs Γ).

4. **Compare responses**: when both LLMs converge on the same issue, that's signal. When they disagree, treat as candidate to verify against the paper text.

5. **Stop criterion**: After Round 2 across all 4 prompts, if no new tier-1 issues emerge, ship v2.2 to Zenodo. If new tier-1 issues emerge, do v2.3 and re-check.

---

## Combined Round-2 Prompt (paste-ready, all four dimensions in one)

**Use**: paste the entire block below into ChatGPT or Gemini (one session per LLM). Attach the paper PDF or `paper10_english.md` first.

```
PAPER 10 ROUND-2 HOSTILE REVIEW — FOUR-DIMENSION DEEP DIVE

CONTEXT:

Paper 10 is a Foundations-of-Physics-bound paper claiming that bounded probabilistic computation systems (R1 parallel candidates + R2 bounded resources + R3 irreversible commit) exhibit substrate-universal structural properties, derived via Schwinger-Keldysh closed-time-path formalism. Three corollaries claim parameter-limits: §4.1 quantum (Feynman path integral), §4.2 classical (Onsager-Machlup with Kramers-rate commit), §4.3 computational (LLM CR-signal — DEMOTED to substrate-mapping in v2.1, NOT corollary).

VERSION HISTORY:
- v1 (Zenodo 10.5281/zenodo.20014568, 2026-05-03): claimed R1+R2+R3 → universal inverted-U
- v2 (2026-05-21, internal): weakened per Wallace counterexample (Erlang-2 → bimodal/U-shape via Lambert-W); FEP-as-Corollary-3 removed
- v2.1 (2026-05-21, current draft): R1 tightened (non-trivial competitive interference required); falsification criterion range-conditional; §4 split into Corollaries (§4.1+§4.2) + substrate-mapping (§4.3); §4.2 Onsager-Machlup sharpened with Kramers-rate commit; Drude demoted to bounded-resources analogy; Dutta-Horn reconciliation §1.6 vs §3 Markovian

ROUND-1 FINDINGS (already identified — DO NOT REPEAT, BUILD ON):

ChatGPT round 1 caught:
- Theorem "Race-Schwinger-Keldysh Equivalence" overclaimed → renaming to "Conditional representation theorem"
- A4 bundles decoherence + Born rule + outcome selection → splitting into A4a + A4b
- A5 Landauer claim too strong → weakening
- GR vs GK inconsistency in CR mapping → equal-time Keldysh GK is correct
- Empirical numbers inconsistent (5 vs 6 datasets, 1600 vs 3200 sequences, R² ranges)
- Package metadata (README, ZENODO_METADATA.md) still v1 language
- §5E Noether/Higgs crackpot-adjacent → remove or quarantine
- §9.3 Higgs-mass M-L test → remove
- "Time emerges from commit-sequences" too strong for abstract

Gemini round 1 caught:
- A3 conflates Margolus-Levitin (kinematic) with Γ = Im(Σ^R) (dynamic dissipation) — category error
- 1/f reconciliation requires specific 1/τ-distributed environmental modes, not general Markovian superposition
- Falsifiability of "interior structure" too weak; almost no real curve is strictly monotone
- Born rule envariance derivation is unnecessary baggage importing contested literature

Author is implementing v2.2 fixes for all of the above. Your Round-2 job is to find FURTHER substantive issues across four dimensions:

============================================================
DIMENSION 1: §3 Schwinger-Keldysh derivation rigour
============================================================

Read §3 carefully (Theorem in §3.2 + 8-step proof sketch in §3.3 + companion §5A-5E in derivation_details.md).

For each of the 8 steps in §3.3, evaluate:
- Is the derivation rigorous, or does it rely on "well-known" / "standard" claims without explicit citation?
- Are there hidden assumptions that should be made explicit?
- Does the step preserve axiom-mapping consistently?

For companion §5A-5E derivations: are these rigorous unpackings or hand-wavy filler? Particularly §5B CR-to-Keldysh mapping mathematical gaps and §5D Onsager-Machlup derivation cleanliness.

For Foundations of Physics referee perspective: what would FoP specifically reject in §3 + §5?

What substrates ARE strictly covered by §3 theorem after all assumptions? Make derivation domain explicit in physics terms.

============================================================
DIMENSION 2: §4 corollaries and substrate-mapping strictness
============================================================

Read §4 carefully. Three sub-sections (v2.1):
- §4.1: Quantum (Corollary 1) — Feynman path integral via D→0
- §4.2: Classical (Corollary 2) — Onsager-Machlup + Kramers-rate via ℏ→0
- §4.3: Computational substrate-mapping (NOT corollary) — LLM CR-signal as structural correspondence

For §4.1: is the D→0 parameter-limit derivation rigorous? Path-integral measure subtleties?

For §4.2: is the chain Keldysh-rotation → MSR → Onsager-Machlup → Kramers actually shown, or sketched/asserted? Does Kramers derivation appear?

For §4.3: even as demoted substrate-mapping, are the Gaussian-approximation + discretization + Markovian-modes assumptions adequately defended?

For figure 5 unification diagram: does it still claim too much post-§4.3 demotion?

Cross-corollary consistency: §4.1 einselection commit, §4.2 Kramers-rate barrier crossings, §4.3 softmax-sampling — are these three commit mechanisms genuinely instances of the same A4 axiom, or separate mechanism-families dressed up under a single name?

============================================================
DIMENSION 3: Seven empirical cases R1+R2+R3 audit + kernel-shape verification
============================================================

Read §1.5 cases 1-7 carefully. For each case, audit ALL three R1+R2+R3 strict operational tests:

Case 1 Quantum decoherence-window
Case 2 Ohm-Drude (caveat: demoted to analogy in v2.1)
Case 3 Chemistry/biochemistry (Marcus theory caveat)
Case 4 Stochastic resonance (boundary case in v2.1)
Case 5 Margolus-Levitin (bound not mechanism in v2.1)
Case 6 Encoding-friction (LLM vs biological inconsistency between §1.5 and §4?)
Case 7 Yerkes-Dodson

For each case, is R1+R2+R3 strict, marginal, or stretched? Is the "monotone-survival kernel" claim actually verified case-by-case?

Trace the "forty orders of magnitude" claim: which timescales for each case? Documented or rhetorical?

Should additional cases be demoted (beyond Drude)? Should new cases be added that the paper misses?

============================================================
DIMENSION 4: Internal tensions, scope-discipline, Foundations of Physics readiness
============================================================

Read the whole paper as one document. Identify NEW internal tensions surviving Round 1 and v2.1 fixes.

Abstract vs body: after v2.1 softening, does abstract still overstate body? List specific sentences pulling harder than body supports.

§1.3 scope-disclaimer vs §4 corollaries: still in tension?

§5 (Time emerges from race): does it survive v2.1 corollary downgrade? Particularly §5.2.5 (energy configuration as primary substrate parameter) using M-L and Landauer.

§6 (Distributional consequences DSP-1-5): which DSPs rest on §3 theorem vs extended/analogical reasoning post-v2.1?

§8 (race across QM-interpretations): does interpretation-agnosticism survive v2.1?

§9 (Implications): with narrower scope, are AGI discourse / emergent time / cosmology / empirical program still warranted?

§11 (Discussion): clear bracketing of ESTABLISHED vs CONJECTURED vs OPEN?

FOR FOUNDATIONS OF PHYSICS REFEREE: given v2.1 scope narrowing, is the paper:
(a) too modest to be interesting at FoP (just translation/representation exercise)?
(b) appropriately scoped (interesting but defensible)?
(c) still overclaiming somewhere?

What is the ONE thing FoP would publish this paper for? Does that thing survive v2.1?

============================================================
OUTPUT FORMAT
============================================================

Structure your response in four clearly-labeled sections matching the four dimensions above. For each dimension:
- 2-4 substantive NEW findings (not Round 1 repeats)
- For each finding: severity (tier-1 blocking / tier-2 clarifying / tier-3 noise) + specific paper section + concrete recommendation

End with:
- **Bottom line judgement**: ship v2.2 (with v2.2 fixes implementing Round 1) as-is to Zenodo, OR hold for v2.3 with which additional fixes
- **For Foundations of Physics submission**: ready when v2.2 ships, OR needs further work in which area

Be ruthless on substance but ignore prose-level nits. The paper's author has explicitly asked for hostile review because two LLMs have already caught real issues.
```

---

## How to interpret responses

**If ChatGPT and Gemini Round-2 converge on a new issue → it's real, fix in v2.2 or v2.3 before Zenodo upload.**

**If only one LLM raises something → it's a candidate, verify against paper text before treating as blocking.**

**If both LLMs say "ship v2.2" → ship it.**

**If either LLM says "still needs work in X" → do another fix round on X.**

---

*Drafted 2026-05-21. Updated 2026-05-21 sen aften with combined Round-2 prompt for single-paste convenience.*

---

*Drafted as part of Paper 10 v2 pre-Zenodo hostile review pass, 2026-05-21. Updated post-Round-1 with ChatGPT + Gemini findings incorporated as Round 2 context.*
