from cubic_solver.solvers.base import BaseSolver

from ..solutions.identity import IdentitySolution


class IdentitySolver(BaseSolver):
    def __init__(self, d: float) -> None:
        self.d = d

    def solve(self) -> IdentitySolution:
        return IdentitySolution(self.d != 0)
