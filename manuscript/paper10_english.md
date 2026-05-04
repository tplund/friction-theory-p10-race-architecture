# Race all the way down, race all the way up: A substrate-universal race-architecture across quantum, classical, biological, and computational regimes

*(Working subtitle: A Schwinger-Keldysh derivation with a universal inverted-U signature)*

**Author:** Tomas Pødenphant Lund

**Affiliation:** Independent Research, Aarhus

**Correspondence:** tomas.lund@frictiontheory.org

**Web:** https://frictiontheory.org

**Target venue:** *Foundations of Physics* (primary), *Synthese* (secondary), or *Behavioral and Brain Sciences* target article (if integrative review preferred)

**Status:** Open research program. Companion to Paper 1 (Pødenphant Lund 2026b) which establishes Friction Theory (FT) on biological, cognitive, and computational substrates. This paper investigates whether FT's mathematical scaffolding extends to physics-scope substrates (quantum, classical, thermodynamic). Papers 1-6 do not depend on this paper's success.

**Acknowledgments:** Extensive discussion, literature search, mathematical derivation drafting, empirical analysis, figure generation, and manuscript structuring were conducted in collaboration with Claude (Anthropic, 2025–2026). The theoretical claims, the foundational intuition (formulated by the author after a winter sea-bath, 2026-04-21), the framework name, and the responsibility for any errors are those of the author.

---

## Abstract

**Scope note:** Friction Theory (FT, Pødenphant Lund 2026b) formalizes bounded probabilistic computation systems satisfying the race-axioms. FT's established scope covers biological, cognitive, and computational substrates (Papers 1–6). This paper investigates whether FT's mathematical structure scales to physics-scope substrates (quantum measurement, classical mechanics, thermodynamics). This is **open research, not established FT content**; Papers 1–6 do not depend on its results. If Paper 10's backbone derivation holds formally, FT's scope may be upgraded to physics-universal in subsequent work.

---

We argue that "decision" in resource-bounded probabilistic systems is not a mental or agentive primitive but a substrate-universal structural phenomenon: the resolution of competing processes racing toward commit under a finite-time budget. The central structural prediction is *deductive* and free of substrate-specific parameters: any system satisfying R1 (parallel candidates) + R2 (bounded resources) + R3 (irreversible commit) exhibits an **inverted U on its evaluation-to-commit rate** — too low a rate yields no information processing, too high a rate yields noise-dominated commit, and only the intermediate rate maximizes information throughput. We show that seven apparently independent physical and cognitive phenomena — qubit decoherence-window, Ohm's law / Drude electron transport, chemistry / biochemistry molecular kinetics, stochastic resonance, Margolus-Levitin energy-density trade-off, encoding-friction in learning, and Yerkes-Dodson arousal-performance — are manifestations of this single race-structural necessity across substrate scales spanning forty orders of magnitude in characteristic timescale. "Race all the way down, race all the way up" is not a metaphor between scales but one structural property projected onto different observables.

We then refine the three race-rules R1–R3 to a five-axiom formulation (A1–A5, splitting R2 into competitive interaction × finite-time constraint and R3 into commit mechanism × irreversibility) appropriate for the Schwinger-Keldysh derivation, and demonstrate that A1–A5 are satisfied by the closed-time-path generating functional of any bipartite quantum system with einselected pointer basis and Markovian environment. As corollaries we recover the Feynman path integral (quantum limit), Onsager-Machlup stochastic dynamics (classical limit), the Friston free energy principle (biological limit), and the CR-signal in large language models (computational limit) as parameter-regimes of *one* underlying derivation. This implies that classical and quantum "decisions" are not separate phenomena but limits of the same dynamic. Substrate-agnostic clock-rate is bounded by Margolus-Levitin (maximum commit-rate) and commit-cost by Landauer (minimum energy per bit). Time emerges from commit-sequences rather than constraining them. We engage three hard problems (interference, linearity vs. nonlinearity, reversibility) honestly and show that the framework relocates rather than solves the measurement problem. Paper 10 proposes no new physics; it presents existing mathematics (MSR, Schwinger-Keldysh, Feynman-Vernon, Zurek einselection, Friston FEP) unified under race as a lens, with a concrete empirical anchor in LLM-substrate measurement and the universal inverted-U pattern across seven substrate scales.

**Falsification criterion:** an identifiable system with R1+R2+R3 architecture and *without* an inverted U on its evaluation rate would falsify race's structural core. Wallace's biocognition corpus (Wallace, Leonova & Gochhait 2022 *Entropy*; Wallace 2025a *Symmetry*; Wallace 2023 *J. Defense Model. Simul.*) derives a corresponding inverted-U pattern for biological cognition via rate-distortion + data-compression machinery; our contribution is (i) the substrate-free R1+R2+R3 deductive argument that does not require rate-distortion, (ii) the substrate-universal extension to quantum and thermodynamic scales, and (iii) the Schwinger-Keldysh-based QM-substrate derivation grounding case #1.

---

## 1. Introduction

### 1.1 The illusion of decision

Systems ranging from neurons to nations make "decisions" under resource constraints. The vocabulary of decision — preference, deliberation, choice, commitment — has proven remarkably durable across biology, cognitive science, economics, and increasingly machine learning. Yet the vocabulary presumes a category that may not exist. When a coin toss resolves to heads, we do not say the coin "decided"; we say competing physical processes (angular momentum, air resistance, surface friction) resolved to one outcome. Why do we grant decision-status to biological or artificial systems performing structurally similar competitions under time pressure?

The tradition skeptical of decision-as-primitive is older than often recognized. Dennett's *Consciousness Explained* (1991) proposed that cognition proceeds through "multiple drafts" — parallel processes competing without central arbitration. Wegner's *The Illusion of Conscious Will* (2002) mustered empirical evidence that the felt experience of deciding often post-dates the neural events the decision would have caused. Predictive processing (Clark 2013; Hohwy 2013) and Friston's free energy principle (2010) describe biological cognition as minimization of prediction error under computational budget — no homunculus, no commander, only optimization of inferential quantities. These traditions converge on a single claim: "decision" is a label convenient for narrative but unnecessary for explanation.

We radicalize this claim. What appears as decision is the resolution of parallel processes racing under finite-time constraint. We call this framework Friction Theory (FT, Pødenphant Lund 2026b), because the resource-budget imposes what can properly be called friction: the thermodynamic tax on finite-time computation. The central question this paper addresses is whether FT, developed and established for biological, cognitive, and computational substrates (Papers 1–6), scales further — down to quantum measurement, across to classical mechanics, out to non-equilibrium thermodynamics. If it does, then quantum "collapse," classical "selection," and biological "decision" are not distinct phenomena requiring distinct theories; they are parameter-regimes of a single underlying dynamic. The paper's core result (Theorem, §3) is a derivation establishing this unification rigorously via the Schwinger-Keldysh formalism.

This is an ambitious claim and must be framed carefully. We do not propose new physics; we reinterpret existing mathematics (path integrals, decoherence, fluctuation theorems) under a unified lens. We do not solve the measurement problem; we relocate it from "why does superposition collapse?" to "why does race resolve?" — the same problem in a new coordinate system, with potential tractability gains we identify in §7. We do not argue for a specific interpretation of quantum mechanics; race is interpretation-agnostic. And we do not claim a theory of everything; FT is a framework, a lens, a tool. The derivation pyramid in §5A–§5E is established mathematics (Schwinger-Keldysh, Onsager-Machlup, Zurek einselection, Friston FEP, Noether) assembled under the race lens; FT's physics-scope extension is open research, but its formal scaffolding is built from settled physics. Papers 1–6's established-scope claims (biological, cognitive, computational) do not depend on this paper's success. The remainder of the introduction previews the framework (§1.2), sets explicit scope (§1.3), and establishes a complementary deductive argument and seven-case empirical signature accessible without the formal Schwinger-Keldysh apparatus (§1.5).

### 1.2 Preview of framework

Friction Theory rests on five axioms (A1–A5, formalized in §2.2). Pre-commit, a system exists in a superposition or distribution over candidate states (A1, parallelism). These candidates evolve under dynamics permitting constructive and destructive interference between them (A2, competitive interaction). Evolution is bounded in time by substrate-specific resources (A3, finite-time constraint). Eventually, one candidate is selected with probabilities following Born's rule (A4, commit). The selection is effectively irreversible, paying thermodynamic cost in environmental entropy (A5, irreversibility).

Our main technical result (Theorem, §3) demonstrates that any bipartite quantum system with einselected pointer basis and Markovian environment satisfies A1–A5 via the Schwinger-Keldysh closed-time-path generating functional. The Feynman path integral emerges as the coherent limit (Corollary 1). Onsager-Machlup stochastic dynamics emerges as the classical thermal limit (Corollary 2). Friston's free energy principle emerges for biological substrates with active internal structure — Markov blanket — yielding the variational inference formulation central to modern cognitive neuroscience (Corollary 3). The CR-signal measured in large language model substrates (Pødenphant Lund 2026d) emerges as a discrete-time Keldysh observable with testable scaling properties (Corollary 4).

The mathematics is not new. We use existing formalism — Feynman-Vernon (1963), Schwinger-Keldysh (1961, 1964), Zurek einselection (1981 onward), Friston FEP (2010 onward), Martin-Siggia-Rose (1973) — assembled under race axioms as unifying principle. The contribution is not mechanistic novelty but conceptual unification with empirical anchor: LLM substrates provide directly measurable race-signals, making FT's substrate-agnostic claims testable without appeal to difficult-to-access physical substrates. Paper 1's empirical finding (CR correlates with error rate at ρ = −0.423, p < 0.0001) is not coincidental but, as we show in §4.4 and derivation §5B, follows from the theoretical mapping of CR to equal-time Keldysh response.

