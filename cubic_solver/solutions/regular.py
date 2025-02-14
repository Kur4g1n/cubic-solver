from typing import Iterable

from .base import BaseSolution


class Solution(BaseSolution):
    def __init__(self, roots: Iterable[float], n_digits: int):
        self._roots = list(roots)
        self._n_digits = n_digits

    @property
    def roots(self) -> list[float]:
        return self._roots

    @property
    def has_roots(self) -> bool:
        return bool(self._roots)

    @property
    def _roots_repr(self) -> str:
        return ", ".join(f"{root:.{self._n_digits}f}" for root in self._roots)

    def __repr__(self):
        return f"Solution({self._roots_repr})"

    def __str__(self):
        return f"Real solutions: {self._roots_repr}" if self._roots else "No real solutions"
