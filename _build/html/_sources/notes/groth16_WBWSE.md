# White-Box Weak SE of Groth16

This section shows that [Groth16](g16) is *white-box weakly simulation extractable*.

::::{margin}
:::{note}
The content here is excerpted almost verbatim from the paper {cite}`BKS21` for learning purposes. All copyrights belong to the original author.

We also omit the definitions involved, which will be supplemented successively in the future.
:::
::::

````{prf:theorem} Groth16 is WB-W-SE
:nonumber: True
Assume that $\left\{u_i(x)\right\}_{i=0}^l$ are linearly independent and $\operatorname{Span}\left\{u_i(x)\right\}_{i=0}^l \cap \operatorname{Span}\left\{u_i(x)\right\}_{i=l+1}^m=\emptyset$. 

Then [Groth16](g16) achieves **weak white-box SE** against algebraic adversaries under the $(2 n-1, n-1)$-dlog assumption.
````

:::{tip} 
The proof splits in two branches:

We show that either $\mathcal{A}$ uses simulated elements, and in this case it can only use them for a single simulation query $k$, or it does not use them at all. In particular, this implies that $\mathcal{A}$ cannot combine several elements from different queries algebraically for the $\pi$ it submits. 

We then argue that the non-simulation case reduces to knowledge soundness, and in the simulation case we show that $\mathcal{A}$ supplies $\phi$ that is equal to one of the simulated instances, which proves that $\mathcal{A}$ reuses a simulated proof, potentially randomized. 
:::

::::{prf:proof}
Let $q$ denote the number of simulation queries of $\mathcal{A}$, and $\left\{a_{i, j}\right\}_{j=0}^l$ denote the instance for the $i$ th query. We now add the three proof elements $\left[\tilde{a}_i\right]_1,\left[\tilde{b}_i\right]_2,\left[\tilde{c}_i\right]_1$ revealed in each simulation to the list of elements that $\mathcal{A}$ can use as an algebraic extraction basis: $\tilde{a}_i=\mu_i, \tilde{b}_i=\nu_i$, and $\tilde{c}_i=\left(\mu_i \nu_i-\alpha \beta-\sum_{j=0}^l a_{i, j}\left(\beta u_j(x)+\alpha v_j(x)+\right.\right.$ $\left.\left.w_j(x)\right)\right) / \delta$. We write out the representation of $A$ and $B(C$ follows the same pattern as $A)$ from the verification equation as the linear combination of the public CRS and new simulated proof elements:

$$
\begin{aligned}
&A=\cdots+\sum_{i=1}^q A_{8, i} \mu_i+\sum_{i=1}^q A_{9, i} \frac{\mu_i \nu_i-\alpha \beta-\sum_{j=0}^l a_{i, j}\left(\beta u_j(x)+\alpha v_j(x)+w_j(x)\right)}{\delta} \\
&B=\cdots+\sum_{i=1}^q B_{5, i} \nu_i
\end{aligned}
$$

Our goal is to reduce the theorem to the knowledge-soundness case by restricting the coefficients related to the new simulated proofs variables, namely $A_{8, i}, A_{9, i}, B_{5, i}, C_{8, i}, C_{9, i}$. 

We will show that a successful $\mathcal{A}$ must either reuse one of the simulated proofs (potentially randomizing it), or it must not have used any simulation-related variables, thus allowing for the reuse of the extraction argument from knowledge soundness. 

We start by inspecting coefficients of the following monomials (affected by simulated proofs):

$$
\begin{array}{cc}
\alpha \beta \text { in } A B-C \delta: A_1 B_1-\sum_{i=1}^q A_{9, i} B_3+\sum_{i=1}^q C_{9, i}=1 & \mu_i \beta \text { in } A B: A_{8, i} B_1=0 \\
\mu_i \nu_j(i \neq j) \text { in } A B: A_{8, i} B_{5, j}=0 & \mu_i \gamma \text { in } A B: A_{8, i} B_2=0 \\
\mu_i \nu_i \text { in } A B-C \delta: A_{9, i} B_3+A_{8, i} B_{5, i}-C_{9, i}=0 & \mu_i \delta \text { in } A B-C \delta: A_{8, i} B_3-C_{8, i}=0 \\
\mu_i \nu_i \nu_j / \delta \text { in } A B: A_{9, i} B_{5, j}=0 & \nu_i \alpha \text { in } A B: B_{5, i} A_1=0 \\
\mu_i \nu_i \beta / \delta \text { in } A B: A_{9, i} B_1=0 & \nu_i \beta \text { in } A B: B_{5, i} A_2=0 \\
& \nu_i \delta \text { in } A B: B_{5, i} A_3=0
\end{array}
$$

