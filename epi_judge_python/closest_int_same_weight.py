from test_framework import generic_test


#O(1)
def closest_int_same_bit_count(x: int) -> int:
    # TODO - you fill in here.
    fitstBitofx = x & 1
    if fitstBitofx:
        reverseOrNotX = ~x
    else:
        reverseOrNotX = x
        
    firstSetBit = reverseOrNotX&(~(reverseOrNotX-1))
    mask = firstSetBit | (firstSetBit>>1)
    return mask ^ x

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('closest_int_same_weight.py',
                                       'closest_int_same_weight.tsv',
                                       closest_int_same_bit_count))
