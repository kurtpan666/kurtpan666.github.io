# The Merkle–Damgård Transform
Let (Gen, $h$ ) be a compression function for inputs of length $n+n^{\prime} \geq 2 n$ with output length $n$. Fix $\ell \leq n^{\prime}$ and $I V \in\{0,1\}^{n}$. 

Construct hash function (Gen, $H$ ) as follows:
- Gen: remains unchanged.
- $H$ : on input a key $s$ and a string $x \in\{0,1\}^{*}$ of length $L<2^{\ell}$, do:
	1. Append a 1 to $x$, followed by enough zeros so that the length of the resulting string is $\ell$ less than a multiple of $n^{\prime}$. Then append $L$, encoded as an $\ell$-bit string. Parse the resulting string as the sequence of $n^{\prime}$-bit blocks $x_{1}, \ldots, x_{B}$.
	2. Set $z_{0}:=I V$.
	3. For $i=1, \ldots, B$, compute $z_{i}:=h^{s}\left(z_{i-1} \| x_{i}\right)$.
	4. Output $z_{B}$.

````{prf:theorem}
If $(\mathrm{Gen}, h)$ is collision resistant, then so is $(\mathrm{Gen}, H)$
````

````{prf:proof}
Let $\mathcal{A}$ be a probabilistic polynomial-time adversary and $\varepsilon$ a function such that $\mathcal{A}$ succeeds in the $\mathrm{Hash}$-$\mathrm{coll}$ experiment with (Gen, $H$ ) with probability $\varepsilon$. We construct an adversary $\mathcal{A}^{\prime}$ that succeeds in the $\mathrm{Hash}$-$\mathrm{coll}$ experiment with (Gen,$h)$ with probability $\varepsilon$. 

Upon receiving $s$, $\mathcal{A}^{\prime}$ invokes $\mathcal{A}$ upon $s$ and receives back a pair $x, x^{\prime} .$ 

---

We show that for any $s$, a collision in $H^{s}$ yields a collision in $h^{s}$. Let $x$ and $x^{\prime}$ be two different strings of length $L$ and $L^{\prime}$, respectively, such that $H^{s}(x)=H^{s}\left(x^{\prime}\right)$. Let $x_{1}, \ldots, x_{B}$ be the $B$ blocks of the padded $x$, and let $x_{1}^{\prime}, \ldots, x_{B^{\prime}}^{\prime}$ be the $B^{\prime}$ blocks of the padded $x^{\prime}$. Let $z_{0}, z_{1}, \ldots, z_{B}$ (resp., $z_{0}^{\prime}, z_{1}^{\prime}, \ldots, z_{B^{\prime}}^{\prime}$ ) be the intermediate results during computation of $H^{s}(x)$ (resp., $\left.H^{s}\left(x^{\prime}\right)\right)$. There are two cases to consider:

Case 1: $L \neq L^{\prime}$. In this case, the last step of the computation of $H^{s}(x)$ is $z_{B}:=h^{s}\left(z_{B-1} \| x_{B}\right)$, and the last step of the computation of $H^{s}\left(x^{\prime}\right)$ is $z_{B^{\prime}}^{\prime}:=h^{s}\left(z_{B^{\prime}-1}^{\prime} \| x_{B^{\prime}}^{\prime}\right)$. Since $H^{s}(x)=H^{s}\left(x^{\prime}\right)$ we have $h^{s}\left(z_{B-1} \| x_{B}\right)=$ $h^{s}\left(z_{B^{\prime}-1}^{\prime} \| x_{B^{\prime}}^{\prime}\right)$. However, $L \neq L^{\prime}$ and so $x_{B} \neq x_{B^{\prime}}^{\prime}$. (Recall that the last $\ell$ bits of $x_{B}$ encode $L$, and the last $\ell$ bits of $x_{B^{\prime}}^{\prime}$ encode $L^{\prime}$.) Thus, $z_{B-1} \| x_{B}$ and $z_{B^{\prime}-1}^{\prime} \| x_{B^{\prime}}^{\prime}$ are a collision with respect to $h^{s}$.

Case 2: $L=L^{\prime}$. This means that $B=B^{\prime}$. Let $I_{i} \stackrel{\text { def }}{=} z_{i-1} \| x_{i}$ denote the $i$ th input to $h^{s}$ during computation of $H^{s}(x)$, and define $I_{B+1} \stackrel{\text { def }}{=} z_{B}$. Define $I_{1}^{\prime}, \ldots, I_{B+1}^{\prime}$ analogously with respect to $x^{\prime}$. Let $N$ be the largest index for which $I_{N} \neq I_{N}^{\prime}$. Since $|x|=\left|x^{\prime}\right|$ but $x \neq x^{\prime}$, there is an $i$ with $x_{i} \neq x_{i}^{\prime}$ and so such an $N$ certainly exists. Because

$$
I_{B+1}=z_{B}=H^{s}(x)=H^{s}\left(x^{\prime}\right)=z_{B}^{\prime}=I_{B+1}^{\prime},
$$
we have $N \leq B$. By maximality of $N$, we have $I_{N+1}=I_{N+1}^{\prime}$ and in particular $z_{N}=z_{N}^{\prime}$. But this means that $I_{N}, I_{N}^{\prime}$ collide under $h^{s}$.

---


- If $H^{s}(x) \neq H^{s}\left(x^{\prime}\right)$ then $\mathcal{A}^{\prime}$ just halts. 

Otherwise, 
- IF $L \neq L^{\prime}$ then $\mathcal{A}^{\prime}$ outputs $z_{B} \| L$ and $z_{B^{\prime}}^{\prime} \| L^{\prime}$ and halts. 

- IF $L=L^{\prime}$, then $\mathcal{A}^{\prime}$ works backwards from the last block to the first to find the maximal $N$. 
	- Then, $\mathcal{A}^{\prime}$ outputs $I_N$ and $I^{\prime}_N$ and halts. 

Note that $\mathcal{A}^{\prime}$ can compute all the $z$-values by computing $H$ and storing all the intermediate values. So whenever $\mathcal{A}$ finds a collision, $\mathcal{A}^{\prime}$ also finds a collision.  Thus, $\mathcal{A}^{\prime}$ succeeds in $\mathrm{Hash}$-$\mathrm{coll}$ for (Gen, $\left.h\right)$ with probability $\varepsilon$, implying that $\varepsilon(n)$ is negligible. Thus, (Gen, $H)$ is collision-resistant as required.
````