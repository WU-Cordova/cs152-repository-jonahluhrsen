import os
from datastructures.istack import IStack
from typing import Generic

from datastructures.linkedlist import LinkedList, T

class ListStack(Generic[T], IStack[T]):
    """
    ListStack (LinkedList-based Stack)

    """

    def __init__(self, data_type:object) -> None:
        self.data_type = data_type
        self._list = LinkedList(data_type=data_type)

    def push(self, item: T):
        if not isinstance(item, self.data_type):
            raise TypeError("the item is not of the correct type")
        self._list.append(item = item)
        """
        Pushes an item onto the stack.

        Args:
            item (T): The item to push onto the stack.
        
        Raises:
            TypeError: If the item is not of the correct type.

        """

    def pop(self) -> T:
        if self._list.empty:
            raise IndexError("the stack is empty")
        return self._list.pop()


    def peek(self) -> T:
        if self._list.empty:
            raise IndexError("the stack is empty")
        return self._list.back
    
        """
        Returns the top item from the stack without removing it.

        Returns:
            T: The top item from the stack.
        
        Raises:
            IndexError: If the stack is empty.
        """

    @property
    def empty(self) -> bool:
        return self._list.empty

    def clear(self):
        self._list.clear()
        """
        Clears all items from the stack.
        """

    def __contains__(self, item: T) -> bool:

        return item in self._list
        """
        Checks if an item exists in the stack.

        Args:
            item (T): The item to check for.

        Returns:
            bool: True if the item exists in the stack, False otherwise.

        """

    def __eq__(self, other) -> bool:
        if not isinstance(other, ListStack):
            return False
        return self._list == other._list
        """
        Compares two stacks for equality.

        Args:
            other (ListStack): The stack to compare with.

        Returns:
            bool: True if the stacks are equal, False otherwise.

        """
        

    def __len__(self) -> int:
        return len(self._list)
        """
        Returns the number of items in the stack.

        Returns:
            int: The number of items in the stack.
        """

    def __str__(self) -> str:
        return str(self._list)
        """
        Returns a string representation of the stack.

        Returns:
            str: A string representation of the stack.
        """
       

    def __repr__(self) -> str:
        return f"Stack items: {str(self)}"
        """
        Returns a detailed string representation of the stack.

        Returns:
            str: A detailed string representation of the stack.

        """
    

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
