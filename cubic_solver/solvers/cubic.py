import cmath
import math

from cubic_solver.solvers.base import BaseSolver

from ..solutions.regular import Solution


def cube_root(x):
    return math.copysign(abs(x) ** (1 / 3), x)


class CubicSolver(BaseSolver):
    def __init__(
        self, a: float, b: float, c: float, d: float, n_digits: int, display_digits: int = 4
    ) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.n_digits = n_digits
        self.display_digits = display_digits

    def solve(self) -> Solution:
        a, b, c, d = self.a, self.b, self.c, self.d
        p = (3 * a * c - b**2) / (3 * a**2)
        q = (2 * b**3 - 9 * a * b * c + 27 * a**2 * d) / (27 * a**3)

        delta = (q / 2) ** 2 + (p / 3) ** 3

        if delta >= 0:
            u = cmath.sqrt(delta)
            A = (-q / 2 + u) ** (1 / 3)
            B = (-q / 2 - u) ** (1 / 3)

            y1 = A + B
            y2 = -1 / 2 * (A + B) + 1j * math.sqrt(3) / 2 * (A - B)
            y3 = -1 / 2 * (A + B) - 1j * math.sqrt(3) / 2 * (A - B)

        else:
            u = cmath.sqrt(delta)
            A = (-q / 2 + u) ** (1 / 3)
            B = (-q / 2 - u) ** (1 / 3)

            y1 = A + B
            y2 = -1 / 2 * (A + B) + 1j * cmath.sqrt(3) / 2 * (A - B)
            y3 = -1 / 2 * (A + B) - 1j * cmath.sqrt(3) / 2 * (A - B)

        x1 = y1 - b / (3 * a)
        x2 = y2 - b / (3 * a)
        x3 = y3 - b / (3 * a)

        roots = list(set([x1, x2, x3]))
        filtered_roots = [round(root.real, self.n_digits) for root in roots if root.imag == 0]

        return Solution(sorted(filtered_roots), n_digits=self.display_digits)
