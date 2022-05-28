# RSA-based Encryption

## RSA assumption

````{prf:definition} The RSA problem
:nonumber: true
Given a modulus $N$ and an integer $e>2$ relatively prime to $\phi(N)$, to compute $\left[y^{1 / e} \bmod N\right]$ for a modulus $N$ of unknown factorization.
````

````{prf:algorithm} RSA key generation GenRSA
:nonumber: true
**Input**: Security parameter $1^{n}$

**Output**: $N, e, d$ 

$(N, p, q) \leftarrow$ GenModulus $\left(1^{n}\right)$

$\phi(N):=(p-1)(q-1)$

**choose** $e>1$ such that $\operatorname{gcd}(e, \phi(N))=1$

**compute** $d:=\left[e^{-1} \bmod \phi(N)\right]$ 

**return** $N,e, d$
````

````{prf:definition} The RSA experiment
:nonumber: true
RSA-inv$_{\mathcal{A}, \operatorname{GenRSA}}(n)$ :
1. Run $\operatorname{GenRSA}\left(1^{n}\right)$ to obtain $(N, e, d)$.
2. Choose a uniform $y \in \mathbb{Z}_{N}^{*}$.
3. $\mathcal{A}$ is given $N, e, y$, and outputs $x \in \mathbb{Z}_{N}^{*}$.
4. The output of the experiment is defined to be 1 if $x^{e}=y \bmod N$, and 0 otherwise.
````

````{prf:definition} The RSA problem is hard
:nonumber: true
The RSA problem is hard relative to $\mathrm{GenRSA}$ if for all probabilistic polynomial-time algorithms $\mathcal{A}$ there exists a negligible function $\mathrm{negl}$ such that $\mathrm{Pr}[$ RSA-inv$_{\mathcal{A}, \operatorname{GenRSA}}(n)=1] \le \mathrm{negl}$.
````

````{prf:definition} The RSA assumption 
:nonumber: true
There exists a $\mathrm{GenRSA}$ algorithm relative to which the RSA problem is hard. 
````

## Plain RSA Encryption

````{prf:algorithm} The plain RSA encryption scheme 
:nonumber: true
- Gen: on input $1^{n}$ run GenRSA $\left(1^{n}\right)$ to obtain $N, e$, and $d$. The public key is $\langle N, e\rangle$ and the private key is $\langle N, d\rangle$.
- Enc: on input a public key $p k=\langle N, e\rangle$ and a message $m \in \mathbb{Z}_{N}^{*}$, compute the ciphertext

$$
c:=\left[m^{e} \bmod N\right] .
$$
- Dec: on input a private key $s k=\langle N, d\rangle$ and a ciphertext $c \in \mathbb{Z}_{N}^{*}$, compute the message

$$
m:=\left[c^{d} \bmod N\right] \text {. }
$$
````

## Padded RSA and PKCS #1 v1.5

````{prf:algorithm} The padded RSA encryption scheme
:nonumber: true

- Enc: on input a public key $p k=\langle N, e\rangle$ and a message $m \in\{0,1\}^{\|N\|-\ell(n)-1}$, choose a uniform string $r \in\{0,1\}^{\ell(n)}$ and interpret $\hat{m}:=r \| m$ as an element of $\mathbb{Z}_{N}^{*}$. Output the ciphertext

$$
c:=\left[\hat{m}^{e} \bmod N\right] .
$$
- Dec: on input a private key $s k=\langle N, d\rangle$ and a ciphertext $c \in \mathbb{Z}_{N}^{*}$, compute

$$
\hat{m}:=\left[c^{d} \bmod N\right],
$$

and output the $\|N\|-\ell(n)-1$ least-significant bits of $\hat{m}$.
````

let $k$ denote the length of $N$ in bytes; i.e., $k$ is the integer satisfying $2^{8(k-1)} \leq N<2^{8 k}$. 

Messages $m$ to be encrypted are assumed to have length an integer number of bytes ranging from one to $k-11$. 

````{prf:algorithm} RSA PKCS #1 v1.5
:nonumber: true
Encryption of a $D$-byte message $m$ is computed as: 
`(0x00||0x02||r||0x00||m)` $^e \bmod N$

where $r$ is a randomly generated, $(k-D-3)$-byte string with none of its bytes equal to `0x00`.
````

## OAEP and PKCS #1 v2

````{prf:algorithm} The RSA-OAEP encryption scheme
:nonumber: true

- Enc: on input a public key $\langle N, e\rangle$ and a message $m \in\{0,1\}^{\ell}$, set $m^{\prime}:=m \| 0^{k}$ and choose a uniform $r \in\{0,1\}^{k}$. Then compute

$$
t:=m^{\prime} \oplus G(r), \quad s:=r \oplus H(t)
$$
and set $\hat{m}:=s \| t$. Output the ciphertext $c:=\left[\hat{m}^{e} \bmod N\right]$.
- Dec: on input a private key $\langle N, d\rangle$ and a ciphertext $c \in \mathbb{Z}_{N}^{*}$, 
    - compute $\hat{m}:=\left[c^{d} \bmod N\right]$. If $\|\hat{m}\|>\ell+2 k$, output $\perp$. Otherwise, parse $\hat{m}$ as $s \| t$ with $s \in\{0,1\}^{\ell+k}$ and $t \in\{0,1\}^{k}$. 
    - Compute $r:=H(t) \oplus s$ and $m^{\prime}:=G(r) \oplus t$. 
    - If the $k$ least-significant bits of $m^{\prime}$ are not all 0 , output $\perp$. Otherwise, output the $\ell$ most-significant bits of $m^{\prime}$.
````

