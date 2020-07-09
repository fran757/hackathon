"""File i/o with path completion and type casting.
Specific parsing iteration method for each mode.
"""

class Parser:
    """Base parser with file access and path completion."""

    methods = {}

    def __init__(self, path, mode):
        self.file = open(path, mode)
        self.mode = mode

    def next(self, *args):
        """Handle next line."""
        return self.methods[self.mode](self, *args)

    def close(self):
        """Close file."""
        print("close")
        self.file.close()


def parser(mode):
    """Register function as parsing method for given mode."""
    def wrapper(method):
        Parser.methods[mode] = method
    return wrapper


@parser("r")
def read(self):
    """Read line to list and cast elements to practical types."""
    line = self.file.readline().split()
    for i, value in enumerate(line):
        for cast in [int, float, str]:
            try:
                line[i] = cast(value)
                break
            except ValueError:
                continue
    return line


@parser("w")
def write(self, *args, separator=" "):
    """Write given args to a new line."""
    self.file.write(separator.join(map(str, args)) + "\n")
