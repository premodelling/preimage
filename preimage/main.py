"""
The main module
"""

import sys
import os


def main():

    # the quadratic function
    print(quadratics.quadratic(x=list(range(-5, 5)), a=1, b=-2, c=3))

    # docstring & help functions
    print(help(quadratics.quadratic_solve))

    # determinants
    values = [quadratics.determinant(a, b, c) for a, b, c in zip([0, 0, 1, 3], [0, 3, 3, 3], [0, 0, 1, 2])]
    print(values)

    # solve
    solutions = [quadratics.quadratic_solve(a, b, c) for a, b, c in zip([5, 1, 1], [1, -4, 1], [-3, 4, 1])]
    print(solutions)

    # strings
    s1 = 'Dog'
    s2 = 'Rin-Tin-Tin'
    print(s1 + ":" + s2)
    print(f"{s1}:{s2}")


if __name__ == '__main__':
    root = os.getcwd()
    sys.path.append(root)

    import preimage.algebra.quadratics

    quadratics = preimage.algebra.quadratics.Quadratics()

    main()
