import pytest

from cubic_solver.factory import SolverFactory


@pytest.fixture(scope="module")
def factory():
    return SolverFactory()


@pytest.fixture(scope="module")
def get_solution(factory: SolverFactory):
    def wrapper(a: float, b: float, c: float, d: float, n: int = 10, display_digits: int = 4):
        solver = factory.create_solver(a, b, c, d, n, display_digits)
        return solver.solve()

    return wrapper
