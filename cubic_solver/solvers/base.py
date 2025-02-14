from abc import ABCMeta, abstractmethod

from cubic_solver.solutions.base import BaseSolution


class BaseSolver(metaclass=ABCMeta):
    @abstractmethod
    def solve(self) -> BaseSolution:
        pass
