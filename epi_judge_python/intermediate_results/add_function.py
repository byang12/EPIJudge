import random

def add_two_bits(c,d):
    carry,result = 0
    if c ^ d:
        carry = 0
        result = 1
    else:
        if c|d:
            carry,result = 1

    return (carry,result)


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
        
#a = random.randint(0,65536)
#b = random.randint()
#i=0
#while(i<100000):
#    i+=1
#    if a+b != add_function(a,b):
#        print(a,b)


print(add_function(8,8))
