# Paper 10 — Derivation Sketch (Companion Document)

**Companion to**: *"Race all the way down, race all the way up: A substrate-universal race-architecture across quantum, classical, biological, and computational regimes"* (Paper 10 master). Working subtitle: "A Schwinger-Keldysh derivation with a universal inverted-U signature".

**Status:** First formalisation of race-axioms + main theorem. Mathematical sketch, not peer-review-grade rigorous. Details require further checking and elaboration in subsequent iteration.

**Cross-reference to master §1.5.** Paper 10 master §1.5 establishes the inverted-U signature deductively from R1+R2+R3 alone (substrate-free, requiring no Schwinger-Keldysh machinery). The deductive argument and seven-case empirical table cross-validate with this derivation: §1.5 establishes what any race-system must phenomenologically exhibit; the present derivation shows how the QM-substrate physically realises this via the Schwinger-Keldysh closed-time-path formalism. The two arguments are independent but mutually supporting.

---

## 1. Motivation

**FT/BFT context.** Friction Theory (FT, Pødenphant Lund 2026b) formalises bounded probabilistic computation systems satisfying the race-axioms. FT's established scope covers biological, cognitive, and computational substrates (Papers 1–6). This derivation investigates whether FT's mathematical structure scales to physics-scope (quantum, classical, thermodynamics). This is *exploratory*; if the derivation holds formally in peer review, FT's scope may be upgraded to physics-universal. Until then we do *not* claim that established FT covers quantum / classical / thermodynamic substrates.

Paper 10's core claim: Race is the framework's substrate-agnostic principle, mathematically instantiated via the Schwinger-Keldysh formalism. Classical and quantum race are parameter-limits of the same derivation, not separate phenomena.

The present file formalises the five race-axioms (A1–A5) and states a main theorem: any quantum bipartite system with einselection satisfies A1–A5 via the standard Schwinger-Keldysh derivation, with classical / biological / computational regimes as parameter-limits.

---

## 2. Formal race-axioms

A race-system consists of:
- **Configuration space** $\mathcal{C}$ (Hilbert space, classical phase space, or general measure space)
- **State $\rho$** (density operator or probability measure on $\mathcal{C}$)
- **Environment $E$** (bath of degrees of freedom)
- **Time parameter $t \in [0, T]$**

### A1 (Parallelism / Superposition)

The pre-commit state admits representation as a path-integral generating functional:

$$Z[J] = \int \mathcal{D}\phi\, e^{iS_{\text{eff}}[\phi]/\hbar_{\text{eff}}}\, \exp\left(i \int J\phi\, dt\right)$$

Observable expectations are computed as functional derivatives. The integration measure $\mathcal{D}\phi$ over path-histories formalises "parallel evaluation".

### A2 (Competitive Interaction)

Path histories carry weights $w[\phi] = e^{iS_{\text{eff}}[\phi]/\hbar_{\text{eff}}}$. The effective action includes an interaction kernel on the Schwinger-Keldysh closed-time-path contour:

$$S_{\text{eff}}[\phi_+, \phi_-] = S[\phi_+] - S[\phi_-] + S_{\text{diss}}[\phi_+, \phi_-]$$

The dissipation term $S_{\text{diss}}$ couples the branches and generates environment-induced competition.

### A3 (Finite-Time Constraint)

The commit-rate functional $\Gamma : (\text{States} \times \text{Environment}) \to [0, \infty)$ sets the commit-timescale $\tau_c = 1/\Gamma$. The Margolus-Levitin bound:

$$\tau_c \geq \frac{\pi \hbar}{2 E_{\text{avg}}}$$

For Schwinger-Keldysh: $\Gamma = \text{Im}(\Sigma^R)$ (imaginary part of the retarded self-energy).

### A4 (Commit / Selection)

In the large-time limit $t \gg \tau_c$:

$$\rho_S(t \gg \tau_c) = \sum_i p_i |i\rangle\langle i|$$

where:
- Pointer basis selected by $[|i\rangle\langle i|, H_{SE}] \approx 0$ (Zurek 1981, 1982)
- $p_i = |\langle i | \psi(0)\rangle|^2$ via Zurek envariance (2003, 2005)
- Off-diagonal decay: $\rho_{ij}(t) = \rho_{ij}(0)\, e^{-\Gamma_{ij} t}$

### A5 (Irreversibility)

Post-commit environment entanglement entropy:

$$S(\rho_E(t_{\text{commit}})) - S(\rho_E(0)) \geq k_B \ln 2 \cdot N_{\text{bits}}$$

(Landauer 1961). Poincaré recurrence $T_P \gg t_{\text{observation}}$ gives effective irreversibility.

---

## 3. Primary Theorem

**Theorem (Race-Schwinger-Keldysh Equivalence):**

Let $(S, H_S, H_E, H_{SE})$ be a bipartite quantum system. Assume:

- **(i) Einselection:** $\exists$ pointer basis $\{|i\rangle_S\}$ with $[|i\rangle\langle i|, H_{SE}] \approx 0$
- **(ii) Markovianity:** Environment has macroscopic degrees of freedom → effectively Markovian evolution
- **(iii) Thermal initial state:** $\rho(0) = \rho_S(0) \otimes \rho_E(0)$, with $\rho_E(0)$ in thermal equilibrium at temperature $T$

Then the reduced system dynamics, derived via the Schwinger-Keldysh generating functional

