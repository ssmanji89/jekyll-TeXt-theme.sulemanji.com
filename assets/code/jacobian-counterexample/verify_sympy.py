#!/usr/bin/env python3
"""Independent exact verification with SymPy 1.14.x."""

from fractions import Fraction

import sympy as sp


def main() -> None:
    x, y, z = sp.symbols("x y z")
    u = 1 + x * y
    mapping = sp.Matrix(
        [
            u**3 * z + y**2 * u * (4 + 3 * x * y),
            y + 3 * x * u**2 * z + 3 * x * y**2 * (4 + 3 * x * y),
            2 * x - 3 * x**2 * y - x**3 * z,
        ]
    )

    determinant = sp.cancel(mapping.jacobian((x, y, z)).det())
    assert determinant == -2

    points = (
        (sp.Rational(0), sp.Rational(0), sp.Rational(-1, 4)),
        (sp.Rational(1), sp.Rational(-3, 2), sp.Rational(13, 2)),
        (sp.Rational(-1), sp.Rational(3, 2), sp.Rational(13, 2)),
    )
    expected = sp.Matrix([sp.Rational(-1, 4), 0, 0])
    images = [mapping.subs(dict(zip((x, y, z), point))) for point in points]
    assert all(image == expected for image in images)

    normalized = sp.Matrix(
        [
            mapping[0].subs({y: 2 * y, z: 2 * z}) / 2,
            mapping[1].subs({y: 2 * y, z: 2 * z}) / 2,
            -mapping[2].subs({y: 2 * y, z: 2 * z}) / 2,
        ]
    )
    assert sp.cancel(normalized.jacobian((x, y, z)).det()) == 1
    lean_points = (
        (sp.Rational(1), sp.Rational(-3, 4), sp.Rational(13, 4)),
        (sp.Rational(-1), sp.Rational(3, 4), sp.Rational(13, 4)),
    )
    lean_images = [normalized.subs(dict(zip((x, y, z), point))) for point in lean_points]
    assert lean_images[0] == lean_images[1]

    print(f"PASS SymPy exact determinant: {determinant}")
    for index, (point, image) in enumerate(zip(points, images), start=1):
        rendered = tuple(Fraction(int(v.p), int(v.q)) for v in image)
        print(f"PASS SymPy collision point {index}: F{point} = {rendered}")
    print("PASS SymPy normalized Lean variant: determinant 1 and exact collision")


if __name__ == "__main__":
    main()
