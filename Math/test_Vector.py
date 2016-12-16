import unittest
from Vector import Vector

class TestVectorMethods(unittest.TestCase):

    def test_vector(self):
        v1 = Vector(1, 2, 3)
        self.assertEqual(v1.coords, [1, 2, 3])
        v2 = Vector(2, 3, 4, 5)
        self.assertEqual(v2.coords, [2, 3, 4, 5])

    def test___getitem__(self):
        v1 = Vector(1, 2)
        self.assertEqual(v1[0], 1)
        self.assertEqual(v1[1], 2)
        self.assertRaises(IndexError)

    def test_add(self):
        v1 = Vector(1, 2)
        v2 = Vector(3, 4)
        v1.add(v2)
        self.assertEqual(v1.coords, [4, 6])

    def test___add__(self):
        v1 = Vector(1, 2)
        v2 = Vector(3, 4)
        v3 = v1 + v2
        self.assertEqual(v3, Vector(4, 6))
        self.assertEqual(v1, Vector(1, 2)) # Make sure __add__ didn't change
        self.assertEqual(v2, Vector(3, 4)) # the original vectors

    def test___iadd__(self):
        v1 = Vector(1, 2)
        v1 += 2
        self.assertEqual(v1, Vector(3, 4))
        v1 += Vector(2, 2)
        self.assertEqual(v1, Vector(5, 6))

    def test___radd__(self):
        v1 = Vector(1, 2)
        v2 = 2 + v1
        self.assertEqual(v2, Vector(3, 4))

    def test_sub(self):
        v1 = Vector(1, 2)
        v2 = Vector(3, 4)
        v1.sub(v2)
        self.assertEqual(v1, Vector(-2, -2))
        v1.sub(1)
        self.assertEqual(v1, Vector(-3, -3))

    def test___sub__(self):
        v1 = Vector(1, 2)
        v2 = Vector(3, 4)
        v3 = v1 - v2
        self.assertEqual(v3, Vector(-2, -2))
        self.assertEqual(v1, Vector(1, 2)) # Make sure __add__ didn't change
        self.assertEqual(v2, Vector(3, 4)) # the original vectors

    def test___isub__(self):
        v1 = Vector(1, 2)
        v1 -= 2
        self.assertEqual(v1, Vector(-1, 0))
        v1 -= Vector(2, 2)
        self.assertEqual(v1, Vector(-3, -2))

    def test___rsub__(self):
        v1 = Vector(1, 2)
        v2 = 2 - v1
        self.assertEqual(v2, Vector(1, 0))

    def test___neg__(self):
        v1 = Vector(1, 2)
        self.assertEqual(-v1, Vector(-1, -2))
        self.assertEqual(v1, Vector(1, 2))

    def test_mult(self):
        v1 = Vector(1, 2)
        v1.mult(3)
        self.assertEqual(v1, Vector(3, 6))
        v1.mult(Vector(1, 2))
        self.assertEqual(v1, Vector(3, 12))
        
    def test___mul__(self):
        v1 = Vector(1, 2)
        v2 = Vector(3, 4)
        self.assertEqual(v1 * v2, Vector(3, 8))

    def test___imul__(self):
        v1 = Vector(1, 2)
        v1 *= 2
        self.assertEqual(v1, Vector(2, 4))
        v1 *= Vector(1, 2)
        self.assertEqual(v1, Vector(2, 8))

    def test___rmul__(self):
        v1 = Vector(1, 2)
        v2 = 2 * v1
        self.assertEqual(v2, Vector(2, 4))

    # def test_upper(self):
    #     self.assertEqual('foo'.upper(), 'FOO')

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()
