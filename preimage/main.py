"""
The main module
"""


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

    # dict
    emily = dictionaries.new_student(name='Emily Bronte')
    print(emily)
    dictionaries.add_grade(record=emily, course='Physics', grade=89)
    dictionaries.add_grade(record=emily, course='Anthropology', grade=91)
    print(emily)


if __name__ == '__main__':

    import preimage.functions.quadratics
    import preimage.functions.dictionaries

    quadratics = preimage.functions.quadratics.Quadratics()
    dictionaries = preimage.functions.dictionaries.Dictionaries()

    main()
