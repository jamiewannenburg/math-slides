---
author:
- J. J. Wannenburg
institute: 
- 'Institute of Computer Science, Academy of Sciences of the Czech Republic, Czech Republic'
title: 'Epimorphisms in Varieties of Heyting Algebras'
subtitle: 'UJ Workshop'
date: 'January 2019'
titlegraphic: 'images/EUHorisontal.jpg'
thanks: 'This work was carried out within the project *Supporting the internationalization of the Institute of Computer Science of the Czech Academy of Sciences* (no.\ CZ.02.2.69/0.0/0.0/18\_053/0017594), funded by the Operational Programme Research, Development and Education of the Ministry of Education, Youth and Sports of the Czech Republic. The project is co-funded by the EU.'
...

# Test Animation {data-x="1024" data-y="768" data-scale="1"}

![](images/LatticeOperations-animation.svg)

::: notes

Some notes in *markdown*.

:::

---------------------------------

# Environments {data-x="2048" data-y="768" data-scale="1"}


Thm
:    In the join of the six covers of $\overline{\mathbf{C_4}}$ within $\mathsf{M}$, every subquasivariety is a variety.

## Example

$p, p \to q \vdash_{\mathbf{R^t}} q$
:   Suppose that $e \leq p$ and $e \leq p \to q$. By the law of residuation $p \leq q$, then $e \leq q$, by the transitivity of $\leq$.

------------------

# This slide has columns {data-x="2048" data-y="1540" data-scale="1"}

::: columns

:::: column
left
::::

:::: column
right
::::

:::

-------------------

# Using full-slide and columns {.full-slide data-x="4200" data-y="1500" data-scale="1"}

::: columns

:::: column
Recall that the Rieger-Nishimura lattice $\mathbf{RN}$ is the one-generated free Heyting algebra depicted below.
::::

:::: column

::::

:::

![](images/RN.svg)

-------------------


# Disappearing images {.full-slide data-x="4200" data-y="-350" data-scale="1"}



![](images/Xn-1.svg){.disappear}

---------------------------------

# {.full-slide .unselectable data-x="4200" data-y="-350" data-scale="1"}

![](images/Xn-2.svg){.disappear}

---------------------------------

# {.full-slide .unselectable data-x="4200" data-y="-350" data-scale="1"}

![](images/Xn.svg)

---------------------------------


# Fixed image {.full-slide data-x="2050" data-y="5540" data-scale="1"}

::: columns

:::: column
Keeping a 'fixed' floating image and creating space

Let $\mathbf{Y} \in (\mathsf{W}_2)_*$ and $f,g : \mathbf{Y} \rightarrow \mathbf{X}_2^\infty$  *different* Esakia morphisms such that $\langle f(y), g(y) \rangle \in R$ for every $y \in Y$.

One can show that there exists $\bot \in Y$ such that $f(\bot)=\alpha$ and $g(\bot)=\beta$
in some component of $\mathbf{X}_2^\infty$.
::::

:::: column

::::

:::

![](images/X2pinfty-epic-1.svg){.disappear .fixed}

::: notes

Suppose we have two *different* homomorphisms from an Esakia space $\mathbf{Y}$ of width 2 into $X_2^{\infty}$, that agree on the correct partition at every point. One can show that there is an element of $Y$ that get mapped to these positions by $f$ and $g$ in some component of $X_2^{\infty}$. 

:::

---------------------------------

# {.full-slide data-x="2050" data-y="5760" data-scale="1"}

::: columns

:::: column
<div class="space" style="height: 285px"></div>

We may suppose w.l.o.g. that $Y = {\uparrow}\bot$.
::::

:::: column

::::

:::

![](images/X2pinfty-epic-2.svg){.disappear .fixed}

::: notes

We may take $Y = {\uparrow}\bot$.
:::

---------------------------------

# {.full-slide data-x="2050" data-y="5970" data-scale="1"}

::: columns

:::: column
<div class="space" style="height: 150px"></div>

By the Lemma, there is a subposet $Z \subseteq Y$ such that the restriction
$$ f: Z \rightarrow {\uparrow} \alpha \setminus \{\top\} $$
is a poset isomorphism.

We label every element of $Z$ as the 'prime' of its copy under $f$ in $X$.

We can show that for $x' \in Z$
$$g(x') = \max(x/R).$$
::::

:::: column

::::

:::

![](images/X2pinfty-epic-3-animation.svg){.disappear .fixed}

::: notes

By the Lemma, there is a subposet $Z$ of $Y$ that is isomorphically mapped by $f$ onto $\mathbf{X}_n^\infty \setminus \{\top\}$.
We label these elements using primes.

We can prove that $g$ sends every element of this poset to the maximum of its corresponding equivalence class.
:::

---------------------------------

# {.full-slide data-x="2050" data-y="6540" data-scale="1"}

::: columns

:::: column
<div class="space" style="height: 150px"></div>

Since $g(\bot) = \beta \leq c$,
there exists $y \in Y$ such that $g(y) = c$.

Since $c$ is incomparable with $d=g(b')$, we have $y$ incomparable with $b'$.

Then $y$ is comparable with $a'$, since $\mathbf{Y}$ has width $\leq 2$.

But then, $g(y) = c$ is comparable with $g(a') = a$.

From this contradiction it follows that $f = g$.
::::

:::: column

::::

:::

![](images/X2pinfty-epic-4.svg){.disappear .fixed}

::: notes

Since $g$ sends $\bot$ to $\beta$, which is below $c$ there is an element $y$ that gets sent to $c$. Since $c$ is comparable with $d$ in the image, and $g$ is order-presering, $y$ must be incomparable with $b'$. But then $y$ is comparable with $a'$, since $Y$ has width 2. So, the images of $y$ and $a'$ under $g$ (i.e., $a$ and $c$) must be comparable. Which is clearly false from the picture.

Therefore $f=g$.

:::

---------------------------------

# {.full-slide data-x="2050" data-y="6540" data-scale="1"}

![](images/X2pinfty-epic-4.svg)

---------------------------------


# {.unselectable data-x="1024" data-y="768" data-scale="5"}

thank you
