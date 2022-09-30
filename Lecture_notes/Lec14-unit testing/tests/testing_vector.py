from importlib.resources import path
import unittest
import sys, os

# changes directory to this files path
os.chdir(os.path.dirname(__file__))
path_to_vector_module = os.path.abspath("../")

# adds this path to sys.path where Python will look when importing modules
sys.path.append(path_to_vector_module)

from vector import Vector

class TestVector(unittest.TestCase):
    def setUp(self) -> None:
        self.x, self.y = 1, 2 
    
    def create_2D_vector(self) -> "Vector":
        return Vector(self.x, self.y)

    def test_create_2D_vector(self) -> None:
        v = self.create_2D_vector()
        self.assertEqual(v.numbers, (self.x, self.y))

    def test_create_5D_vector(self):
        v = Vector(-1,0,-5,-50.2, 52.2)
        self.assertEqual(v.numbers, (-1,0,-5,-50.2,52.2))

    def test_create_empty_vector(self):
        with self.assertRaises(ValueError):
            v = Vector()

    def test_2_vector_equal(self) -> None:
        v1 = self.create_2D_vector()
        v2 = Vector(1,2)
        self.assertEqual(v1, v2)

    def test_2_vector_not_equal(self) -> None:
        v1 = self.create_2D_vector()
        v2 = Vector(1,-2)
        self.assertNotEqual(v1,v2)
    
    def test_add_2_vectors(self) -> None:
        v1 = self.create_2D_vector()
        v2 = Vector(1,-2)
        self.assertEqual(v1+v2, Vector(2,0))

    def test_add_vectors_diff_dimensions(self) -> None:
        v1 = self.create_2D_vector()
        v2 = Vector(1,1,1)
        self.assertRaises(TypeError)

    def test_multiply_scalar(self) -> None:
        v1 = self.create_2D_vector()
        v2 = v1*5
        self.assertEqual(v2, Vector(5,10))

    def test_reverse_multiply_scalar(self) -> None:
        v1 = self.create_2D_vector()
        v2 = 5*v1
        self.assertEqual(v2, Vector(5,10))

    def test_len_vector(self) -> None:
        v1 = self.create_2D_vector()
        self.assertEqual(len(v1), 2)

    def test_getitem(self) -> None:
        v1 = self.create_2D_vector()
        for i, number in enumerate((1,2)):
            self.assertEqual(v1[i], number)

# if we run this module directly as main, run the code in the conditional
if __name__ == "__main__":
    unittest.main() # the code that is ran is unittest.main() which runs all our tests

# the code not ran if imported, because then __name__ is not "__main__"