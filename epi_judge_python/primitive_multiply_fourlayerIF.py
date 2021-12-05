from test_framework import generic_test


def multiply(x: int, y: int) -> int:
    # TODO - you fill in here.
    def add_function(a,b):
        currentSum = 0
        pointerBit = 1
        carry = 0
        while a or b:
            aCurrentBit = a & 1
            bCurrentBit = b & 1
            if aCurrentBit & bCurrentBit & carry: # three 1
                carry = 1
                currentSum = currentSum | pointerBit
            else:
                if aCurrentBit ^ bCurrentBit ^ carry: # one 1
                    carry = 0
                    currentSum = currentSum | pointerBit
                else:
                    if aCurrentBit | bCurrentBit | carry: # two 1
                        carry = 1
                    else: # three 0
                        carry = 0
                
            a = a>>1
            b = b>>1
            pointerBit = pointerBit<<1
        
        if carry:
            currentSum = currentSum | pointerBit
        
        return currentSum
    
    current_sum = 0
    while x:
        if x&1:
            current_sum = add_function(current_sum,y)
        x = x>>1
        y = y<<1
        
    return current_sum


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_multiply.py',
                                       'primitive_multiply.tsv', multiply))
