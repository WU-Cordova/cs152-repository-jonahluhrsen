from typing import Iterable, Optional
from datastructures.ibag import IBag, T


class Bag(IBag[T]):
    def __init__(self, *items: Optional[Iterable[T]]) -> None:
        self._bag: dict[T, int] = {}
        #raise NotImplementedError("__init__ method not implemented")
        if items is not None:
            for item in items:
                self.add[item]
        else:
            raise TypeError("Item Cannot Be Added To Bag")

    def add(self, item: T) -> None:
        if item is None: raise TypeError("Item Cannot Be None")
        if item in self._bag:
            self._bag[item] += 1
        else: 
            self._bag[item] = 1

    def remove(self, item: T) -> None:
        if item not in self._bag:
            raise ValueError("Item is not in the bag")
        else:
            if self._bag[item] > 1:
                self._bag[item] -= 1
            else:
                del self._bag[item]

    def count(self, item: T) -> int:
        return self._bag.get(item, 0)

    def __len__(self) -> int:
        return sum(self._bag.values())

    def distinct_items(self) -> Iterable[T]:
        return self._bag.keys()

    def __contains__(self, item) -> bool:
        return item in self._bag

    def clear(self) -> None:
        self._bag.clear()