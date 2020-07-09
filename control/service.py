"""Load a service from package."""
from functools import partial
import importlib
import os
import re

from data import Driver


def _load(service):
    """Load valid solver modules into registry."""
    registry = {}

    valid = "[a-z]+(.py)?"
    all_files = filter(partial(re.fullmatch, valid), os.listdir(service))
    for name in all_files:
        name = re.sub(r"\.py", "", name)
        module = importlib.import_module(f".{name}", package=service)
        try:
            registry[name] = getattr(module, service)
        except AttributeError:
            continue
    return registry


class Service:
    """Build a service router for a service package fiven by name."""

    services = {}

    @classmethod
    def load(cls, name):
        """Load service module and return registered service class."""
        importlib.import_module(name)
        return cls.services[name]

    def __init_subclass__(cls, name, default="default"):
        """Register available modules in given service package."""
        cls.services[name] = cls
        cls.name = name
        cls.registry = _load(name)
        cls.default = default

    def __init__(self, name):
        """Instanciate the service with specific module name."""
        if name is None:
            name = self.default
        self.path = f"{self.name}/{name}"

        try:
            self.call = self.registry[name]
        except KeyError:
            raise ValueError(f"No {self.name} service named {name}.")

    def __call__(self, alias):
        """Use service on an instance."""
        print(f"\nrunning on {alias}")
        driver = Driver(alias)
        instance = driver.read()
        return self.call(instance)

    def close(self):
        """Close service with appropriate procedures."""
