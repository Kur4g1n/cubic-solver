from cubic_solver.solvers.base import BaseSolver

from ..solutions.regular import Solution


class LinearSolver(BaseSolver):
    def __init__(self, c: float, d: float, n_digits: int, display_digits: int = 4) -> None:
        self.c = c
        self.d = d
        self.n_digits = n_digits
        self.display_digits = display_digits

    def solve(self) -> Solution:
        return Solution([round(-self.d / self.c, self.n_digits)], self.display_digits)
