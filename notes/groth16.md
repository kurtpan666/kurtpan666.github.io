# Groth16
We briefly describe the trusted-setup zkSNARK scheme defined in {cite}`Groth16`



(g16)=
## Groth16 Scheme

````{prf:algorithm} $(\sigma, \tau) \leftarrow \operatorname{Setup}(R)$
:label: g16-setup


$$
\begin{gathered}
\alpha, \beta, \gamma, \delta, x \leftarrow \mathbb{Z}_{p}^{*}\\
\tau=(\alpha, \beta, \gamma, \delta, x)\\
\boldsymbol{\sigma}_{1}=\left(\begin{array}{l}
\alpha, \beta, \delta,\left\{x^{i}\right\}_{i=0}^{n-1},\left\{\frac{\beta u_{i}(x)+\alpha v_{i}(x)+w_{i}(x)}{\gamma}\right\}_{i=0}^{\ell} \\
\left\{\frac{\beta u_{i}(x)+\alpha v_{i}(x)+w_{i}(x)}{\delta}\right\}_{i=\ell+1}^{m},\left\{\frac{x^{i} t(x)}{\delta}\right\}_{i=0}^{n-2}
\end{array}\right) \\
\boldsymbol{\sigma}_{2}=\left(\beta, \gamma, \delta,\left\{x^{i}\right\}_{i=0}^{n-1}\right) \\
\boldsymbol{\sigma}=\left(\left[\boldsymbol{\sigma}_{1}\right]_{1},\left[\boldsymbol{\sigma}_{2}\right]_{2}\right)
\end{gathered}
$$
````


```{prf:algorithm} $\pi \leftarrow \operatorname{Prove}\left(R, \sigma, a_{1}, \ldots, a_{m}\right)$
:label: g16-proof


$$
\begin{gathered}
A=\alpha+\sum_{i=0}^{m} a_{i} u_{i}(x)+r \delta \\ B=\beta+\sum_{i=0}^{m} a_{i} v_{i}(x)+s \delta \\
C=\frac{\sum_{i=\ell+1}^{m} a_{i}\left(\beta u_{i}(x)+\alpha v_{i}(x)+w_{i}(x)\right)+h(x) t(x)}{\delta}+A s+B r-r s \delta \\
\pi=\left([A]_{1},[C]_{1},[B]_{2}\right)
\end{gathered}
$$
```


```{prf:algorithm} $0 / 1 \leftarrow \operatorname{Vfy}\left(R, \sigma, a_{1}, \ldots, a_{\ell}, \pi\right)$
:label: g16-verify


$$
[A]_{1} \cdot[B]_{2}=[\alpha]_{1} \cdot[\beta]_{2}+\sum_{i=0}^{\ell} a_{i}\left[\frac{\beta u_{i}(x)+\alpha v_{i}(x)+w_{i}(x)}{\gamma}\right]_{1} \cdot[\gamma]_{2}+[C]_{1} \cdot[\delta]_{2}
$$
```

{prf:ref}`g16-proof`

---



By Theorem 3 in {cite}`BKS21` , the output of Rerand is statistically indistinguishable from a fresh proof of the same underlying statement.


## Proofs for Groth16
We now have four different proofs for Groth16. 

- https://eprint.iacr.org/2016/260.pdf
- https://eprint.iacr.org/2017/620.pdf
- https://eprint.iacr.org/2020/811.pdf
- https://eprint.iacr.org/2021/219.pdf
 
 (According to Mary Maller's talk at zkSummit )

## Previous Work

- {cite}`Kil92` gave the first **sublinear communication zero-knowledge argument** that sends fewer bits than the size of the statement to be proved.
- {cite}`Mic00` proposed **sublinear size arguments** by letting the prover in a communication efficient argument compute the verifier’s challenges using a cryptographic function, 
	- (as re-marked in {cite}`Kil95`) this leads to **sublinear size NIZK proofs** when the interactive argument is public coin and zero-knowledge.


```{bibliography}
:filter: docname in docnames
```


```{prf:algorithm} PROVE-EQUAL-NAIVE $\left(x_{i}, x_{j}\right)$ 

 Prove that $x_{i}=x_{j}$
1. $P$ sends $V$ the value of $x_{i}^{0} \oplus x_{j}^{0}$.
2. $V$ uniformly chooses $b \in\{0,1\}$, and sends $b$ to $P$.
3. $P$ reveals $x_{i}^{b}$ and $x_{j}^{b}$, who accepts iff $x_{i}^{b} \oplus x_{j}^{b}$ is equal to the value sent in Step 1.

```


when you refers to [Groth16](g16) scheme.