import sys
import time
import math
import shutil
from collections.abc import Sequence

from aalib.duration import duration
from aalib.colors import FMT


def simple_progress(
    current: int,
    total: int,
    start_time: float,
    message: str = "",
    color: FMT = FMT.RESET,
    file=sys.stdout,
    max_bar_size: int = 80,
):
    percent = 100 * (current + 1) // total
    elapsed = time.time() - start_time
    avg_time = elapsed / (current + 1)
    remaining = duration(avg_time * (total - current - 1))
    size = math.ceil(math.log10(total))

    term_width = shutil.get_terminal_size((80, 24)).columns

    parts = [
        f"{percent}%",
        f"({current:0{size}}/{total})",
        f"ETA: {remaining}",
        f"({duration(avg_time)}/elem)",
    ]

    if message:
        parts.append(message)

    message_len = lambda: (sum(map(len, parts))) + len(parts) + 1

    while term_width - message_len() - 1 < 2:
        parts = parts[:-1]

    bar_len = min(term_width - message_len() - 1, max_bar_size)

    if bar_len <= 6:
        bar = braille_progress(percent / 100, bar_len)
    else:
        filled_len = int(bar_len * percent // 100)
        bar = (
            "━" * (filled_len - 1)
            + "╸"
            + str(FMT.RESET | FMT.GRAY)
            + "━" * (bar_len - filled_len)
        )

    line = f"{color}{bar}{FMT.RESET} {' '.join(parts)}"
    space = " " * (term_width - len(line))

    print(
        f"\r{line}{space}",
        flush=True,
        end="" if current + 1 != total else "\n",
        file=file,
    )


BRAILLE_INDEX = "⠀⡀⡄⡆⡇⡏⡟⡿⣿"


def braille_progress(percent: float, char_width: int) -> str:
    dots = int(percent * char_width * 8)
    res = []
    while dots >= 8:
        res.append(BRAILLE_INDEX[-1])
        dots -= 8
    while len(res) < char_width:
        res.append(BRAILLE_INDEX[dots])
        dots = 0
    return "".join(res)


def progress(
    seq: Sequence,
    message: str = "",
    color: FMT = FMT.RESET,
    file=sys.stdout,
    max_bar_size: int = 80,
    count: int | None = None,
    sample: int = 1,
):
    a0 = time.time()
    if count is None:
        count = len(seq)
    for i, e in enumerate(seq):
        if i % sample == 0:
            simple_progress(
                i,
                count,
                a0,
                message=message,
                color=color,
                file=file,
                max_bar_size=max_bar_size,
            )
        yield e


if __name__ == "__main__":
    for _ in progress(range(20)):
        time.sleep(0.1)

    time.sleep(0.5)
    for _ in progress(range(100), max_bar_size=6, color=FMT.RED):
        time.sleep(0.01)
