# $\# \mathrm{SAT} \in \mathrm{IP}$

## \#SAT problem

````{prf:definition} #SAT
:nonumber: true

Let $\phi$ be any **Boolean formula** on $n$ variables of size $S=\operatorname{poly}(n)$
The goal of \#SAT is to compute the *number of satisfying assignments* of $\phi$ : 

$$
\sum_{x \in\{0,1\}^{n}} \phi(x)
$$
````

## The interactive proof for \#SAT

````{prf:definition} arithmetization
:nonumber: true

The process of replacing the **Boolean formula** $\phi$ with an **arithmetic circuit** $\psi$ computing an **extension polynomial**  $g$ of $\phi$.

````

We can turn $\phi$ into an **arithmetic circuit** $\psi$ over $\mathbb{F}$ that computes the desired **extension** $g$ of $\phi$. 

- For any gate in $\phi$ computing the AND of two inputs $y, z, \psi$ replaces $\operatorname{AND}(y, z)$ with multiplication of $y$ and $z$ over $\mathbb{F}$.  It is easy to check that the bivariate polynomial $y \cdot z$ extends the Boolean function $\operatorname{AND}(y, z)$, i.e., $\operatorname{AND}(y, z)=y \cdot z$ for all $y, z \in\{0,1\}$. 

- Likewise, $\psi$ replaces any gate computing $\operatorname{OR}(y, z)$ by $y+z-y \cdot z$. 

- Any formula leaf of the form $\bar{y}$ (i.e., the negation of variable $y$ ) is replaced by $1-y$

It is easy to check that $\psi(x)=\phi(x)$ for all $x \in\{0,1\}^{n}$, and that the number of gates in the arithmetic circuit $\psi$ is at most $3 S$.

Then apply the sum-check protocol to compute $\sum_{x \in\{0,1\}^{n}} g(x)$