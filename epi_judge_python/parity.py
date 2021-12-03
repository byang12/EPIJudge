from test_framework import generic_test

# XOR associative O(logn)

def parity(x: int) -> int:
    # TODO - you fill in here.
    # iralevant bit on the left
    x = (x >> 32) ^ x
    x = (x >> 16) ^ x
    x = (x >> 8) ^ x
    x = (x >> 4) ^ x
    x = (x >> 2) ^ x
    x = (x >> 1) ^ x
    parityCheck = x & 1 # get rightmost bits
    return parityCheck


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
