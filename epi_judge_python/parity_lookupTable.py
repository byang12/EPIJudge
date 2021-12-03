from test_framework import generic_test
from pickle import load

# Lookup table method O(n/L), L is the number of bits in lookup table
# In this case, L = 16
def parity(x: int) -> int:
    # TODO - you fill in here.
    a_file = open("intermediate_results/parityLookupTable16Bits.pkl", "rb")
    parityLookupTable16Bits = load(a_file)
    a_file.close()
    
    mask_16Bits = 0xFFFF
    parityCheck = 0
    
    for i in range(4):
        parityCheck = parityCheck ^ parityLookupTable16Bits[(x>>(i*16)) & mask_16Bits]

    return parityCheck


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