$$Z[J_+, J_-] = \int \mathcal{D}\phi_+ \mathcal{D}\phi_-\, e^{iS[\phi_+]/\hbar - iS[\phi_-]/\hbar + iS_{\text{IF}}[\phi_+, \phi_-]}$$

(where $S_{\text{IF}}$ is the Feynman-Vernon influence functional), satisfies **all race-axioms A1–A5**.

Specifically:
- **A1** via path-integration over the closed-time-path contour
- **A2** via amplitude interference + dissipation kernel
- **A3** via $\Gamma = \text{Im}(\Sigma^R)$; $\tau_c \sim \hbar/k_B T$ for thermal environment
- **A4** via pointer-basis diagonalisation + Zurek envariance
- **A5** via environment entanglement entropy growth

---

## 4. Corollaries — parameter-limits

### Corollary 1 (Quantum Regime)

For $D \to 0$ (weak noise, $\hbar$ finite), race reduces to the coherent Feynman path integral:

$$Z \to K(B, t_B; A, t_A) = \int \mathcal{D}x(t)\, e^{iS[x(t)]/\hbar}$$

with Born probabilities $P(A \to B) = |K|^2$ emerging from envariance in subsequent measurement.

### Corollary 2 (Classical Stochastic Regime)

For $\hbar \to 0$ (classical limit) with finite $D$, the Keldysh branches collapse via fluctuation-dissipation → MSR → Onsager-Machlup:

$$P[x(t)] \propto \exp\left(-\frac{1}{2D}\int dt\, \left(\dot{x} + \nabla U/\gamma\right)^2\right)$$

with Freidlin-Wentzell large-deviation commit to the most-probable path.

### Corollary 3 (Biological Regime)

For strongly dissipative environments with active internal degrees of freedom (Markov blanket), Onsager-Machlup + marginalisation → Friston variational free energy:

$$F[q] = \langle \log q(\phi) - \log p(\phi, o)\rangle_q$$

FEP minimisation = race commit in the biological substrate (Sengupta-Friston 2018).

### Corollary 4 (Computational Substrate / LLM)

For discrete-time computational substrates, Paper 1's CR-signal

$$\text{CR}(t) = |\{i : p_i(t) > \theta\}|$$

is the discrete-time analog of the Keldysh response function $G^R$. Empirical anchor for race-axiom A2 in computational substrates.

---

## 5. Proof Sketch

**Step 1.** Total system partition function on the Schwinger-Keldysh contour $C = C_+ \cup C_-$:

$$Z = \text{Tr}\left[T_C \exp\left(-i \int_C dt\, H\right) \rho(0)\right]$$

**Step 2.** Integrate out the environment (assumption (iii)). The result is an effective generating functional over the system fields:

$$Z_{\text{eff}}[J_+, J_-] = \int \mathcal{D}\phi_+ \mathcal{D}\phi_-\, \exp\{iS_S[\phi_+] - iS_S[\phi_-] + iS_{\text{IF}}[\phi_+, \phi_-]\}$$

(Feynman-Vernon 1963)

**Step 3.** For Markovian environment (assumption (ii)), $S_{\text{IF}}$ has local-in-time form with dissipative kernel $\eta$ and noise kernel $\nu$.

**Step 4.** Rotate to Keldysh basis: $\phi_{cl} = (\phi_+ + \phi_-)/2$, $\phi_q = \phi_+ - \phi_-$. Dissipation renders the $\phi_q$ propagator damped at rate $\Gamma$.

**Step 5.** For $t \gg \tau_c = 1/\Gamma$, $\phi_q$ is suppressed → semiclassical dynamics in $\phi_{cl}$. Establishes **A3, A4**.

**Step 6.** Pointer basis emerges as eigenstates of the dominant effective potential. Off-diagonal elements suppressed as $e^{-\Gamma t}$ (Zurek einselection). Establishes **A4**.

**Step 7.** Born rule via Zurek envariance argument + Gleason's theorem.

**Step 8.** Environment entanglement entropy $\Delta S_E \geq k_B \ln 2 \cdot N_{\text{bits}}$ via Landauer. Establishes **A5**.

QED (sketch).

---

## 5A. Envariance derivation for the Born rule (unpacking A4)

Race-axiom A4 states that the post-commit state has Born probabilities $p_i = |\langle i|\psi(0)\rangle|^2$. This section derives the Born rule from envariance (environment-assisted invariance, Zurek 2003, 2005), shifting it from "postulate" to "derived from race-bipartite-structure + einselection".

### 5A.1 Setup

Let the system-environment composite be in a pure state with Schmidt decomposition:

$$|\Psi_{SE}\rangle = \sum_k \alpha_k |s_k\rangle_S |e_k\rangle_E$$

with $\{|s_k\rangle\}$ and $\{|e_k\rangle\}$ orthonormal in $\mathcal{H}_S$ and $\mathcal{H}_E$, $\alpha_k \in \mathbb{C}$.

### 5A.2 Envariance definition

A transformation $U_S$ on the system is **envariant** if $\exists V_E$ on the environment such that:

$$(U_S \otimes V_E) |\Psi_{SE}\rangle = |\Psi_{SE}\rangle$$

The transformation can be "undone" by an environment-only operation.

### 5A.3 Phase-envariance lemma

For $U_S = \sum_k e^{i\phi_k} |s_k\rangle\langle s_k|$ (diagonal phase rotation in the Schmidt basis), the inverse is $V_E = \sum_k e^{-i\phi_k} |e_k\rangle\langle e_k|$:

