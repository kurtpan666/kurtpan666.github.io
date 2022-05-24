

# Polynomial Interpolation
For a given set of $k + 1$ points $\left(x_{j}, y_{j}\right)$ with no two $x_{j}$ values equal, to find the polynomial of lowest degree that assumes at each value $x_{j}$ the corresponding value $y_{j}$.

## Lagrange interpolation polynomial

$$
L(x):=\sum_{j=0}^{k} y_{j} \ell_{j}(x)
$$

### Lagrange basis polynomials:

$$
\ell_{j}(x):=\prod_{\substack{0 \leq m \leq k \\ m \neq j}} \frac{x-x_{m}}{x_{j}-x_{m}}  \quad ,j\in [0,k]
$$
Note that:

$$
\forall(i \neq j): \ell_{j}\left(x_{i}\right)=0
$$

$$
\ell_{j}\left(x_{j}\right):=1
$$

It follows that $y_{j} \ell_{j}\left(x_{j}\right)=y_{j}$, $L\left(x_{j}\right)=y_{j}$


> - https://en.wikipedia.org/wiki/Lagrange_polynomial
