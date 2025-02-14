from abc import ABCMeta, abstractmethod
from collections.abc import Iterable


class BaseSolution(metaclass=ABCMeta):
    @property
    @abstractmethod
    def roots(self) -> Iterable[float]: ...

    @property
    @abstractmethod
    def has_roots(self) -> bool: ...

    @abstractmethod
    def __str__(self) -> str: ...

    @abstractmethod
    def __repr__(self) -> str: ...
