"""Handling of input/output files through aliases.
Parsing method to read an Instance and write/retrieve a Solution.
Driver instanciated for one instance by alias.
Parser (loaded with Driver.load) implements 'next' iterative parsing method.
"""
from model import Instance, Solution
from .driver import DriverBase


# todo: download input files

# todo-dev: single output file description

class Driver(DriverBase):
    """Custom model building methods."""

    def read(self):
        """Read instance from file."""
        reader = self.load("r", "in")
        return Instance()  # todo: implement

    def write(self, solution):
        """Write solution to file."""
        writer = self.load("w", "out")
        # todo: implement

    def retrieve(self):
        """Read solution from file."""
        reader = self.load("r", "out")
        return Solution()  # todo: implement
