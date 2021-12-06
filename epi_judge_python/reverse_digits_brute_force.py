from test_framework import generic_test


def reverse(x: int) -> int:
    # TODO - you fill in here.
    sign = 1
    if x<0:
        sign = -1
    x = x*sign
    xString = str(x)
    i = len(xString) - 1
    reverseX = ''
        
    while i>=0:
        reverseX = reverseX + xString[i]
        i = i - 1
    return sign*int(reverseX)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
