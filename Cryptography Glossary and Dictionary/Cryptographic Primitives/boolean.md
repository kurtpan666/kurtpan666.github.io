# Boolean formulae and CNF form

````{prf:definition}

A **Boolean formula** over the variables $u_{1}, \ldots, u_{n}$ consists of the variables and the logical operators AND $(\wedge)$, NOT $(\neg)$ and OR $(\vee)$

**Assignment**: If $\varphi$ is a Boolean formula over variables $u_{1}, \ldots, u_{n}$, and $z \in\{0,1\}^{n}$, then $\varphi(z)$ denotes the value of $\varphi$ when the variables of $\varphi$ are assigned the values $z$ (where we identify 1 with TRUE and 0 with FALSE). 

A formula $\varphi$ is *satisfiable* if there there exists some assignment $z$ such that $\varphi(z)$ is TRUE. Otherwise, we say that $\varphi$ is *unsatisfiable*. 
````



````{prf:definition}

A Boolean formula over variables $u_{1}, \ldots, u_{n}$ is in **CNF form** (Conjunctive Normal Form) if it is an AND of OR's of variables or their negations. 

A CNF formula has the form

$$
\bigwedge_{i}\left(\bigvee_{j} v_{i_{j}}\right)
$$
where each $v_{i_{j}}$ is either a variable $u_{k}$ or to its negation $\neg u_{k}$. 

The terms $v_{i_{j}}$ are called the **literals** of the formula and the terms $\left(\vee_{j} v_{i_{j}}\right)$ are called its **clauses**. 

A $k \mathrm{CNF}$ is a CNF formula in which all clauses contain at most $k$ literals.

Let $\mathrm{SAT}$ be the language of all satisfiable CNF formulae and $\mathrm{3SAT}$ be the language of all satisfiable 3CNF formulae. 
````