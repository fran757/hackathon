"""Default, empty solver implementation."""

from model import Solution
from tools import chrono


@chrono
def solve(instance):
    """Compute nothing."""
    return Solution()  # todo: implement
