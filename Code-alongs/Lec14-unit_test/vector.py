#import matplotlib.pyplot as plt
from plotter import PlotVectors

class Vector:
    """ A class to represent a Euclidean vector with magnitude and direction"""

    # in Python >= 3.10 - can use float | int in annotation
    def __init__(self, *numbers: float) -> None:  # *numbers is variadic parameter
        # error checking
        for number in numbers:
            if not isinstance(number, (float, int)):
                raise TypeError(f"{number} is not valid number in a vector")

        if len(numbers) <= 0:
            raise ValueError("Vector can't be empty")

        # to take care of booleans
        self._numbers = tuple(float(number) for number in numbers)

    @property
    def numbers(self) -> tuple:
        return self._numbers

    def __add__(self, other: "Vector") -> "Vector":
        if self.validate_vectors(other):
            numbers = (a+b for a, b in zip(self.numbers, other.numbers))
            return Vector(*numbers)

    def __sub__(self, other: "Vector") -> "Vector":
        if self.validate_vectors(other):
            numbers = (a-b for a, b in zip(self.numbers, other.numbers))
            return Vector(*numbers)

    def __mul__(self, value: float) -> "Vector":
        print("__mul__ is called")
        if not isinstance(value, (int, float)):
            raise TypeError(
                f"The value for multiplication must be int or float not {type(value)}")
        numbers = (value*a for a in self.numbers)
        return Vector(*numbers)

    # to make multiplication commutative, i.e. a*v = v*a
    def __rmul__(self, value: float) -> "Vector":
        print("__rmul__ is called ...")
        return self*value

    # for using len() method on a Vector object
    def __len__(self) -> int:
        """ Returns number of components in a Vector not the length"""
        return len(self.numbers)

    def norm(self) -> float:
        """ Returns the Euclidean norm of a Vector"""
        return sum(a**2 for a in self.numbers)**.5

    def validate_vectors(self, other: "Vector") -> bool:
        """ validates if two vectors have same length """
        if not isinstance(other, Vector) or len(other) != len(self):
            raise TypeError(f"Both must be Vector and have the same length")
        return len(self) == len(other)

    def __getitem__(self, item: int) -> float:
        return self.numbers[item]

    def plot(self, *others):
        for vector in tuple((self, *others)):
            if Vector.is2D(vector):
                pass
            
        plot_vector = PlotVectors(self, *others)
        plot_vector.plot()

    @staticmethod # bound to the class and not dependent on the object itself
    def is2D(vector: "Vector") -> bool:
        if len(vector) != 2:
            raise ValueError(
                f"Vector dimension must be 2 not {len(vector)}")
        return True

    def __repr__(self) -> str:
        return f"Vector{self.numbers}"

    def __eq__(self, other) -> bool:
        if not self.validate_vectors(other):
            return False

        for num1, num2 in zip(self.numbers, other.numbers):
            if num1 != num2:
                return False
        
        return True
        

    # NOTE: There are many more features to be implemented, feel free to do it
    # TODO: implement norm between vectors
    # TODO: implement dot product
    # TODO: implement vector product
    # TODO: implement conjugate 
    # TODO: implement projection