First, we show that all $A_{9, i}=0$. Assume the contrary: $A_{9, k} \neq 0$ for some $k$. Then from Equation $\left(\mu_k \nu_k \nu_j / \delta\right)$ for all $j: B_{5, j}=0$. From Equation $\left(\mu_i \nu_i\right)$ for all $i$ we have that $C_{9, i}=$ $A_{9, i} B_3$, which, substituted into Equation $(\alpha \beta)$ give us $A_1 B_1=1$. Hence $B_1 \neq 0$, but from Equation $\left(\mu_k \nu_k \beta / \delta\right)$ we see that $A_{9, k} B_1=0$, but neither $A_{9, k}$ nor $B_1$ is zero, a contradiction.

Thus, all $A_{9, i}=0$, and furthermore Equation $(\alpha \beta)$ simplifies to $A_1 B_1+\sum_{i=1}^q C_{9, i}=1$ and Equation $\left(\mu_i \nu_i\right)$ simplifies to $A_{8, i} B_{5, i}=C_{9, i}$.

We now show, that if at least one $A_{8, k} \neq 0$, then $\mathcal{A}$ reuses the $k$ th simulated proof, and otherwise if all $A_{8, i}=0$ it does not use any simulation-related elements.
- Assume, first, that all $A_{8, i}=0$ : From Equation $\left(\mu_i \nu_i\right)$ all $C_{9, i}=0$. Then, $A_1 B_1=1$ by Equation $(\alpha \beta)$, so from Equation $\left(\nu_i \alpha\right)$ all $B_{5, i}=0$ (since $A_1 \neq 0$ ), and from Equation $\left(\mu_i \delta\right)$ all $C_{8, i}=0$ because all $A_{8, i}=0$. We now have cancelled all the simulation-related variables, and thus $\mathcal{A}$ does not use simulation queries when constructing its proof, and we can reduce the proof to the knowledge soundness case.
- Assume, otherwise, that at least one $A_{8, k} \neq 0$ : Then $B_1=B_2=0$ from Equation $\left(\mu_k \beta\right)$ and Equation $\left(\mu_k \gamma\right.$ ). For all $j \neq k$ from Equation $\left(\mu_k \nu_j\right)$ we have $B_{5, j}=0$, and since $C_{9, j}=B_{5, j} A_{8, j}$, all $C_{9, j}=0$ for $j \neq k$ too. From Equation $(\alpha \beta)$ we obtain $C_{9, k}=1$, thus $B_{5, k}=1 / A_{8, k}$ by Equation $\left(\mu_i \nu_i\right)$. Since now $B_{5, k} \neq 0$, from the Equations $\left(\nu_k \alpha\right),\left(\nu_k \beta\right)$, $\left(\nu_k \delta\right)$ we have $A_1=A_2=A_3=0$. Thus, we are only left with exactly one nonzero triple $\left(A_{8, k}, B_{5, k}, C_{9, k}\right)$, which means $\mathcal{A}$ has used at most one simulated proof number $k$, not being able to combine several simulated proofs into one.
We next look at additional coefficients related to monomials that include $\nu_k$ and $\mu_k$. From Equations $\left(\nu_i \beta / \delta\right),\left(\nu_i \alpha / \delta\right),\left(\nu_i / \delta\right)$ we have $\sum_{i=l+1}^m A_{6, i}\left(\beta u_i(x)+\alpha v_i(x)+w_i(x)\right) / \delta+\sum_{i=0}^{n-2} A_{7, i} x^i t(x) / \delta=$ 0 (related terms of $A$ are the only terms matching this $\nu_i$ in $B$ ):

