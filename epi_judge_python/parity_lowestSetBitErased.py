from test_framework import generic_test

# lowest set bit erased. O(k), k is the number of set bits in x
def parity(x: int) -> int:
    # TODO - you fill in here.
    parityCheck = 0
    while(x):
        x = x & (x-1)
        parityCheck = parityCheck ^ 1
    return parityCheck


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
