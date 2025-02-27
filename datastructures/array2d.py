from __future__ import annotations
import os
from typing import Iterator, Sequence
from datastructures.iarray import IArray
from datastructures.array import Array
from datastructures.iarray2d import IArray2D, T
from copy import copy

#finished 

class Array2D(IArray2D[T]):

    class Row(IArray2D.IRow[T]):
        def __init__(self, row_index: int, array: IArray, num_columns: int, data_type: type) -> None:
            self.row_index = row_index
            self.array = array
            self.num_cols = num_columns
            self.data_type = data_type
            
        def map_index(self, row_index: int, column_index: int) -> int:
            return row_index * self.num_cols + column_index

        def __getitem__(self, column_index: int) -> T:
            if column_index < 0 or column_index >= self.num_cols:
                raise IndexError("The index is out of bounds")
            index = self.map_index(self.row_index, column_index)
            return self.array[index]
            
        def __setitem__(self, column_index: int, value: T) -> None:
            index = self.map_index(self.row_index, column_index)
            self.array[index] = value
        
        def __iter__(self) -> Iterator[T]:
            yield from (self[i] for i in range(self.num_cols))

        def __reversed__(self) -> Iterator[T]:
            yield from (self[i] for i in reversed(range(self.num_cols)))

        def __len__(self) -> int:
            return self.num_cols
        
        def __str__(self) -> str:
            return f"[{', '.join([str(self[column_index]) for column_index in range(self.num_cols)])}]"
        
        def __repr__(self) -> str:
            return f'Row {self.row_index}: [{", ".join([str(self[column_index]) for column_index in range(self.num_cols - 1)])}, {str(self[self.num_cols - 1])}]'

    def __init__(self, starting_sequence: Sequence[Sequence[T]]=[[]], data_type=object) -> None:
        if not isinstance(starting_sequence, Sequence) or isinstance(starting_sequence, str):
            raise ValueError("starting_sequence needs to be a valid sequence type.")
        if not isinstance (starting_sequence[0], Sequence):
            raise ValueError("This need to pass in same data types")
        for i in range(len(starting_sequence)):
            for j in range(len(starting_sequence[i])):
                if not isinstance(starting_sequence[i][j], data_type):
                    raise ValueError("This needs to be the same type")
        self.__row_len = len(starting_sequence)
        self.__col_len = len(starting_sequence[0])
        for i in range(self.__row_len):
            if len(starting_sequence[i]) != self.__col_len:
                raise ValueError("This needs to be same length")
        self.data_type = data_type
        self.__array2d = Array([data_type() for item in range(self.__row_len * self.__col_len)], data_type = data_type)
        index = 0
        for row_index in range(self.__row_len):
            for column_index in range(self.__col_len):
                self.__array2d[index] = starting_sequence[row_index][column_index]
                index += 1

    @staticmethod
    def empty(rows: int = 0, cols: int = 0, data_type: type = object) -> Array2D:
        starting_sequence = [[data_type() for _ in range(cols)] for _ in range(rows)]
        return Array2D(starting_sequence=starting_sequence, data_type=data_type)

    def __getitem__(self, row_index: int) -> Array2D.IRow[T]:
        if row_index < 0 or row_index >= self.__row_len:
            raise IndexError("The index is out of bounds")
        return Array2D.Row(row_index, self.__array2d, self.__col_len, self.data_type)
    
    def __iter__(self) -> Iterator[Sequence[T]]: 
        for row_index in range(self.__row_len):
                yield self[row_index]
    
    def __reversed__(self):
        for row_index in range(self.__row_len -1, -1,-1):
                yield self[row_index]
    
    def __len__(self): 
        return self.__row_len
                                  
    def __str__(self) -> str: 
        return f'[{", ".join(f"{str(row)}" for row in self)}]'
    
    def __repr__(self) -> str: 
        return f'Array2D {self.__row_len} Rows x {self.__col_len} Columns, items: {str(self)}'

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')