

# Algebraic Intermediate Representation (AIR)

**[Arithmetization](https://nmohnblatt.github.io/zk-jargon-decoder/definitions/arithmetization.html)** is the reduction of computational statements to a set of algebraic statements involving a set of bounded-degree polynomials. 

In the **STARK** protocol, the output of arithmetization is an **Algebraic Intermediate Representation** of a computation. 

Informally, AIR consists of the following three elements:
1. **execution trace** which is a two-dimensional matrix, in which each row represents the **state** of the computation at a single point in time and each column corresponds to an **algebraic register** tracked over all steps of the computation. Let $T$ denote the execution trace matrix.
2. **transition constraints** which define **algebraic relationships** between two (or more) rows of the execution trace.
3. **boundary constraints** which enforce equality between certain cells of the execution trace and a set of constant values. Boundary constraints can be thought of as defining a set of **input and output values** for the computation.

## Execution Trace
Denote $m$ as the width of the execution trace and $n$ as the number of steps in the execution trace, i.e. $T$ is an $m \times n$ matrix. 

We define the **register trace** of a register $k$ as the polynomial interpolation $f_{k}$ of the set $\left\{\left(\omega^{i}, T[i][k]\right) \mid i \in[0, n)\right\}$, where $\omega$ is a generator of a multiplicative subgroup of size $n$ in the base field specified for an instantiation of a STARK protocol. 

The set $\left\{f_{k} \mid k \in[0, m)\right\}$ is called the set of **trace polynomials**.

Notice that if $f_{k}(x)$ is the value in the execution trace matrix in column $k$ and row $i$, then $f_{k}(x \cdot \omega)$ is the value in $k$ at step $i+1$.

For efficient execution of the STARK protocol, $n$ must be a power of two. This allows us to use **FFT-based polynomial evaluation and interpolation**, which have the complexity of $O(n \log n)$ 

Thus, the base field for the STARK protocol must be **2 -smooth** , which indeed is the case for out selected field with modulus $q=2^{128}-45 \cdot 2^{40}+1$.

```{note} 
A field is **k-smooth** if it contains a subgroup (multiplicative or additive) all of whose prime divisors are at most $k$. For example, a prime field of size $q$ such that $q-1$ is divisible by a large power of 2 , is 2 -smooth.
```


In addition to registers of the execution trace, we also use **periodic registers** (also called **periodic columns**), which are not included in the execution trace but can be referenced in transition constraints. 

Periodic columns are typically used in STARKs to encode a small set of values which can be represented by succinct polynomials of size much smaller than $n$. One example is a register where values repeats in a cycle and the length of the cycle is a power of two.

## Constraints
Both boundary and transition constraints are defined by rational functions of the form:

$$
\frac{p(x)}{z(x)}
$$

where, $p(x)$ defines the **constraint relationship** , and $z(x)$ defines the **constraint domain** (a set of steps at which the constraint should hold). This constraint is said to hold if the polynomial $z$ divides the polynomial $p$.

For **boundary constraints**, $p(x)$ has the following form:

$$
p(x)=c\left(f_{k}(x)\right)
$$
where, $f_{k}(x)$ is the trace polynomial for register $k$ against which the constraint is enforced. 

````{prf:example}
For example, to specify that the value in the first column of the first row in the execution trace must be 1 , we could use the following constraint:

$$
\frac{f_{0}(x)-1}{x-1}
$$
````

````{prf:example}

Similarly, to specify that the value in the 7 th row of the second column must be 987 , we could use the following constraint:

$$
\frac{f_{1}(x)-987}{x-\omega^{7}}
$$
````

For **transition constraints** , $p(x)$ has the following form:

$$
p(x)=c\left(\left\{f_{0}(x), \ldots, f_{m-1}(x)\right\},\left\{f_{0}(x \cdot \omega), \ldots, f_{m-1}(x \cdot \omega)\right\}\right)
$$
that is, $p(x)$ is a function of all register values in two consecutive steps of a computation. 

````{prf:example}

For example, the following constraint enforces that a value in the first register of the execution trace must be incremented by 1 at every step:

$$
\frac{f_{0}(x \cdot \omega)-\left(f_{0}(x)+1\right)}{\prod_{i=0}^{n-1}\left(x-\omega^{i}\right)}
$$
````

Additionally, since trace polynomials are evaluated over a multiplicative subgroup of a field, the denominator of the constraint above can be expressed succinctly, and the constraint can be rewritten as:

$$
\frac{f_{0}(x \cdot \omega)-\left(f_{0}(x)+1\right)}{x^{n}-1}
$$

> - {cite}`KCL+21` Section 2.2
> - [Anatomy of a STARK, Part 4](https://aszepieniec.github.io/stark-anatomy/stark#arithmetic-intermediate-representation-air)
