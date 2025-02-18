import sys
from argparse import ArgumentParser
from importlib.metadata import metadata
from typing import NoReturn


class SolverArguementParser(ArgumentParser):
    PACKAGE_NAME = "cubic-solver"

    def __init__(self, **kwargs) -> None:
        # Setting custom package name in cli
        if "__main__" in sys.modules:
            meta = metadata(sys.modules["__main__"].__package__ or self.PACKAGE_NAME)
            kwargs.setdefault("prog", meta["Name"])
        super().__init__(**kwargs)

    def error(self, message: str) -> NoReturn:
        self.exit(22, f"Incorrect input arguements: {message}\n")
