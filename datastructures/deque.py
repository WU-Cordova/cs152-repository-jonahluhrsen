import os
from datastructures.iqueue import IQueue
from datastructures.linkedlist import LinkedList
from typing import TypeVar

T = TypeVar('T')

class Deque[T](IQueue[T]):
    """
    A double-ended queue (deque) implementation.
    """

    def __init__(self, data_type: type = object) -> None:
        self.data_type = data_type
        self._list = LinkedList(data_type=data_type)
        
    def enqueue(self, item: T) -> None:
        if not isinstance(item, self.data_type):
            raise TypeError("Item needs to be the same type")
        self._list.append(item = item)
        """
        Adds an item to the back of the deque.

        Args:
            - item (T): The item to add to the back of the deque.

        Raises:
            - TypeError: If the item is not of the correct type.
        """

    def dequeue(self) -> T:
        if self._list.empty:
            raise IndexError("the deque is empty")
        return self._list.pop_front()
        """
        Removes and returns the item from the front of the deque.

        Returns:
            - T: The item removed from the front of the deque.

        Raises:
            - IndexError: If the deque is empty.
        """

    def enqueue_front(self, item: T) -> None:
        if not isinstance(item, self.data_type):
            raise TypeError("item is not of the correct type")
        self._list.prepend(item = item)
        """
        Adds an item to the front of the deque.

        Args:
            - item (T): The item to add to the front of the deque.

        Raises:
            - TypeError: If the item is not of the correct type.
        """

    def dequeue_back(self) -> T:
        if self._list.empty:
            raise IndexError("the deque is empty")
        return self._list.pop()
        """
        Removes and returns the item from the back of the deque.

        Returns:
            - T: The item removed from the back of the deque.

        Raises:
            - IndexError: If the deque is empty.
        """

    def front(self) -> T:
        if self._list.empty:
            raise IndexError("the deque is empty")
        return self._list.front

        """
        Returns the front item of the deque without removing it.

        Returns:
            - T: The front item of the deque.

        Raises:
            - IndexError: If the deque is empty.
        """

    def back(self) -> T:
        if self._list.empty:
            raise IndexError("the deque is empty")
        return self._list.back
        """
        Returns the back item of the deque without removing it.

        Returns:
            - T: The back item of the deque.

        Raises:
            - IndexError: If the deque is empty.
        """
        

    def empty(self) -> bool:
        return self._list.empty
        """
        Checks if the deque is empty.

        Returns:
            - bool: True if the deque is empty, False otherwise.
        """
    
    def __len__(self) -> int:
        return len(self._list)
        """
        Returns the number of items in the deque.

        Returns:
            - int: The number of items in the deque.
        """
    
    def __contains__(self, item: T) -> bool:
        return item in self._list
        """
        Checks if an item exists in the deque.

        Args:
            - item (T): The item to check for existence.

        Returns:
            - bool: True if the item exists in the deque, False otherwise.
        """
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Deque):
            return False
        return self._list == other._list
        """
        Compares two deques for equality.

        Args:
            - other (Deque): The deque to compare with.

        Returns:
            - bool: True if the deques are equal, False otherwise.
        """
    
    def clear(self):
        """
        Clears all items from the deque.
        """
        self._list.clear()

    def __str__(self) -> str:
        """
        Returns a string representation of the deque.

        Returns:
            - str: A string representation of the deque.
        """
        return str(self._list)
    
    def __repr__(self) -> str:
        """
        Returns a detailed string representation of the deque.

        Returns:
            - str: A detailed string representation of the deque.
        """
        return f"Stack items: {str(self)}"


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
