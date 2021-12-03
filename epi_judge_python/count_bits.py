from test_framework import generic_test


def count_bits(x: int) -> int:
    # TODO - you fill in here.
    numBits = 0
    while(x!=0):
        numBits = numBits + (x&1)
        x = x >> 1
    return numBits


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('count_bits.py', 'count_bits.tsv',
                                       count_bits))
