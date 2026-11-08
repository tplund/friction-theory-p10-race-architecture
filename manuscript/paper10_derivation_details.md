# Paper 10 — Derivation Sketch (Companion Document)

Companion to *Race all the way down, race all the way up: A unifying vocabulary for bounded-commit dynamics across quantum, classical, biological, and computational substrates* (Pødenphant Lund 2026, https://doi.org/10.5281/zenodo.20014567).

Status. This document gives the technical detail behind three parts of the paper: the representation of the race-axioms in Markovian decohering open quantum systems (master §3), the two parameter regimes of that representation (master §4.1 and §4.2), and the structural mapping between the language-model CR signal and an equal-time Keldysh observable (master §4.3). It is a sketch. The representation is an organisation of standard open-system results under the axioms, not a theorem with a proof, and the language-model mapping is an analogy under stated assumptions, not a parameter limit. Steps that would need tightening for a formal treatment are flagged where they occur.

Scope. The inverted-U discussed in master §1.4 is not derived here. The master treats its specific shape as kernel-conditional, a pattern shared by the catalogued cases rather than a consequence of the axioms alone, and nothing below bears on it.

## 1. Motivation

Paper 10 proposes race as a shared vocabulary for bounded-commit dynamics: parallel evaluation of candidates, competition between them, a finite-time constraint, an irreversible commit. This sketch asks a narrower question. In one substrate where the physics is well understood, Markovian decohering open quantum systems, can the standard Schwinger-Keldysh treatment be read as satisfying the five race-axioms, and do the quantum and classical-stochastic regimes arise as parameter limits of the same generating functional? The answer sketched below is yes, under three explicit assumptions.

It does not show that quantum, classical, biological and computational systems share a single underlying derivation (master §1.3); it shows that the vocabulary applies in each.

## 2. Formal race-axioms

The name and the accumulator reading come from the race models of decision research (Vickers 1970; Ratcliff 1978; Usher & McClelland 2001; Brown & Heathcote 2008), where parallel accumulators compete and the first to a threshold sets the outcome; master §2.2 sets out how the axioms below relate to that tradition. What follows states the axioms in a form general enough to apply to physical substrates.

A race-system consists of:
- a configuration space $\mathcal{C}$ (Hilbert space, classical phase space, or general measure space);
- a state $\rho$ (density operator or probability measure on $\mathcal{C}$);
- an environment $E$ (a bath of degrees of freedom);
- a time parameter $t \in [0, T]$.

### A1 (Parallelism / Superposition)

The pre-commit state admits representation as a path-integral generating functional:

$$Z[J] = \int \mathcal{D}\phi\, e^{iS_{\text{eff}}[\phi]/\hbar_{\text{eff}}}\, \exp\left(i \int J\phi\, dt\right)$$

Observable expectations are computed as functional derivatives. The integration over path-histories $\mathcal{D}\phi$ is what "parallel evaluation" refers to.

### A2 (Competitive Interaction)

Path histories carry weights $w[\phi] = e^{iS_{\text{eff}}[\phi]/\hbar_{\text{eff}}}$. On the Schwinger-Keldysh closed-time-path contour the effective action includes a term coupling the two branches:

$$S_{\text{eff}}[\phi_+, \phi_-] = S[\phi_+] - S[\phi_-] + S_{\text{diss}}[\phi_+, \phi_-]$$

The dissipation term $S_{\text{diss}}$ couples the branches and generates environment-induced competition.

### A3 (Finite-Time Constraint)

A commit-rate functional $\Gamma : (\text{States} \times \text{Environment}) \to [0, \infty)$ sets the commit timescale $\tau_c = 1/\Gamma$. The kinematic floor is the Margolus-Levitin (1998) bound,

$$\tau_c \geq \frac{\pi \hbar}{2 E_{\text{avg}}},$$

with $E_{\text{avg}}$ the mean energy above the ground state. In the Schwinger-Keldysh treatment the rate is set by the imaginary part of the retarded self-energy, $\Gamma(\omega) = -2\,\text{Im}\,\Sigma^R(\omega)$ evaluated on shell (conventions differ by the factor 2; $\text{Im}\,\Sigma^R < 0$ in the retarded convention).

### A4 (Commit / Selection)

For $t \gg \tau_c$:

$$\rho_S(t \gg \tau_c) = \sum_i p_i |i\rangle\langle i|$$

where the pointer basis is selected by $[|i\rangle\langle i|, H_{SE}] \approx 0$ (Zurek 1981, 1982), off-diagonal elements decay as $\rho_{ij}(t) = \rho_{ij}(0)\, e^{-\Gamma_{ij} t}$, and the weights $p_i = |\langle i | \psi(0)\rangle|^2$ are the Born probabilities, taken as empirical input (§5A).

### A5 (Irreversibility)

Where a commit includes a logically irreversible operation, erasing or resetting $N_{\text{bits}}$ raises the thermodynamic entropy of the environment by at least

$$\Delta S_E \geq k_B \ln 2 \cdot N_{\text{bits}}$$

(Landauer 1961). Other commit events produce entropy without falling under this specific bit-erasure bound.

A Poincaré recurrence time $T_P \gg t_{\text{observation}}$ makes the irreversibility effective rather than absolute.

## 3. Representation result

Representation (race-axioms in Markovian decohering open quantum systems). Let $(S, H_S, H_E, H_{SE})$ be a bipartite quantum system, and assume:

- (i) Einselection: there is a pointer basis $\{|i\rangle_S\}$ with $[|i\rangle\langle i|, H_{SE}] \approx 0$.
- (ii) Markovianity: the environment has macroscopically many degrees of freedom, so the reduced evolution is effectively Markovian.
- (iii) Thermal initial state: $\rho(0) = \rho_S(0) \otimes \rho_E(0)$, with $\rho_E(0)$ in thermal equilibrium at temperature $T$.

Then the reduced system dynamics, obtained from the Schwinger-Keldysh generating functional

$$Z[J_+, J_-] = \int \mathcal{D}\phi_+ \mathcal{D}\phi_-\, e^{iS[\phi_+]/\hbar - iS[\phi_-]/\hbar + iS_{\text{IF}}[\phi_+, \phi_-]}$$

(with $S_{\text{IF}}$ the Feynman-Vernon influence functional, written in units of $\hbar$ as in master §3.2), admits an organisation under the race-axioms A1–A5:

- A1 corresponds to path integration over the closed-time-path contour;
- A2 to amplitude interference together with the dissipation kernel;
- A3 to the damping rate $\Gamma = -2\,\text{Im}\,\Sigma^R$, which depends on the coupling and the spectrum of the bath; $\hbar/k_B T$ is the bath's thermal correlation time, a separate scale, and the Margolus-Levitin bound is a third;
- A4 to pointer-basis diagonalisation, with Born weights as input;
- A5 to entropy production in the environment, bounded by Landauer where bits are erased.

Every ingredient is standard. What the section adds is the reading: the same five-axiom organisation used elsewhere in the paper can be read directly off this formalism.

## 4. Parameter regimes

### Regime 1 (quantum)

For $D \to 0$ (vanishing environmental noise, $\hbar$ finite) the generating functional reduces to the coherent Feynman path integral,

$$Z \to K(B, t_B; A, t_A) = \int \mathcal{D}x(t)\, e^{iS[x(t)]/\hbar},$$

with outcome probabilities $P(A \to B) = |K|^2$ supplied by the Born rule at a subsequent measurement (§5A).

### Regime 2 (classical stochastic)

For $\hbar \to 0$ with finite noise intensity $D$, the Keldysh branches collapse to the Martin-Siggia-Rose form and then to the Onsager-Machlup path probability. With the noise convention $\langle\eta(t)\eta(t')\rangle = 2D\,\delta(t-t')$ used in §5C,

$$P[x(t)] \propto \exp\left(-\frac{1}{4D}\int dt\, \left(\dot{x} + \nabla U/\gamma\right)^2\right),$$

and in the weak-noise limit the Freidlin-Wentzell large-deviation result concentrates the commit on the minimum-action path.

### Substrate-mapping (computational substrate / language model)

This is not a third parameter limit. Language-model token generation is not a continuous-time field theory and has no natural continuum limit. What §5B develops instead is a structural analogy between Paper 1's Competing Routes count,

$$\text{CR}(t) = |\{w : p_w(t) > \theta\}|,$$

and the equal-time Keldysh component $G^K(t,t)$, the distribution-width observable of the formalism, as distinct from the retarded response $G^R$, which measures linear response to a perturbation. CR tracks distribution width, so the comparison is to $G^K(t,t)$, not to $G^R$. The analogy holds only under the assumptions listed in §5B.3.

## 5. Construction sketch

Step 1. Write the partition function of system plus environment on the Schwinger-Keldysh contour $C = C_+ \cup C_-$:

$$Z = \text{Tr}\left[T_C \exp\left(-i \int_C dt\, H\right) \rho(0)\right]$$

Step 2. Integrate out the environment, using assumption (iii). The result is an effective generating functional over the system fields (Feynman & Vernon 1963):

$$Z_{\text{eff}}[J_+, J_-] = \int \mathcal{D}\phi_+ \mathcal{D}\phi_-\, \exp\{iS_S[\phi_+]/\hbar - iS_S[\phi_-]/\hbar + iS_{\text{IF}}[\phi_+, \phi_-]\}$$

The integration over both branches corresponds to A1.

Step 3. For a Markovian environment (assumption (ii)), $S_{\text{IF}}$ takes a local-in-time form with a dissipative kernel $\eta$ and a noise kernel $\nu$. The branch coupling these kernels introduce corresponds to A2.

Step 4. Rotate to the Keldysh basis, $\phi_{cl} = (\phi_+ + \phi_-)/2$ and $\phi_q = \phi_+ - \phi_-$. Dissipation damps the $\phi_q$ propagator at rate $\Gamma$.

Step 5. For $t \gg \tau_c = 1/\Gamma$ the quantum field $\phi_q$ is suppressed and the dynamics become semiclassical in $\phi_{cl}$. The damping rate setting the timescale corresponds to A3.

Step 6. Under assumption (i), the effective dynamics single out the pointer basis as the eigenstates of the dominant effective potential, with off-diagonal elements suppressed as $e^{-\Gamma t}$ (Zurek einselection). This corresponds to A4.

Step 7. The weights on the pointer states are the Born probabilities, taken as input (§5A).

Step 8. Entropy is produced in the environment; where the commit includes logically irreversible erasure, it is at least $k_B \ln 2 \cdot N_{\text{bits}}$ (Landauer 1961). This corresponds to A5.

Points that need tightening for a formal treatment are listed in §6.

## 5A. Born rule (scope note)

In the quantum regime, outcome selection is operationalised by the Born rule $p_i = |\langle i | \psi(0)\rangle|^2$ as established empirical content. The framework does not attempt to derive the Born rule from the race-axioms. Several derivations have been proposed in the foundations literature (Zurek 2003, 2005, the envariance argument; Deutsch 1999 and Wallace 2012, the decision-theoretic derivation), and each has been contested (for envariance, Schlosshauer & Fine 2005). The race framework is agnostic on which succeeds: the probability measure is an empirical input rather than a derived result.

## 5B. CR-to-Keldysh structural mapping (detail for master §4.3)

The substrate-mapping proposes that Paper 1's CR count on a language model is structurally analogous to the equal-time Keldysh component, a distribution-width observable. This section states the mapping, its assumptions, the predictions it makes, and how far the existing data go.

### 5B.1 CR definition

For token generation at step $t$ with vocabulary $W$:
- logit vector $l(t) \in \mathbb{R}^{|W|}$;
- softmax at temperature $T$: $p_w(t) = \exp(l_w(t)/T)/Z(t)$;
- CR count: $\text{CR}(t) = |\{w : p_w(t) > \theta\}|$ for a threshold $\theta$.

Two measurement facts govern every number in §5B.7. First, the mapping is defined on the count. Paper 1 also uses a ratio quantity under the name CR (the top-two probability ratio), and which of the two a dataset stores is a precondition for reading it. Second, served models return only the top-$k$ alternatives per position, so a count computed from them is censored at $k$.

### 5B.2 Keldysh components (continuum)

After rotation to the classical/quantum basis, $\phi_c = (\phi_+ + \phi_-)/2$ and $\phi_q = \phi_+ - \phi_-$, the two response functions are:
- retarded: $G^R(t, t') = -i\theta(t-t')\langle[\phi(t), \phi(t')]\rangle$;
- Keldysh: $G^K(t, t') = -i\langle\{\phi(t), \phi(t')\}\rangle$, which carries the population and distribution information.

The equal-time component $G^K(t,t)$ is the symmetric correlator, which for a Gaussian field is the variance; it is this quantity the mapping treats as the distribution width.

### 5B.3 The mapping and its assumptions

The mapping reads CR as a threshold functional of a discretised Keldysh observable,

$$\text{CR}(t) \approx \mathcal{F}_\theta\left[G^K_{\text{LLM}}(t,t)\right],$$

under three assumptions:

- Gaussian approximation. Around its mode, and under some ordering of the candidate tokens, the per-step softmax is approximately Gaussian with variance $\sigma^2(t)$, and $\sigma^2(t)$ tracks the width $G^K(t,t)$. Tokens have no natural metric ordering, so this is the strongest of the three assumptions.
- Discretisation. The integer count approximates the continuous threshold functional.
- Markovian modes. The effective decay rate $\Gamma_{\text{eff}}$ of the discrete process inherits the Markovian-modes structure of §3.

Under the Gaussian approximation, with peak probability $p_{\max}(t)$, the tokens above threshold are those within $\sigma(t)\sqrt{2\ln(p_{\max}/\theta)}$ of the mode, so

$$\text{CR}(t) \approx 2\,\sigma(t)\sqrt{2\ln\!\big(p_{\max}(t)/\theta\big)}\;\propto\;\sigma(t) \propto \sqrt{G^K(t,t)}$$

at fixed $p_{\max}$ and $\theta$. The proportionality to $\sigma$ is the content the mapping uses; the prefactor depends on $\theta$ and on the mode height.

### 5B.4 Decay rate

A3's commit timescale $\tau_c = 1/\Gamma$ has a formal analogue on the language-model substrate in an effective decay rate $\Gamma_{\text{eff}}$, which the analogy would let depend on softmax temperature and context. The energy scale in the Margolus-Levitin bound has no counterpart defined for this substrate, so the bound is noted only as the formal analogue and is not used. The observable consequence the mapping carries is the autocorrelation prediction in §5B.5.

### 5B.5 Predictions and what they discriminate

1. Autocorrelation. $C_{\text{CR}}(\tau) = \langle\text{CR}(t)\,\text{CR}(t+\tau)\rangle_t$ should decay exponentially on a timescale $1/\Gamma_{\text{eff}}$. Exponential autocorrelation is generic for short-memory token-level series, so agreement is consistency, not confirmation.
2. Temperature. CR is a non-monotonic function of softmax $T$ with a peak at intermediate $T$. At low $T$ the softmax concentrates its mass on the argmax and few tokens clear the threshold; at intermediate $T$ the distribution broadens and more do; at high $T$ it approaches uniform $1/V$, and once $1/V < \theta$ none can. The peak position depends on $V$ and $\theta$. This follows from thresholding a softmax and does not discriminate the mapping from any other account of a thresholded softmax.
3. Context length. Longer context should modify $\Gamma_{\text{eff}}$, and CR profiles should reflect it. Not tested.
4. Correctness. Paper 1 reports that CR correlates with error at $\rho = -0.423$ ($p < 0.0001$). The mapping is consistent with this: high CR means a wide pre-commit distribution and so a higher chance that sampling lands on a wrong token. Any account in which a wider distribution means more sampling error predicts the same correlation, so it does not discriminate either.

### 5B.6 Discrete-time limits

Token generation is discrete and the continuum Keldysh formalism is not. Known limitations:
- CR is integer-valued, which adds quantisation noise to $\mathcal{F}_\theta$, and censored at $k$ when read from top-$k$ lists.
- The time step is the forward pass, not a physical timescale.
- Attention gives the model access to the whole context, a form of non-Markovian memory that the Markovian-modes assumption idealises away.

Extending the mapping to non-Markovian Keldysh treatments is research-level work (§6, item 2).

### 5B.7 Empirical status

The analysis covers five datasets (about 1,600 sequences, thinking disabled, direct-answer responses only) and is stratified by instrument, because the datasets do not all store the same quantity under the name CR.

On the three count-instrumented substrates, the exponential fit gives $R^2$ 0.980–0.997 and a fitted decay constant of 0.34–0.46 tokens. On the two ratio-instrumented substrates the decay form is equally clean ($R^2$ 0.992–0.994), but no timescale is read off: the runner discards values at or above 100 before fitting, which removes 59 % and 73 % of tokens there and so leaves the lag unit ill-defined.

Every fitted timescale is shorter than one token. The correlation is essentially gone at the first lag: $C(1)/C(0)$ is at most 0.105 across the five substrates, and 0.004 and −0.028 on the two ratio-instrumented ones. A step down followed by a flat line is the shape an exponential with $\Gamma_{\text{eff}} \gg 1$ fits well, which is why $R^2$ is high and why a high $R^2$ carries little information here. What the data show is that CR carries no detectable memory beyond the adjacent token, which is what a Markov process looks like. They do not measure $\tau_c$, which lies below the resolution of a per-token series.

The framework's primary measure is entropy in nats, and only one of the five datasets keeps per-token entropy. On that one the same pattern appears ($R^2$ 0.993, fitted decay 0.43 tokens). One substrate is suggestive only.

A minority of sequences departs from the pattern. Per-sequence power-spectrum fits find a sub-population of about 1 % with a $1/f$ spectrum, against none in matched white-noise Monte Carlo (master §4.3, Figure 6).

Overall, the data bear on one of the three assumptions and not on the identification itself. The Markovian-modes assumption is supported in bulk, with no memory beyond the adjacent token, and departs in a tail of about 1 %. The exponential form is consistent with the mapping but generic. The Gaussian-Keldysh identification is untested; the test that would discriminate it is not run: instrument the same model and the same sequences with both CR measures concurrently and without masking, and ask whether the two autocorrelations stand in the relation the local-Gaussian link predicts, testing the exponential against stretched-exponential and ARMA alternatives by information criterion.

## 5C. Onsager-Machlup from the classical limit (detail for master §4.2)

Regime 2 identifies the classical stochastic race with the Onsager-Machlup path integral and a Freidlin-Wentzell commit. This section sets out the chain from Schwinger-Keldysh through the classical limit.

### 5C.1 Setup: Langevin dynamics

Take a classical stochastic system governed by the overdamped Langevin equation

$$\partial_t \phi(t) = F[\phi(t)] + \eta(t), \quad \langle\eta(t)\eta(t')\rangle = 2D\,\delta(t-t'),$$

where $\phi$ is the state variable, $F$ the deterministic drift (typically $F = -\nabla U/\gamma$ for a potential $U$), and $\eta$ Gaussian noise of intensity $D$.

### 5C.2 Martin-Siggia-Rose transformation

Introducing a response field $\hat\phi$ turns the Langevin equation into a path integral:

$$P[\phi] = \int \mathcal{D}\hat\phi\, \exp\left\{\int dt\, \left[i\hat\phi(\partial_t\phi - F[\phi]) - D\hat\phi^2\right]\right\}$$

Integrating out $\hat\phi$ (Gaussian) gives

$$P[\phi] \propto \exp\left\{-\frac{1}{4D}\int dt\, (\partial_t\phi - F[\phi])^2\right\},$$

the Onsager-Machlup (1953) path probability. For $F = -\nabla U/\gamma$:

$$P[x(t)] \propto \exp\left\{-\frac{1}{4D}\int dt\, (\dot{x} + \nabla U/\gamma)^2\right\}$$

(The Jacobian term that appears for multiplicative noise or a non-constant drift derivative under Stratonovich discretisation is omitted, as is usual at this level.)

### 5C.3 Connection to Schwinger-Keldysh

Start from the Schwinger-Keldysh action of §3,

$$S_{SK}[\phi_+, \phi_-] = S[\phi_+] - S[\phi_-] + S_{IF}[\phi_+, \phi_-],$$

rotate to $\phi_c = (\phi_+ + \phi_-)/2$ and $\phi_q = \phi_+ - \phi_-$, and take $\hbar \to 0$, in which the quantum field is small. To leading order in $\phi_q$,

$$S_{SK} \to \int dt\, \left\{\phi_q \left[\partial_t\phi_c - F[\phi_c]\right] + iD\phi_q^2\right\} + \mathcal{O}(\phi_q^3),$$

so that $e^{iS_{SK}}$ has exactly the Martin-Siggia-Rose form of §5C.2 with $\hat\phi \equiv \phi_q$, the noise intensity fixed by the fluctuation-dissipation relation. Integrating out $\phi_q$ then gives the Onsager-Machlup path integral. The chain is Schwinger-Keldysh, Keldysh rotation, classical limit, Martin-Siggia-Rose, Onsager-Machlup; each step is standard (Martin, Siggia & Rose 1973; Kamenev 2011).

### 5C.4 Freidlin-Wentzell commit

In the weak-noise limit $D \to 0$ the path probability concentrates sharply,

$$P[x(t)] \propto \exp\left\{-\frac{S_{OM}[x]}{2D}\right\}, \qquad S_{OM}[x] = \frac{1}{2}\int dt\, (\dot{x} + \nabla U/\gamma)^2,$$

which is the same expression as §5C.2. Large-deviation theory (Freidlin & Wentzell 1984) gives two statements. Unconditionally, as $D \to 0$ the path measure concentrates on the zero-action, deterministic trajectory. A rare transition between basins, conditional on its occurring, concentrates on the minimum-action trajectory $x^*$ connecting them, and its rate falls as $e^{-\Delta U/k_B T}$ (Kramers 1940). The commit in the race sense is the second: which basin the trajectory ends in.

### 5C.5 Axiom mapping (Regime 2)

- A1 (parallelism): $\int \mathcal{D}x$ over all paths, the parallel evaluation of candidate trajectories.
- A2 (competition): $\exp(-S_{OM}/2D)$ weights paths differentially; the Onsager-Machlup action is the competition metric.
- A3 (constraint): the noise intensity and the drift set the commit timescale. For thermal noise $D = k_B T/\gamma$, the diffusive time over a characteristic length $\ell$ is $\tau_c \approx \gamma\ell^2/(2k_B T)$, and barrier crossing adds the Kramers factor $e^{\Delta U/k_B T}$.
- A4 (commit): Freidlin-Wentzell concentration on the minimum-action path between basins, a classical counterpart of pointer-basis selection (a path, not a basis).
- A5 (irreversibility): the dissipative drift produces entropy in the thermal bath; the Landauer bound applies only where the commit erases bits.

### 5C.6 Examples

- Overdamped Brownian motion in a potential: $F = -\nabla U/\gamma$, the standard Onsager-Machlup case.
- Chemical reaction rates: Kramers escape, $\tau \propto e^{\Delta U/k_B T}$, a direct Freidlin-Wentzell application.
- Neural accumulation: subthreshold membrane voltage driving a spike can be written in this form.

## 6. Known gaps

1. Pointer-basis uniqueness. Zurek's argument has technical subtleties; a formal treatment needs a precise statement and careful citation.
2. Markovianity. Assumption (ii) is a scope restriction rather than a gap. Real environments have non-Markovian corrections (non-local Feynman-Vernon kernels, memory effects), and extensions exist in the literature (time-convolutionless master equations, hierarchical equations of motion, the Breuer-Petruccione formalism). The representation is stated for the Markovian case; the non-Markovian case would need its own construction. The language-model data in §5B.7 bear on the Markovian-modes assumption of the mapping, not on assumption (ii), which concerns physical environments.
3. Born rule. Taken as input (§5A).
4. Biological regime. The biological regime is not treated as a parameter limit of the quantum representation. Master §4.4 instead runs the operational tests directly at four levels of living organisation.
5. CR-to-Keldysh mapping. Developed in §5B as an analogy under three assumptions; the discriminating test is not run.
6. Quantum speed limit. A3 uses Margolus-Levitin; the unified Levitin-Toffoli (2009) bound, which also covers the Mandelstam-Tamm form, may be the more appropriate statement.
7. Closed systems. A closed quantum system without an environment is the evaluation-only limit: A1 and A2 hold, but there is no commit, so it is not a complete race.

## 7. Correspondence with the master

| Master | This document |
|---|---|
| §2.2 Five axioms A1–A5 | §2 |
| §3.2 Representation result, §3.3 construction | §3, §5, §5A |
| §4.1 Quantum regime | §4 (Regime 1) |
| §4.2 Classical stochastic regime | §4 (Regime 2), §5C |
| §4.3 Computational substrate-mapping | §4, §5B |
| §4.4 Biological regime | not derived here (§6, item 4) |

Master §5 (time as commit count) draws on the Margolus-Levitin bound stated in A3.

## References

Brown, S. D. & Heathcote, A. (2008). The simplest complete model of choice response time: Linear ballistic accumulation. *Cognitive Psychology* 57(3), 153–178. https://doi.org/10.1016/j.cogpsych.2007.12.002

Deutsch, D. (1999). Quantum theory of probability and decisions. *Proc. R. Soc. A* 455, 3129–3137.

Feynman, R. P. & Vernon, F. L. Jr. (1963). The theory of a general quantum system interacting with a linear dissipative system. *Annals of Physics* 24, 118–173.

Freidlin, M. I. & Wentzell, A. D. (1984). *Random Perturbations of Dynamical Systems.* Springer.

Kamenev, A. (2011). *Field Theory of Non-Equilibrium Systems.* Cambridge University Press.

Keldysh, L. V. (1964). Diagram technique for nonequilibrium processes. *Zh. Eksp. Teor. Fiz.* 47, 1515–1527; *Sov. Phys. JETP* 20, 1018 (1965).

Kramers, H. A. (1940). Brownian motion in a field of force and the diffusion model of chemical reactions. *Physica* 7, 284–304.

Landauer, R. (1961). Irreversibility and heat generation in the computing process. *IBM J. Res. Dev.* 5, 183–191.

Levitin, L. B. & Toffoli, T. (2009). Fundamental limit on the rate of quantum dynamics: the unified bound is tight. *Phys. Rev. Lett.* 103, 160502.

Margolus, N. & Levitin, L. B. (1998). The maximum speed of dynamical evolution. *Physica D* 120, 188–195.

Martin, P. C., Siggia, E. D. & Rose, H. A. (1973). Statistical dynamics of classical systems. *Phys. Rev. A* 8, 423–437.

Onsager, L. & Machlup, S. (1953). Fluctuations and irreversible processes. *Phys. Rev.* 91, 1505–1512.

Ratcliff, R. (1978). A theory of memory retrieval. *Psychological Review* 85(2), 59–108. https://doi.org/10.1037/0033-295X.85.2.59

Schlosshauer, M. & Fine, A. (2005). On Zurek's derivation of the Born rule. *Found. Phys.* 35, 197–213.

Schwinger, J. (1961). Brownian motion of a quantum oscillator. *J. Math. Phys.* 2, 407–432.

Usher, M. & McClelland, J. L. (2001). The time course of perceptual choice: The leaky, competing accumulator model. *Psychological Review* 108(3), 550–592. https://doi.org/10.1037/0033-295X.108.3.550

Vickers, D. (1970). Evidence for an accumulator model of psychophysical discrimination. *Ergonomics* 13(1), 37–58. https://doi.org/10.1080/00140137008931117

Wallace, D. (2012). *The Emergent Multiverse: Quantum Theory According to the Everett Interpretation.* Oxford University Press.

Zurek, W. H. (1981). Pointer basis of quantum apparatus: Into what mixture does the wave packet collapse? *Phys. Rev. D* 24, 1516.

Zurek, W. H. (1982). Environment-induced superselection rules. *Phys. Rev. D* 26, 1862.

Zurek, W. H. (2003). Decoherence, einselection, and the quantum origins of the classical. *Rev. Mod. Phys.* 75, 715.

Zurek, W. H. (2005). Probabilities from entanglement, Born's rule from envariance. *Phys. Rev. A* 71, 052105.
