import operator as op
import numpy as np

# TODO:
#  - Change implementation so that we can represent any general vector
#      <x1, x2, x3, ..., xn>.
#  - Add more operator overloads
#    https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types
#  - Add support for scalar multiplication, addition, etc. This will require
#    checking if the type of argument is Vector, and if it isn't, assume it's
#    scalar.
#  - Should we be using numpy? is math.sqrt faster?

class Vector:
    def __repr__(self):
        return 'Vector' + str(self.coords) + ''
        # return 'Vector(' + str(self.coords[0]) + [', ' + str(c) for c in
        #                                           self.coords[1:]] + ')'
    def __str__(self):
        return self.__repr__()

    def __init__(self, *args):
        self.coords = list(args)
        self.size = len(self.coords)
        return None

    def __getitem__(self, key):
        return self.coords[key]

    def add(self, v):
        if type(v) is Vector:
            self.coords = list(map(op.add, self.coords, v.coords))
        else:
            self.coords = [c + v for c in self.coords]
        return self
            
    def __add__(self, v):
        if type(v) is Vector:
            return Vector(*list(map(op.add, self.coords, v.coords)))
        else:
            return Vector(*[c + v for c in self.coords])

    def __iadd__(self, v):
        return self.add(v)

    def __radd__(self, c):
        return self + c

    def sub(self, v):
        if type(v) is Vector:
            self.coords = list(map(op.sub, self.coords, v.coords))
        else:
            self.coords = [c - v for c in self.coords]
        return self
            
    def __sub__(self, v):
        if type(v) is Vector:
            return Vector(*list(map(op.sub, self.coords, v.coords)))
        else:
            return Vector(*[c - v for c in self.coords])

    def __isub__(self, v):
        return self.sub(v)

    def __rsub__(self, c):
        return -self + c

    def __neg__(self):
        return self * (-1)

    def mult(self, b):
        if type(b) is Vector:
            self.coords = list(map(op.mul, self.coords, b.coords))
        else:
            self.coords = [c * b for c in self.coords]
        return self

    def __mul__(self, b):
        if type(b) is Vector:
            return Vector(*list(map(op.mul, self.coords, b.coords)))
        else:
            return Vector(*[c * b for c in self.coords])

    def __imul__(self, b):
        return self.mult(b)

    def __rmul__(self, b):
        return self * b

    def div(self, b):
        self.coords = [c/b for c in self.coords]
        return self

    def __truediv__(self, b):
        return Vector(*self.coords).div(b)

    def dot(self, v):
        return sum([a * b for (a, b) in zip(self.coords, v.coords)])

    def __eq__(self, other):
        return self.coords == other.coords
