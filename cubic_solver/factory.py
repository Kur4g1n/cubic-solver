from cubic_solver.solvers.base import BaseSolver

from .solvers import CubicSolver, IdentitySolver, LinearSolver, QuadraticSolver


class SolverFactory:
    @staticmethod
    def create_solver(
        a: float, b: float, c: float, d: float, n_digits: int = 10, display_digits: int = 4
    ) -> BaseSolver:
        if a != 0:
            return CubicSolver(a, b, c, d, n_digits, display_digits)
        elif b != 0:
            return QuadraticSolver(b, c, d, n_digits, display_digits)
        elif c != 0:
            return LinearSolver(c, d, n_digits, display_digits)
        else:
            return IdentitySolver(d)
