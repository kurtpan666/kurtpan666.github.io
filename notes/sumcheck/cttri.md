# IP for Counting Triangles in Graphs

````{prf:definition} Doubly-efficient IP
:nonumber: true

- Provers run in *polynomial* time
- Verifiers run in *linear* time
````

````{prf:definition} The Counting Triangles Problem
:nonumber: true

The input is the adjacency matrix $A$, and the goal is to determine the number of unordered node triples $(i, j, k) \in V \times V \times V$ such that $i, j$, and $k$ are all connected to each other, i.e., $(i, j),(j, k)$ and $(i, k)$ are all edges in $E$.
````

A function $f_{A}$ mapping $\{0,1\}^{\log n} \times\{0,1\}^{\log n}$ to $\{0,1\}$:  Define $f_{A}(x, y)$ so that it interprets $x$ and $y$ as the binary representations of some integers $i$ and $j$ between 1 and $n$, and outputs $A_{i, j}$. 



Then the number of triangles, $\Delta$, in $G$ can be written:

$$
\Delta=\frac{1}{6} \sum_{x, y, z \in\{0,1\}^{\log n}} f_{A}(x, y) \cdot f_{A}(y, z) \cdot f_{A}(x, z) .
$$

$\widetilde{f}_{A}$ is the multilinear extension of $f_{A}$ over $\mathbb{F}$

To see that this equality is true, observe that the term for $x, y, z$ in the above sum is 1 if edges $(x, y),(y, z)$, and $(x, z)$ all appear in $G$, and is 0 otherwise. The factor $1 / 6$ comes in because the sum over ordered node triples $(i, j, k)$ counts each triangle 6 times, once for each permutation of $i, j$, and $k$.


$$
g(X, Y, Z)=\widetilde{f}_{A}(X, Y) \cdot \widetilde{f}_{A}(Y, Z) \cdot \widetilde{f}_{A}(X, Z)
$$

$$
6 \Delta=\sum_{x, y, z \in\{0,1\}\}^{\log n}} g(x, y, z)
$$

So applying the sum-check protocol to $g$ yields an IP computing $6 \Delta$.

