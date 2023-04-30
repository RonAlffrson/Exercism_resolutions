def square(number):
    """:param number: int - the number of the square
        :return: int - how many grains were on a given square"""
    if (1 > number or number > 64):
        raise ValueError("square must be between 1 and 64")
    else:
        return 2 ** (number - 1)


def total():
    """:return: int - number of grains on the chessboard"""
    square_number = 1
    number_of_grains = 2 ** (square_number - 1)
    while square_number != 64:
        square_number += 1
        number_of_grains += 2 ** (square_number - 1)
    return number_of_grains
