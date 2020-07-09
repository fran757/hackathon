"""Progress bar utility."""

from dataclasses import dataclass


@dataclass
class Bar:
    """Knowing estimated computation time (can be any unitless arbitrary value),
    update a loading bar on each call given current remaining time.
    """
    total: int
    message: str = "Progress"
    advanced: int = 0

    def advance(self, step):
        """Print simple loading bar, just knowing remaining time estimate."""
        self.advanced += step
        ratio = 100. * self.advanced / self.total
        progress = round(50 * ratio)
        display = "█" * progress + "-" * (50 - progress)
        print(f"{self.message:<10}: |{display}| {ratio:.1f}% Complete", end="\r")

    def __del__(self):
        print()
