import math

from cubic_solver.solvers.base import BaseSolver

from ..solutions.regular import Solution


class QuadraticSolver(BaseSolver):
    def __init__(
        self, b: float, c: float, d: float, n_digits: int, display_digits: int = 4
    ) -> None:
        self.b = b
        self.c = c
        self.d = d
        self.n_digits = n_digits
        self.display_digits = display_digits

    def solve(self) -> Solution:
        b, c, d = self.b, self.c, self.d
        discriminant = c**2 - 4 * b * d
        if discriminant < 0:
            return Solution([], self.display_digits)
        if discriminant == 0:
            root = -c / (2 * b)
            return Solution([root], self.display_digits)
        sqrt_disc = math.sqrt(discriminant)
        root1 = (-c + sqrt_disc) / (2 * b)
        root2 = (-c - sqrt_disc) / (2 * b)
        roots = list(set([round(root, self.n_digits) for root in [root1, root2]]))
        return Solution(sorted(roots), self.display_digits)
