from collections.abc import Iterator, Iterable
from typing import TypeVar, Generic, Optional

T = TypeVar("T")


class Peekable(Generic[T], Iterator[T]):
    def __init__(self, iterable: Iterable[T]):
        self.iterable = iter(iterable)
        self.cache: list[T] = list()

    def __iter__(self) -> Iterator[T]:
        return self

    def __next__(self) -> T:
        if self.cache:
            return self.cache.pop()
        return next(self.iterable)

    def peek(self) -> Optional[T]:
        try:
            if self.cache:
                return self.cache[0]
            pop = next(self.iterable)
            self.cache.append(pop)
            return pop
        except StopIteration:
            return None

    def push_back(self, item: T):
        self.cache = [item] + self.cache

    def is_empty(self) -> bool:
        return self.peek() is None
