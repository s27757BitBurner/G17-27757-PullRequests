import math
from abc import ABC, abstractmethod

class SquareGenerator(ABC):
    @abstractmethod
    def generate_squares(self, start, end):
        pass

    def calculate_square_roots(self, squares):
        return [math.sqrt(i) for i in squares]

class CubicGenerator(SquareGenerator):
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("End of the range cannot be less than the start.")
        return [i ** 3 for i in range(start, end + 1)]

    def calculate_cube_roots(self, cubes):
        return [math.pow(i, 1/3) for i in cubes]

cubic_generator = CubicGenerator()

try:
    squares = cubic_generator.generate_squares(1, 10)
    print("Squares:", squares)

    cube_roots = cubic_generator.calculate_cube_roots(squares)
    print("Cube roots:", cube_roots)
except ValueError as e:
    print(e)
