from test_framework import generic_test


# brute force O(n)
def parity(x: int) -> int:
    # TODO - you fill in here.
    parityCheck = 0
    while(x!=0):
        parityCheck = parityCheck ^ (x&1)
        x = x>>1
    return parityCheck


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