$$(U_S \otimes V_E) |\Psi_{SE}\rangle = \sum_k e^{i\phi_k} e^{-i\phi_k} \alpha_k |s_k\rangle|e_k\rangle = |\Psi_{SE}\rangle \quad \checkmark$$

**Implication.** The reduced system state $\rho_S = \text{Tr}_E |\Psi_{SE}\rangle\langle\Psi_{SE}|$ cannot depend on the phases $\{\phi_k\}$ (since they can be "erased" by the environment without touching the system). Algebraic consistency forces decoherence:

$$\rho_S = \sum_k |\alpha_k|^2 |s_k\rangle\langle s_k|$$

Off-diagonal elements must vanish. This yields A4's pointer-basis diagonalisation.

### 5A.4 Swap-envariance lemma

For equal-amplitude Schmidt components $|\alpha_i| = |\alpha_j|$, the system swap $U_S: |s_i\rangle \leftrightarrow |s_j\rangle$ (with appropriate phase) is envariant if the environment swap $V_E: |e_i\rangle \leftrightarrow |e_j\rangle$ undoes it.

**Implication.** $p_i = p_j$ whenever $|\alpha_i|^2 = |\alpha_j|^2$, by pure symmetry.

### 5A.5 Fine-graining to rational amplitudes

For $|\alpha_k|^2 = m_k/M$ rational, introduce $M$ virtual environmental ancillas: replace each Schmidt component with $m_k$ equal-amplitude sub-components. The composite state becomes:

$$|\Psi_{SE}\rangle = \frac{1}{\sqrt{M}} \sum_k \sum_{j=1}^{m_k} |s_k\rangle |e_{k,j}\rangle$$

with $M$ total equal-amplitude Schmidt components. Per 5A.4 each has probability $1/M$. The probability of $s_k$ is $m_k/M = |\alpha_k|^2$.

### 5A.6 Continuity extension

Rational amplitudes are dense; the Born rule $p_k = |\alpha_k|^2$ extends to all real $|\alpha_k|^2$ by continuity of the probability measure. Gleason's theorem (1957) is invoked for $\mathcal{H}_S$ with $\dim \geq 3$ to ensure unique probability assignment.

### 5A.7 Result

$$\boxed{p_i = |\langle i|\psi(0)\rangle|^2 \quad \text{(Born rule, derived from envariance)}}$$

**Status.** The A4 Born rule is now *derived*, not *postulated*. The race-bipartite structure + einselection + envariance uniquely fix the probability measure.

### 5A.8 Known critiques and alternative derivations

- **Schlosshauer-Fine (2005):** critique of circularity in the fine-graining step (5A.5). Argues that ancilla introduction presumes the probability structure being derived.
- **Zurek (2005, 2018) responses:** defends envariance by arguing that the environment-many-degrees-of-freedom assumption is physical, not circular.
- **Deutsch-Wallace decision-theoretic derivation (1999, 2012):** alternative route. Rational agent + expected utility maximisation $\Rightarrow$ Born rule. Independent derivation; same conclusion.
- **Wallace (2012) *The Emergent Multiverse*:** most rigorous Everett-compatible Born derivation via decision theory.

**Strategy.** Cite both envariance and Deutsch-Wallace; convergence to the same Born rule from independent derivations gives robustness against single-derivation critique.

### 5A.9 Explicit response to the Schlosshauer-Fine (2005) critique

Schlosshauer-Fine (2005) argue that the envariance argument (5A.5) is circular: the fine-graining step introduces $M$ ancilla states to construct an equal-amplitude Schmidt decomposition, and this construction implicitly presumes a probability measure over ancillas — which is precisely what is to be derived.

**Response (Zurek 2005).** Ancilla states are Hilbert-space vectors, not probability distributions. They do not introduce new probabilities but fine-grain the existing composite-state structure. The only "probability" invoked is via the swap-envariance symmetry argument (5A.4), which is purely structural — equal-amplitude states $|s_i\rangle, |s_j\rangle$ can be swapped without changing the composite state, so their probability assignment must be equal (by symmetry alone, no prior probability postulate).

**Status.** Zurek's defence is defensible but actively disputed. Paper 10's robustness rests on a double derivation: *even if* Schlosshauer-Fine's critique holds, the Deutsch-Wallace (1999, 2012) decision-theoretic derivation yields the Born rule from a purely structural rationality argument without fine-graining. Convergence of two independent derivations to the same Born rule is stronger than any single derivation.

**The paper cites both explicitly** as complementary derivations:
- Zurek envariance: directly from bipartite state structure
- Deutsch-Wallace: from rational-agent decision theory

If one falls, the other stands. A4 is thereby robust against single-derivation critique.

---

## 5B. CR-to-Keldysh mapping (unpacking Corollary 4)

Corollary 4 claims that Paper 1's CR-signal (Competing Routes metric) from the LLM substrate is the discrete-time analog of the Keldysh response function. This section develops the mapping formally and states testable predictions against existing Paper 1 data.

### 5B.1 CR-signal definition (from Paper 1)

For LLM token-generation at step $t$ with vocabulary $W$:
- Logit vector $l(t) \in \mathbb{R}^{|W|}$
- Softmax distribution at temperature $T$: $p_w(t) = \exp(l_w(t)/T)/Z(t)$
- **CR signal:** $\text{CR}(t) = |\{w : p_w(t) > \theta\}|$ for threshold $\theta$

CR measures the number of tokens with significant mass in the pre-commit distribution.

### 5B.2 Keldysh response function (continuum)

In Schwinger-Keldysh, after rotation to classical/quantum basis:
- $\phi_c = (\phi_+ + \phi_-)/2$
- $\phi_q = \phi_+ - \phi_-$

