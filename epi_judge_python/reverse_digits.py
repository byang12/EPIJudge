from test_framework import generic_test


def reverse(x: int) -> int:
    # TODO - you fill in here.
    result  = 0
    remains = abs(x)
    while remains>0:
        result = result*10 + remains%10
        remains = remains//10
    if x<0:
        result = -result
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
