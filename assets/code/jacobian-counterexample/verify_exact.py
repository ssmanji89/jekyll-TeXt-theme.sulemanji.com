#!/usr/bin/env python3
"""Dependency-free exact verification of the Alpöge/Fable counterexample.

This script implements sparse multivariate polynomials over the rational
numbers. It proves, by coefficient comparison, that the Jacobian determinant
is the constant -2 and checks the announced three-point collision exactly.
No floating-point arithmetic or computer-algebra package is used.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Dict, Iterable, Mapping, Tuple

Monomial = Tuple[int, int, int]
Coefficients = Dict[Monomial, Fraction]


@dataclass(frozen=True)
class Poly:
    terms: Mapping[Monomial, Fraction]

    def __post_init__(self) -> None:
        cleaned = {m: Fraction(c) for m, c in self.terms.items() if c != 0}
        object.__setattr__(self, "terms", cleaned)

    @staticmethod
    def constant(value: int | Fraction) -> "Poly":
        value = Fraction(value)
        return Poly({(0, 0, 0): value}) if value else Poly({})

    @staticmethod
    def variable(axis: int) -> "Poly":
        exponent = [0, 0, 0]
        exponent[axis] = 1
        return Poly({tuple(exponent): Fraction(1)})

    def __add__(self, other: int | Fraction | "Poly") -> "Poly":
        other = as_poly(other)
        result: Coefficients = dict(self.terms)
        for monomial, coefficient in other.terms.items():
            result[monomial] = result.get(monomial, Fraction(0)) + coefficient
        return Poly(result)

    __radd__ = __add__

    def __neg__(self) -> "Poly":
        return Poly({m: -c for m, c in self.terms.items()})

    def __sub__(self, other: int | Fraction | "Poly") -> "Poly":
        return self + (-as_poly(other))

    def __rsub__(self, other: int | Fraction | "Poly") -> "Poly":
        return as_poly(other) - self

    def __mul__(self, other: int | Fraction | "Poly") -> "Poly":
        other = as_poly(other)
        result: Coefficients = {}
        for left_monomial, left_coefficient in self.terms.items():
            for right_monomial, right_coefficient in other.terms.items():
                monomial = tuple(a + b for a, b in zip(left_monomial, right_monomial))
                result[monomial] = (
                    result.get(monomial, Fraction(0))
                    + left_coefficient * right_coefficient
                )
        return Poly(result)

    __rmul__ = __mul__

    def __pow__(self, exponent: int) -> "Poly":
        if exponent < 0:
            raise ValueError("polynomial exponents must be nonnegative")
        result = Poly.constant(1)
        base = self
        power = exponent
        while power:
            if power & 1:
                result = result * base
            base = base * base
            power >>= 1
        return result

    def derivative(self, axis: int) -> "Poly":
        result: Coefficients = {}
        for monomial, coefficient in self.terms.items():
            exponent = monomial[axis]
            if exponent:
                derived = list(monomial)
                derived[axis] -= 1
                result[tuple(derived)] = coefficient * exponent
        return Poly(result)

    def evaluate(self, point: Tuple[Fraction, Fraction, Fraction]) -> Fraction:
        total = Fraction(0)
        for monomial, coefficient in self.terms.items():
            term = coefficient
            for coordinate, exponent in zip(point, monomial):
                term *= coordinate**exponent
            total += term
        return total

    def is_constant(self, value: int | Fraction) -> bool:
        return self == Poly.constant(value)


def as_poly(value: int | Fraction | Poly) -> Poly:
    return value if isinstance(value, Poly) else Poly.constant(value)


def determinant_3x3(matrix: Tuple[Tuple[Poly, Poly, Poly], ...]) -> Poly:
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def jacobian(polynomials: Iterable[Poly]) -> Tuple[Tuple[Poly, Poly, Poly], ...]:
    return tuple(tuple(poly.derivative(axis) for axis in range(3)) for poly in polynomials)


def main() -> None:
    x = Poly.variable(0)
    y = Poly.variable(1)
    z = Poly.variable(2)
    u = 1 + x * y

    p = u**3 * z + y**2 * u * (4 + 3 * x * y)
    q = y + 3 * x * u**2 * z + 3 * x * y**2 * (4 + 3 * x * y)
    r = 2 * x - 3 * x**2 * y - x**3 * z
    mapping = (p, q, r)

    determinant = determinant_3x3(jacobian(mapping))
    assert determinant.is_constant(-2), determinant.terms

    points = (
        (Fraction(0), Fraction(0), Fraction(-1, 4)),
        (Fraction(1), Fraction(-3, 2), Fraction(13, 2)),
        (Fraction(-1), Fraction(3, 2), Fraction(13, 2)),
    )
    expected = (Fraction(-1, 4), Fraction(0), Fraction(0))
    images = tuple(tuple(poly.evaluate(point) for poly in mapping) for point in points)
    assert all(image == expected for image in images), images
    assert len(set(points)) == 3

    # The map used by the public Lean formalization is the exact normalization
    # L(X,Y,Z) = (P(X,2Y,2Z), Q(X,2Y,2Z), -R(X,2Y,2Z)) / 2.
    u_lean = 1 + 2 * x * y
    p_lean = u_lean**3 * z + 4 * y**2 * u_lean * (2 + 3 * x * y)
    q_lean = y + 3 * x * u_lean**2 * z + 12 * x * y**2 * (2 + 3 * x * y)
    r_lean = -x + 3 * x**2 * y + x**3 * z
    lean_mapping = (p_lean, q_lean, r_lean)
    lean_determinant = determinant_3x3(jacobian(lean_mapping))
    assert lean_determinant.is_constant(1), lean_determinant.terms
    lean_points = (
        (Fraction(1), Fraction(-3, 4), Fraction(13, 4)),
        (Fraction(-1), Fraction(3, 4), Fraction(13, 4)),
    )
    lean_images = tuple(
        tuple(poly.evaluate(point) for poly in lean_mapping) for point in lean_points
    )
    assert lean_images[0] == lean_images[1]

    print("PASS exact sparse-polynomial identity: det(JF) == -2")
    for index, (point, image) in enumerate(zip(points, images), start=1):
        print(f"PASS collision point {index}: F{point} = {image}")
    print("PASS normalized Lean variant: det(JL) == 1 and its two points collide")
    print("PASS conclusion: F is polynomial, everywhere étale, and not injective")


if __name__ == "__main__":
    main()