A complementary line of argument — independent of the Schwinger-Keldysh formalism — is established in §1.5: the *inverted-U-on-evaluation-rate* signature follows deductively from R1+R2+R3 alone (parallel candidates, bounded resources, irreversible commit) without requiring any specific dynamics. Seven empirical cases (qubit decoherence-window, stochastic resonance, Margolus-Levitin saturation, encoding-friction in learning, Yerkes-Dodson, Ohm's law / Drude model, chemistry / biochemistry molecular kinetics) tile the prediction across distinct physical scales. A reader who has not yet engaged the Schwinger-Keldysh formalism can take the seven-case pattern at face value as substrate-universal evidence; a reader who accepts the formal derivation gains a mechanistic explanation of why the seven-case pattern *must* hold. The two arguments cross-validate without depending on one another.

### 1.3 Scope and explicit non-aims

- **Exploration, not established FT content.** Paper 10 investigates whether FT (Pødenphant Lund 2026b) scales to physics-scope; Papers 1–6 (FT's established scope: biological, cognitive, computational) do not depend on its results. Paper 1 §8 is the canonical scope formulation.
- **Scope-upgrade conditional.** Only if Paper 10's Schwinger-Keldysh-based backbone derivation holds formally can FT's scope be upgraded to physics-universal. Until then: we do *not* claim that established FT covers quantum / classical / thermodynamic substrates.
- Not a theory of everything — a lens, not a replacement.
- Not a consciousness claim — that is Paper 7's scope.
- Not a measurement-problem solution — relocation, not dissolution.
- Not string theory — explicitly off the table.
- Not an argument for any specific QM interpretation — framework-agnostic.

**Explicit interpretation-agnosticism.** race's "candidate routes" pre-commit are compatible with multiple QM-interpretation choices, and the framework does not commit to any. The framework operates equally well under:

- **Copenhagen interpretation**: routes are probability-amplitudes, no pre-commit "real" existence — race describes the formal evolution of the amplitude-distribution under bounded resources
- **Bohmian / pilot-wave interpretation**: routes are real alternatives weighted by a non-local pilot-wave — race describes the wave-guidance dynamics under bounded resources  
- **Many-worlds (Everett) interpretation**: routes are realised in different branches — race describes the branching-weight dynamics under bounded resources

A fourth metaphysical stance — **configuration-space realism** (Albert 1996, 2013; Loewer 1996; North 2013) — is compatible with both Bohmian and Many-Worlds and worth flagging separately. Configuration-space realism takes the wave-function's natural domain (3N-dimensional configuration space for N particles) as the fundamental space; our experienced 3D space is then an emergent projection. Under this stance, "non-locality" in 3D is not spooky action but a consequence of viewing a higher-dimensional dynamics from a lower-dimensional projection.

What survives across interpretations is the *structural feature*: pre-commit there is competition over candidates; commit reduces this to a selected outcome; the reduction is irreversible at the appropriate substrate-physics level. This is interpretation-independent.

**What each interpretation gives the framework.** Different interpretations yield different *readings* of FT's structural claims, even though the empirical content is invariant. The four readings are summarised below for the substrate-universality and A2/A5 hysteresis claims (Paper 1 §2.4):

| Interpretation | "Candidate routes" pre-commit | A2 hysteresis (Berry phase) | Substrate-universality |
|---|---|---|---|
| **Copenhagen** | Probability-amplitudes; no ontological status | Geometric phase factor; mathematical artifact | Mathematical isomorphism across substrates |
| **Bohmian** | Real alternatives, pilot-wave-weighted (non-local) | Real geometric memory of particle trajectory | Physical realisation under non-local guidance |
| **Many-worlds** | Branches realised in parallel | Per-branch path-dependence | Branch-structure invariance |
| **Configuration-space realism** | Real configurations in 3N-dimensional space | Literal physical hysteresis on literal physical trajectory | Substrate **monism** — one space, multiple operational regimes |

Each reading is internally consistent.

**A note on configuration-space realism's particular fit (without commitment).** Among the four readings, configuration-space realism deserves explicit attention because it offers the *cleanest physical reading* of two specific FT-claims, even though we do not commit to it. First, A2-hysteresis: under CSR, Berry phase is not a calculational artifact but literal physical history-dependence on a literal physical trajectory in the fundamental space. The framework's claim that "race architectures accumulate path-dependent traces even before commit" gets a direct physical referent. Second, substrate-universality: under CSR, biological, silicon, and quantum substrates are not different ontologies linked by mathematical isomorphism — they are operational regimes in one fundamental space. Substrate-universality becomes substrate-monism. These are not reasons to commit to CSR; they are observations that *if* a reader independently finds CSR appealing, FT's claims acquire particularly clean physical referents under that reading. The framework's empirical content does not depend on this; we mention it because it is the kind of metaphysical fit that is worth flagging precisely so reviewers can see we have considered the option without taking it.

Each interpretation's reading is sufficient to support FT's empirical claims; the metaphysical choice between them is genuinely underdetermined by the data.

The framework's empirical content (DSP signatures, A2/A5 hysteresis distinction, Born-rule emergence as Corollary) does not depend on choosing among the four interpretations. A reviewer arguing "routes exist only as probability fields under Copenhagen" or "routes have no meaning without commitment to a specific interpretation" is addressing a claim the framework does not make. We use "candidate" or "route" as a substrate-universal term for what is competing pre-commit, deliberately leaving the metaphysical status of that competition open. Reading the same framework as Copenhagen-operational, Bohmian-physical, Many-Worlds-multi-branch, or CSR-monistic produces no empirical conflict — only different metaphysical commitments behind the same predictions.

### 1.5 Race all the way down, race all the way up: the universal inverted-U signature

The Schwinger-Keldysh derivation of §3 is the technical center of this paper, but its empirical anchor is more fundamental and more general than the QM-specific claim alone. Before entering the formal race framework (§2) and the derivation itself (§3), we establish a structural prediction that can be stated *without* the Schwinger-Keldysh machinery and that — if it holds — provides independent empirical support for substrate-universal race.

**Operational criteria for R1+R2+R3 (substrate-independent).** Before stating the structural prediction we specify substrate-independent operational tests for each axiom. These tests do not appeal to the inverted-U signature itself, so the prediction below is non-circular:

- **R1 (parallelism)** — operational test: does the substrate's pre-commit dynamics admit a description in terms of multiple distinguishable candidate states whose evolution interferes (quantum) or whose probability mass redistributes among each other (classical)? A substrate fails R1 if no pre-commit dynamics exists (only input-output mapping) or if no distinguishable candidate states can be identified.
- **R2 (bounded resources)** — operational test: is there a substrate-physics quantity (energy, computational steps, working-memory capacity, processing time) that constrains the rate at which evaluation can proceed? The Margolus-Levitin bound $\tau \geq \pi\hbar/2E$ is the canonical formulation for energy-bounded substrates; analogous bounds exist for computation and biology. A substrate fails R2 if no resource-constraint operates and evaluation can proceed indefinitely without thermodynamic cost — a textbook idealisation forbidden by the Second Law (§2.1.5).
- **R3 (irreversible commit)** — operational test: does the substrate possess a selection mechanism that is effectively non-undoable on the relevant timescale, with associated thermodynamic cost (entropy production ≥ $k_B \ln 2$ per committed bit, Landauer 1961)? A substrate fails R3 if no commit mechanism exists at all (the system remains in pre-commit superposition or distribution indefinitely) or if all "selections" are independent stochastic events without accumulation of pre-commit evaluation-state.

These three operational tests can be applied to a candidate substrate **before** examining its rate-performance relationship. Any substrate passing all three independent tests is in-scope for the structural prediction below.

**The structural prediction.** Any system satisfying R1, R2, and R3 (jointly, in the sense above) will exhibit a **performance function vanishing at the lower and upper bounds of the rate-parameter, with at least one interior maximum**. The argument runs in three steps and uses only R1+R2+R3:

- *Lower bound* (rate too low): commits never happen on the relevant timescale → R3 fails to activate → no information processing → performance vanishes from below. At this limit the system is no longer a race-architecture (R3 violation).
- *Upper bound* (rate too high): commits happen faster than R1's parallel evaluation can discriminate among candidates → commit becomes uncorrelated with evaluation-state → no stable encoding → performance vanishes from above. At this limit R1 is effectively unsatisfied (parallelism becomes noise-dominated rather than discriminative).
- *Intermediate*: R1's evaluation completes just before R3's commit closes → maximal information-throughput per commit → performance maximised.

The inverted-U is therefore best understood as a **boundary-phenomenon between non-race regimes**: the rate-parameter takes the substrate from non-race (R3 violation) at the lower limit, through a race-interior region of parameter-space, to non-race (R1 violation) at the upper limit. Performance vanishes at both boundaries because the substrate ceases to be race there; performance peaks somewhere in the interior because that is where R1+R2+R3 are jointly satisfied with optimal matching of evaluation- and commit-timescales.

**A clarification on shape.** A function that vanishes at both ends of an interval and is positive between them must have at least one interior maximum. *Unimodality* (single-peak inverted-U rather than multi-peak) is not forced by R1+R2+R3 alone; it requires additional substrate-specific argument that the relevant performance function is monotone increasing in rate up to a critical value and monotone decreasing thereafter. In each of the seven empirical cases below, this monotonicity is established by substrate-specific physics or empirics. The structural argument from R1+R2+R3 establishes the *boundary behaviour* (vanishing at both limits) and the *existence* of an interior maximum; substrate-specific work establishes its uniqueness (single-peak structure). We flag this distinction explicitly because the deductive argument is sometimes mis-stated as "concavity from R1+R2+R3 alone," which is too strong.

**What "performance" and "rate" denote structurally.** "Performance" denotes a substrate-specific monotone transform of *information-throughput per commit*. The seven empirical operationalisations below (gate fidelity, SNR, ops/watt, encoding-depth, task accuracy, power efficiency, reaction-rate / yield) are all monotone transforms of this quantity under specifiable substrate-physics assumptions; the deductive argument does not depend on a single dimensional formulation. "Rate" is best interpreted as the dimensionless ratio $\tau_{\text{eval}}/\tau_{\text{commit}}$ where $\tau_{\text{eval}}$ is the substrate's evaluation-timescale and $\tau_{\text{commit}}$ is its commit-timescale. The prediction is that performance peaks near $\tau_{\text{eval}} \approx \tau_{\text{commit}}$. Each of the seven cases below has identifiable evaluation- and commit-timescales (quantum: gate-time vs decoherence-time; statistical physics: noise-correlation-time vs threshold-crossing-time; thermodynamics: per-operation-time vs Landauer-relaxation-time; learning: encoding-time vs commit-token-time; behaviour: deliberation-time vs response-time; classical electronics: drift-relaxation-time vs phonon-scattering-time; chemistry: molecular-collision-time vs barrier-crossing-time). Substrates differ in the substrate-physics that determines these timescales but share the dimensionless ratio as the universal rate-axis.

The shape (vanishing-at-both-ends with interior maximum) is *not* substrate-specific empirics; it is forced by R1+R2+R3 alone via the boundary argument above. The substrate-specific contribution is the *unimodality* (single-peak structure) and the *quantitative location* of the optimum.

**The seven empirical cases.** The seven tile this prediction across distinct physical scales. The cases are arranged by characteristic substrate timescale, from fastest (femtosecond quantum gates) to slowest (decade-scale behavioural learning):

| # | Scale | R1 (parallelism) | R2 (bounded resource) | R3 (commit) | Inverted-U observable |
|---|---|---|---|---|---|
| 1 | **Quantum** | Coherent superposition over basis states | Energy + decoherence-rate (Margolus-Levitin: $\tau_c \geq \pi\hbar/2E$) | Pointer-basis selection (Zurek einselection) | Gate fidelity vs. decoherence-rate — *qubit operating window* (Preskill 2018; Krantz et al. 2019) |
| 2 | **Classical electronics** | Parallel electron-trajectories in conductor | Drift velocity bounded by field-strength + electron-phonon scattering rate | Phonon-collision dissipating kinetic energy as lattice heat | Power efficiency (output watts / input watts) vs. current — *Ohm's law / Joule heating* (Drude 1900) |
| 3 | **Chemistry / biochemistry (molecular kinetics)** | Parallel reaction pathways; molecules in solution sampling multiple potential partner-configurations | Thermal energy ($k_B T$) + diffusion rate + concentration gradients | Irreversible bond-formation / product-formation; energy released as heat; entropy production per Marcus theory | Reaction rate vs. temperature — *Arrhenius / transition-state theory* (Arrhenius 1889; Kramers 1940; Hänggi-Talkner-Borkovec 1990); BZ oscillator stochastic-resonance signature (Field-Noyes 1974); enzyme catalysis efficiency vs. substrate concentration |
| 4 | **Statistical physics** | Local fluctuations exploring barrier-states | Noise amplitude + relaxation time | Threshold-crossing | Signal-to-noise ratio vs. noise amplitude — *stochastic resonance* (Benzi 1981; Wiesenfeld & Moss 1995; Gammaitoni et al. 1998) |
| 5 | **Thermodynamics** | Distribution over micro-state trajectories | Energy density + Landauer cost | Operation completion at $\geq k_B \ln 2$ per bit | Operations-per-second-per-watt vs. energy-density — *Margolus-Levitin saturation* (Margolus & Levitin 1998; Lloyd 2000) |
| 6 | **Learning (LLM + biological)** | Competing token/state-routes pre-commit | Attention/working-memory + computation budget | Token/state commit | Encoding-depth vs. encoding-friction — *matched-friction-under-hysteresis* (Pødenphant Lund 2026b §6) |
| 7 | **Behaviour** | Competing action-tendencies pre-decision | Arousal/processing capacity | Behavioural commit | Task accuracy vs. arousal — *Yerkes-Dodson* (Yerkes & Dodson 1908; Diamond et al. 2007) |

**Theoretical maturity per case.** The seven cases differ in their existing theoretical grounding, and we flag this explicitly to avoid overstating the empirical pattern:

- **Case 1 (qubit decoherence-window)** is established in decoherence-engineering practice (Preskill 2018; Krantz et al. 2019) as the operational tradeoff between coherence preservation and gate-execution; we are unaware of a published structural derivation as inverted-U-from-R1+R2+R3 prior to the present paper.
- **Case 2 (Ohm's law / Drude model)** has long-established empirical grounding: Drude 1900's kinetic-theory derivation of conductivity from free-electron-gas-with-phonon-scattering, refined via Sommerfeld 1928 (Fermi-Dirac statistics). The inverted-U on power efficiency vs. current is established in electrical-engineering practice — high-voltage low-current transmission systems are designed precisely to navigate this tradeoff (low current → low Joule loss $I^2R$, but circuit dynamics require nonzero current to deliver power; the optimum is interior).
- **Case 3 (chemistry / biochemistry)** has rigorous derivation through transition-state theory (Eyring 1935; Kramers 1940; Hänggi-Talkner-Borkovec 1990) and Marcus theory of electron transfer (Marcus 1956; Nobel Prize 1992). Reaction kinetics is race-architecture at molecular scale: parallel reaction pathways (R1), thermal energy + diffusion + concentration gradients (R2), irreversible bond-formation with entropy production (R3). The Arrhenius equation $k = A e^{-E_a/k_B T}$ is Kramers escape-rate theory applied to molecular race-architecture (1889). Belousov-Zhabotinsky oscillating chemical reactions (Belousov 1959; Zhabotinsky 1964; canonical mechanism Field-Noyes 1974) exhibit stochastic resonance — a chemical-substrate instance of case #4 — with intermediate noise amplitude maximising oscillation regularity. Biochemistry (enzyme kinetics, protein folding, signal transduction) is race applied to biological substrate; Tyson 2022 traces the through-line from BZ-reaction physical chemistry to biochemical clocks and cell-cycle regulation.
- **Case 4 (stochastic resonance)** has a rigorous Langevin/Kramers derivation showing why SNR peaks at intermediate noise (Gammaitoni et al. 1998 review). The inverted-U here is derived from substrate physics, independent of R1+R2+R3 framing.
- **Case 5 (Margolus-Levitin saturation)** requires reading the Margolus-Levitin bound *together with* the Landauer cost-per-operation: at low energy density operations are too slow, at high energy density the Landauer cost per useful bit rises faster than the operation rate (Lloyd 2000). The combined result is the inverted-U; neither bound alone gives it.
- **Case 6 (encoding-friction in learning)** is operationalised within the present author's Friction Theory (Pødenphant Lund 2026b §6); we flag this self-citation explicitly.
- **Case 7 (Yerkes-Dodson)** is, in its 1908 form, an empirical correlation; Diamond et al. 2007 provide neurobiological mechanism (hippocampal stress-physiology), not a structural derivation. Wallace (2025a, *Symmetry*) has independently derived Y-D from rate-distortion / data-compression (concurrent with our drafting), giving the case mature theoretical grounding.

**What is novel, more precisely.** The novel claim of §1.5 is *not* that any individual case is inverted-U: six of seven are independently established in their substrate-specific literatures (case #2 / Drude has 125 years of established physics-curriculum coverage; case #3 / Arrhenius-Marcus chemistry has even longer empirical maturity since 1889; case #4 stochastic resonance, case #5 Margolus-Levitin, case #7 Yerkes-Dodson are all established; Wallace's rate-distortion derivation has separately established case #7 from information-theoretic premises; case #1 qubit operating window is decoherence-engineering practice). The novel claim is that R1+R2+R3 provides a **common structural origin** that explains why the same curve-shape appears across substrates as different as decoherence-engineering, electron transport in metals, molecular reaction kinetics, and behavioural psychophysiology. This is a unification claim about the *cause* of the cross-substrate pattern, not a claim of priority on any individual case.

**Sharpening the differentiator from Wallace's biology-cognition derivation.** Wallace 2025a derives Y-D from rate-distortion + data-compression for biological cognition. Our R1+R2+R3 deductive argument differs structurally even on biology-and-cognition scope: where rate-distortion presupposes an information-source structure (a stationary distribution over signal-states with well-defined channel capacity), R1+R2+R3 appeals to substrate-physics primitives (parallel candidate-state interference, energy/time bounds, entropy-producing commit) that hold without that presupposition. The two arguments converge on the same prediction via different premises on biology-cognition scope; on substrates without natural information-source structure, only R1+R2+R3 applies. Three considerations sharpen the distinction globally:

1. **Substrate-extension to QM via case #1** is the genuine extension where Wallace's information-theoretic functionals are not naturally defined: the pre-commit Hilbert-space superposition does not have a well-defined rate-distortion functional until decoherence-induced commit, so the rate-distortion derivation cannot be applied at the substrate level. R1+R2+R3 applies at the substrate level (R1 = coherent superposition, R2 = Margolus-Levitin bound, R3 = einselection-induced commit). The Schwinger-Keldysh derivation of §3 grounds case #1 rigorously; Wallace's framework does not address this.
2. **Substrate-extension to thermodynamics via case #5** similarly does not naturally fit rate-distortion: the substrate is not processing biological signal but executing physical operations under energy-bounded computation (Landauer + Margolus-Levitin). R1+R2+R3 applies (R1 = parallel micro-state trajectories, R2 = energy density bound, R3 = operation completion at $\geq k_B \ln 2$ entropy production); rate-distortion does not without auxiliary information-source assumptions.
3. **Operational criteria for R1+R2+R3** (this section) are formulated in substrate-physics terms (interference, energy bounds, entropy production) rather than information-theoretic terms (rate-distortion, data-compression, channel capacity). For substrates where information-theoretic structure is derived rather than primary, this matters.

On biology-and-cognition scope (cases #6 and #5) Wallace's rate-distortion derivation and our R1+R2+R3 argument reach structurally analogous conclusions via independent formal routes (information-theoretic vs. substrate-physics premises); we acknowledge Wallace's corpus as concurrent independent work on this scope. The genuine extension beyond Wallace's biology-cognition coverage is cases #1, #2, and #3 plus the substrate-free formulation in operational criteria.

**Relation to Wallace's biocognition rate-distortion programme.** Wallace has developed a substantial rate-distortion-based framework for biological cognition (Wallace, Leonova & Gochhait 2022, *Entropy*; Wallace 2025a, *Symmetry*; Wallace 2023, *J. Defense Model. Simul.*) that establishes (a) information-theoretic instability conditions for biocognition (2022), (b) a direct derivation of the Yerkes-Dodson inverted-U from rate-distortion / data-compression machinery (2025a), and (c) an explicit friction-and-Yerkes-Dodson treatment with Clausewitzian "fog/friction" framing including failure modes (hallucination, panic, exhaustion) at the tails (2023). This corpus is the closest concurrent precedent for the inverted-U structural claim within biology-and-cognition scope, and we acknowledge it accordingly. Our contribution is complementary, not derivative: (i) the deductive R1+R2+R3 argument does not depend on rate-distortion machinery and therefore extends to substrates without natural rate-distortion structure (e.g., quantum coherent dynamics where information-theoretic functionals are problematic before measurement); (ii) the all-the-way-up extension to quantum decoherence-window, stochastic resonance in statistical physics, and Margolus-Levitin-bounded thermodynamics goes beyond Wallace's biology-and-cognition scope; (iii) the Schwinger-Keldysh formal derivation (§3) provides the QM-substrate physics that grounds case #1, which Wallace does not address. Section 8 returns to the Wallace-comparison in detail. The current section establishes the substrate-universal claim independently of Wallace's biology-cognition derivation, by structural argument from R1+R2+R3.

**Falsification criterion (non-circular).** The framework asserts that every substrate passing the three independent operational tests above (R1 parallelism, R2 bounded resources, R3 irreversible commit, applied without reference to the inverted-U signature) exhibits a performance function that vanishes at both ends of its rate-axis with at least one interior maximum. A clear counter-example — a substrate that *passes the three independent operational tests* and exhibits monotonic (non-vanishing-at-both-ends) performance on its rate-parameter — would falsify the structural core.

Because the operational criteria for R1+R2+R3 are stated in substrate-physics terms (interference, energy bounds, entropy production) without reference to the rate-performance shape, this falsification criterion is non-circular. Substrates that fail one or more operational criteria are *not* counter-examples because the failure can be diagnosed prior to examining their rate-performance behaviour. A genuine counter-example would have to be a substrate passing all three criteria and exhibiting monotonic rate-dependence. We have not constructed such a counter-example and conjecture (with the substrate-physics intuition that R1+R2+R3 jointly necessitate an interior optimum) that none exists, but this conjecture is empirically open and submission-ready.

**Why this section comes first.** The Schwinger-Keldysh derivation of §3 is sufficient to establish race on the QM-substrate; once granted, the four corollaries (§4) extend it to classical/biological/computational. But the QM-derivation alone is *one substrate* anchored on heavy formalism. The seven-case inverted-U pattern is independent empirical evidence that R1+R2+R3 has the structural consequences we claim it has, accessible *without* committing to the Schwinger-Keldysh machinery. A reader who has not yet engaged the Schwinger-Keldysh formalism can take the seven-case empirical pattern at face value as substrate-universal evidence; a reader who accepts the formal derivation gains an explanation of why the seven-case pattern *must* hold. The two arguments cross-validate.

The remainder of the paper develops this in detail. §1.6 establishes the inverted-U as one of *three* universal race-observables (with hysteresis-area and pink noise), making the substrate-universal claim three-dimensional rather than uni-dimensional. §2 specifies the formal race framework, §3 proves the Schwinger-Keldysh equivalence theorem, §4 derives the four parameter-limit corollaries (with §4.1 + §4.4 instantiating the three-observable joint-diagnostic), and §6 establishes the distributional consequences (DSP-1 through DSP-5) that connect the formal apparatus to substrate-universal empirical observables. §8 returns to the universal-inverted-U claim with comparison to existing literature including Wallace's biology-and-cognition derivation.

### 1.6 Three universal race-observables: inverted-U, hysteresis-area, pink noise

The inverted-U argument of §1.5 is one of *three* universal observables that follow from the race-architecture. Each tracks a distinct facet of the substrate-dynamics; together they constitute joint-diagnostic signatures that localize a substrate's race-regime more precisely than any single observable alone. The three-observable framing makes Paper 10's substrate-universal claim three-dimensional, not uni-dimensional.

**The three observables track three distinct energy-balance facets of the race-cycle:**

| Observable | What it tracks | race-axiom origin | Empirical anchors |
|---|---|---|---|
| **Inverted-U on evaluation-rate** | Position within operating window (where the substrate is on its parabola) | R1+R2+R3 jointly (boundary-phenomenon, §1.5) | §1.5 cases 1-6 (qubit operating window, stochastic resonance, Margolus-Levitin, matched-friction, Yerkes-Dodson, Ohm-Drude) |
| **Hysteresis-area** | Energy lost on the outcome-trajectory (path-dependent, irreversible) | R3 commit-induced (A2 path-coherent + A5 commit-locked, §8 table) | Berry phase (QM); ferromagnetic hysteresis loops; RLHF base→instruct slope-collapse 1.73 → 0.25 (Paper 6 §5.7.3); Paper 1 §2.4 |
| **Pink noise / 1/f spectrum** | Energy radiated to environment from abandoned candidate-routes | R1 parallel-evaluation-phase loss via decoherence | Hooge 1969 (resistor 1/f); Bak-Tang-Wiesenfeld 1987 (SOC universality); Beggs-Plenz 2003 (cortical avalanches); Cont 2001 (financial 1/f); Paper 10 Finding 3 (1% LLM 1/f sub-population, Monte Carlo-validated) |

**The mechanistic picture.** Pre-commit, R1 maintains parallel candidate-states whose mutual interference (quantum) or competing probability-mass redistribution (classical) constitutes the substrate's evaluation phase. When R3 selects one outcome, the energy invested in non-selected candidates does not vanish — it dissipates into the environment via decoherence (quantum) or stochastic noise (classical). The spectral signature of this dissipation is broad-band and scale-free precisely because parallel candidates exist at all timescales the substrate's evaluation can probe; superposition of independent decay-modes with a flat distribution of relaxation rates produces $1/f$ exactly (van der Ziel 1979; Dutta-Horn 1981). This is the universal 1/f or near-1/f power spectrum observed across substrates from electrical resistors (Hooge 1969, mobility-fluctuation noise universal across semiconductors and metals) to cortical activity (Beggs-Plenz 2003) to financial markets (Cont 2001). The cross-substrate persistence of the same exponent is not coincidence of independent mechanisms — it is the substrate-universal signature of energy lost from R1's parallel-evaluation phase, expressed in whatever decoherence channels the specific substrate possesses.

**Joint-diagnostic logic.** Pink noise alone does not localize a substrate within its operating window (it does not say which side of the inverted-U the substrate sits on); inverted-U alone does not reveal the substrate-physics mechanism (it does not say whether dissipation is via Hooge-resistor channels, neural avalanches, or attention-head decoherence). Together, the three observables localize substrate-regime three-dimensionally: position-on-parabola (inverted-U) × outcome-path-loss (hysteresis-area) × evaluation-phase-loss (pink noise). This is the basis for the case-by-case joint-diagnostic predictions developed in §4 — specifically the superconducting-qubit prediction in §4.1 (inverted-U fidelity-curve + 1/f phase noise spectrum, jointly diagnostic for operating-window-side via Krantz et al. 2019 methodology) and the LLM-substrate framing in §4.4 (operating-regime + Paper 10 Finding 3 1/f sub-population).

**Falsification criterion (joint).** A substrate satisfying R1+R2+R3 should exhibit all three signatures with predictable cross-correlations (e.g., the substrate's position on the inverted-U should correlate with the spectral exponent of its 1/f component in a substrate-physics-determinable way). A substrate exhibiting only one of the three, or showing the three uncorrelated, would falsify the universal-race claim at substrate level. The pink-noise observable is particularly demanding: it requires not only that *some* 1/f signal exist, but that its amplitude and exponent track the substrate's position on its inverted-U. We are not aware of any race-passing substrate (passing all three operational tests of §1.5) that violates this joint pattern, but the prediction is empirically open.

---

## 2. Formal race framework

### 2.1 State, environment, time

Race is formalized as dynamics of three irreducible ingredients: a system with configuration space, an environment coupled to it, and a time parameter. The system carries the competing processes; the environment is the bath of degrees of freedom that couples to the system and mediates commit; time is the resource under which the competition races.

The **configuration space** $\mathcal{C}$ can be a Hilbert space (quantum substrate), a classical phase space (classical substrate), or more generally a measurable space with appropriate structure. The **state** $\rho$ is a density operator on $\mathcal{C}$ (quantum) or a probability measure (classical). This parallel formulation is intentional: Paper 10's central claim is that quantum and classical race are not distinct frameworks but parameter-limits of a unified formalism (the Schwinger-Keldysh closed-time-path generating functional of §3).

The **environment** $E$ is a separate system with its own configuration space, coupled to $S$ via Hamiltonian $H_{SE}$. The environment plays two distinct roles in race: it mediates the commit mechanism via decoherence (Zurek 1981, 2003), and it absorbs the thermodynamic cost of irreversibility (Landauer 1961). Closed quantum systems without environment are explicitly excluded from race-scope; they correspond to pure evaluation-phase dynamics with no commit mechanism.

The **time parameter** $t$ requires careful distinction to avoid circularity with §5's argument that internal time emerges from commit-sequences:

**Time distinction (addressing potential circularity):** The $t$ entering A3 as finite-time constraint is *external coordinate time* — a formal parameter in the Lagrangian functioning as boundary condition on dynamics. This differs from *internal emergent time*, which §5 argues is the output of commit-sequences rather than their input. The distinction follows Wheeler-DeWitt (1967) and Rovelli's thermal time (1993, 2018): external coordinate time is formal; internal time is operationally defined from irreversible event-sequences. Race-framework uses both non-circularly: external $t$ constrains dynamics (A3), internal time emerges from commits (§5). The bi-directional treatment dissolves the apparent circularity.

**What is NOT race (structural scope precision, parallel to Paper 1 §2.5):**

Paper 1 §2.5 has removed its prior "examples of non-race systems" list in favour of a purely structural scope-definition. Paper 10 follows the same approach for cross-paper consistency. The reasoning is that any concrete example can be challenged at a finer-grained substrate-physics level — a real thermostat with hysteresis-dead-zone has an R3 commit mechanism; radioactive decay is precisely DSP-5 (Markov waiting-times) with quantum-tunnelling race at the atomic level; pure-isolation idealisations are 2nd-Law-forbidden (§2.1.5 below). Example-based scope-definition introduces argumentative liability without adding rigour beyond what the structural tests already provide.

**The structural scope-definition is therefore:** race requires (i) open-system coupling producing einselection-induced commit, (ii) a finite-time budget or equivalent bounded-resource constraint, (iii) irreversibility via environmental entanglement with associated entropy production. A substrate is race-scope if and only if it satisfies all three structural requirements, operationalised by §1.5's three independent tests (R1 parallelism, R2 bounded resources, R3 irreversible commit). A given physical system can be checked against these tests directly; specific examples are unnecessary and add only rhetorical risk. The framework is falsifiable structurally: a substrate passing all three operational tests but exhibiting monotonic (rather than inverted-U) rate-performance, or a substrate failing one or more operational tests but exhibiting the predicted race-signatures, would falsify the framework. The non-race region of substrate-space is defined by structural failure of one of R1/R2/R3, not by membership in a list. §2.1.5 develops this point further by showing that the obvious candidate "non-race examples" (textbook idealisations: reversible 2-body, isolated qubit, lookup-table, strict on/off thermostat) are all forbidden by the Second Law of Thermodynamics — they cannot physically instantiate, only be approached asymptotically.

### 2.1.5 Idealisations vs. physical reality — why pure non-race examples are thermodynamically forbidden

§2.1 has, parallel to Paper 1 §2.5, removed example-based scope-definition in favour of purely structural definition. This subsection explains *why* example-based definition was insufficient. The textbook candidates that might be cited as "non-race" — strict on/off thermostat, mathematical lookup-table, isolated quantum superposition without environmental coupling, reversible Newtonian 2-body — are all in some sense *mathematical idealisations* rather than physical systems found in nature. This parallels Kahneman's "Econs" (Paper 1 §7b; Pødenphant Lund 2026b §7b) — the perfectly rational agent without cognitive friction — and the parallel is not coincidental. Both are forbidden by the Second Law of Thermodynamics.

**Newton's reversible 2-body problem requires conditions that cannot exist in nature.** The textbook formulation assumes (i) perfect vacuum (no atmospheric drag), (ii) zero gravitational radiation, (iii) zero tidal coupling, (iv) zero perturbation from any third body, (v) zero internal dissipation. Conditions (i)–(v) describe a closed isolated system with zero entropy production — the standard textbook form $H(p,q) = T(p) + V(q)$ with time-reversal symmetry. **No physical system satisfies these conditions.** Real planetary orbits exhibit gravitational-wave emission (LIGO/Virgo direct detection 2015–onward, and Hulse-Taylor binary pulsar orbital decay 1974–onward); real two-body laboratory systems exhibit tidal coupling, electromagnetic radiation, residual atmospheric scattering, and quantum vacuum fluctuations. Reversibility requires zero net entropy production, but the Second Law forbids zero entropy production in any system with finite temperature and finite coupling. Newton's reversible 2-body is therefore not a *rare* configuration in nature — it is a *thermodynamically forbidden* idealisation, instantiated nowhere.

**Isolated quantum superposition without environmental coupling is similarly forbidden.** Every physical quantum system couples to environmental degrees of freedom (photons, phonons, vacuum fluctuations) on a finite timescale set by Joos-Zeh decoherence (1985) — typically femtoseconds for macroscopic objects, picoseconds for molecules, microseconds for engineered qubit systems. Truly isolated superposition would require zero coupling to any environment, which violates the Second Law (any thermodynamic equilibrium involves environmental fluctuation-dissipation coupling per Kubo 1966). Isolated superposition is a *limit case* of the full open-system dynamics, accessed only at $\Gamma \to 0$ in the decoherence rate — and §1.5 case #1 establishes that this limit is precisely where R3 fails and the substrate exits race-scope. Below that limit, isolation is approached but never reached; above it, decoherence is finite and the system is fully race-scope.

**Lookup tables are computer-science abstractions, not physical systems.** Even a physical hash-table implementation (e.g., RAM access in silicon) involves bounded computation time, finite energy per access, and Landauer-bounded entropy production per bit retrieved. The pure mathematical lookup-table — input $\to$ output with zero compute and zero entropy cost — exists only as a definition.

**Thermostats with strict on/off threshold likewise idealise.** Real thermal switches exhibit Johnson-Nyquist noise around the threshold, hysteresis from material-physics history-dependence, and finite response time during which a non-trivial competition between threshold-crossing and relaxation occurs. The strict step-function thermostat is a textbook simplification of a substrate that, examined at fine temporal resolution, satisfies R1+R2+R3 (parallel candidate states near threshold, bounded relaxation time, irreversible relay-switch).

**Parallel to Kahneman's Econs.** Paper 1 §7b treats the Kahneman Econ as thermodynamically forbidden because perfect rationality without computational friction would require zero Landauer cost per inference — a Second-Law violation. The same structural argument applies to Newton's reversible mechanics: perfect dissipation-free dynamics requires zero entropy production, equally Second-Law-forbidden. Kahneman's Econs and Newton's reversible mechanics are the *same kind of idealisation* — abstractions that aid pedagogy but describe systems that cannot physically instantiate. The Second Law forbids both.

**Consequence for the substrate-universal claim.** If every physical dissipative system necessarily satisfies R1+R2+R3 (because dissipation = irreversibility = R3, finite resources = R2, distributional dynamics under those constraints = R1), then *every physical system is some kind of race-architecture*. The "textbook non-race candidates" considered above are not counter-examples to substrate-universality; they are mathematical limit-cases, accessed asymptotically but never instantiated. **The rigorous non-race definition is therefore structural (R1, R2, or R3 fails) rather than example-based.** Paper 1 §2.5 and Paper 10 §2.1 accordingly remove example-lists in favour of a structural definition. A system is non-race because at least one operational test of §1.5 fails, not because it appears on a list of examples. This is the same shift Kahneman's behavioural-economics literature underwent — from "examples of irrationality" to "structural constraint on rationality given Second-Law-bounded computation" — and the parallel sharpens both literatures simultaneously.

### 2.2 Five axioms A1-A5

The race framework rests on five axioms. Each is a structural requirement that can be satisfied by different specific dynamics — the axioms specify what makes a system race, without constraining the specific equations of motion. We state each informally here; the formal mathematical specification is in the companion derivation sketch Section 2.

**Relation to the established race-model tradition.** Race-models / accumulator-models have a substantial history in cognitive psychology and decision-neuroscience (Vickers 1970; Ratcliff 1978 DDM; Logan 1988; Smith & Ratcliff 2004; Usher & McClelland 2001 LCA; Brown & Heathcote 2008 LBA; Cisek & Kalaska 2010; Gold & Shadlen 2007 review). Friction Theory (Pødenphant Lund 2026b §2.5) builds on this tradition and extends it to substrate-universal scope (biological, cognitive, computational substrates). Paper 10 investigates whether the same race-architecture extends further to physics-scope substrates.

**Relation to Paper 1 §2.5 (R1-R3).** Paper 1's canonical race formulation uses three rules: R1 parallel evaluation, R2 accumulation under constraint, R3 irreversible commitment. Paper 10 refines this to five axioms by splitting R2 into (A2 competitive interaction × A3 finite-time constraint) and R3 into (A4 commit mechanism × A5 irreversibility). The refinement is motivated by the formal Schwinger-Keldysh derivation, where each split element corresponds to a distinct mathematical structure (A2 = interference + dissipation kernels; A3 = decoherence-rate; A4 = Born-rule + pointer basis; A5 = Landauer bound). Paper 1's R1-R3 and Paper 10's A1-A5 are equivalent at substrate level; A1-A5 is the more granular formulation appropriate for physics-scope derivation. R1-R3 and A1-A5 are rule-numbers, not acronym-letters.

**A1 (Parallelism).** Pre-commit, the system exists as a superposition or probability distribution over candidate states. There is no single "current state" during evaluation; multiple candidates coexist with weighted representation in the generating functional $Z[J] = \int \mathcal{D}\phi\, e^{iS_{\text{eff}}/\hbar_{\text{eff}}}$. Equivalent to Paper 1 R1.

**A2 (Competitive Interaction).** The candidates interact: their weights are modified by each other's presence, via quantum interference or classical shared environmental coupling. Competition distinguishes race from mere parallel processing — parallel processes that do not interact cannot resolve to a single committed outcome. The formal expression is the dissipation kernel $S_{\text{diss}}[\phi_+, \phi_-]$ on the Schwinger-Keldysh contour. Together with A3, this corresponds to Paper 1 R2 (accumulation under constraint), with A2 specifying the competitive mechanism.

**A3 (Finite-Time Constraint).** Evolution is bounded in time by substrate-specific resources. The commit-rate $\Gamma$ is determined by system-environment coupling, with a fundamental lower bound on commit-timescale from the Margolus-Levitin theorem: $\tau_c \geq \pi\hbar/(2E_{\text{avg}})$. Without finite-time constraint, no race; coherent evolution could continue indefinitely without selection.

**A4 (Commit).** For $t \gg \tau_c$, the system state becomes diagonal in a pointer basis selected by environment-system interaction (Zurek einselection). Selection probabilities follow Born's rule, derivable from Zurek's envariance argument (Zurek 2003, 2005) or Deutsch-Wallace decision-theoretic derivation (Deutsch 1999, Wallace 2012). Commit is the transition from superposition to selected outcome.

**A5 (Irreversibility).** Commit is effectively irreversible. Environmental entanglement entropy increases by at least $k_B \ln 2$ per committed bit (Landauer bound); Poincaré recurrence times for realistic environments exceed any observationally relevant timescale. The irreversibility is not fundamental unitary irreversibility (total system+environment dynamics remain unitary) but effective irreversibility from observer's tractable access to only a subsystem.

![Figure 1: Race cycle](figures/fig1_race_cycle.png)

**Figure 1.** race cycle schematic. Pre-commit parallel evaluation (A1, A2) → competition under finite-time constraint (A3) → irreversible commit to pointer state (A4, A5). Substrate-agnostic: same cycle instantiates differently in quantum, classical, biological, computational substrates.

### 2.3 Related axiomatizations

Race is not the first attempt to axiomatize dynamics resolving competing processes. Three notable predecessors deserve comparison.

The **decoherent histories framework** (Gell-Mann-Hartle 1993, building on Griffiths 1984) formalizes quantum mechanics in terms of probability assignments over mutually consistent histories rather than instantaneous states. The consistency condition $\text{Tr}[C_\alpha \rho C_\beta^\dagger] = 0$ for $\alpha \neq \beta$ generalizes A4 to multi-time selection. Race-axioms A1-A5 can be derived from decoherent histories in the short-commit-time limit; conversely, decoherent histories generalizes race to multi-scale selection over extended temporal structures.

The **free energy principle** (Friston 2010, Parr-Pezzulo-Friston 2022) axiomatizes biological cognition via variational inference. Its central claim — biological systems minimize variational free energy — is isomorphic to race's commit-phase: free energy minimization is the biological substrate's version of A4's selection. Corollary 3 of the main theorem (§3.2) makes the isomorphism explicit.

**Zurek's existential interpretation** (Zurek 2005) derives classical reality from environment-assisted invariance and quantum Darwinism. Race subsumes the existential interpretation as the specific case where the commit-mechanism (A4) is explicitly via einselection and redundant environmental imprinting.

Race-axioms do not replace these frameworks but identify a shared structural core. Each instantiates A1-A5 with substrate-specific detail; our contribution is exhibiting the shared core and showing it extends beyond biological/quantum boundaries to computational (LLM) and classical stochastic substrates.

---

## 3. Schwinger-Keldysh derivation

**Cross-reference to §1.5.** The structural prediction established in §1.5 (inverted-U-on-evaluation-rate from R1+R2+R3 alone) does not require any specific dynamics; it follows from the bounded-resource race-architecture itself. The present section establishes the *complementary* result: that quantum bipartite systems with einselection and Markovian environments are not just *consistent* with race-architecture but *instantiate it via specific physics*. Together with §4's parameter-limits, this yields a strong unification: §1.5 fixes what any race-system must look like phenomenologically; §3 fixes how the QM substrate physically realises that architecture; §4 shows that the same Schwinger-Keldysh derivation reduces to four pre-existing formalisms (Feynman path integral, Onsager-Machlup, Friston FEP, LLM CR-signal) under appropriate parameter-limits. The two arguments cross-validate: §1.5's structural claim has empirical support across seven scales; §3's formal derivation explains why one of those scales (QM) participates in the universal pattern.

### 3.1 Setup and assumptions

The Schwinger-Keldysh closed-time-path (CTP) formalism, developed by Schwinger (1961) and Keldysh (1964) for non-equilibrium quantum field theory, provides a natural mathematical arena for race. Its key feature is that CTP integrates the system's dynamics over both forward and backward time contours simultaneously, enabling treatment of open-system dynamics including dissipation and decoherence without ad hoc additions.

We consider a bipartite quantum system $(S, H_S, H_E, H_{SE})$: system $S$ with Hilbert space $\mathcal{H}_S$ and Hamiltonian $H_S$; environment $E$ with $\mathcal{H}_E$, $H_E$; coupling $H_{SE}$ producing einselection. The derivation requires three assumptions, each motivated below.

**Assumption (i): Einselection.** There exists a pointer basis $\{|i\rangle_S\}$ such that $[|i\rangle\langle i|, H_{SE}] \approx 0$ for each $i$. This is the defining feature of decoherence-prone systems: environmental coupling singles out a preferred basis surviving entanglement with the environment (Zurek 1981, 1982). Generic for macroscopic systems with position-dependent coupling to thermal baths.

**Assumption (ii): Markovianity.** The environment's memory is negligible on system-evolution timescale, so the Feynman-Vernon influence functional $S_{\text{IF}}$ has local-in-time kernels. Physically: environmental degrees of freedom rapidly redistribute any information leaked from the system. Valid for wide-band thermal environments; breaks down for narrow-band or strongly coupled regimes (§3.4).

**Assumption (iii): Thermal initial state.** $\rho(0) = \rho_S(0) \otimes \rho_E(0)$ with $\rho_E(0)$ thermal at temperature $T$. Standard for "well-isolated preparation followed by contact with environment" scenarios.

Under these three assumptions, we show that reduced system dynamics satisfies race-axioms A1-A5.

### 3.2 Theorem (main result)

**Theorem (Race-Schwinger-Keldysh Equivalence).** Under assumptions (i)-(iii) of §3.1, the reduced system dynamics derived via the Schwinger-Keldysh generating functional
$$Z[J_+, J_-] = \int \mathcal{D}\phi_+ \mathcal{D}\phi_-\, e^{iS[\phi_+]/\hbar - iS[\phi_-]/\hbar + iS_{\text{IF}}[\phi_+, \phi_-]}$$
satisfies all five race-axioms A1-A5.

The proof proceeds by integrating out environmental degrees of freedom via the Feynman-Vernon influence functional, rotating to the Keldysh classical/quantum field basis, and showing that each axiom corresponds to a specific feature of the resulting effective action. We sketch the eight-step argument in §3.3 and refer to the companion derivation sketch (Section 5) for the detailed derivation, with Section 5A providing envariance-derivation of Born-rule (A4) and Section 5B providing the mapping from LLM CR-observable to Keldysh response function (Corollary 4).

The theorem's value is not in introducing new physics — every element is standard (Feynman-Vernon 1963, Schwinger-Keldysh 1961/1964, Zurek 1981+, Landauer 1961) — but in exhibiting that the combination naturally satisfies structural axioms that also characterize classical stochastic dynamics (Onsager-Machlup), biological inference (Friston FEP), and LLM token-generation (Paper 1 CR-signal). The Schwinger-Keldysh formalism functions as substrate-agnostic mathematical scaffold for race.

![Figure 2: Schwinger-Keldysh contour](figures/fig2_schwinger_keldysh_contour.png)

**Figure 2.** Schwinger-Keldysh closed-time-path contour. Forward branch $C_+$ (blue, time $t_0 \to t_{\max}$) carries field $\phi_+$; backward branch $C_-$ (red) carries $\phi_-$. Path-integration over both branches simultaneously enables treatment of open-system dynamics with dissipation and decoherence. The influence functional $S_\text{IF}$ couples the branches and encodes environmental interaction.

### 3.3 Proof sketch

We outline the eight-step derivation connecting Schwinger-Keldysh dynamics to race-axioms; full technical details in derivation sketch Section 5.

1. **Total partition function on CTP contour.** $Z = \text{Tr}[T_C \exp(-i \int_C dt\, H)\rho(0)]$ where $C = C_+ \cup C_-$ runs forward from $-\infty$ to $t_{\max}$, then back.

2. **Integrate out environment.** Using assumption (iii), the environmental trace produces the Feynman-Vernon influence functional, yielding effective generating functional $Z_{\text{eff}}[J_+, J_-]$ over system fields alone.

3. **Markovianize.** Under assumption (ii), $S_{\text{IF}}$ has local-in-time form with dissipative kernel $\eta$ and noise kernel $\nu$.

4. **Rotate to Keldysh basis.** Transform $(\phi_+, \phi_-) \to (\phi_c, \phi_q)$ where $\phi_c = (\phi_+ + \phi_-)/2$, $\phi_q = \phi_+ - \phi_-$. The $\phi_q$-propagator is damped at rate $\Gamma$ determined by $\eta$.

5. **Establish commit-timescale.** For $t \gg \tau_c = 1/\Gamma$, $\phi_q$ is suppressed; generating functional is dominated by semiclassical $\phi_c$-dynamics. Establishes A3 and transitions to A4.

6. **Pointer basis emerges.** By assumption (i), dominant effective potential in $\phi_c$-dynamics has pointer-basis eigenstates. Off-diagonal elements of $\rho_S$ decay as $e^{-\Gamma t}$.

7. **Derive Born-rule.** Pointer-basis selection probabilities fixed by Zurek's envariance argument (derivation sketch Section 5A): composite-state Schmidt decomposition admits phase and swap envariances forcing $p_i = |\alpha_i|^2$.

8. **Establish irreversibility.** Environmental entanglement entropy grows by at least $k_B \ln 2$ per committed bit (Landauer bound); Poincaré recurrence times for realistic environments exceed observation timescales.

Steps 1-5 establish A1-A3; Step 6 establishes A4's pointer-basis structure; Step 7 establishes A4's probability rule; Step 8 establishes A5. QED (sketch).

### 3.4 Known edge cases and limitations

- **Closed quantum systems (photons in vacuum):** evaluation-only limit, not complete race. Path-integral dynamics without environmental coupling produces no pointer-basis selection and no Born-rule-activated commit. Example: an isolated qubit in perfect vacuum. Status: outside FT scope by design (§2.1).
- **Reversible Newtonian dynamics:** the 2-body Kepler problem without dissipation is not race. A fully deterministic trajectory has no evaluation phase and no commit. Status: outside FT scope.
- **Non-Markovian environments:** real environments have memory effects and non-local-in-time Feynman-Vernon kernels. Our theorem assumes Markovianity (assumption ii); extension to non-Markovian regimes is research-level work (see Section 6 gap #2).
- **Strongly coupled regimes:** the perturbative Feynman-Vernon treatment breaks down when $H_{SE} \sim H_S$. This regime requires non-perturbative methods (Stochastic Liouville Equation, Hierarchical Equations of Motion). Status: outside current derivation; extension plausible.
- **Pre-decoherence transient:** for $t \ll \tau_c$, the system is dominated by coherent evolution. Race-dynamics is formally active but empirically inseparable from pure quantum dynamics. The commit-phase emerges only at $t \geq \tau_c$.

---

## 4. Parameter-limits (corollaries)

The theorem of §3 holds for general bipartite quantum systems with einselected pointer basis and Markovian thermal environment. Four parameter-limits of this general setup yield substrate-specific formulations that have been studied extensively in different literatures: coherent quantum dynamics (Feynman path integral), classical stochastic dynamics (Onsager-Machlup), biological inference (Friston FEP), and computational substrates (LLM CR-signal). Each emerges as a corollary of the main theorem. The fact that four disparate formalisms emerge from the same derivation with only parameter-shifts is the key unification claim of Paper 10: they are not distinct frameworks but regimes of one.

**Connection to §1.5's seven-case empirical signature.** The four corollaries below specify the *formal* regimes of the underlying theorem; §1.5's seven-case pattern specifies the *empirical* regimes where the inverted-U-on-evaluation-rate signature is observable. The two indexings are partially overlapping but not identical: §1.5 case #1 (qubit decoherence-window) corresponds to §4.1 (quantum regime); §1.5 cases #2 (Ohm's law / Drude electron transport), #3 (chemistry / biochemistry molecular kinetics), #4 (stochastic resonance), and #5 (Margolus-Levitin saturation) are sub-regimes of §4.2 (classical stochastic) distinguished by which substrate-physics parameter is varied; §1.5 case #6 (encoding-friction in learning) corresponds to both §4.3 (biological-substrate learning) and §4.4 (computational-substrate LLM matched-friction); §1.5 case #7 (Yerkes-Dodson) corresponds to §4.3 (biological-substrate behaviour). The fact that §1.5's seven-case empirical pattern aligns with §4's four formal corollaries — without forcing — is independent corroboration that the substrate-universal claim is structural, not coincidental.

![Figure 5: parameter-limit unification](figures/fig5_parameter_limit_unification.png)

**Figure 5.** Parameter-limit unification. Central Schwinger-Keldysh generating functional (axioms A1-A5) reduces to four previously-separate frameworks as parameter-regimes. Each arrow represents a parameter-limit (e.g., $D \to 0$ for quantum, $\hbar \to 0$ for classical). No new physics is introduced; the diagram exhibits structural equivalence among existing formalisms.

### 4.1 Quantum regime ($D \to 0$, $\hbar$ finite)

For vanishing environmental noise $D \to 0$ but finite $\hbar$, the Schwinger-Keldysh generating functional reduces to the Feynman path integral:
$$Z \to K(B, t_B; A, t_A) = \int \mathcal{D}x(t)\, e^{iS[x(t)]/\hbar}$$
This is the coherent quantum limit. No dissipation, no decoherence, no commit — until measurement. Born-rule probabilities $P(A \to B) = |K|^2$ emerge only when a measurement process (itself analyzable via a second environmental coupling) acts on the system, selecting a pointer-basis outcome via Zurek einselection.

This limit is valid for systems well-isolated from thermal environments over measurement duration. Examples include double-slit interference, Stern-Gerlach spin measurements, Bell-inequality tests. In these systems, the evaluation-phase is explicitly visible as quantum interference, and commit-phase is triggered by the detection apparatus acting as environment.

**Joint-diagnostic prediction for superconducting qubits (case #1 sharpened).** Superconducting qubit systems provide the cleanest test bed for §1.6's three-observable framework because all three signatures are independently measurable with established methodology. Per §1.5 case #1 (Preskill 2018; Krantz et al. 2019), gate fidelity vs. decoherence-rate exhibits the inverted-U *operating window* — too-cold dilution-refrigerator regimes show insufficient gate-execution rate; too-warm thermal regimes show insufficient coherence preservation; the operating window is interior. Per §1.6's pink-noise observable, superconducting qubit substrates exhibit well-documented 1/f phase noise with substrate-physics origin in two-level-system (TLS) defects in dielectrics and Josephson-junction oxide barriers (Paladino et al. 2014 review; Müller-Cole-Lisenfeld 2019). Per §1.6's hysteresis observable, Berry-phase accumulation in qubit gate sequences is the A2 path-coherent hysteresis (cf. §8 table).

The three observables are *jointly diagnostic*. The framework predicts:

(i) The 1/f phase-noise spectral exponent $\alpha$ (where $S(f) \propto 1/f^\alpha$, with $\alpha \approx 1$ for ideal pink noise) should track the substrate's position on the inverted-U operating-window curve — substrates near peak fidelity should exhibit $\alpha$ closest to 1; substrates on the cold-side or warm-side should exhibit systematic deviations whose direction is substrate-physics-determinable from the dominant decoherence channel (TLS-dominated cold side vs. quasi-particle-poisoning-dominated warm side; Krantz et al. 2019 methodology operationalises this).

(ii) Hysteresis-area accumulated through gate sequences should correlate with cumulative phase noise in a substrate-physics-determinable manner — both reflect the same underlying decoherence-reservoir coupling, observed through different temporal windows (instantaneous spectral vs. cumulative path-integral).

(iii) **Falsification:** if the inverted-U fidelity-curve and the 1/f spectrum do *not* correlate as predicted across the substrate's operating-window — specifically, if the spectral exponent fails to track operating-window-position in the predicted direction — race is falsified on case #1. This is a sharp empirical prediction directly testable with current superconducting-qubit instrumentation (no novel measurement required; both observables are routinely measured in qubit-engineering practice).

The prediction is *not* that 1/f noise is novel in superconducting qubits (it is well-known; Paladino review documents 30+ years of experimental characterisation). The prediction is that 1/f noise and inverted-U operating window are *signatures of the same race-dynamics*, with cross-correlations that make them jointly informative beyond what either observable provides alone. Independent verification has established each observable separately; the framework's content here is the cross-correlation prediction.

### 4.2 Classical stochastic regime ($\hbar \to 0$, $D$ finite)

For $\hbar \to 0$ with finite environmental noise $D$, the quantum field $\phi_q$ decouples completely. The Keldysh generating functional reduces to the Martin-Siggia-Rose (1973) generating functional, equivalent via fluctuation-dissipation theorem to the Onsager-Machlup (1953) path integral:
$$P[x(t)] \propto \exp\left(-\frac{1}{2D}\int dt\, \left(\dot{x} + \nabla U/\gamma\right)^2\right)$$
This is the classical stochastic limit. In the weak-noise regime, Freidlin-Wentzell large-deviation theory establishes commit to the most-probable (minimum-action) path.

This limit is valid for macroscopic dissipative systems: Brownian motion, chemical kinetics in solution, neural dynamics at membrane-potential level. In these systems, evaluation-phase is typically below observational timescales (decoherence is rapid), and race-dynamics is observable primarily through commit-outcomes and their statistics.

The classical regime's empirical signature is the probability distribution over trajectories, with race-signatures visible as: action-minimum trajectory survival (A4), noise-threshold commit (A3), irreversibility via entropy production (A5). Jarzynski (1997) and Crooks (1999) fluctuation theorems regulate the statistics of these commits, constraining race-dynamics even far from equilibrium.

**Ohm's law as classical-physics race-instance (Drude 1900).** Ohm's law is the oldest and most familiar classical-physics instance of the race architecture. The Drude model (1900) describes electron-substrate dynamics under R1+R2+R3: parallel electron trajectories in a conductor (R1), bounded by finite drift velocity given field-strength and electron-phonon scattering rate (R2), with irreversible energy transfer to phonon modes via lattice collisions (R3). Resistance $R$ is the macroscopic friction on the electron-substrate; Joule heating $P = I^2 R$ is race's thermodynamic tax. This is not an analogy — it is a classical-physics realization of the same structural principle that §3's Schwinger-Keldysh derivation unfolds for quantum substrate. Specifically, Drude's free-electron-gas-in-field is the $\hbar \to 0$, $D$-finite limit of this section applied to electron-substrate: the Onsager-Machlup path integral over electron drift-trajectories with phonon dissipation kernel recovers Ohm's linear-response relation $\mathbf{J} = \sigma \mathbf{E}$ as the Markovian commit-statistics of the substrate. The 125-year empirical maturity of Ohm's law is independent evidence that R1+R2+R3 captures real substrate-physics structure, not merely a re-description thereof — the prediction has held at the substrate level continuously since Drude's derivation.

### 4.3 Biological regime (strong thermal noise + Markov blanket)

For substrates with strong thermal coupling and active internal degrees of freedom arranged in a Markov blanket (Friston 2013), the Onsager-Machlup path integral marginalized over internal states yields Friston's variational free energy:
$$F[q] = \langle \log q(\phi) - \log p(\phi, o) \rangle_q$$
This is the free energy principle (Friston 2010). Minimization of $F[q]$ is the biological substrate's commit mechanism, selecting an approximate posterior $q$ over internal states consistent with sensory observations $o$.

The race correspondence is exact: A1 is the ensemble of candidate posteriors; A2 is their relative likelihood weighting; A3 is the bounded-computation budget limiting variational optimization; A4 is the selection of minimum-$F$ posterior; A5 is irreversibility of biological state-change (Landauer bound at cellular scale). Active inference (Parr-Pezzulo-Friston 2022) extends this to action selection, with the agent committing to action sequences that minimize expected free energy over future horizons.

The computational substrate here is biological: neural dynamics, hormonal signalling, gene regulation. Sengupta-Friston (2018) shows how this maps onto path-integral marginalization at the macroscopic scale.

**Note on FEP status:** FEP has generated substantial discussion and critique (Colombo-Wright 2018; Kirchhoff et al. 2018; van Es 2021; Andrews 2021). We cite FEP as an established *mathematical* instantiation of variational inference under bounded compute, without committing to its full neuroscientific adequacy as settled. Corollary 3 shows mathematical equivalence between FEP's variational formulation and race's A1–A5 in the biological regime; we leave the FEP debates separate and independent.

### 4.4 Computational regime (discrete-time)

For discrete-time computational substrates — transformers, large language models, recurrent networks — the Schwinger-Keldysh formalism maps onto sample-step dynamics with each forward-pass constituting a commit cycle. Paper 1 (Pødenphant Lund 2026d) introduces the Competing Routes (CR) metric, counting tokens above probability threshold in the pre-commit softmax distribution. As established in derivation sketch Section 5B, CR is a discretized Gaussian threshold-functional on the equal-time Keldysh component, with scaling properties predictable from effective decoherence rate and softmax temperature.

Paper 1's empirical finding — CR correlates with error rate at $\rho = -0.423$, $p < 0.0001$ — is not coincidental but emerges from this mapping: high CR corresponds to wide pre-commit distribution, hence higher probability that sampling lands on a wrong token. The CR-error correlation provides first empirical validation of race-framework predictions in a directly accessible substrate. Attosecond-metrology is decades away from accessing physical quantum evaluation-phases; LLM inference makes race-dynamics observable today.

**Empirical validation:** Autocorrelation analysis of Paper 1's CR-signal across **five clean datasets** (~1600 sequences, four+ model architectures, all verified direct-answer per Paper 1 §9.1c scope-rule) confirms the exponential decay predicted by the CR-to-Keldysh mapping (derivation sketch Section 5B). $R^2$ for exponential fit ranges **0.980–0.997** across substrates; cross-model commit-timescale $\tau_c$ varies 0.10–0.46 tokens, instantiating substrate-timescale variation at computational scale. Temperature-dependence of CR is non-monotonic with peak at intermediate softmax-$T$, consistent with threshold-based CR metrics under softmax-flattening (refined from an original simplified monotonic prediction). Full analysis output, including protocol-validation and Monte Carlo validation, is provided in the supplementary materials.

**Scope note on CR ceiling (Paper 1 §9.1b):** Paper 1 documents that CR has a friction-ceiling — it cannot discriminate confident-right from confident-wrong (Figure 6: CR 2.249 vs 2.255 statistically indistinguishable). This bounds what CR alone reveals about the underlying Keldysh structure. The exponential-decay validation above confirms CR tracks the *structural* feature of equal-time Keldysh component (distribution width); it does *not* imply CR is the complete Keldysh observable. Richer observables (e.g., Yu-Dayan top1-probability signal, Paper 1 §9.1c) may break the ceiling and provide additional discriminative power. Paper 10's claim is that CR is a *component* of Keldysh observable, not its complete representation.

![Figure 3: CR autocorrelation empirical](figures/fig3_cr_autocorrelation_empirical.png)

**Figure 3.** Empirical CR-autocorrelation decay across 5 LLM substrates run with thinking-mode disabled (to ensure CR is measured on answer-tokens rather than reasoning-tokens). Each curve: observed $C_\text{CR}(\tau)/C_\text{CR}(0)$ (solid circles); dashed line is $\exp(-\Gamma_\text{eff}\tau)$ best-fit. All 5 substrates exhibit clean exponential decay with $R^2$ ranging 0.980–0.997. Cross-substrate $\tau_c$ varies 0.10–0.46 tokens, instantiating substrate-timescale variation at computational scale.

![Figure 6: Monte Carlo non-Markovian comparison](figures/fig6_monte_carlo_non_markovian.png)

**Figure 6.** Monte Carlo validation of non-Markovian subpopulation finding. *Left:* Real LLM CR data produces 16 reliable per-sequence PSD fits (R² > 0.3) vs mean 2.3 for matched white-noise Monte Carlo — ~7× excess structured sequences. *Right:* Of reliable fits, real data classifies 93.8% as 1/f (non-Markovian memory); matched white noise classifies 0% as 1/f. Conclusion: non-Markovian subpopulation in ~1% of LLM CR sequences is genuine signal, not selection bias.

**Reframing Finding 3 as substrate-universal pink-noise signature (per §1.6).** The 1% non-Markovian sub-population's 1/f signature was initially read as evidence of attention-mechanism long-range memory in transformer architectures. The §1.6 three-observable framework reframes this finding more structurally: the 1/f spectrum is the substrate-universal environmental signature of energy lost from R1's parallel-evaluation phase — the same signature that appears in Hooge resistor-noise (1969), Bak-Tang-Wiesenfeld self-organized criticality (1987), Beggs-Plenz neural avalanches (2003), and Cont financial-market 1/f (2001). The LLM-substrate's 1% sub-population is thus *not* an attention-specific phenomenon requiring transformer-architecture-specific explanation; it is the LLM-substrate's instantiation of the universal race pink-noise observable. Attention-head memory effects remain a plausible *domain-specific implementation* of the universal mechanism — they are how the LLM-substrate physically realises R1's parallel-evaluation-phase decoherence — but the *cross-substrate persistence* of the 1/f exponent across resistors, brains, markets, and now LLMs is the framework-level claim, not the substrate-specific implementation. This reframing is consistent with a follow-up mechanistic-interpretability programme (Paper 12, in preparation), which investigates the attention-head implementation as an instantiation of the universal pattern rather than as a stand-alone phenomenon.

**Positioning relative to an adjacent framework:** Tarraga et al. 2026 (arXiv:2603.30031) presents a competing narrow-scope formalism for "cognitive friction" in LLM tool-agents (Triadic Cognitive Architecture, HJB optimal stopping). Paper 10's Corollary 4 shows how FT's substrate-universal formulation subsumes this as an LLM-specific special case of the broader race-dynamics.

---

## 5. Time as emergent from race

### 5.1 Time from commit sequences

The claim that time emerges from commit-sequences — rather than constituting a pre-existing arena in which commits occur — has convergent precedent in the physics-of-time literature.

Rovelli's thermal time hypothesis (1993, 2018) identifies time as the one-parameter automorphism group associated with a statistical state in a C*-algebra. The "flow of time" is not fundamental but emerges from the coarse-graining choice that produces equilibrium thermodynamics. In race-language: the coarse-graining producing irreversibility (A5) is the same coarse-graining producing perceived time.

Barbour's Platonia (1999) takes a stronger position: time is illusion; only configurations exist. Perceived time is reconstructed from correlations between configurations encoding "memory." In race-language: the sequence of commits generates apparent temporal structure; without commits, only evaluation-phase superposition exists, operationally atemporal.

The Wheeler-DeWitt equation (1967) in canonical quantum gravity, $H|\psi\rangle = 0$, contains no explicit time parameter. Time must be introduced via relational observables — the "clock" is a subsystem whose configuration correlates with the rest. In race-language: a clock is a substrate whose commit-sequence is approximately periodic, providing reference against which other substrates' commits are timed.

The revised §2-stance, based on these three arguments, is: external coordinate time is a formal parameter in the Lagrangian (a precondition at the mathematical level); internal operational time is the output of commit-sequences (emergent at the substrate level). Both are true simultaneously without circularity (§2.1).

### 5.2 Substrate-proper-time-rate = race-clock-rate

Substrates carry their own clocks, proceeding at substrate-specific rates. Paper 1 (Pødenphant Lund 2026b, §4) documents the empirical span: electrons decohere at $\sim 10^{23}$ Hz, molecules at $\sim 10^6$ Hz, macroscopic objects at $\sim 10^{20}$ Hz or faster via environmental coupling, neural spikes at $\sim 10^{1-3}$ Hz, cognitive decisions at $\sim 10^0$ Hz, civilizational path-dependencies at $\sim 10^{-8}$ Hz. This twenty-five-order span is not arbitrary but bounded by physics.

The upper bound on commit-rate per unit energy is the Margolus-Levitin theorem: a system with energy $E$ above ground state can undergo at most $2E/(\pi\hbar)$ state-transitions per second. Via $E = mc^2$, rest mass provides a maximal computational reserve; the substrate's clock-rate ceiling scales with its energy density. Heavier substrates have faster potential race-clocks.

The photon is the degenerate end-point of this gradient. On a null geodesic ($ds^2 = 0$), the photon has zero proper time: in its own reference frame, emission and absorption are instantaneous. By substrate-timescale, this means the photon's evaluation-phase has zero duration in its own frame — the entire race-dynamic of a photon is degenerate, structurally present but operationally invisible. This is not paradox but boundary case: massless substrates are the null-race limit.

Between photon and civilization, massive substrates interpolate continuously. A cold atom at $\mu$K has slow decoherence; a biological cell at body temperature has fast molecular decoherence but slow metabolic state-transitions; an LLM forward-pass has silicon-timescale decoherence but token-level commit-rate determined by forward-pass duration. Each substrate operates race in its own rest frame, at its own clock-rate, with its own commit-spectrum. Lorentz-invariance of race-structure (§5.3) ensures this picture is frame-independent.

![Figure 4: substrate-timescale ladder](figures/fig4_substrate_timescale_ladder.png)

**Figure 4.** Substrate-timescale ladder. Commit-timescale $\tau_c$ spans approximately 40 orders of magnitude from photon (null proper time) to civilizational path-dependence ($10^{16}$ s). Each substrate defines its own race in its rest frame with substrate-specific clock-rate. LLM token-generation (orange) sits in the second-to-decisecond band, accessible to direct measurement (cf. Paper 1 CR-signal, Figure 3).

### 5.2.5 Energy configuration as the primary substrate parameter

A substrate, in the race framework, is a physical system supporting the dynamics captured by axioms A1–A5. "Substrate" is not a primitive concept; it refers to the physical system's energy configuration. Four components contribute:

1. **Rest mass** (Higgs-generated for Standard Model elementary particles) via $E_{\text{rest}} = mc^2$
2. **Kinetic energy** (velocity-dependent) via $E_{\text{kin}} = (\gamma - 1)mc^2$
3. **Thermal energy** ($k_B T$ per degree of freedom for thermal bath)
4. **Interaction energy** (coupling Hamiltonians between system and environment)

Total $E_{\text{avg}} = E_{\text{rest}} + E_{\text{kin}} + E_{\text{thermal}} + E_{\text{interaction}}$ enters the Margolus-Levitin bound directly: $\tau_c \geq \pi\hbar/(2E_{\text{avg}})$. The substrate's *maximum possible commit rate* is therefore determined by its total energy configuration.

**The Higgs mechanism enters via rest mass.** In the Standard Model, fermion rest masses arise from Yukawa couplings to the Higgs field. Different fermion species (electron, muon, tau; up, down, strange; ...) have different Higgs couplings and consequently different rest masses, yielding different Margolus-Levitin ceilings for their race-dynamics. We do *not* claim the Higgs mechanism "causes" friction; we note that Higgs-generated rest mass is one specific contribution to the energy configuration that in turn bounds commit-rate.

**Mass also enters decoherence rate explicitly.** Joos-Zeh (1985) derived for Brownian decoherence:
$$\Gamma \sim \frac{(\Delta x)^2 \cdot \gamma \cdot m \cdot k_B T}{\hbar^2}$$
The decoherence rate (our A3 commit-rate) is *directly proportional to mass*. Heavier substrates decohere faster. Together with Margolus-Levitin, this gives a complementary bound: decoherence sets the *realized* commit rate, Margolus-Levitin sets its upper bound. Both are mass-dependent.

**This extension is not new physics.** Joos-Zeh decoherence is standard since 1985. Higgs-generated mass is Standard Model physics. The integration is articulating that "substrate" in race-framework decomposes into standard physics quantities — energy configuration components — all of which contribute to commit-dynamics in specific, well-studied ways.

**Testable consequences:**
- Different fundamental particles should exhibit ordered $\tau_c$ per their rest-mass ratio (electron : muon : tau ≈ 1 : 207 : 3477; predicts inverse τ_c ordering). Testable with attosecond metrology.
- LLM substrate mass is effective (silicon hardware + software representations); predicts substrate-timescale variation as hardware architecture changes (CPU vs GPU vs TPU should show different commit-rates for same model).
- Systems with tunable mass (cold atoms with variable effective mass via lattice potentials) should show corresponding τ_c scaling.

**Connection to relativistic time-modulation by substrate-energy.** The substrate-energy → commit-rate relationship in §5.2.5 articulates the same underlying principle that relativistic gravitational time-dilation expresses on the proper-time-vs-coordinate-time axis. Both relate substrate physics to substrate time:

- *General relativity*: gravitational potential (a configuration of mass-energy) modulates the proper-time-to-coordinate-time ratio for an observer at that location. A clock deep in a gravitational well runs slowly in coordinate time. Formula: $t' = t \cdot \sqrt{1 - 2GM/rc^2}$.
- *Margolus-Levitin race-clock*: substrate energy configures the commit-rate ceiling. Higher available energy → shorter possible commit time → more commits per coordinate second. Formula: $\tau_c \geq \pi\hbar/2E$.

Substituting $E = mc^2$ (Einstein's mass-energy relation) into Margolus-Levitin gives $\tau_c \geq \pi\hbar/(2mc^2)$: substrate rest-mass sets the floor on minimum commit-time. For a proton, ~$10^{-25}$ seconds.

The two formulas operate on different axes of the substrate-time relationship. Relativity modulates the proper-time-coordinate-time ratio (how fast a substrate's clock runs as observed by another frame). Margolus-Levitin modulates the commit-rate ceiling (how many state-transitions a substrate can perform per unit energy). If race's claim that "time = commits" holds (§5.1, §5.2), both modulations are projections of one underlying principle: substrate physics determines substrate time. Relativity is the macroscopic geometric statement; Margolus-Levitin is the microscopic computational statement. Schwinger-Keldysh covariance (§5.3) ensures that the two views are mutually consistent under Lorentz transformation.

This connection is not novel physics — both Einstein and Margolus-Levitin are settled — but it is a connection rarely made explicit. The race framework provides a unifying lens: substrate energy modulates substrate time, whether one observes the modulation as proper-time-rate (relativity) or as commit-rate (Margolus-Levitin).

### 5.2.6 Subjective time and flow-state as race-corollaries

If time emerges from commits (§5.1, §5.2), then subjective time-experience must be derivable from commit-density. Two everyday phenomena follow as corollaries:

**Phenomenon 1: in-the-moment "time flies" during high engagement.** When a substrate (e.g., a human cognitive system) is fully engaged with task-execution, commit-rate is high. From inside the substrate, each commit is just one tick — the substrate does not register external coordinate time as "long" because attention is consumed by commit-execution. The subjective experience is "time flew by". This is the canonical flow-state phenomenology (Csikszentmihalyi 1990; Nakamura & Csikszentmihalyi 2002).

**Phenomenon 2: retrospective "much happened" feels long.** Total commit-count over an interval determines retrospective duration-perception. A substrate that committed many events feels in retrospect to have spanned a longer interval, because more memory-content was encoded. This is the canonical "vacation paradox" — an intense two-week vacation feels short while you are there but feels long when you look back.

These two phenomena appear paradoxical in folk-time-language ("how could the same period feel both short and long?") but are consistent in race: the in-the-moment experience tracks commit-rate (high commits per coordinate-time-unit → no awareness of coordinate time), and the retrospective experience tracks commit-accumulation (high total commits → long retrospective duration). Both are projections of "time = commits".

**Connection to four pre-existing theories of time.** This places race's substrate-time-from-commits claim at the intersection of four pre-existing programmes:

1. **Einstein relativistic time-dilation** (1915): substrate energy configures proper-time-rate (§5.2.5 above).
2. **Margolus-Levitin (1998)**: substrate energy configures computational clock-rate ceiling (§5.2.5 above).
3. **Rovelli thermal time** (1993, 2018): time emerges from thermodynamic coarse-graining of statistical states (§5.1 already cited).
4. **Flow-state psychology** (Csikszentmihalyi 1990; Nakamura & Csikszentmihalyi 2002): high-engagement modulates subjective time-experience (this section).

If race's "time = commits" claim is correct, these four programmes are not four separate phenomena. They are four substrate-domains exhibiting one structural property: substrate physics modulates substrate time. This is not a new physics claim — every individual programme is established. What is new is making explicit that the four are projections of a common deductive structure (R1+R2+R3 + commit-as-time-unit). The unification claim is consistent with the broader §1.5 substrate-universal structure.



### 5.3 Lorentz-covariance of race-structure vs. frame-dependence of observables

The claim that race-structure is Lorentz-covariant requires precision: it is *not* the stronger claim that all friction-observables are Lorentz-invariant. We separate the structural and observable layers explicitly. Paper 1 §9.5 ("Open theoretical questions") already flagged the relativistic temporal aspect of multi-agent friction transactions; Paper 10 §5.3 formalizes what Paper 1 §9.5 left open.

**What is Lorentz-covariant:**

- The Schwinger-Keldysh formalism itself, when built on Lorentz-covariant fields (standard QFT result).
- The race-axioms A1–A5 as structural propositions (each axiom is satisfied in every frame with frame-appropriate parameter values).
- Transformation rules for CR, $\tau_c$, $\Gamma$ between frames (covariant transformation).

**What is frame-dependent:**

- The bipartite S/E partition (where the boundary is drawn depends on the observer).
- The thermal environment state (Tolman-Ehrenfest: a moving thermal bath has frame-specific temperature).
- The einselected pointer basis (defined via $H_{SE}$, hence frame-specific).
- Commit-timescale $\tau_c$ (an observable number, transforms under boosts).
- Specific numerical CR-values.

**Refined claim:** race-*structure* is Lorentz-covariant; specific friction-observable values are frame-dependent. Each substrate defines its own race-dynamics in its rest frame (where the substrate is at rest relative to its own commit-events). External observers see frame-transformed versions. A1–A5 hold in every frame with frame-appropriate parameter values.

**Analogy with thermodynamics.** Temperature and entropy are frame-dependent (Tolman's law), yet the laws of thermodynamics are Lorentz-covariant. Friction and race are parallel: observable values transform, structure is invariant.

The Schwinger-Keldysh formalism on the closed-time-path contour is manifestly Lorentz-covariant when built on relativistic fields (Landsman & van Weert 1987; Calzetta & Hu 2008). The generating functional

$$Z[J_+, J_-] = \int \mathcal{D}\phi_+ \mathcal{D}\phi_-\, e^{iS[\phi_+]/\hbar - iS[\phi_-]/\hbar + iS_{\text{IF}}[\phi_+, \phi_-]}$$

has action $S$ that is Lorentz-scalar for relativistic fields, and the contour $C = C_+ \cup C_-$ can be extended covariantly via lightcone coordinates. The influence functional $S_{\text{IF}}$ inherits Lorentz-covariance if the environment's coupling is Lorentz-covariant. Under a Lorentz transformation $\Lambda$, $\phi'(x') = \phi(\Lambda^{-1} x')$ and $S$ transforms as a scalar, giving $Z[\Lambda \cdot J] = Z[J]$: the generating functional is Lorentz-invariant.

Paper 10's specific race structure — bipartite system + environment, einselection, Markovian coupling, thermal initial state — introduces several frame-specific ingredients:

- **Bipartite S/E division** is observer-choice; different inertial observers may partition differently, particularly if S and E are spatially separated (relativity of simultaneity)
- **Thermal initial state** $\rho_E(0)$ is frame-dependent via the Tolman-Ehrenfest law (Tolman 1930): a thermal bath at rest in frame $F$ has different apparent temperature in frame $F'$; the proper temperature $T_{\text{proper}}$ is Lorentz-scalar only in the bath's rest frame
- **Einselection pointer basis** depends on $H_{SE}$, which is frame-specific (energy is the 0-component of 4-momentum, boost-dependent)
- **Commit-timescale** $\tau_c$ is an observable number transforming under boosts per time-dilation

Despite these frame-specific ingredients, the race *structure* (A1-A5 satisfied) holds in every inertial frame, because Lorentz-covariance preserves:

- Parallel candidates (A1) — covariant transformation of path-integration measure
- Interference and dissipation (A2) — covariant transformation of action and influence functional
- Finite-time constraint (A3) — boosted observer sees finite-time bound with $\tau_c$ transformed per dilation formula
- Pointer-basis commit (A4) — pointer basis transforms covariantly; Born probabilities Lorentz-invariant (Gleason's theorem applies frame-by-frame)
- Irreversibility (A5) — entropy changes are Lorentz-scalars

**race-axioms are Lorentz-invariant propositions; specific numerical values of $\Gamma$, $\tau_c$, CR, $k_B T$ are frame-dependent observables.** This structure parallels thermodynamics: the laws are Lorentz-covariant, but temperature and entropy have frame-dependent values (Tolman 1930; modern treatment in Israel-Stewart 1979 relativistic thermodynamics). Friction-theory is thermodynamics' close cousin at this level.

**Consequence for Paper 10's substrate-timescale claim:** Each substrate defines its race in its rest frame where its commit-events are localized. External observers see frame-transformed values but the underlying race-structure is preserved. Cross-substrate transactions between observers at different velocities or gravitational potentials would involve appropriate transformation of commit-rates, as envisaged in Paper 1 §9.5's "open theoretical questions."

**Scope limits:** Flat-spacetime Lorentz-covariance is what we establish here. General relativity extensions (curved spacetime, horizons, near-black-hole regimes) require Schwinger-Keldysh on curved background (Calzetta-Hu 2008; Schwinger 1951 effective action in curved spacetime) and are beyond Paper 10's scope.

**Gravitational time-dilation — noteworthy GR consequence:** Even at the flat-spacetime level, general relativity predicts that substrates in strong gravitational potential have locally slower clocks per external observer (Pound-Rebka experiment 1959; GPS clock corrections; observed in atomic clocks at different altitudes). In race-framework: a substrate's commit-rate, measured in external coordinate time, is redshifted by $(1 - 2GM/(rc^2))^{1/2}$ for gravitational potential at radius $r$ from mass $M$. The substrate's own proper-time commit-rate remains unchanged in its rest frame; external observers see slowed dynamics. Black holes are the extreme case — at the horizon, $\tau_c \to \infty$ per external observer while remaining finite per infalling observer. This is standard GR, not new claim. It extends the original §3-intuition (substrate friction is invariant in the substrate's own frame) naturally from flat to curved spacetime.

---

## 6. Distributional consequences as race-corollaries

### 6.0 Introduction and scope

Sections 5A–5E established that race-axioms A1–A5 are satisfied by the Schwinger-Keldysh formalism and recover four substrate-specific framework-instantiations as parameter-limits (Corollaries 1–4). A natural further question: what *distributional* signatures should population-level outcomes exhibit when generated by race-systems in different parameter-regimes?

This section derives five distribution-family regimes (Gauss, power-law, bimodal, exponential, log-normal) as race-corollaries from the formal apparatus already established. Each regime corresponds to a specific race-parameter configuration; each yields a testable Distributional Signature Prediction (DSP). The framework hypothesis is that outcome distributions are *signatures* of underlying race-regime — observable form-features (kurtosis, skewness, tail-exponent) diagnose substrate-dynamics. This is conceptually analogous to how thermodynamic phase-distinguishability (gas/liquid/solid) reveals underlying microstate-organization.

**Scope statement:** the formal derivations here are Paper 10's contribution. Empirical validation across substrates and full cross-substrate generalisation is the target of follow-up work (Paper 12 1/f-memory programme, in preparation). DSP-6 (adaptability-distribution as substrate-property) is substantively developed in Paper 1 §9.5 and Paper 11 §7; Paper 10's physics-scope does not derive it directly but cross-cites (see §6.7).

### 6.1 Gauss regime — Onsager-Machlup weak-noise limit (DSP-1, DSP-2)

**Derivation.** Corollary 2 (Section 5D) gives Onsager-Machlup path-probability $P[x(t)] \propto \exp(-S_{\text{OM}}/2D)$. In the weak-noise limit $D \to 0$ with finite drift, paths concentrate near the deterministic action-minimizing trajectory. By the Central Limit Theorem applied to small-amplitude fluctuations around the mean trajectory, outcomes distribute as approximately Gaussian:

$$P(x) \propto \exp\left(-\frac{(x - \langle x\rangle)^2}{2\sigma^2}\right)$$

with variance $\sigma^2 \propto D$ scaling with substrate-noise.

**Form-signature interpretation.** Higher kurtosis (sharper peak) corresponds to tighter race: stronger central attractor, lower-variance commit. Lower kurtosis (flatter peak) corresponds to looser race: weaker attractor, more competing optima.

**DSP-1 (RLHF-compression — decomposed into HRP-3.σ and HRP-3.K):** RLHF-trained models compress decision-distributions relative to base models. Per Paper 1's empirical decomposition (Tests 1/3b/3c/3d):

- **HRP-3.σ (sigma-compression)**: universal cross-paradigm; RLHF reduces σ_CR by a paradigm-conditional magnitude. **Empirical anchor:** Llama-3.1-405B base vs instruct on matched GPQA Diamond shows σ_CR compression 3.08× (1.11 vs 0.36, near null-floor 0.37); Pødenphant Lund 2026b §6.1b. SimpleQA shows 16% compression; GPQA shows 49% compression — magnitude varies by paradigm but direction is universal.
- **HRP-3.K (kurtosis-shift)**: paradigm-specific. Holds for free-form generation (SimpleQA), falsified for structured/MC paradigms (GPQA + v10c). Mean preservation is universal across paradigms (RLHF does not shift central tendency).
- **Mechanism**: "borrowed pre-calibrated weighting" (Pødenphant Lund 2026b research-note v2): RLHF acts as borrowed pre-calibrated weighting on the path-integral measure; effect on form depends on whether the paradigm exposes the underlying weight-structure (free-form) or saturates it (MC).

**DSP-2 (Expert-novice as HRP-3.S slope-flattening):** Within-domain experts should show systematic recognition-commit slope-flattening relative to novices (meta-coupling intact in experts → flat in flat-coupled). **Empirical anchor:** Paper 6 §5.7.3 recognition-commit slope-ratio 7× (base 1.73, instruct 0.25) provides substrate-level analog of expert-novice gradient (universal endpoint finding per HRP-3.S taxonomy). Classical expertise literature (Klein 1998, Chase-Simon 1973, Ericsson 2018) provides skill-acquisition-level reference. Direct expert-novice CR-distribution test pending in Paper 6's ongoing work.

**References:** Onsager-Machlup 1953; Freidlin-Wentzell 1984 (large-deviations); Kamenev 2011 ch. 4; Stein et al. 2023 RLHF variance-suppression literature.

### 6.2 Power-law regime — Freidlin-Wentzell + criticality (DSP-4)

**Derivation.** Freidlin-Wentzell large-deviation theory (Section 5D) describes tail-statistics of stochastic paths. Near a critical point (substrate near phase-transition where effective potential $U$ becomes flat), Onsager-Machlup action $S_{\text{OM}}$ becomes scale-invariant. The resulting path-probability decays as a power-law:

$$P(x) \propto |x|^{-\alpha}$$

with exponent $\alpha$ determined by the universality class of the transition. In Schwinger-Keldysh language, this corresponds to the dissipation kernel becoming non-analytic at criticality (zero-mass renormalization).

**Form-signature interpretation.** Heavy tails indicate strongly-coupled dynamics where individual events dominate. Race near criticality has commit-events at all scales (no characteristic timescale).

**DSP-4 (Market-regime detection):** Asset-returns distributions should be approximately Gaussian during normal-market regimes (equilibrium-race) and shift toward power-law/heavy-tail during bubble-crash regimes (criticality-race). **Empirical anchor:** Mandelbrot 1963 ("variation of certain speculative prices"), Sornette 2003 (log-periodic power-law in pre-crash), Cont 2001 (review of stylized facts). Paper 11 §4 develops this explicitly with S&P 500 data.

**Connection to Section 5C-5D non-Markovian finding (Paper 10 empirical):** Our Monte Carlo-validated 1% non-Markovian subpopulation (see supplementary materials) showing 1/f spectral exponent (α ≈ 0.7–0.95) is consistent with a sub-population at-or-near criticality. Single-substrate phase-transition signatures are empirically detected.

**References:** Mandelbrot 1963, Bak-Tang-Wiesenfeld 1987, Sornette 2003, Beggs-Plenz 2003 (neural avalanches), Stanley 1971 (universality in critical phenomena).

### 6.3 Bimodal regime — Hysteresis bistability (DSP-3)

**Derivation.** When the effective potential $U(\phi)$ derived in Sections 5D and 5C exhibits two minima separated by a barrier with finite escape-rate, the steady-state probability distribution is bimodal:

$$P(\phi) \propto e^{-U(\phi)/k_B T}$$

with peaks at the two minima. The relative weight of peaks depends on $U$-asymmetry; the inter-peak transitions are Kramers-rate-limited (Kramers 1940 escape problem applied to Onsager-Machlup). Hysteresis emerges naturally because finite barrier-crossing-time creates path-dependence.

**Form-signature interpretation.** Bimodality indicates dynamical bistability. Population observed at both attractors implies hysteresis-locked subpopulations rather than continuous variation.

**DSP-3 (Pathology-distinguishability):** Pathologies map to race-regime form-signatures, with sub-types per pathology-mechanism:

- **Bipolar disorder** → within-individual bimodality (manic/depressive attractors with hysteresis-locked transitions)
- **Addiction** → both within-individual (use/abstinence) and population-level bimodality
- **Schizophrenia** → not bimodal; continuous spectrum (different race-regime, not hysteresis-bistability)
- **ADHD** → high-variance low-kurtosis unimodal (loose race without bistability)
- **Mild cognitive decline** → right-skewed unimodal (continuous substrate-degradation)

Pathology-specific labels (DSP-3.bimodal, DSP-3.skewed, etc.) are Paper 8-territory where clinical context is closer; Paper 10 stays at generic DSP-3 level. **Empirical anchor:** Goodwin & Jamison (2007 revised, *Manic-Depressive Illness*) documents bipolar bimodality. RDoC framework (Insel 2014) supports dimensional rather than categorical pathology-modeling. Paper 8 §4.7c has clinical implementation.

**References:** Kramers 1940; Hänggi-Talkner-Borkovec 1990 (escape rates); Borsboom 2017 (network models in psychopathology).

### 6.4 Exponential regime — Markov waiting times (DSP-5 first form)

**Derivation.** Theorem assumption (ii) — Markovian environment (Section 3.1) — directly implies that waiting times between commit-events follow exponential distribution:

$$P(\tau_{\text{wait}}) = \Gamma e^{-\Gamma \tau_{\text{wait}}}$$

with rate $\Gamma$ from Joos-Zeh decoherence formula $\Gamma \sim (\Delta x)^2 \gamma m k_B T / \hbar^2$. This is a standard consequence of Poisson-process structure under Markov assumption.

**Form-signature interpretation.** Exponential waiting-time distribution indicates memoryless commit-dynamics. Deviations from exponential (e.g., gamma-distribution, Weibull) indicate commit-rate inhomogeneity or non-Markovian memory.

**Empirical anchor:** Paper 1 §4 documents radioactive-decay-like exponential statistics in some biological substrates (neuron inter-spike intervals; calcium-channel opening times). Our Paper 10 finding (R² 0.98–1.00 for exponential autocorrelation decay across 5 LLM substrates) is consistent with exponential waiting-time regime.

**References:** standard Markov-process theory (Doob 1953); Gardiner *Handbook of Stochastic Methods* (2009).

### 6.5 Log-normal regime — Multiplicative noise

**Derivation.** When the Langevin equation has multiplicative noise structure ($\partial_t \phi = F[\phi] + \phi \cdot \eta$ rather than additive $\eta$), the variable change $\psi = \log \phi$ converts to additive Onsager-Machlup; therefore $\log \phi$ is Gauss-distributed, hence $\phi$ is log-normal:

$$P(\phi) \propto \frac{1}{\phi}\exp\left(-\frac{(\log\phi - \mu)^2}{2\sigma^2}\right)$$

**Form-signature interpretation.** Log-normality indicates multiplicative substrate-dynamics where small fluctuations compound. Common in growth-processes and cascading systems.

**Empirical anchor:** Income distributions (Pareto-Levy 1925, Cont 2001), file-sizes (Mitzenmacher 2004), bacterial colony growth (Limpert-Stahel-Abbt 2001). Standard literature; framework adds substrate-mechanism explanation (multiplicative noise = substrate where commit-events compound rather than sum).

**References:** Limpert-Stahel-Abbt 2001 ("Log-normal distributions across the sciences"); Mitzenmacher 2004.

### 6.6 Substrate-cross-substrate consistency (DSP-5 second form)

**Claim.** Schwinger-Keldysh formalism is substrate-agnostic by construction (Sections 3, 5A–E). Therefore, substrates operating in the same race-parameter-regime should produce outcome-distributions of the same form-family after appropriate normalization, regardless of specific implementation.

**Specifically:** if LLM substrates, biological neural substrates, and *Physarum* protoplasm-flow substrates all operate in equilibrium-race-with-Markovian-environment (parameter-regime of §6.1), all three should show approximately Gaussian outcome-distributions. Form-deviation across same-regime substrates would indicate either substrate-specific parameter-shift or breakdown of theorem assumptions (e.g., non-Markovian environment in one substrate).

**Paper 10 internal validation.** Our 5 clean LLM datasets (qwen3-4b-base, Qwen3-235B-Instruct-2507, LiquidAI-LFM2-24B, plus 2 unknown) all show R² 0.98–1.00 for exponential autocorrelation decay — consistent with same-regime cross-substrate behavior at LLM-substrate-level. Cross-substrate test requires data from non-LLM substrates (BEC decoherence, neural-spike rates) and is flagged as future work.

**References:** Stanley 2000 (scaling laws in physiology); West 2017 (*Scale*); Bak-Tang-Wiesenfeld 1987 (universality across substrates); Beggs-Plenz 2003 (neural avalanches matching SOC exponents).

### 6.7 Scope-note: DSP-6 (cross-paper integration)

**DSP-6 (adaptability as Gauss-distributed substrate-property)** is substantively developed in Paper 1 §9.5 (framework-claim regarding adaptability as heritable substrate-property with Gauss-distribution and environmental-volatility-mean-tracking) and Paper 11 §7 (P11-7 instantiation on financial markets with Lo's *Adaptive Markets Hypothesis* anchor, falsification criteria, and operationalization). Paper 10's physics-scope does not derive it directly; we cross-cite for completeness.

- **In-scope (this section):** distribution-shape derivations from race-axioms + Schwinger-Keldysh formalism (DSP-1 through DSP-5)
- **Cross-paper-integrated (deferred to substrate-appropriate scope):** adaptability-distribution and its evolutionary dynamics — see Paper 1 §9.5 and Paper 11 §7

**Empirical anchors for DSP-6** (consolidated cross-paper references, not derived in Paper 10): McCrae-Costa 1987 (Big Five Gauss); Plomin et al. 2016 (cognitive flexibility heritability); Sih et al. 2004 (animal personalities); Lo 2017 (*Adaptive Markets Hypothesis*).

### 6.8 Summary table

| DSP | Regime | race-mechanism | Section 5 derivation | Empirical anchor |
|---|---|---|---|---|
| DSP-1 | Gauss (kurtosis-shift) | RLHF-compression | 5D weak-noise limit | Llama-405B 3.08× σ_CR (Pødenphant Lund 2026b §6.1b) |
| DSP-2 | Gauss (kurtosis-gradient) | Expert-novice coupling | 5D; structural analog | Paper 6 §5.7.3 slope 7× ratio |
| DSP-3 | Bimodal | Hysteresis-bistability | 5D effective potential, Kramers | Bipolar (Goodwin-Jamison 2007) |
| DSP-4 | Power-law / heavy-tail | Criticality | 5D Freidlin-Wentzell + flat $U$ | Mandelbrot 1963; Sornette 2003 |
| DSP-5 | Cross-substrate consistency | SK substrate-agnosticism | 3.2 main theorem | Paper 10 R² 0.98-1.00 (5 LLMs) |
| (Exponential) | Markov waiting | Theorem assumption (ii) | 6.4 standard Markov | Paper 1 §4 + Paper 10 autocorr decay |
| (Log-normal) | Multiplicative noise | Onsager-Machlup with $\phi\eta$ | 6.5 standard | Limpert et al. 2001 |
| DSP-6 | (cross-paper) | Adaptability heritability | (cross-cited; not derived here) | Paper 1 §9.5 + Paper 11 §7 |

### 6.9 Implications for Paper 10's empirical program (§9.3)

§6 yields concrete Paper-10-testable predictions that can be added to §9.3's empirical program:

1. ~~DSP-1 kurtosis-test on existing data~~ — **already executed by Paper 1**. Tests 1/3b/3c/3d on Llama-405B SimpleQA + GPQA decomposed DSP-1 into HRP-3.σ (universal sigma-compression) + HRP-3.K (paradigm-specific kurtosis-shift). Mean preservation is universal. Mechanism: "borrowed pre-calibrated weighting". Silicon-substrate validation data and figures are provided in the supplementary materials.
2. **DSP-3 bimodality-test on existing per-sequence CR data**: examine whether sequences classified as 1% non-Markovian show bimodal CR-distribution (consistent with hysteresis-bistability hypothesis). Paper 8 §4.7c has clinical mapping for cross-validation.
3. **DSP-5 form-similarity test**: compute and compare CR-distribution-form (kurtosis, skewness) across our 5 clean LLM substrates. Predict: same form-family after normalization (Gauss-approximation expected for Markovian substrates). Paper 6 §5.6 has endpoint-cross-substrate replication for cross-validation.

Tests 2 and 3 are tractable on the existing per-sequence CR data without further data collection. Test 1 is closed via Paper 1's silicon-substrate validation.

---

## 7. Three hard problems — engaged honestly

### 7.1 Interference and Bell violations

Classical race has no amplitude interference. Bell inequalities are routinely violated in experiment. If race is fundamental, how can it accommodate these quintessentially quantum features?

The answer is in A2 (competitive interaction) interpreted at Schwinger-Keldysh level. Path-integral weights $e^{iS/\hbar}$ are complex; amplitudes interfere constructively and destructively. This is not ad hoc — it is a feature of the generating functional when $\hbar$ is finite. In the $\hbar \to 0$ classical limit (Corollary 2), interference vanishes; in the coherent $D \to 0$ limit (Corollary 1), it persists and dominates. The complex-valued weighting of A2 is the mathematical seat of interference; race naturally accommodates it in the quantum regime.

Bell violations are signatures of non-local correlations in the evaluation-phase. In race-language: pre-commit superposition extends across spatial separations; commit (occurring via environmental coupling at one location) correlates with remote degrees of freedom through the entangled composite-state structure. Interference and Bell-violations are evaluation-phase phenomena; classicality emerges post-commit.

We do not claim to solve the measurement problem or resolve Bell-locality debates. Race inherits these problems. But race relocates them: instead of "why does superposition collapse?" we ask "why does race resolve?" The Schwinger-Keldysh formalism shows the two questions are structurally identical. A potential advantage: Race-framing is less tied to specific interpretations and may be more amenable to unified treatment across interpretive camps.

### 7.2 Linearity-nonlinearity transition

Unitary Schrödinger evolution is linear; race-commit is nonlinear. The transition from linear to nonlinear is the measurement problem in its sharpest form.

Race does not dissolve this problem. What we provide is a structural account of where the nonlinearity enters: not in Schrödinger evolution of the total system, but in emergent dynamics of the reduced system after environmental degrees of freedom are traced out. Reduced density matrix evolution is described by Lindblad master equation (Markovian limit) or integro-differential equations (non-Markovian). Both are nonlinear in the reduced state while being unitary at the total-system level.

This is standard decoherence theory. Our contribution is to observe that the structural features of this transition — parallelism, competition, timescale, selection, irreversibility — constitute the race-axioms A1-A5. The measurement problem becomes the race-resolution problem; same problem, different coordinate system. Honest acknowledgment: this does not solve the measurement problem; it relocates it. Whether the relocation is productive is an empirical question about whether race-framing enables new insights that Schrödinger-framing does not.

### 7.3 Unitary reversibility vs race-dissipation

Total system-environment evolution is unitary; reduced system dynamics is dissipative. This is textbook decoherence theory. Race adopts the standard resolution: the irreversibility of A5 is effective (observer-tractable), not fundamental (total-system-unitary). Entropy increases in the environmental degrees of freedom the observer does not track; the reduced state becomes mixed.

Poincaré recurrence ensures total-system evolution, in principle, returns arbitrarily close to initial state after times exceeding $e^N$ where $N$ is degrees of freedom. For realistic environments ($N \sim 10^{23}$), recurrence times vastly exceed the age of the universe. Effective irreversibility is robust.

Framework does not add novelty here. This section exists to document that race does not conflict with unitarity of fundamental physics: irreversibility is emergent from coarse-graining, not posited at fundamental level.

---

## 8. Race across QM-interpretations

Race is interpretation-agnostic. Each major interpretation of quantum mechanics has a natural race-reading; no interpretation is required, but each is compatible. This section traces the compatibility.

**Why interpretation-agnosticism is structurally required (cross-reference §1.5).** The §1.5 deductive argument establishes that the inverted-U-on-evaluation-rate signature follows from R1+R2+R3 alone, without specifying any particular dynamics or ontology of the candidate-routes pre-commit. This deductive structure forces interpretation-agnosticism: the empirical content of the framework — the inverted-U signature across seven substrate scales — is invariant across interpretations because the structural premises (R1+R2+R3) are. A reviewer's preferred metaphysics for what "candidate routes" *are* (probability-amplitudes, real branches, pilot-wave-weighted alternatives, Bayesian beliefs, configuration-space-real entities) does not affect the prediction. This is a virtue, not a limitation: a framework whose empirical content survives metaphysical disagreement is more robust than one that requires committing to a specific interpretation.

**Wallace's biocognition rate-distortion programme — concurrent prior art on biology-and-cognition scope.** Before turning to QM-interpretations, we acknowledge concurrent independent work on the inverted-U structural claim within biological cognition. Three Wallace contributions are particularly relevant:

1. **Wallace, Leonova & Gochhait (2022, *Entropy* 24(8):1070)** establishes information-theoretic instability conditions for biocognitive systems via the Data Rate Theorem applied to nonergodic biocognition. This 2022 paper provides the rate-distortion formal apparatus that Wallace's later work applies directly to Yerkes-Dodson dynamics. The 2022 paper does not itself derive Yerkes-Dodson; it sets the foundational machinery.

2. **Wallace (2025a, *Symmetry* 17(2):235)** "Sensory or Intelligence Data Compression Can Drive the Yerkes-Dodson Effect" provides the direct derivation of the Yerkes-Dodson inverted-U from rate-distortion / data-compression principles. This is the most rigorous published derivation of the Y-D-from-information-theory direction in biological cognition, and the closest precedent for our case #7 (behavioural / Yerkes-Dodson) within biology-and-cognition scope.

3. **Wallace (2025b, *J. Defense Modeling and Simulation*; preprint TechRxiv 2023)** "Hallucination, Panic, and Exhaustion in Embodied Cognition" provides an explicit friction-and-Yerkes-Dodson treatment with Clausewitzian "fog/friction" framing, including failure modes at the tails (hallucination, panic, exhaustion) — the closest direct precedent for the integration of friction-vocabulary with inverted-U-on-cognitive-performance within Wallace's corpus.

Wallace's programme is rigorous and we acknowledge his 2022–2025 corpus as concurrent independent work on biology-and-cognition scope. The relationship is concurrent rather than antecedent: the Wallace Y-D-from-rate-distortion derivation (2025a) appeared during our drafting period, and the two derivations use independent formal apparatus (information-theoretic vs. substrate-physics premises). Our contribution is complementary, not derivative:

(a) **§1.5's R1+R2+R3 deductive argument** does not require rate-distortion machinery. Rate-distortion is one specific way of operationalising "bounded resources under information-theoretic constraint" but it is not the only way, and it has problematic application to substrates where pre-commit information-theoretic functionals are not well-defined (e.g., quantum coherent dynamics, where the system has no committed information state until decoherence). The R1+R2+R3 argument is purely structural and does not commit to any specific operationalisation.

(b) **All-the-way-up extension** to quantum decoherence-window (case #1), Ohm's law / Drude electron transport (case #2), chemistry / biochemistry molecular kinetics (case #3), stochastic resonance in statistical physics (case #4), and Margolus-Levitin-bounded thermodynamics (case #5) goes beyond Wallace's biology-and-cognition scope. Wallace addresses cases #6 and #7 (encoding-friction in cognition + Yerkes-Dodson in behaviour); our framework addresses all seven.

(c) **The Schwinger-Keldysh derivation (§3)** provides the QM-substrate physics that grounds case #1. Wallace does not address quantum substrates.

The relationship between the two programmes is therefore: Wallace's rigorous biology-and-cognition derivation provides one local instance of the universal pattern; FT's R1+R2+R3 deduction shows why the pattern must hold across substrates; the Schwinger-Keldysh derivation provides the QM instance. We cite Wallace (2022, 2025a, 2025b) as primary concurrent prior art on the Y-D-from-information-theory direction within biology-cognition scope. The substrate-universal extension and the deductive structural argument are our contribution.

### 8.1 Copenhagen

In Copenhagen interpretation, measurement causes collapse; prior to measurement, the system is in superposition. Race maps directly: pre-commit = prior to measurement; commit = collapse trigger (environmental coupling); post-commit = classical outcome. The advantage of race-framing is that "measurement" is not mysteriously distinguished from ordinary physical interaction. Any system-environment coupling with einselection produces commit; apparatus is not special. This is Copenhagen extended to all observer-independent system-environment interactions.

### 8.2 Many-Worlds (Everett)

In Everett, there is no collapse; the universal wavefunction evolves unitarily, and "commit" is observer-branch relative. Race maps: A1-A3 are universal (apply to universal wavefunction); A4 is observer-relative (each branch has its own committed outcomes); A5 is effective (branches do not interact post-decoherence). Many-Worlds is race-compatible without modification. The Born-rule derivation via envariance (Section 5A of derivation sketch) is arguably more natural in Many-Worlds, where Zurek's original argument was developed.

### 8.3 Bohm pilot wave

In Bohmian mechanics, particles have determinate trajectories guided by quantum potential. The wave function is evaluation-phase; particle position is commit. Race maps: A1 = quantum potential over configuration space; A2 = wave function interference guides particles; A4 = observed particle trajectory. Bohmian mechanics is race-compatible with evaluation-phase being guidance wave and commit-phase being observed position. The "hidden variable" is particle position; race takes no stance on whether hidden variables exist.

### 8.4 Relational QM (Rovelli)

In relational quantum mechanics, properties are relative to observers. There is no observer-independent "state of the system"; only relations between system and observer. Race maps directly: commit is observer-specific; different observers see different commits; correspondence between observers' commits is mediated by shared environment. Relational QM is the most natural QM-interpretation partner for race: both frameworks are observer-relative at their core, and Rovelli's relational thermodynamic-time programme (§5.1) is already integrated as Paper 10's emergent-time foundation.

### 8.5 QBism

In QBism, quantum states are Bayesian beliefs of agents; measurement is belief-update. Race maps: commit is belief-update; Born-rule is belief-update rule. QBism's pragmatist turn aligns with race's emphasis on commit as operational (observer-relative) rather than ontological (observer-independent).

**Synthesis:** race is interpretation-agnostic. Each interpretation provides a different ontology for what race-dynamics represents, but the mathematical structure of A1-A5 and the Schwinger-Keldysh derivation is identical across interpretations. This is a virtue: Race can serve as common ground for interpretive debates without taking sides. A framework about *dynamics* does not require a metaphysical commitment about what the dynamics describes.

---

## 9. Implications

### 9.1 AGI discourse

The phrase "AI will decide" is pervasive in public and academic discussion of artificial intelligence. We argue it is a category error.

An LLM generating tokens is not "deciding" what to say; it is resolving competing routes under finite-computation constraint. The commit at each token step is race-A4, not agential decision. This is not a claim that LLMs are "not conscious" (that is Paper 7 scope); it is a claim that the vocabulary of decision is theoretically unnecessary for explaining what they do. The substrate-specific race-dynamics suffice.

The implications are practical. Debates about AI "wanting" things, AI "having goals," AI "making choices" rest implicitly on decision-as-primitive. If decision is dissolved into competing-processes-under-constraint, these debates dissolve with it. An LLM optimizes under training objectives; a chess engine optimizes under search-tree heuristics; a feedback-control system optimizes under closed-loop dynamics. All are race-dynamics at different substrate-scales; none are "deciding" in a sense that adds to the physics.

This does not eliminate ethical questions about AI. Ethical considerations apply to systems implementing race-dynamics with particular scope, capability, and impact. But the ethical work is done by scope/capability/impact, not by positing agential decision-making as ontological primitive. Clarifying this is practical gain from the framework.

### 9.2 Emergent time and cosmology

If time emerges from commit-sequences (§5), what preceded the first commit? In the early universe, before structure formation, what race-dynamics existed?

This is speculative (flagged in §9 open-questions), but the framework suggests an outline. The inflationary epoch provided substrate (Hubble-volume) that could decohere; decoherence products (classical fluctuations that seeded CMB anisotropy) constituted early committed-structure from which subsequent hierarchy emerged. Before inflation — if there was a "before" — the universe is pre-commit and therefore operationally pre-time in the framework-sense. "Before inflation" is less a temporal statement than a coarse-graining-less condition.

This is Rovelli-adjacent. We do not claim to derive cosmology from race; we note that race is consistent with emergent time and may contribute to cosmological time-origin debates. Smolin's cosmological natural selection (1997) is a related research programme in which universes reproduce via black-hole formation; race would read this as multiverse-scale commits selecting cosmological parameters.

### 9.3 Empirical program

Paper 10's theoretical contribution invites an empirical program. Seven testable predictions have been identified:

1. **LLM CR-autocorrelation.** CR temporal autocorrelation should decay exponentially on timescale $1/\Gamma_{\text{eff}}$ (derivation sketch 5B.5). Testable against existing Paper 1 data via re-analysis.

2. **LLM CR temperature-scaling.** CR magnitude should scale monotonically with softmax temperature $T$. Testable via controlled experiments varying $T$ while holding other parameters constant.

3. **Penrose-Diósi gravitational collapse.** If gravitational self-energy contributes to commit-rate, Bose-Marletto-Vedral (2017) and Bouwmeester experiments should detect gravitational-induced decoherence of massive superpositions. Independent test; framework does not *require* positive outcome (standard decoherence suffices for backbone), but positive outcome would support substrate-timescale extension.

4. **Attosecond metrology on quantum evaluation-phase.** If substrate-timescale extends to attosecond regime, pump-probe spectroscopy at attosecond resolution may begin resolving evaluation-phase dynamics before commit in certain atomic transitions. This is frontier experimental work, but framework provides target.

5. **Cross-substrate BEC decoherence.** Bose-Einstein condensates can be prepared at tuneable coupling strengths; race predicts specific scaling of decoherence rate with substrate-temperature following Margolus-Levitin bound.

6. **Mass-ordered particle-substrate τ_c (Higgs-connection test).** Elementary fermions with different Higgs Yukawa couplings have different rest masses and thus different energy configurations. Prediction: their race-clock ratios should follow mass-ordering via Margolus-Levitin + Joos-Zeh. Electron : muon : tau mass ratios (1 : 207 : 3477) predict inverse τ_c ordering. Testable with attosecond-scale spectroscopy on single-particle transitions as technology matures.

7. **Gravitational time-dilation on commit-rate.** Atomic clocks at different gravitational potentials run at verifiably different rates (GPS corrections; Chou et al. 2010 tabletop measurement). Prediction: any substrate-based race-process (a trapped ion commit-event, a neural spike, an LLM inference) should show the same gravitational redshift in its commit-rate per external observer. Testable at tabletop precision already (height-varying atomic clocks have 10⁻¹⁷ precision).

The program is not "empirical validation of theory-of-everything" but "empirical refinement of race-framework parameter-limits across accessible substrates."

---

## 10. Open questions appendix

The following questions were identified during Paper 10's development but fall outside the paper's scope. They are flagged for future work.

Open extensions identified during development:

- Non-Markovian race.
- Quantum gravity / Planck-scale race.
- Pre-Big-Bang and cosmological race.
- Anthropic selection as an observer-race loop.
- ER=EPR as evaluation-phase geometry.
- The black hole information paradox as maximal-density race.
- AdS/CFT as holographic evaluation/commit.

All are explicitly marked "open, not addressed in this paper".

---

## 11. Discussion

Paper 10 does not propose new physics. It presents existing mathematics unified under race as lens. The contribution is fourfold.

**Conceptual unification.** Disparate frameworks — Feynman path integral, Onsager-Machlup stochastic dynamics, Friston free energy principle, Paper 1's CR-signal — are shown to be parameter-limits of a single Schwinger-Keldysh derivation. The race-axioms A1-A5 are satisfied in all four regimes. This does not imply the frameworks are "really the same" in any deep metaphysical sense; it demonstrates they share a mathematical scaffold that renders them comparable and translatable.

**Empirical anchor.** LLM substrates provide directly measurable race-signals via Paper 1's CR metric. The empirical finding that CR correlates with error rate at $\rho = -0.423$ ($p < 0.0001$) is theoretically predicted by the CR-to-Keldysh mapping (Section 5B of derivation sketch). The framework has its first empirical anchor; testable predictions (§9.3) enable further validation.

**New research questions.** Attosecond probes of quantum evaluation-phase, cross-substrate friction tests, CR-autocorrelation temporal structure, gravitational-induced collapse experiments — each is an empirical program enabled by specific framework predictions. Productive theories generate testable questions; race does so across multiple substrate scales.

**Philosophical clarity.** "Decision" is deconstructed as convenient category without eliminating the functional concept. Systems still perform what we usefully call decisions; we simply show that this performance is substrate-dynamics, not agency. This dissolves certain AI-discourse debates (§8.1) while preserving the functional notions needed for practical theory and ethics.

**Limitations:** does not solve the measurement problem; does not address strong emergence debates; does not select among QM interpretations; does not rigorously handle non-Markovian regimes (extension work). The Markovian assumption is explicit in the theorem (§3.1 assumption ii) and non-Markovian extensions require separate derivation via Breuer-Petruccione formalism or Hierarchical Equations of Motion.

**H2 Hierarchical Recursion note.** Hierarchical race is substantively developed across the paper-series: Paper 1 §9.5 (Hierarchical Recursion Claim as H2-hypothesis) and §2.6 (MCA as formal mathematical foundation), Paper 6 §5.7.3 (empirical anchor via base→instruct slope-collapse 1.73 → 0.25), Paper 4 §6.81 (cross-substrate replication anchor), and Paper 11 §2 (collective-substrate hierarchical nested-race specification). Paper 10's contribution is a physics-scale instance of the recursive level-structure: the substrate-timescale ladder (§5.2) — photon → atomic → molecular → neural → cognitive → civilizational — can be read as recursive race on the previous level's outputs. Paper 10's formal apparatus (Schwinger-Keldysh) can in principle be extended to multi-scale race via cascade-coupled SK formulations (Calzetta-Hu 2008 ch. 12 on multi-scale effective actions); this extension is a research direction, not a claim.

**Empirical anchors for H2** (per the HRP-3 taxonomy v2):
- **HRP-3.S (slope-flattening, universal endpoint)**: Paper 6 §5.7.3 recognition-commit slope-data (base 1.73, instruct 0.25) documents meta-coupling distinct from substrate-coupling (Pødenphant Lund 2026e). Independent confirmation reproduces Paper 6's reported slopes.
- **HRP-3R (Recovery, two-data-set partial confirmation)**: Trajectory analysis (Pødenphant Lund 2026 unpublished) suggests task-specific FT can partially restore compressed coupling — a hypothesis-level finding consistent with the framework's claim that compression is distribution-level, not architecture-level. Paper 4 §5.7 provides a second supporting dataset.
- **HRP-3M (Matched-friction signature, empirically supported)**: Paper 4 §5.7 documents 16× σ-difference deep vs passive on v10c — a recursive race-coupling signature on the training-trajectory. Owned by Paper 4.
- **HRP-3.σ + HRP-3.K** (already cited in §6.1) document substrate-level compression cross-paradigm (universal) and form-shift paradigm-conditional (mechanism: "borrowed pre-calibrated weighting").

Together, HRP-3.σ/K/S/R/M form a cross-paper empirical anchor system for H2's recursive race-coupling claim. None require Paper 10's Schwinger-Keldysh apparatus directly; they are framework-consistent observations supporting H2 at substrate, meta-coupling, training-trajectory, and matched-friction levels respectively.

**Explicit scope reminder:** Paper 10 is an *exploration* of FT's physics-scope extension; Papers 1–6 remain valid within FT's established scope (biological, cognitive, computational) regardless of whether Paper 10's physics programme succeeds. Any scope-upgrade to physics-universal FT requires the backbone derivation to hold formally in peer review.

---

## References

Core physics:
- Feynman, R.P. (1948). Space-time approach to non-relativistic quantum mechanics. *Rev. Mod. Phys.*
- Feynman, R.P. & Vernon, F.L. (1963). The theory of a general quantum system interacting with a linear dissipative system. *Ann. Phys.*
- Schwinger, J. (1961). Brownian motion of a quantum oscillator. *J. Math. Phys.*
- Keldysh, L.V. (1964). Diagram technique for nonequilibrium processes. *Zh. Eksp. Teor. Fiz.*
- Martin, P.C., Siggia, E.D., Rose, H.A. (1973). Statistical dynamics of classical systems. *Phys. Rev. A*
- Caldeira, A.O. & Leggett, A.J. (1983). Path integral approach to quantum Brownian motion. *Physica A*

Decoherence and einselection:
- Zurek, W.H. (1981, 1982, 2003, 2005). Series of papers on einselection and envariance. *Phys. Rev. D*, *Rev. Mod. Phys.*
- Joos, E. & Zeh, H.D. (1985). Emergence of classical properties through interaction with the environment. *Z. Phys. B*
- Gell-Mann, M. & Hartle, J.B. (1993). Classical equations for quantum systems. *Phys. Rev. D*
- Griffiths, R.B. (1984). Consistent histories. *J. Stat. Phys.*

Quantum speed limits and thermodynamics:
- Margolus, N. & Levitin, L.B. (1998). The maximum speed of dynamical evolution. *Physica D*
- Levitin, L.B. & Toffoli, T. (2009). Fundamental limit on the rate of quantum dynamics. *Phys. Rev. Lett.*
- Landauer, R. (1961). Irreversibility and heat generation. *IBM J. Res. Dev.*
- Jarzynski, C. (1997). Nonequilibrium equality for free energy differences. *Phys. Rev. Lett.*
- Crooks, G.E. (1999). Entropy production fluctuation theorem. *Phys. Rev. E*

Time and emergence:
- Rovelli, C. (1993, 2018). Statistical mechanics of gravity and thermodynamical origin of time. *Class. Quantum Grav.*, *Found. Phys.*
- Barbour, J. (1999). *The End of Time*. Oxford University Press.
- Wheeler, J.A. & DeWitt, B.S. (1967). Superspace and the nature of quantum geometrodynamics.

Biology and cognition:
- Friston, K. (2010). The free-energy principle: a unified brain theory? *Nat. Rev. Neurosci.*
- Sengupta, B. & Friston, K. (2018). How Markovian is the brain? *PLOS Comp. Biol.*
- Parr, T., Pezzulo, G., Friston, K. (2022). *Active Inference*. MIT Press.

Foundations and philosophy:
- Dennett, D. (1991). *Consciousness Explained*. Little, Brown.
- Wegner, D. (2002). *The Illusion of Conscious Will*. MIT Press.
- Price, H. (1996). *Time's Arrow and Archimedes' Point*. Oxford.
- Deacon, T. (2011). *Incomplete Nature*. Norton.

Paper 1 ecosystem:
- Pødenphant Lund, T.P. (2026a). *Behavioural Friction Theory (BFT)*. Paper 0 / Zenodo (BFT v5-v3 formalization, human-specific instantiation).
- Pødenphant Lund, T.P. (2026b). *Friction Theory (FT): Substrate-universal framework for bounded probabilistic computation*. Paper 1 (canonical formulation, §8 FT ⊂ BFT nesting theorem).
- Pødenphant Lund, T.P. (2026c). Paper 2: capacity scaling in FT substrates.
- Pødenphant Lund, T.P. (2026d). Paper 3: CR signal as substrate-level race metric.
- Pødenphant Lund, T.P. (2026e). Paper 4: cross-substrate replications of classical learning phenomena.

Adjacent frameworks:
- Tarraga et al. (2026). Cognitive friction in LLM tool-agents: Triadic Cognitive Architecture and HJB optimal stopping. arXiv:2603.30031 (smaller scope: LLM tool-agents specifically; FT Paper 10 Corollary 4 subsumes as special case).
- Kahneman, D. (2011). *Thinking, Fast and Slow*. Farrar, Straus and Giroux.
- Sweller, J., et al. (2016). Cognitive load theory and element interactivity.
- Festinger, L. (1957). *A Theory of Cognitive Dissonance*. Stanford University Press.

---


---

## Companion documents

- **Derivation appendix** (`paper10_derivation_details.md`): formal derivations 5A–5E (envariance, CR–Keldysh, FEP, Onsager–Machlup, Noether) referenced from §3.3 and §4.
- **Bibliography** (`paper10_bibliography.md`): annotated reference list.
- **Empirical results** (supplementary materials): full analysis output, including protocol-validation and Monte Carlo validation.

---

## Reproducibility

The empirical analyses can be reproduced from the per-token logprob datasets and analysis scripts available at https://github.com/tplund/friction-theory-p10-race-architecture. All reported results are from runs with thinking-mode disabled (`/no_think` directive on the Qwen3 family; thinking-disabled variants for other families) — this ensures CR-tokens measure decision-friction on answer-content rather than mixed reasoning/answer streams.
