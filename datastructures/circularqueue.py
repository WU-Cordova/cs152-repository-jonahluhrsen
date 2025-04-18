from typing import Any

from datastructures.array import Array
from datastructures.iqueue import IQueue, T

class CircularQueue(IQueue[T]):

    def __init__(self, maxsize: int = 0, data_type=object) -> None:
       
        starting_sequence = [data_type() for _ in range(maxsize + 1)]
        self.circularqueue = Array(starting_sequence=starting_sequence, data_type=data_type)
        self._front = 0
        self._rear = 0

    def enqueue(self, item: T) -> None:
        if self.full:
            raise IndexError
        self.circularqueue[self._rear] = item
        self._rear = (self._rear + 1) % len(self.circularqueue)

    def dequeue(self) -> T:
        if self.empty:
            raise IndexError
        item = self.circularqueue[self._front]
        self._front = (self._front + 1) % len(self.circularqueue)
        return item

    def clear(self) -> None:
        self.circularqueue = Array(len(self.circularqueue))
        self._front = 0
        self._rear = 0

    @property
    def front(self) -> T:
        if self.empty:
            raise IndexError
        return self.circularqueue[self._front]

    @property
    def full(self) -> bool:
        return (self._rear + 1) % len(self.circularqueue) == self._front

    @property
    def empty(self) -> bool:
        return self._front == self._rear

    @property
    def maxsize(self) -> int:
        return len(self.circularqueue) - 1

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, CircularQueue):
            return False
        for item in range(len(self)):
            if self.circularqueue[(self._front + item) % len(self)] != other.circularqueue[(other._front + item) % len(other)]:
                return False
        return True

    def __len__(self) -> int:
        return  (self._rear - self._front + len(self.circularqueue)) % len(self.circularqueue)

    def __str__(self) -> str:
        return str(self.circularqueue)

    def __repr__(self) -> str:
        return f'ArrayQueue({repr(self.circularqueue)})'