import pytest

from cubic_solver import main_logger


@pytest.mark.parametrize(
    "a, b, c, d, has_roots, expected_str",
    [
        (0, 0, 0, 0, True, "All real numbers"),
        (0, 0, 0, 1, False, "No real solutions"),
    ],
)
def test_identity(get_solution, a, b, c, d, has_roots, expected_str):
    main_logger.debug(f"Testing {d} = 0: {expected_str}")
    solution = get_solution(a, b, c, d)
    assert solution.has_roots is has_roots
    assert str(solution) == expected_str


@pytest.mark.parametrize(
    "a, b, c, d, expected_roots",
    [
        (0, 0, 1, 0, [0]),
        (0, 0, 1, -1, [1]),
    ],
)
def test_linear(get_solution, a, b, c, d, expected_roots):
    main_logger.debug(f"Testing {c}*x + {d} = 0: {expected_roots}")
    solution = get_solution(a, b, c, d)
    assert solution.roots == expected_roots


@pytest.mark.parametrize(
    "a, b, c, d, expected_roots",
    [
        (0, 1, 0, 0, [0]),
        (0, 1, 0, -1, [-1, 1]),
        (0, 1, -2, 1, [1]),
        (0, 1, 0, 1, []),
    ],
)
def test_quadratic(get_solution, a, b, c, d, expected_roots):
    main_logger.debug(f"Testing {b}*x^2 + {c}*x + {d} = 0: {expected_roots}")
    solution = get_solution(a, b, c, d)
    assert solution.roots == expected_roots


@pytest.mark.parametrize(
    "a, b, c, d, expected_roots",
    [
        (1, 0, 0, 0, [0]),
        (1, 0, 0, -1, [1]),
        (1, 3, 3, 1, [-1]),
        (1, 0, -1, 0, [-1, 0, 1]),
        (1, -6, 11, -6, [1, 2, 3]),
    ],
)
def test_cubic(get_solution, a, b, c, d, expected_roots):
    main_logger.debug(f"Testing {a}*x^3 + {b}*x^2 + {c}*x + {d} = 0: {expected_roots}")
    solution = get_solution(a, b, c, d)
    assert solution.roots == expected_roots
