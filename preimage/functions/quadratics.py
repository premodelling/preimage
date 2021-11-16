import math


class Quadratics:

    def __init__(self):
        """

        """

    @staticmethod
    def quadratic(x: list, a: float, b: float, c: float) -> list:
        """
        The quadratic equation

        :param x: the values of variable x
        :param a: the coefficient of x^2
        :param b: the coefficient of x
        :param c: the constant
        :return:
        """

        y = [a * (i ** 2) + (b * i) + c for i in x]

        return y

    @staticmethod
    def determinant(a: float, b: float, c: float) -> float:
        """
        The determinant, i.e., b^2 - 4ac

        :param a: the coefficient of x^2
        :param b: the coefficient of x
        :param c: the constant
        :return:
        """

        return (b ** 2) - (4 * a * c)

    def quadratic_solve(self, a: float, b: float, c: float):
        """

        The quadratic solver

        :param a: the coefficient of x^2
        :param b: the coefficient of x
        :param c: the constant
        :return:
        """

        quotient = -b/(2 * a)

        det = self.determinant(a=a, b=b, c=c)

        if det < 0:
            return []
        elif det == 0:
            return [quotient]
        else:
            difference = math.sqrt(det) / (2 * a)
            return [quotient - difference, quotient + difference]