Response functions:
- Retarded: $G^R(t, t') = -i\theta(t-t')\langle[\phi(t), \phi(t')]\rangle$
- Keldysh: $G^K(t, t') = -i\langle\{\phi(t), \phi(t')\}\rangle$ (population/distribution encoding)

The equal-time Keldysh component $G^K(t,t)$ measures the distribution width at time $t$.

### 5B.3 Formal mapping (claim)

CR, as an equal-time distribution-width estimator, maps to a discretised Keldysh observable:

$$\text{CR}(t) \approx \mathcal{F}_\theta\left[G^K_{LLM}(t,t)\right]$$

where $\mathcal{F}_\theta$ is a threshold functional. For Gaussian approximation: if $p_w(t)$ is approximately Gaussian about its mode with variance $\sigma^2(t) \propto G^K(t,t)$, then:

$$\text{CR}(t) \approx \sigma(t) \cdot \sqrt{\ln(1/\theta)}$$

CR scales as $\sigma(t) \propto \sqrt{G^K(t,t)}$.

### 5B.4 Decoherence-rate mapping

A3 states the commit-timescale $\tau_c = 1/\Gamma$. For the LLM substrate:
- Effective decoherence rate $\Gamma_{\text{eff}} \propto 1/T$ (softmax temperature)
- Margolus-Levitin: $\tau_c \geq \pi\hbar_{\text{eff}}/(2E_{\text{eff}})$
- $k_B T_{\text{eff}}$ sets the effective thermal energy scale

Empirical prediction:

$$\text{CR}(t) \propto \exp(-\Gamma_{\text{eff}} \cdot t_{\text{internal}})$$

### 5B.5 Testable predictions against Paper 1 data

If the mapping holds:

1. **Autocorrelation decay.** $C_{\text{CR}}(\tau) = \langle\text{CR}(t)\text{CR}(t+\tau)\rangle_t$ should decay exponentially on timescale $1/\Gamma_{\text{eff}}$.
2. **Temperature scaling.** CR magnitude is a *non-monotonic* function of softmax $T$ with peak at intermediate $T$. At low $T$: softmax concentrates mass at argmax, few tokens above threshold → low CR. At intermediate $T$: distribution broadens, more tokens above threshold → high CR (peak). At high $T$: distribution approaches uniform $1/V$; if $1/V < \theta$ no tokens can be above threshold → low CR. Peak position depends on vocabulary size $V$ and threshold $\theta$. The original simplified "monotonic increase" prediction was empirically falsified in temperature-sweep datasets; the non-monotonic peaked prediction is empirically confirmed (see supplementary materials).
3. **Context-length dependence.** Longer context modifies $\Gamma_{\text{eff}}$; CR profiles reflect this.
4. **Correctness correlation.** Paper 1's empirical finding (CR ~ $-0.423$ correlation with errors, $p < 0.0001$) is predicted by the mapping: high CR = large uncertainty = higher error probability. This is already observed empirically; the mapping provides theoretical explanation.

### 5B.6 Discrete-time artifacts

LLM token-generation is discrete; the continuum Keldysh formalism is continuous. Known limitations:
- CR is integer-valued, not real; quantisation noise on $\mathcal{F}_\theta$
- Token-step time is the forward-pass duration, not Planck-scale
- Attention mechanism introduces non-Markovian memory (context-dependence)

Extension to non-Markovian Keldysh formalism is research-level work (see Section 6 gap #2).

### 5B.7 Result and empirical status

The Paper 1 CR-signal is a discrete-time Keldysh observable on the LLM substrate. Existing Paper 1 empirical data (CR-error correlation $-0.423$) is consistent with the mapping and receives theoretical explanation.

**Empirical validation status:**

- **Prediction #1 (autocorrelation exponential decay): strongly confirmed.** Analysis of 6 Paper 1 datasets (~3200 sequences across 5 model architectures, including Qwen3.5 9B, Qwen3 235B, Llama 3.1 base, Liquid LFM2, mixed T-sweep) shows $R^2 \in [0.901, 0.997]$ for exponential fit of $C_{\text{CR}}(\tau)$. Cross-substrate $\tau_c$ varies 0.10–0.68 tokens, instantiating substrate-timescale variation at the computational scale.

- **Prediction #2 (temperature scaling): refined and confirmed.** Original simplified prediction ("monotonic increase") is *incorrect* for threshold-based CR. Correct prediction: CR(T) is *non-monotonic with a peak* (determined by $V$ and $\theta$). Empirically observed peak at $T \approx 0.45$–$0.55$ or $T < 0.30$ in two datasets.

Full analysis with limitations is provided in supplementary materials.

**Overall status.** Corollary 4 is now empirically validated for the LLM substrate. Paper 10 has a direct empirical anchor in an accessible substrate, not depending on attosecond metrology or hard-to-access physical substrates.

---

## 5C. FEP derivation (unpacking Corollary 3)

Corollary 3 claims that biological race = Friston variational free energy minimisation. This section develops the derivation formally via Schwinger-Keldysh → MSR → marginalisation over the Markov blanket.

### 5C.1 Free energy principle recap

Friston (2010) formalises biological inference as minimisation of variational free energy:

$$F[q] = \mathbb{E}_{q(\phi)}[\log q(\phi) - \log p(\phi, o)]$$

where $q(\phi)$ is the variational approximation to the true posterior $p(\phi|o)$ over internal states $\phi$, and $p(\phi, o)$ is the generative model over internal states and observations $o$.

This decomposes as:

$$F[q] = \underbrace{D_{KL}[q(\phi) \| p(\phi)]}_{\text{complexity}} - \underbrace{\mathbb{E}_q[\log p(o|\phi)]}_{\text{accuracy}}$$

Minimisation of $F$ is the biological agent's commit mechanism: select $q^*$ that balances complexity and accuracy.

### 5C.2 Markov blanket structure

Friston (2013) specifies biological agents as systems with a *Markov blanket* — a conditional-independence structure separating internal states $\phi$ from external states $\eta$ via sensory states $s$ and active states $a$:

$$p(\phi, s, a, \eta) = p(\phi | s, a) \cdot p(s | \eta) \cdot p(a | \phi) \cdot p(\eta)$$

Blanket partition: $(\phi)$ agent-internal, $(s, a)$ blanket, $(\eta)$ environment.

This structure has a direct QFT analog: Markov blanket = system-environment interface with explicit separation of degrees of freedom.

### 5C.3 Derivation: Schwinger-Keldysh → FEP

**Step 1.** Start with the total Schwinger-Keldysh generating functional for the bipartite agent-environment system:

$$Z[J_+, J_-] = \int \mathcal{D}\phi_+ \mathcal{D}\phi_- \mathcal{D}\eta_+ \mathcal{D}\eta_-\, e^{iS_{\text{total}}[\phi, \eta]/\hbar}$$

**Step 2.** Classical thermal limit ($\hbar \to 0$, finite $T$): the Keldysh branches collapse via fluctuation-dissipation $\to$ Martin-Siggia-Rose generating functional (biological substrates are effectively classical on cognitive timescales, per Corollary 2 derivation).

$$Z_{\text{MSR}}[J] = \int \mathcal{D}\phi \mathcal{D}\eta \, e^{-S_{\text{MSR}}[\phi, \eta]/2D}$$

**Step 3.** Impose the Markov blanket structure: decompose $S_{\text{MSR}}$ into blanket-conformant terms:

$$S_{\text{MSR}}[\phi, \eta] = S_S[\phi, a] + S_B[s, a, \phi, \eta] + S_E[\eta, s]$$

where the blanket coupling $S_B$ only couples $(\phi, a)$ to $(s, \eta)$ through blanket states.

**Step 4.** Marginalise over external states $\eta$ conditional on observations $o = s$:

$$Z_{\text{eff}}[J; o] = \int \mathcal{D}\phi \mathcal{D}a\, e^{-S_{\text{eff}}[\phi, a; o]/2D}$$

where $S_{\text{eff}}$ includes effective coupling to observations via the Markov blanket's $p(s|\eta)$ structure.

**Step 5.** Stationary-phase / saddle-point approximation for variational $q$:

$$q^*(\phi) = \arg\min_{q} F[q]$$

where $F[q]$ emerges from $S_{\text{eff}}$ via the standard variational thermodynamic formula:

$$F[q] = \mathbb{E}_q[S_{\text{eff}}/2D] + S_{\text{entropy}}[q]$$

For appropriate normalisation, this is *exactly* Friston's variational free energy with:
- $\mathbb{E}_q[S_{\text{eff}}/2D] \leftrightarrow -\mathbb{E}_q[\log p(\phi, o)]$ (likelihood term from the action)
- $S_{\text{entropy}}[q] \leftrightarrow \mathbb{E}_q[\log q(\phi)]$ (entropy term from Legendre transform)

**Step 6.** Biological commit: the agent's state evolves toward $q^*$ via gradient flow on $F$:

$$\partial_t q(\phi) = -\nabla_q F[q]$$

This is standard Friston active inference dynamics. Convergence to $q^*$ is the biological race commit in the A4 sense.

### 5C.4 Axiom mapping (Corollary 3)

- **A1 (parallelism):** $q(\phi)$ is a distribution over an ensemble of candidate internal states
- **A2 (competition):** variational optimisation weights candidates via $F[q]$ (competitive via likelihood × prior)
- **A3 (constraint):** bounded compute $\to$ $q$ cannot reach the exact posterior; approximation is forced by time-budget
- **A4 (commit):** $q^* = \arg\min F$ is the selected posterior (biological analog of pointer-basis selection)
- **A5 (irreversibility):** free-energy minimisation is dissipative (Landauer analog in the biological substrate; ATP consumption per state change)

### 5C.5 Sengupta-Friston reference

Sengupta-Friston (2018) "How Markovian is the brain?" is a preliminary path-integral formulation of FEP. Full derivation-rigorisation is research-level work (their article is a starting point, not final).

### 5C.6 Known critiques (FEP-specific)

- **Colombo-Wright (2018):** FEP has been criticised for circularity — agents defined as free-energy minimisers, then claimed to minimise free energy
- **Kirchhoff et al. (2018):** empirical vs. normative FEP distinction, some predictions may be tautological
- **van Es (2021):** Markov blanket assumption may not be biologically realised
- **Andrews (2021):** FEP vs. Bayesian brain distinction

**Position.** We cite FEP as *mathematical* instantiation of variational inference under bounded compute. Corollary 3 shows mathematical equivalence; FEP-as-settled-neuroscience-theory is a separate question on which we take no stand.

### 5C.7 Status

Corollary 3 now has a formal derivation path from Schwinger-Keldysh via MSR + Markov blanket marginalisation to Friston variational free energy. Each step uses established mathematics; the only new move is to assemble them under the race lens.

**Full rigour** requires a detailed Sengupta-Friston extension to arbitrary non-equilibrium regimes + rigorous convergence proof for the gradient flow on $F$. Paper 10 offers a derivation path; peer-review-grade proof is research-level work.

---

## 5D. Onsager-Machlup derivation (unpacking Corollary 2)

Corollary 2 claims that classical stochastic race = Onsager-Machlup path integral with Freidlin-Wentzell commit. This section develops the derivation formally from Schwinger-Keldysh via the classical limit.

### 5D.1 Setup — Langevin dynamics

Consider a classical stochastic system governed by the overdamped Langevin equation:

$$\partial_t \phi(t) = F[\phi(t)] + \eta(t), \quad \langle\eta(t)\eta(t')\rangle = 2D\,\delta(t-t')$$

where $\phi$ is the state variable, $F$ is the deterministic drift (typically $F = -\nabla U/\gamma$ for potential $U$), and $\eta$ is Gaussian noise of intensity $D$.

### 5D.2 MSR (Martin-Siggia-Rose) transformation

Introduce an auxiliary "response field" $\hat\phi$ to convert the Langevin equation to a path integral. Path probability:

$$P[\phi] = \int \mathcal{D}\hat\phi\, \exp\left\{\int dt\, i\hat\phi(\partial_t\phi - F[\phi]) - D\hat\phi^2\right\}$$

Gaussian-integrate out $\hat\phi$:

$$P[\phi] \propto \exp\left\{-\frac{1}{4D}\int dt\, (\partial_t\phi - F[\phi])^2\right\}$$

This is the **Onsager-Machlup (1953) path probability**. For $F = -\nabla U/\gamma$ (overdamped, potential-driven):

$$P[x(t)] \propto \exp\left\{-\frac{1}{4D}\int dt\, (\dot{x} + \nabla U/\gamma)^2\right\}$$

### 5D.3 Connection to Schwinger-Keldysh

Start from the full Schwinger-Keldysh action (from the main theorem):

$$S_{SK}[\phi_+, \phi_-] = S[\phi_+] - S[\phi_-] + S_{IF}[\phi_+, \phi_-]$$

Rotate to the Keldysh basis: $\phi_c = (\phi_+ + \phi_-)/2$ (classical field), $\phi_q = \phi_+ - \phi_-$ (quantum field).

Take the classical limit $\hbar \to 0$: quantum field fluctuations become small. Expand the action to leading order in $\phi_q$:

$$S_{SK} \to \int dt\, \phi_q \left[\partial_t\phi_c - F[\phi_c]\right] + iD\phi_q^2 + \mathcal{O}(\phi_q^3)$$

**Critical observation.** This *is* the MSR action with the identification $\hat\phi \equiv \phi_q$. The classical limit of Schwinger-Keldysh *is* the MSR formalism.

Integrating out $\phi_q$ via Gaussian → Onsager-Machlup path integral (step 5D.2). **Chain complete: SK → Keldysh rotation → classical limit → MSR → OM.**

### 5D.4 Freidlin-Wentzell commit

For weak-noise limit $D \to 0$, the OM path probability concentrates sharply:

$$P[x(t)] \propto \exp\left\{-\frac{S_{OM}[x]}{2D}\right\}$$

where the Onsager-Machlup action is:

$$S_{OM}[x] = \frac{1}{2}\int dt\, (\dot{x} + \nabla U/\gamma)^2$$

Large-deviation theory (Freidlin-Wentzell 1984) yields: the dominant path is the minimum-action "instanton" trajectory $x^*$. The system commits to $x^*$ with probability $\to 1$ as $D \to 0$.

### 5D.5 Axiom mapping (Corollary 2)

- **A1 (parallelism):** $\int \mathcal{D}x$ over all paths — parallel evaluation of candidate trajectories
- **A2 (competition):** $\exp(-S_{OM}/2D)$ weights paths differentially — Onsager-Machlup action is the competition metric
- **A3 (constraint):** noise intensity $D$ and drift $F$ set the commit-timescale via fluctuation-dissipation: $\tau_c \sim \gamma/(k_B T)$ for thermal noise $D = k_B T/\gamma$
- **A4 (commit):** Freidlin-Wentzell minimum-action path selection (classical analog of pointer-basis selection)
- **A5 (irreversibility):** dissipative drift $F = -\nabla U/\gamma$ produces entropy; Landauer bound satisfied via thermal bath

### 5D.6 Examples

- **Overdamped Brownian motion** in a potential: $F = -\nabla U/\gamma$, standard OM
- **Chemical reaction rates:** Kramers escape $\tau \propto e^{S_{OM}/2D}$ (direct Freidlin-Wentzell application)
- **Neural population dynamics:** subthreshold membrane voltage $\phi$ drives spike-commits in the OM regime
- **Soft-matter self-assembly:** colloidal self-organisation follows OM dynamics

### 5D.7 Status

Corollary 2 now has a formal derivation chain: Schwinger-Keldysh → Keldysh rotation → classical limit → MSR → Onsager-Machlup + Freidlin-Wentzell. Each step uses established mathematics (Kamenev 2011 *Field Theory of Non-Equilibrium Systems* is canonical; Altland-Simons *Condensed Matter Field Theory* chapter on Keldysh is alternative).

Completes the theoretical pyramid: 5A (Born rule via envariance), 5B (CR-Keldysh mapping), 5C (FEP via Markov blanket marginalisation), 5D (Onsager-Machlup via classical limit). All four corollaries of the main theorem now have formal unpackings.

---

## 5E. Noether reformulation of race (symmetry ↔ conservation)

Noether's theorem (1918) states that every differentiable symmetry of a physical system's action produces a conservation law. This section shows that the race-framework is compatible with Noether structure, identifies which symmetries survive in open race-systems, develops envariance (Section 5A) as the primary race-Noether instance, and states a formal Proposition on the symmetry-commit duality.

### 5E.1 Context: Noether in closed vs. open systems

In closed systems (unitary QM, Hamiltonian mechanics) Noether gives direct conservation:
- Time translation → energy
- Space translation → momentum
- Rotation → angular momentum
- U(1) gauge → electric charge

Race-systems are *open* (system + environment). This breaks some symmetries:
- Environmental coupling typically breaks time-translation symmetry (environment has finite thermal bath → energy dissipation)
- Commit events (A4) are discrete and break continuous symmetries
- A5 irreversibility breaks time-reversal symmetry

**Central question.** Which Noether conservations survive in race, and which become *quantised* at commit events?

### 5E.2 Symmetries surviving within the evaluation phase

Pre-commit ($t \ll \tau_c$) the system's dynamics is approximately unitary (Section 3 Theorem Step 5). Under this approximation:
- The Hamiltonian action $S[\phi]$ has standard closed-system symmetries
- Noether conservations apply *locally* over the evaluation-phase duration
- For example, energy is conserved within system+environment (before coarse-graining over the environment)

This is not new physics. It is the recognition that the race evaluation phase *is* standard unitary dynamics, so the Noether apparatus applies directly there.

### 5E.3 Envariance as the primary race-Noether instance

Zurek's envariance argument (Sections 5A.2–5A.7) is precisely a Noether-type argument in structural form:

**Symmetry.** For the Schmidt-decomposed state $|\Psi_{SE}\rangle = \sum_k \alpha_k |s_k\rangle|e_k\rangle$, the transformation $U_S \otimes V_E$ (phase rotations on system, inverse phases on environment) leaves the state invariant — the composite system-environment is *envariant*.

**Conservation law.** The reduced system state $\rho_S$ cannot depend on phases that can be annulled by environment alone. Algebraic consistency forces decoherence + Born-rule probability measure:

$$\rho_S = \sum_k |\alpha_k|^2 |s_k\rangle\langle s_k|, \quad \sum_k p_k = 1$$

**Conservation.** $\sum_k p_k = 1$ (probability-measure conservation) is race's primary Noether conservation, derived from envariance symmetry.

**Consequence.** The Born rule is not a postulate but a Noether consequence of bipartite envariance symmetry. This gives Section 5A.7's result deeper structural anchoring.

### 5E.4 Classical limit: Hamilton-Noether

In Corollary 2's classical limit ($\hbar \to 0$) the path integral reduces to a stationary-phase-dominant classical trajectory. The classical Hamilton action has standard Noether conservations: energy (time translation), momentum (space translation), angular momentum (rotation). In the Onsager-Machlup regime with dissipative drift $F = -\nabla U/\gamma$:
- Energy is *not* conserved (dissipates into environment)
- Phase-space volume contracts (dissipation)
- Probability normalisation ($\int P[x(t)] \mathcal{D}x = 1$) is conserved

The last is analogous to the envariance conservation: Race preserves *probability*, even when other classical-mechanical conservations are broken.

### 5E.5 Commit events as discrete symmetry breaking

A4 commit selects one pointer state. This is discrete breaking of continuous symmetries:
- Phase symmetry (continuous U(1)) is broken when one phase relation is fixed
- Permutation symmetry between equal-amplitude states is broken by selection
- Time-reversal symmetry is broken at commit (A5 irreversibility)

**Landauer bound as quantised symmetry breaking.** Each commit-bit costs at least $k_B \ln 2$ entropy in the environment. This is *quantised* symmetry breaking: continuous symmetry is broken in discrete packets, each with a minimum entropy cost.

**Analog to the Higgs mechanism.** In particle physics, spontaneous symmetry breaking breaks continuous gauge symmetry and produces massive particles. In race, commit breaks continuous evaluation-phase symmetry and produces *committed states* (massless evaluation → "massive" commit outcome). Structurally analogous; mathematics differs but is parallel.

**Concrete examples of broken-symmetry-as-commit:**

- **Ferromagnet magnetisation.** Rotation symmetry broken at the Curie temperature → commit to a specific magnetisation direction
- **Higgs vacuum selection.** SU(2)×U(1) symmetry broken → commit to a specific vacuum configuration
- **Crystallisation.** Translation symmetry broken → commit to a specific crystal-lattice orientation
- **Biological morphogenesis.** Isotropy broken → commit to a body-axis

This indicates a **general correspondence**: broken-symmetry events *are* race-commit events.

### 5E.6 Formal statement

**Proposition (race-Noether duality).** A continuous symmetry $\mathcal{S}$ of $S_{SK}$ is either (a) preserved through commit (giving a conserved quantity via Noether) or (b) broken at commit (corresponding to commit-event selection).

Case (a): standard conservation laws (energy, momentum, probability).

Case (b): order parameter $\mathcal{O}$ with $\langle \mathcal{O}\rangle_{\text{pre-commit}} = 0$, $\langle \mathcal{O}\rangle_{\text{post-commit}} \neq 0$. Commit is $\mathcal{S}$-breaking.

### 5E.7 Axiom consequences

- **A1 (parallelism):** under $\mathcal{S}$-invariance, all rotations of state are equivalent → degenerate candidates populate the evaluation phase
- **A2 (competition):** interaction term $S_{\text{IF}}$ may break $\mathcal{S}$ → lifts degeneracy
- **A4 (commit):** specific pointer-state selection = specific symmetry-breaking direction
- **A5 (irreversibility):** post-commit, $\mathcal{S}$-breaking is locked in; entropy attached to direction-choice

### 5E.8 Information conservation (open research)

**Hypothesis.** The evaluation phase preserves an "information quantity" that is Noether-conserved under path-integral symmetries; commit events expropriate discrete amounts of this information to the environment (Landauer bound lower limit).

Tentative formulation:
- Define an information current $J^\mu_I$ analogous to the probability current in QM
- Claim: $\partial_\mu J^\mu_I = 0$ in the evaluation phase (information continuity)
- Commit breaks this by projecting onto the pointer basis; environment absorbs ejected information

This is *open research direction*, not established derivation. Related work: Lloyd's "ultimate physical limits" (2000), Margolus-Levitin (1998), holographic-principle information bounds.

### 5E.9 Testable predictions

1. **Symmetry-breaking timescale = commit-timescale.** The race theorem predicts that time-to-symmetry-breaking scales as Margolus-Levitin: $\tau_c \geq \pi\hbar/(2E_{\text{gap}})$ where $E_{\text{gap}}$ is the energy gap between broken-symmetry states. Testable in condensed matter (e.g., spin-crossover systems).
2. **Inverse-symmetry-breaking (commit-reversal) cost.** Reversing a symmetry-breaking commit requires Landauer energy $\geq k_B T \ln 2$ per bit. Testable in mechanical bistable systems.
3. **LLM analogy.** Fine-tuning is symmetry-breaking of the pretrained model's isotropic parameter space. Fine-tuning cost (gradient-descent work) scales with tuning depth per Noether-Landauer.

### 5E.10 Status and significance

Section 5E reinterprets existing race derivations in Noether language:
- **Envariance = label-permutation symmetry → Born-rule conservation** (rigorous, based on Section 5A)
- **Classical limit Hamilton-Noether → standard classical conservations** (standard physics)
- **Commit events = discrete symmetry breaking** (Landauer bound quantifies)
- **Information conservation** (open research)

The section adds no new theorems. It anchors existing race derivations in the Noether framework, strengthening the paper's positioning as "unified reading of existing physics" by showing that race conservation laws emerge from standard symmetry arguments.

**Implication for peer review.** Physicists familiar with Noether but not race will recognise the envariance derivation as a Noether variant. This shifts the paper from "exploration of a new concept" to "reformulation in standard-physics language".

---

## 6. Known Gaps / Next Steps for Peer-Review Rigour

1. **Formal proof of pointer-basis uniqueness.** Zurek's original argument has technical subtleties; careful citation + precise statement is needed.
2. **Markovianity assumption.** Explicitly stated in theorem assumption (ii); not a gap but a scope-restriction. Real environments have non-Markovian corrections (Feynman-Vernon non-local kernels, memory effects). Extension to non-Markovian regimes exists in the literature (Shibata-Shimasaki time-convolutionless master equation, Hierarchical Equations of Motion, Breuer-Petruccione formalism). The backbone theorem holds for the Markovian case; the non-Markovian case yields broader corollaries but requires separate derivation. **Not a paper-blocker** — scope-restriction, clearly announced.

   **Empirical note.** Fourier power-spectrum analysis of 4 LLM-substrate datasets shows $\alpha \in [0.08, 0.17]$ (close to white noise $\alpha = 0$), indicating Markovian dynamics. Assumption (ii) is empirically validated on the LLM substrate (see supplementary materials).
3. **Envariance derivation details.** ~~gap~~ Addressed in Section 5A. Full peer-review rigour still requires explicit treatment of the Schlosshauer-Fine (2005) critique + parallel Deutsch-Wallace (2012) derivation as backup.
4. **Active inference path-integral.** ~~gap~~ Addressed in Section 5C. SK → MSR → Markov blanket marginalisation → Friston $F[q]$ derivation in 6 steps with axiom-mapping. Full rigour requires peer-review-grade convergence proof + extension to non-equilibrium; backbone derivation-path is now established.
5. **CR-to-Keldysh mapping.** ~~gap~~ Addressed in Section 5B. Formal mapping via threshold functional on equal-time Keldysh component + four testable predictions against Paper 1 data. Full empirical validation awaits separate re-analysis work.
6. **Quantum speed limit sharpness.** Margolus-Levitin in A3; the Levitin-Toffoli (2009) unified bound may be more appropriate.
7. **Edge cases.** Closed quantum systems without environment = evaluation-only limit, not complete race. Explicit acknowledgment in paper.
8. **Relativistic extension.** Schwinger-Keldysh in curved spacetime gives Lorentz invariance automatically (standard QFT), but is spelled out for §5.3 of the master.

---

## 7. Connection to Paper 10 master

This derivation operationalises the "Derivation Strategy" section of the master:

| Pyramid level | Document section |
|---|---|
| Abstract axioms A1–A5 | Section 2 |
| Unification (MSR/SK) | Section 3 Theorem |
| Quantum limit | Corollary 1 |
| Classical limit | Corollary 2 |
| Biological instance | Corollary 3 |
| LLM/CR instance | Corollary 4 |

Paper 10's §5 (time as emergent from race) instantiates Corollary 1. §5.3 (Lorentz-covariance of race-structure) emerges from Schwinger-Keldysh covariance (standard QFT).
