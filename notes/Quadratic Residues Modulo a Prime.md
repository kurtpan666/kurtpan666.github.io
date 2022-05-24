# Quadratic Residues Modulo a Prime
> Katz-Lindell 15.4.1

In a group $\mathbb{G}$, an element $y \in \mathbb{G}$ is a **quadratic residue** if there exists an $x \in \mathbb{G}$ with $x^{2}=y$.

In this case, we call $x$ a **square root** of $y$. 

An element that is not a quadratic residue is called a **quadratic non-residue**. 

In an abelian group, the set of quadratic residues forms a subgroup.

In the specific case of $\mathbb{Z}_{p}^{*}$, we have that $y$ is a quadratic residue if there exists an $x$ with $x^{2}=y \bmod p$. 

```{admonition} Proposition
Let $p>2$ be prime. Every quadratic residue in $\mathbb{Z}_{p}^{*}$ has exactly two square roots.
```

Let $\mathrm{sq}_{p}: \mathbb{Z}_{p}^{*} \rightarrow \mathbb{Z}_{p}^{*}$ be the function  $\mathrm{sq}_{p}(x) \stackrel{\text { def }}{=}\left[x^{2} \bmod p\right]$. 

The above shows that $\mathrm{sq}_{p}$ is a two-to-one function when $p>2$ is prime. 

This immediately implies that *exactly half the elements of $\mathbb{Z}_{p}^{*}$ are quadratic residues*. 

We denote the set of quadratic residues modulo $p$ by $\mathcal{Q} \mathcal{R}_{p}$, and the set of quadratic non-residues by $\mathcal{Q} \mathcal{N} \mathcal{R}_{p}$. 

We have just seen that for $p>2$ prime

$$
\left|\mathcal{Q} \mathcal{R}_{p}\right|=\left|\mathcal{Q N} \mathcal{R}_{p}\right|=\frac{\left|\mathbb{Z}_{p}^{*}\right|}{2}=\frac{p-1}{2} .
$$
Define $\mathcal{J}_{p}(x)$, the **Jacobi symbol** of $x$ modulo $p$, as follows. 

Let $p>2$ be prime, and $x \in \mathbb{Z}_{p}^{*}$. Then

$$
\mathcal{J}_{p}(x) \stackrel{\text { def }}{=}\left\{\begin{array}{l}
+1 \text { if } x \text { is a quadratic residue modulo } p \\
-1 \text { if } x \text { is not a quadratic residue modulo } p .
\end{array}\right.
$$
The notation can be extended in the natural way for any $x$ relatively prime to $p$ by setting $\mathcal{J}_{p}(x) \stackrel{\text { def }}{=} \mathcal{J}_{p}([x \bmod p])$.

---
Can we characterize the quadratic residues in $\mathbb{Z}_{p}^{*}$ ? 

We begin with the fact that $\mathbb{Z}_{p}^{*}$ is a cyclic group of order $p-1$ . 

Let $g$ be a generator of $\mathbb{Z}_{p}^{*}$. 

This means that

$$
\mathbb{Z}_{p}^{*}=\left\{g^{0}, g^{1}, g^{2}, \ldots, g^{\frac{p-1}{2}-1}, g^{\frac{p-1}{2}}, g^{\frac{p-1}{2}+1}, \ldots, g^{p-2}\right\}
$$
(recall that $p$ is odd, so $p-1$ is even). 

Squaring each element in this list and reducing modulo $p-1$ in the exponent  yields a list of all the quadratic residues in $\mathbb{Z}_{p}^{*}$ :

$$
\mathcal{Q} \mathcal{R}_{p}=\left\{g^{0}, g^{2}, g^{4}, \ldots, g^{p-3}, g^{0}, g^{2}, \ldots, g^{p-3}\right\}
$$

Each quadratic residue appears twice in this list. Therefore, the quadratic residues in $\mathbb{Z}_{p}^{*}$ are exactly those elements that can be written as $g^{i}$ with $i \in\{0, \ldots, p-2\}$ an even integer.

The above characterization leads to a simple way to compute the Jacobi symbol and thus tell whether an element $x \in \mathbb{Z}_{p}^{*}$ is a quadratic residue or not.

```{admonition} Proposition
 Let $p>2$ be a prime. Then $\mathcal{J}_{p}(x)=x ^ {\frac{p-1}{2}} \bmod p$.
```


```{prf:algorithm} Deciding quadratic residuosity modulo a prime
:label: qrmodprime

**Input**: A prime $p$; an element $x \in \mathbb{Z}_{p}^{*}$

**Output**: $\mathcal{J}_{p}(x)$ (or, equivalently, whether $x$ is a quadratic residue or quadratic non-residue)

$b:=\left[x^{\frac{p-1}{2}} \bmod p\right]$

**if** $b=1$ **return** "quadratic residue"

**else return** "quadratic non-residue"
```


