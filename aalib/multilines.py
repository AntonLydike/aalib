from __future__ import annotations
import shutil
import time
from threading import Lock


class LineOstream:
    line: int
    base: MultilineCtx

    def __init__(self, line: int, base: MultilineCtx):
        self.line = line
        self.base = base

    def write(self, msg: str) -> int:
        for line in msg.split("\n"):
            if line:
                self.base.print(self.line, line)
        return len(msg)

    def flush(self):
        pass


class MultilineCtx:
    """
    Allow printing to multiple lines simultaneously

    if initalized with four lines, they are ID'd like this:

    - line 3 (also line -1)
    - line 2 (also line -2)
    - line 1 (also line -3)
    - line 0 (also line -4)
    """

    def __init__(self, lines: int):
        self.lines = lines
        self.line = 0
        self.lock = Lock()
        print("\n" * (lines - 1), end="")

    def print(self, line: int, msg: str):
        with self.lock:
            if line < 0:
                line = self.lines + line
            if line > self.lines - 1:
                raise IndexError("Line out of range", line, 0, self.lines)

            width = shutil.get_terminal_size((80, 24)).columns

            # figure out how many lines to move:
            move_lines = self.line - line
            if move_lines < 0:
                move = "\033[F" * abs(move_lines)
            elif move_lines == 0:
                move = "\r"
            else:
                move = "\n" * move_lines

            # trim message so it doesn't overflow
            whitespace = ""
            # only fill message if it's printable characters
            if msg.isprintable():
                msg = msg[:width]
                whitespace = " " * (width - len(msg))

            print(f"{move}{msg}{whitespace}", end="", flush=True)
            self.line = line

    def __del__(self):
        print(end="\n" * (self.line + 1))

    def ostream_for(self, line: int) -> LineOstream:
        return LineOstream(line, self)


if __name__ == "__main__":
    import random
    from aalib.progress import progress
    from aalib.colors import FMT

    ctx = MultilineCtx(4)
    for l in range(4):
        ctx.print(l, f"Hello world {l}")
        time.sleep(0.1)

    for l in range(1, 5):
        ctx.print(-l, f"Hello world {-l}")
        time.sleep(0.1)

    bars = [
        progress(range(25), file=ctx.ostream_for(i), color=c, message=f"bar {i}")
        for i, c in enumerate((FMT.BLUE, FMT.MAGENTA, FMT.RED, FMT.YELLOW))
    ]

    elems = list(range(4)) * 25
    random.shuffle(elems)

    for i in elems:
        next(bars[i])
        time.sleep(random.random() * 0.04 + 0.01)
