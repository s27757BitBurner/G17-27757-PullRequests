import math


class SquareGenerator:
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("End of the range cannot be less than the start.")
        return [i ** 2 for i in range(start, end + 1)]

    def calculate_square_roots(self, squares):
        return [math.sqrt(i) for i in squares]


square_generator = SquareGenerator()

try:
    squares = square_generator.generate_squares(1, 10)
    print("Squares:", squares)

    square_roots = square_generator.calculate_square_roots(squares)
    print("Square roots:", square_roots)
except ValueError as e:
    print(e)


class CubicGenerator(SquareGenerator):
    def generate_cubes(self, start, end):
        if end < start:
            raise ValueError("End of the range cannot be less than the start.")
        return [i ** 3 for i in range(start, end + 1)]

    def calculate_cube_roots(self, cubes):
        return [math.pow(i, 1/3) for i in cubes]

cubic_generator = CubicGenerator()

try:
    cubes = cubic_generator.generate_cubes(1, 10)
    print("Cubes:", cubes)

    cube_roots = cubic_generator.calculate_cube_roots(cubes)
    print("Cube roots:", cube_roots)
except ValueError as e:
    print(e)



""" Task 9 """

import math

class SquareGenerator:
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("End of the range cannot be less than the start.")
        return [i ** 2 for i in range(start, end + 1)]

    def calculate_square_roots(self, squares):
        return [math.sqrt(i) for i in squares]

class CubicGenerator(SquareGenerator):
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("End of the range cannot be less than the start.")
        return super().generate_squares(start, end)  # Call the parent class method

    def generate_cubes(self, start, end):
        if end < start:
            raise ValueError("End of the range cannot be less than the start.")
        return [i ** 3 for i in range(start, end + 1)]

    def calculate_cube_roots(self, cubes):
        return [math.pow(i, 1/3) for i in cubes]

cubic_generator = CubicGenerator()

try:
    squares = cubic_generator.generate_squares(1, 10)
    print("Squares:", squares)

    cubes = cubic_generator.generate_cubes(1, 10)
    print("Cubes:", cubes)

    cube_roots = cubic_generator.calculate_cube_roots(cubes)
    print("Cube roots:", cube_roots)
except ValueError as e:
    print(e)
