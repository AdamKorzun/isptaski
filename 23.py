from __future__ import annotations
from typing import Union

class Vector:
    def __init__(self, data = None) -> None:
        if data is None:
            data = []
        elif isinstance(data, Vector):
            self._data = data._data[:]
            self.dimension = data.dimension
        elif not isinstance(data, list):
            raise ValueError()
        else:
            self._data = data
            self.dimension = len(data)

    def __getitem__(self, index: int) -> Union[int, float]:
        if not isinstance(index, int):
            raise ValueError()
        return self._data[index]

    def resize(self, size: int) -> None:
        if not isinstance(size, int):
            raise ValueError()
        if size >= self.dimension:
            self._data += [0] * (size - self.dimension)
        elif size < self.dimension:
            self._data = self._data[:size]
        self.dimension = len(self._data)

    def __setitem__(self, index: int, data: Union[int, float]) -> None:
        if not isinstance(index, int):
            raise ValueError()
        if not isinstance(data, int) or not isinstance(data, float):
            raise ValueError()
        if index >= self.dimension:
            self.resize(index+1)
        self._data[index] = data

    def __repr__(self) -> str:
        return str(self._data)

    def __len__(self) -> int:
        return self.dimension

    def __eq__(self, o: Union[Vector, list]) -> bool:
        if not isinstance(o, Vector):
            raise ValueError()
        if self.dimension != o.dimension:
            return False
        return bytes(self._data) == bytes(o._data)

    def __add__(self, o: Union[Vector, list]) -> Vector:
        if isinstance(o, list):
            o = Vector(o)
        elif not isinstance(o, Vector):
            raise ValueError
        if len(o) > self.dimension:
            more_dims = o._data
            less_dims = self._data
        else:
            less_dims = o._data
            more_dims = self._data

        res = more_dims[:]
        for i in range(len(less_dims)):
            res[i] += less_dims[i]
        
        return Vector(res)

    def __sub__(self, o: Union[Vector, list]) -> Vector:
        if isinstance(o, list):
            o = Vector(o)
        elif not isinstance(o, Vector):
            raise ValueError
        return self.__add__([-x for x in o])

    def __bool__(self) -> bool:
        return not not self._data

    def __neg__(self) -> Vector:
        self._data = [-x for x in self._data]
        return self


a = Vector([1, 2])
b = Vector([1, 2, 0, 3])

print(f'{a = }\n{b = }\n')

print('sum:')
print(a+b)
print(b+a)
print()

print('sub:')
print(a-b)
print(b-a)
print()

print('eq:')
print(a==b)
print(b==a)
print(b!=a)
print(a!=b)
