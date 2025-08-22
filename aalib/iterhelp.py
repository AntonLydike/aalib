from collections.abc import Sequence
from typing import Callable, TypeVar

_T = TypeVar("_T")


def split_at(
    oracle: Callable[[_T], bool], seq: Sequence[_T]
) -> tuple[Sequence[_T], Sequence[_T]]:
    """
    Split list into two when oracle turns true (the true element is included in the second list)
    """
    for i, elm in enumerate(seq):
        if oracle(elm):
            return seq[:i], seq[i:]

    return seq, tuple()
