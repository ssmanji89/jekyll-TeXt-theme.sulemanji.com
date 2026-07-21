---
layout: article
title: "The Jacobian Conjecture Is False in Dimension Three: An Exact Verification Dossier"
date: 2026-07-20 18:30:00 -0500
categories: [mathematics, verification]
tags: [jacobian-conjecture, algebraic-geometry, computer-algebra, lean, reproducibility]
author: Suleman S. Manji
excerpt: "A hand-checkable proof and three independent exact verification paths for the Alpöge/Fable counterexample to the Jacobian conjecture."
meta_description: "Exact independent verification of the Alpöge/Fable three-variable counterexample to the Jacobian conjecture, including a compact determinant proof, rational collision certificate, dependency-free checker, SymPy checker, and Lean cross-check."
description: "Exact independent verification of the Alpöge/Fable counterexample to the Jacobian conjecture."
keywords: "Jacobian conjecture, counterexample, Levent Alpoge, Fable, exact verification, Lean, SymPy"
permalink: "/mathematics/verification/2026/07/20/jacobian-conjecture-counterexample-exact-verification.html"
---

> **Verification status, 20 July 2026:** the two facts needed for the disproof are exact polynomial identities, not numerical evidence. They were independently checked coefficient-by-coefficient without a computer-algebra dependency, checked again in SymPy using rational arithmetic, and cross-checked against a public Lean formalization. The result is extremely new; attribution and conventional publication history are still developing.

## Abstract

Levent Alpöge announced the following polynomial map, crediting Akhil for raising the question and Fable for producing the example:

\[
F=(P,Q,R):\mathbb C^3\longrightarrow\mathbb C^3,
\]

where

\[
\begin{aligned}
P&=(1+xy)^3z+y^2(1+xy)(4+3xy),\\
Q&=y+3x(1+xy)^2z+3xy^2(4+3xy),\\
R&=2x-3x^2y-x^3z.
\end{aligned}
\]

This note supplies a compact exact proof that

\[
\det JF=-2
\]

identically, while three distinct points have the same image. Therefore \(F\) is a polynomial map with nonzero constant Jacobian determinant that is not injective. It has no inverse, polynomial or otherwise, and disproves the Jacobian conjecture in dimension three. Appending identity coordinates gives counterexamples in every dimension \(n\ge 3\). The separate two-variable case is not settled by this construction.

## 1. What must be verified

The Jacobian conjecture says that a polynomial map \(F:\mathbb C^n\to\mathbb C^n\) with nonzero constant Jacobian determinant must have a polynomial inverse. A counterexample therefore needs only two certificates:

1. \(\det JF\) is a nonzero constant everywhere.
2. \(F\) is not injective.

The displayed map supplies both in finite, exact algebra.

## 2. Compact determinant proof

Set

\[
u=1+xy,
\qquad
q=u^2z+y^2(4+3xy).
\]

Then the first two coordinates become

\[
P=uq,
\qquad
Q=y+3xq.
\]

The third coordinate satisfies the polynomial identity

\[
u^2R=x\bigl(u+1-x^2q\bigr).
\]

Indeed, substituting \(xy=u-1\) gives

\[
\begin{aligned}
u+1-x^2q
&=u+1-x^2u^2z-(u-1)^2(1+3u)\\
&=u^2(5-3u-x^2z),
\end{aligned}
\]

and \(R=x(5-3u-x^2z)\).

On the dense open set \(u\ne0\), factor the map through

\[
T(x,y,z)=(x,y,q),
\]

followed by

\[
G(x,y,q)=
\left(
  uq,
  y+3xq,
  \frac{x(u+1-x^2q)}{u^2}
\right).
\]

Because \(\partial q/\partial z=u^2\),

\[
\det JT=u^2.
\]

For \(JG\), multiply its third row by \(u^3\). The resulting matrix is

\[
M=
\begin{pmatrix}
qy & qx & u\\
3q & 1 & 3x\\
2-(u+2)x^2q & x^2(2x^2q-u-2) & -x^3u
\end{pmatrix}.
\]

A direct \(3\times3\) expansion gives the exact factorization

\[
\det M+2u
=-2qx^2(xy+1-u)(3qx^2-u-3)=0,
\]

because \(u=1+xy\). Hence

\[
\det JG=\frac{\det M}{u^3}=-\frac{2}{u^2}.
\]

The chain rule now gives

\[
\det JF=(\det JG)(\det JT)
=\left(-\frac{2}{u^2}\right)u^2=-2
\]

where \(u\ne0\). Since \(\det JF+2\) is a polynomial and vanishes on a Zariski-dense open subset of \(\mathbb C^3\), it vanishes identically. Thus \(\det JF=-2\) everywhere.

The dependency-free verifier linked below proves the same identity directly by sparse-polynomial coefficient comparison, so the conclusion does not depend on the density argument or on trusting the displayed simplification.

## 3. Exact collision certificate

Consider

\[
A=\left(0,0,-\frac14\right),\qquad
B=\left(1,-\frac32,\frac{13}{2}\right),\qquad
C=\left(-1,\frac32,\frac{13}{2}\right).
\]

They are visibly distinct.

At \(A\), \(u=1\) and \(q=-1/4\), so

