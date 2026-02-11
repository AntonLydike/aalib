from collections.abc import Sequence
import configparser
from dataclasses import dataclass
import enum
import random
import sys
from enum import Flag, auto, Enum
from typing import ClassVar, overload


COLOR_SUPPORT = hasattr(sys.stdout, "isatty") and sys.stdout.isatty()


class Color:
    code: int | tuple[int, int, int]
    bright: bool = False

    @overload
    def __init__(self, code: int, bright: bool = False):
        pass

    @overload
    def __init__(self, code: tuple[int, int, int]):
        pass

    def __init__(self, code: int | tuple[int, int, int], bright: bool = False):
        self.code = code
        self.bright = bright

    def codes(self, bg: bool) -> tuple[int, ...]:
        if isinstance(self.code, tuple):
            return (48 if bg else 38, 2, *self.code)
        return (self.code + (90 if self.bright else 30) + (10 if bg else 0),)

    def make_bright(self) -> "Color":
        assert isinstance(self.code, int), "Cannot make RGB color bright!"
        return Color(self.code, True)

    BLACK: "Color" = 0  # pyright: ignore[reportAssignmentType]
    RED: "Color" = 1  # pyright: ignore[reportAssignmentType]
    GREEN: "Color" = 2  # pyright: ignore[reportAssignmentType]
    YELLOW: "Color" = 3  # pyright: ignore[reportAssignmentType]
    BLUE: "Color" = 4  # pyright: ignore[reportAssignmentType]
    MAGENTA: "Color" = 5  # pyright: ignore[reportAssignmentType]
    CYAN: "Color" = 6  # pyright: ignore[reportAssignmentType]
    WHITE: "Color" = 7  # pyright: ignore[reportAssignmentType]
    DEFAULT: "Color" = 9  # pyright: ignore[reportAssignmentType]

    _colors: ClassVar[tuple[str, ...]] = (
        "BLACK",
        "RED",
        "GREEN",
        "YELLOW",
        "BLUE",
        "MAGENTA",
        "CYAN",
        "WHITE",
        "",
        "DEFAULT",
    )

    def __str__(self) -> str:
        return f"\033[{';'.join(map(str, self.codes(False)))}m"

    def __repr__(self) -> str:
        if isinstance(self.code, tuple):
            return f"Color(code={self.code})"
        return (
            f"Color(code={self.code}, bright={self.bright}) # {self._colors[self.code]}"
        )

    @classmethod
    def random(cls) -> "Color":
        return Color(random.randint(1, 6), bright=random.random() > 0.5)


for i, name in enumerate(Color._colors):
    if not name:
        continue
    setattr(Color, name, Color(i))


@dataclass
class Format:
    color: Color = Color.DEFAULT
    bg_color: Color = Color.DEFAULT
    reset: bool = False
    bold: bool = False
    italic: bool = False
    underline: bool = False
    reverse: bool = False
    strikethrough: bool = False

    def __str__(self) -> str:
        fmtcodes = []
        for cond, val in [
            (self.reset, 0),
            (self.bold, 1),
            (self.italic, 3),
            (self.underline, 4),
            (self.reverse, 7),
            (self.strikethrough, 9),
        ]:
            if cond:
                fmtcodes.append(val)

        fmtstr = ";".join(
            map(
                str,
                (
                    *fmtcodes,
                    *self.color.codes(False),
                    *self.bg_color.codes(True),
                ),
            )
        )
        return f"\033[{fmtstr}m"

    RESET: "ClassVar[Format]"


Format.RESET = Format(reset=True)
