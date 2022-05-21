# Groth16
We briefly describe the trusted-setup zkSNARK scheme defined in [Gro16]. 

- [Gro16]: Jens Groth. On the size of pairing-based non-interactive arguments. In Marc Fischlin and Jean-Sebastien Coron, editors, ´ EUROCRYPT 2016, Part II, volume 9666 of LNCS, pages 305–326. Springer, Heidelberg, May 2016.

At a high level, given a description of an arithmetic circuit (over the scalar field of a pairing-friendly elliptic curve), a Groth16 proof proves that a circuit is satisfied by a set of public wires (values known to the verifier) and private wires (values which are not known to the verifier, also called *witness elements*).

## Groth16 Scheme

The Groth16 scheme defines four procedures:

- Setup(desc) $\rightarrow$ crs 
	- Generates a common reference string for the given arithmetic circuit description. crs contains the group elements necessary to compute the expressions in $\mathrm{Groth16.Prove}$ below.

- Prove $\left(\mathrm{crs},\left\{a_{i}\right\}_{i=0}^{\ell},\left\{a_{i}\right\}_{i=\ell+1}^{m}\right) \rightarrow \pi$ 
	- Proves the circuit described by crs is satisfied, where $a_{0}, \ldots, a_{\ell} \in \mathbb{F}$ represent the circuit's public input wires and $a_{\ell+1}, \ldots, a_{m} \in \mathbb{F}$ represent the private wires. $\pi$ is of the form $\left([\eta]_{1},[\theta]_{2},[\iota]_{1}\right)$, where
$$
\begin{gathered}
\boldsymbol{\eta}=\alpha+\sum_{i=0}^{m} a_{i} u_{i}(X)+r\boldsymbol{\delta} \quad \boldsymbol{\theta}=\beta+\sum_{i=0}^{m} a_{i} v_{i}(X)+s \boldsymbol{\delta} \\
\iota=\sum_{i=\ell+1}^{m} \frac{a_{i}\left(\beta u_{i}(X)+\alpha v_{i}(X)+w_{i}(X)\right)+h(X) t(X)}{\boldsymbol{\delta}}+\eta s+\theta r-r s \boldsymbol{\delta}
\end{gathered}
$$
		and all otherwise unspecified constants and polynomials come from crs.


- Prepare $\left(\mathrm{crs},\left\{a_{i_{j}}\right\}_{j=1}^{t}\right) \rightarrow \hat{S}$ 
	- Aggregates any subset of public inputs into a single group element called a *prepared input*: $\hat{S}=\sum_{j=1}^{t} a_{i_{j}} W_{i_{j}}$, where $W_{i}$ are the CRS values whose coefficient represents the value of the $i$-th wire of the circuit.

- $\mathrm{Vfy} \left(\mathrm{crs}, \pi,\left\{a_{0}\right\}_{i=0}^{\ell}\right) \rightarrow\{0,1\}$ 
	- Verifies the proof $\pi=(A, B, C)$ by checking the relation,
$$
e(A, B) \stackrel{?}{=} e\left([\alpha]_{1},[\beta]_{2}\right) \cdot e\left(C,[\delta]_{2}\right) \cdot \prod_{i=0}^{\ell} e\left(a_{i} W_{i},[\gamma]_{2}\right)
$$
		where $[\alpha]_{1},[\beta]_{2},[\gamma]_{2}$, and $[\delta]_{2}$ come from crs. 

	Vfy permits any subset of the public inputs to be prepared as above. The common case will be where all but the first input is prepared, i.e., calls of the form $\mathrm{Vfy}\left(\mathrm{crs}, \pi,\left(a_{0}, \hat{S}\right)\right)$.
- $\operatorname{Rerand}(\pi) \rightarrow \pi^{\prime}$ 
	- Rerandomizes the proof $\pi=(A, B, C)$ by sampling $\zeta, \omega \leftarrow \mathbb{F}$ and computing
$$
\pi^{\prime}:=\left(\zeta^{-1} A, \zeta B+\zeta \omega[\delta]_{2}, C+\omega A\right) .
$$
	By Theorem 3 in [BKSV20], the output of Rerand is statistically indistinguishable from a fresh proof of the same underlying statement.

- [BKSV20]: Karim Baghery, Markulf Kohlweiss, Janno Siim, and Mikhail Volkhov. Another look at extraction and randomization of groth’s zk-SNARK. Cryptology ePrint Archive, Report 2020/811, 2020. https://eprint.iacr.org/2020/8 11.

## Proofs for Groth16
We now have four different proofs for Groth16. 

- https://eprint.iacr.org/2016/260.pdf
- https://eprint.iacr.org/2017/620.pdf
- https://eprint.iacr.org/2020/811.pdf
- https://eprint.iacr.org/2021/219.pdf
 
 (According to Mary Maller's talk at [#zksummit](https://twitter.com/hashtag/zksummit?src=hashtag_click) )


