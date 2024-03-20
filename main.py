""" Task 1 """
squares = [i**2 for i in range(1, 11)]
print(squares)


""" Task 2 """
def generate_squares(start, end):
    return [i**2 for i in range(start, end+1)]

squares = generate_squares(1, 10)
print(squares)

""" Task 3"""
class SquareGenerator:
    def generate_squares(self, start, end):
        return [i**2 for i in range(start, end+1)]

square_generator = SquareGenerator()
squares = square_generator.generate_squares(1, 10)
print(squares)

""" Task 4 and 5"""

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