\[
F(A)=\left(-\frac14,0,0\right).
\]

At both \(B\) and \(C\), \(xy=-3/2\), so \(u=-1/2\), and

\[
q=\frac14\cdot\frac{13}{2}
 +\frac94\left(4-\frac92\right)
=\frac{13}{8}-\frac98
=\frac12.
\]

Therefore

\[
P=uq=-\frac14.
\]

For \(B\),

\[
Q=-\frac32+3\cdot1\cdot\frac12=0,
\qquad
R=2+\frac92-\frac{13}{2}=0.
\]

For \(C\),

\[
Q=\frac32+3\cdot(-1)\cdot\frac12=0,
\qquad
R=-2-\frac92+\frac{13}{2}=0.
\]

Consequently,

\[
F(A)=F(B)=F(C)=\left(-\frac14,0,0\right).
\]

Thus \(F\) is not injective.

## 4. Logical conclusion

The map \(F\) is polynomial and has the nonzero constant Jacobian determinant \(-2\), so it satisfies the hypothesis of the Jacobian conjecture. The explicit collision proves that \(F\) has no set-theoretic inverse, and therefore no polynomial inverse. Hence the Jacobian conjecture is false in dimension three.

For every \(n>3\), the map

\[
(x_1,x_2,x_3,x_4,\ldots,x_n)
\longmapsto
\bigl(F(x_1,x_2,x_3),x_4,\ldots,x_n\bigr)
\]

has the same nonzero constant determinant and the same collision. Therefore the conjecture is false for all \(n\ge3\).

## 5. Independent exact verification

The verification bundle deliberately uses different trust paths. Humanity has produced enough famous false proofs to justify being impolite to every unchecked algebraic miracle.

| Path | Arithmetic | What it checks |
|---|---|---|
| `verify_exact.py` | Custom sparse polynomials over `fractions.Fraction`; no third-party packages | Full coefficient identity \(\det JF=-2\), all three collision points, normalized Lean variant |
| `verify_sympy.py` | SymPy 1.14.0 exact symbolic and rational arithmetic | Independent determinant expansion, compact hand-proof factorization, collisions, normalization relation |
| Public Lean formalization | Lean kernel checking in Google DeepMind's `formal-conjectures` repository | A determinant-one normalized variant, exact collision, and the formal theorem that the conjecture is false over characteristic-zero fields |

Run locally from a clone of this repository:

```bash
cd assets/code/jacobian-counterexample
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
bash run_verification.sh
sha256sum -c SHA256SUMS
```

Published artifacts:

- [`verify_exact.py`](/assets/code/jacobian-counterexample/verify_exact.py)
- [`verify_sympy.py`](/assets/code/jacobian-counterexample/verify_sympy.py)
- [`run_verification.sh`](/assets/code/jacobian-counterexample/run_verification.sh)
- [`requirements.txt`](/assets/code/jacobian-counterexample/requirements.txt)
- [`VERIFICATION-OUTPUT.txt`](/assets/code/jacobian-counterexample/VERIFICATION-OUTPUT.txt)
- [`SHA256SUMS`](/assets/code/jacobian-counterexample/SHA256SUMS)

## 6. Relation to the Lean formalization

The public Lean development uses the normalized map

\[
L(X,Y,Z)=\frac12\Bigl(
P(X,2Y,2Z),
Q(X,2Y,2Z),
-R(X,2Y,2Z)
\Bigr).
\]

The input scaling has determinant \(4\), the output scaling has determinant \(-1/8\), and \(\det JF=-2\). Therefore

\[
\det JL=(-1/8)(-2)(4)=1.
\]

The original collision points become

\[
\left(1,-\frac34,\frac{13}{4}\right),
\qquad
\left(-1,\frac34,\frac{13}{4}\right),
\]

which are exactly the points used by the Lean proof. At the time of this verification, the formalization is an open pull request, not a merged publication. Its decisive theorem is proved without `sorry`; a separate statement about the still-open two-variable case intentionally remains unfinished.

## 7. Provenance and scope

- **Discovery announcement:** Levent Alpöge's public post of 19/20 July 2026, crediting Akhil and Fable.
- **Formalization:** Paul Lezeau, Google DeepMind `formal-conjectures` pull request **#4474**, head commit `00d769cd534669143a50269a3a373cec8bb37015` at the time checked.
- **This publication:** independent reproduction, compact determinant derivation, normalization cross-check, and reproducible verification bundle. It makes no discovery-priority claim.

Primary links:

- [Original announcement](https://x.com/__alpoge__/status/2079028340955197566)
- [Lean formalization PR #4474](https://github.com/google-deepmind/formal-conjectures/pull/4474)
- [MathOverflow community record](https://mathoverflow.net/questions/130777/could-the-jacobian-conjecture-be-undecidable/486468)
- [Wolfram MathWorld entry](https://mathworld.wolfram.com/JacobianConjecture.html)

## Reproducibility record

The included output transcript was generated with:

```text
Python 3.13.5
SymPy 1.14.0
```

Both checkers completed successfully. File digests are recorded in `SHA256SUMS`. No randomized test, floating-point comparison, network call, or GitHub Actions workflow is part of the proof.
