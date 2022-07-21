# Indistinguishability Obfuscation ($\mathcal{iO}$)

````{prf:definition}
A uniform $P P T$ machine $i \mathcal{O}$ is an indistinguishability obfuscator {cite}`Barak12` for a circuit class $\left\{\mathcal{C}_{\lambda}\right\}$ if the following conditions are satisfied:

- (Strong Functionality Preservation) For all security parameters $\lambda \in \mathbb{N}^{+}$, for all $C \in \mathcal{C}_{\lambda}$

$$
\operatorname{Pr}_{C^{\prime} \leftarrow i \mathcal{O}(\lambda, C)}\left[\forall x, C^{\prime}(x)=C(x)\right] \geq 1-\operatorname{negl}(\lambda) .
$$

- For any non-uniform $P P T$ distinguisher $D$, there exists a negligible function $\alpha$ such that the following holds: for all $\lambda \in \mathbb{N}^{+}$, for all pairs of circuits $C_{0}, C_{1} \in$ $\mathcal{C}_{\lambda}$, we have that if $C_{0}(x)=C_{1}(x)$ for all input $x$ and $\left|C_{0}\right|=\left|C_{1}\right|$ (where $|C|$ denotes the size of a circuit), then

$$
\left|\operatorname{Pr}\left[D\left(i \mathcal{O}\left(\lambda, C_{0}\right)\right)=1\right]-\operatorname{Pr}\left[D\left(i \mathcal{O}\left(\lambda, C_{1}\right)\right)=1\right]\right| \leq \alpha(\lambda)
$$
````

```{bibliography}
:filter: docname in docnames
```