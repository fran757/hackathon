"""Compute solution from instance, report gains and upload results."""

from control import Service, upload
from data import Driver
import model
from tools import report


class Solve(Service, name=__name__):
    """Solver service."""
    def __init__(self, name):
        super().__init__(name)
        self.solutions = {}
        self.gains = {}

    def __call__(self, alias):
        print(f"Solving instance {alias}")
        driver = Driver(alias)
        instance = driver.read()
        solution = self.call(instance)

        score = model.score(instance, solution)
        try:
            old_score = model.score(instance, driver.retrieve())
        except FileNotFoundError:
            old_score = 0

        if (delta := score - old_score) > 0:
            driver.write(solution)
        self.gains[alias] = score, delta

    def close(self):
        """Prepare upload package and report gains."""
        upload(self.path, self.gains.keys())
        message = "{key:<30}: score {value[0]:<10}, gain {value[1]}"
        report("Gains", self.gains, message)
