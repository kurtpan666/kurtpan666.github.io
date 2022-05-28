# Schwartz-Zippel 引理
Schwartz-Zippel 引理是关于有限域中的多变量多项式零点个数的紧致上界，具体表述如下：

```{admonition} Schwartz-Zippel 引理

对于域$\mathbb{F}$上的每一个阶最多为$d$的$n$变元非零多项式，对于任意有限集合$S \subseteq F$,

$$
\operatorname{Pr}_{r_{1}, \ldots, r_{n} \leftarrow S}\left[f\left(r_{1}, \ldots, r_{n}\right)=0\right] \leq \frac{d}{|S|}
$$
 等价地，$f$在$S^{n}$中最多有 $d|S|^{n-1}$个根，($Z(f)$是$f$的零点集) ：
 
$$
\left|Z(f) \cap S^{n}\right| \leq d \cdot|S|^{n-1}
$$
```

```{note}
Let $\mathbb{F}$ be a finite field and let $f \in \mathbb{F}\left[X_{1}, \ldots, X_{n}\right]$ be a non-zero $n$ variate polynomial with maximum degree $d$. Let $S$ be a subset of $\mathbb{F}$. 
Then $\operatorname{Pr}\left[f\left(x_{1}, \ldots, x_{n}\right)=0\right] \leq d /|S|$, where the probability is taken over the choice of $x_{1}, \ldots, x_{n}$ according to $x_{i} \stackrel{\$}{\leftarrow} d /(p-1)$.

For a univariate polynomial $f \in \mathbb{Z}_{p}[X]$ of degree $d$, where $p$ is prime, let $x \leftarrow \mathbb{Z}_{p}^{*}$, then $\operatorname{Pr}[f(x)=0] \leq$ $d /(p-1)$.
```



## 归纳证明
### 起始步骤
> **代数基本定理**：n = 1时，上述多项式$f$ 最多可以有$d$个根。

#### 代数基本定理的归纳证明

##### 子起始步骤
$d=0$, 则 $f(x)=c_{0}$ ，$c_{0}$为非零常数。 $f(x)$永远非零，自然有0个根。根的个数不超过$d$。
##### 子递推步骤
> 子归纳假设：对整数$k \geq 0$，任意$k$阶多项式至多有$k$个根。

令$f(x)$为$k+1$阶多项式。要说明的是$f(x)$有至多$k+1$个根。

如果$f(x)$没有根，证毕，因为$0 \leq k+1$。

如果 $f(x)$有至少一个根$a$  , 对于$k$阶多项式$h(x)$，可以将$f(x)$写为$f(x)=(x-a) h(x)$。

由子归纳假设，$h(x)$至多有$k$个根。

再加上$x-a$有一个根，则$f(x)=(x-a) h(x)$有至多$k+1$个根。

$\square$

### 递推步骤

````{prf:proof}

重写$f$如下：

$$
f\left(x_{1}, \ldots, x_{n}\right)=\sum_{i=0}^{d} x_{1}^{i} P_{i}\left(x_{2}, \ldots, x_{n}\right)
$$

$f$为非零多项式，所以一定存在$i$使得$P_{i}\ne 0$。 因为 $\mathrm{deg}(x_{1}^{i} P_{i}) \le d$，于是$\mathrm{deg} (P_i) \le d-i$。

> 归纳假设：对$n-1$变元的上述多项式Schwartz-Zippel 引理成立，即：

$$
\operatorname{Pr}\left[P_{i}\left(r_{2}, \ldots, r_{n}\right)=0\right] \leq \frac{d-i}{|S|}
$$

如果$P_{i}\left(r_{2}, \ldots, r_{n}\right) \neq 0$，取最大的$i$，那么$\mathrm{deg} (f\left(x_{1}, r_{2}, \ldots, r_{n}\right))=i$  (即不等于0) ，所以由起始步骤（代数基本定理）：

$$
\operatorname{Pr}\left[f\left(r_{1}, r_{2}, \ldots, r_{n}\right)=0 \mid P_{i}\left(r_{2}, \ldots, r_{n}\right) \neq 0\right] \leq \frac{i}{|S|}
$$


- 事件$A$ : $f\left(r_{1}, r_{2}, \ldots, r_{n}\right)=0$

- 事件$B$：$P_{i}\left(r_{2}, \ldots, r_{n}\right)=0$
- $B$的补事件：$B^c$




$$
\begin{aligned}
\operatorname{Pr}[A] &=\operatorname{Pr}[A \cap B]+\operatorname{Pr}\left[A \cap B^{c}\right] \\
&=\operatorname{Pr}[B] \operatorname{Pr}[A \mid B]+\operatorname{Pr}\left[B^{c}\right] \operatorname{Pr}\left[A \mid B^{c}\right] \\
& \leq \operatorname{Pr}[B]+\operatorname{Pr}\left[A \mid B^{c}\right] \\
& \leq \frac{d-i}{|S|}+\frac{i}{|S|}=\frac{d}{|S|}
\end{aligned}
$$

$\square$
````

## 直接证明

````{prf:proof}
将$f$写为$f=g+h$，$g \not \equiv 0$是$d$阶齐次多项式，$h$包含所有阶严格小于$d$的项。

> 引理： 如果$g$非零且阶 $1 \leq d<|S|$ ，则存在$y \in S^{n}$  使得 $g(y) \neq 0$. 
> 此外，如果$g$是齐次的，则$y \neq \overrightarrow{0}$.

$\mathcal{Proof}$. 假设对于每个$y \in S^n, g(y)=0$。则一定存在$1 \leq i \leq n$ 和 $a_{1}, \ldots, a_{i-1} \in S$ 使得 $g\left(y_{i}, \ldots, y_{n}\right) \doteq f\left(a_{1}, \ldots, a_{i-1}, y_{i}, \ldots, y_{n}\right) \not \equiv 0$, 但对每个 $a \in S$ ，$g\left(a, y_{i+1}, \ldots, y_{m}\right) \equiv 0$. 

注意到$g$的阶最多为$d$。而对于每个$a \in S$, $\left(y_{i}-a\right) \mid g$, 则 $g$ 的阶至少为 $|S|$, 矛盾。 

此外，如果$g$是齐次的，则$g(\overrightarrow{0})=0$. $\square$


由上述引理，令 $y \neq \overrightarrow{0} \in S^n$ 使得 $g(y) \neq 0$。

注意到$S^n$可以被划分为$|S|^{n-1}$条平行**线**。每条线的形式为$\{x+t y \mid t \in S\}$，$x \in S^{n}$

对于每个$x \in S^{n}$，受限多项式$f(x+t y)$是一个以$t$为变元的单变元多项式，阶最多为$d$。

此外，因为$t^{d}$的系数是$g(y)$，则$f(x+t y)$非零！

因此，由代数基本定理，每条线的零点最多$d$个，则$f$在$S^{n}$中的总零点至多$d|S|^{n-1}$个。

$\square$
````

