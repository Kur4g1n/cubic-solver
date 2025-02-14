from .base import BaseSolution


class IdentitySolution(BaseSolution):
    def __init__(self, no_roots: bool = False) -> None:
        self._no_roots = no_roots

    @property
    def has_roots(self) -> bool:
        return not self._no_roots

    @property
    def roots(self) -> list[float]:
        return []

    def __repr__(self):
        return "IdentitySolution()"

    def __str__(self):
        return "No real solutions" if self._no_roots else "All real numbers"