$$
\begin{aligned}
\nu_k \beta / \delta \text { in } A B: &\left(\sum_{j=l+1}^m A_{6, j} u_j(x)-\sum_{i=1}^q \underline{A_{9, i}} \sum_{j=0}^l u_j(x)\right) B_{5, k}=0 \Longrightarrow \sum_{j=l+1}^m A_{6, j} u_j(x)=0 \\
\nu_k \alpha / \delta \text { in } A B: &\left(\sum_{j=l+1}^m A_{6, j} v_j(x)-\sum_{i=1}^q \underline{A_{9, i}} \sum_{j=0}^l v_j(x)\right) B_{5, k}=0 \Longrightarrow \sum_{j=l+1}^m A_{6, j} v_j(x)=0 \\
\nu_k / \delta \text { in } A B &\left(\sum_{j=l+1}^m A_{6, j} w_j(x)+\sum_{i=0}^{n-2} A_{7, i} x^i t(x)-\sum_{i=1}^q \underline{A_{9, i}} \sum_{j=0}^l w_j(x)\right) B_{5, k}=0 \\
&\left.\Longrightarrow \sum_{j=l+1}^m A_{6, j} w_j(x)=0 \wedge \sum_{i=0}^{n-2} A_{7, i} x^i t(x)=0 \text { (different powers of } x\right)
\end{aligned}
$$

Similarly, from Equations $\left(\nu_i \beta / \gamma\right),\left(\nu_i \alpha / \gamma\right),\left(\nu_i / \gamma\right)$ we have $\sum_{i=0}^l A_{5, i}\left(\beta u_i(x) / \gamma\right)=\sum_{i=0}^l A_{5, i}\left(\alpha v_i(x) / \gamma\right)=$ $\sum_{i=0}^l A_{5, i}\left(w_i(x) / \gamma\right)=0($ the coefficients are also extracted from $A B)$.

$$
\begin{aligned}
&\nu_k \beta / \gamma \text { in } A B:\left(\sum_{j=0}^l A_{5, j} u_j(x)\right) B_{5, k}=0 \Longrightarrow \sum_{j=0}^l A_{5, j} u_j(x)=0 \\
&\nu_k \alpha / \gamma \text { in } A B:\left(\sum_{j=0}^l A_{5, j} v_j(x)\right) B_{5, k}=0 \Longrightarrow \sum_{j=0}^l A_{5, j} v_j(x)=0 \\
&\nu_k / \gamma \text { in } A B:\left(\sum_{j=0}^m A_{5, j} w_j(x)\right) B_{5, k}=0 \Longrightarrow \sum_{j=l+1}^m A_{5, j} w_j(x)=0
\end{aligned}
$$

Because of Equation $\left(\nu_k\right)$ and Equation $\left(\mu_k\right)$ we have $\sum_{i=0}^{n-1} A_{4, i} x^i=0$ and $\sum_{i=0}^{n-1} B_{4, i} x^i=0$ related terms cancelled as well:

$$
\nu_k \text { in } A B:\left(\sum_{i=0}^n A_{4, i} x^i\right) B_{5, k}=0 \Longrightarrow \sum_{i=0}^n A_{4, i} x^i=0
$$
$$
\mu_k \text { in } A B:\left(\sum_{i=0}^{n-1} B_{4, i} x^i\right) A_{8, k}=0 \Longrightarrow \sum_{i=0}^{n-1} B_{4, i} x^i=0
$$
Which also implies $A_{4, i}=B_{4, i}=0$ for all $i$. We now focus on the first critical equation, $\beta$, which has the same elements as in the KS case, except for the additional $C_{9, i}$. Its left side vanishes completely, and on the right we have exactly one additional simulated instance wires set corresponding to $C_{9, k}=1$ :

$$
0=\sum_{i=0}^l a_i u_i(x)+\sum_{i=l+1}^m C_{6, i} u_i(x)-\sum_{i=0}^l a_{k, i} u_i(x)
$$
Because of disjointness ${ }^{11}$ between $u_i(x)$ for witness and instance sets of indices we have both $\sum_{i=0}^l\left(a_i-a_{k, i}\right) u_i(x)=0$ and $\sum_{i=l+1}^m C_{6, i} u_i(x)=0$, thus also $a_i=a_{k, i}$ because of the linear independence of the first set. Then $\mathcal{A}$ has reused the simulated instance $\phi_k=\left\{a_{k, i}\right\}_{i=0}^l$, which concludes the proof.
::::

```{bibliography}
:filter: docname in docnames
```