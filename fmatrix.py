from __future__ import annotations

import sys
import numpy as np
from typing import Iterable, List, Set, Tuple, Generic, TypeVar

T = TypeVar("T")

def random_matrix(max:int = 255, dtype = np.uint8, size:int=4) -> List[List]:
    return [list(r) for r in np.random.randint(max,size=(size,size), dtype=dtype)]

def is_square_matrix(matrix:Iterable[Iterable[T]]) -> bool:
    output = True
    for row in matrix:
        output &= len(matrix) == len(row)
    return output

def flatten(s:Iterable[Iterable[T]]) -> Iterable[T]:
    output = []
    for row in s:
        for x in row:
            output.append(x)
    return output

def sizeof_list_matrix(s:List[List[T]]) -> int:
    return sum([sys.getsizeof(r) for r in s] + [sys.getsizeof(s)])

class InvalidMatrix(Exception):
        pass

class Matrix(Generic[T]):
    def __init__(self, matrix:Iterable[Iterable[T]]=[]):
        if not is_square_matrix(matrix):
            raise InvalidMatrix
        
        self.size = len(matrix)
        self.__s__ = tuple(flatten(matrix))

    def memory(self) -> int:
        return sys.getsizeof(self.__s__) + sys.getsizeof(self.size) + sys.getsizeof(self)

    def __getitem__(self, position: Tuple) -> T:
        return self.__s__[self.size*position[0] + position[1]]

    def rows(self) -> Iterable[Iterable[T]]:
        rows = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(self[i,j])
            rows.append(row)
        return rows

    def columns(self) -> Iterable[Iterable[T]]:
        columns = []
        for i in range(self.size):
            column = []
            for j in range(self.size):
                column.append(self[j,i])
            columns.append(column)
        return columns

    def __hash__(self) -> int:
        return hash(self.__s__)

    def __call__(self, matrix:Iterable[Iterable[T]]=[]) -> Matrix:
        self.__init__(matrix)
        return self
    
    def __repr__(self) -> str:
        return repr(self.rows())

    def __eq__(self, other) -> bool:
        return hash(self) == hash(other)

    def flat(self) -> List:
        return list(self.__s__)

    def rotate_counter_clockwise(self, n:int = 1) -> Matrix:
        m = np.array(self.rows())
        m = np.rot90(axes=(0,1), k=n, m=m)
        m = m.tolist()
        self.__init__(m)
        return self
    
    def rotate_clockwise(self, n:int = 1) -> Matrix:
        k = -n
        return self.rotate_counter_clockwise(k)

    def rotate(self, n:int = 1) -> Matrix:
        if np.sign(n) < 0:
            return self.rotate_counter_clockwise(-n)
        else:
            return self.rotate_clockwise(n)

    def rotations(self) -> Set[Matrix]:
        output = set()
        for i in range(4):
            output.add(self.rotate(1))
        return list(output)
    
    def setAt(self, n:int, pos:Tuple[int,int]) -> Matrix:
        s = self.flat()
        s[self.size*pos[0] + pos[1]] = n
        self.__s__ = tuple(s)
        return self
    
    # ---------------------
    
    def exprint(self):
        print(self.size, end='\n')
            for column in self.columns():
                for row in column:
                    print(row, end='\n')
    
    def transposed(self) -> Matrix:
        self.rotate(1);
