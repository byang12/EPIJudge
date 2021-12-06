from test_framework import generic_test


def power(x: float, y: int) -> float:
    # TODO - you fill in here.
    result = 1.0
    if y<0:
        x = 1/x
        y = -1*y
    while y:
        if y&1:
            result = result*x
        x = x*x
        y = y>>1
    return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
