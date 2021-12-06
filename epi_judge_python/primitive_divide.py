from test_framework import generic_test


def divide(x: int, y: int) -> int:
    # TODO - you fill in here.
    power = 32
    quotient = 0
    while x >= y:
        while (y<<power) > x:
            power = power - 1
        quotient = quotient | (1<<power)
        x = x - (y<<power)
    return quotient


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_divide.py',
                                       'primitive_divide.tsv', divide))
