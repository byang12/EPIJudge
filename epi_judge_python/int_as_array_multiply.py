from typing import List

from test_framework import generic_test


def multiply(num1: List[int], num2: List[int]) -> List[int]:
    # TODO - you fill in here.
    sign = 1
    if num1[0]*num2[0]<0:
        sign = -1
    num1[0],num2[0] = abs(num1[0]), abs(num2[0])
    
    num1Len, num2Len = len(num1), len(num2)
    result = [0]*(num1Len+num2Len)

    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            result[i+j+1] = result[i+j+1] + num1[i]*num2[j] # +1 is essential here
    
    # calculate carry in result list digit by digit
    carry = 0        
    for k in reversed(range(num1Len+num2Len)):
        result[k] = carry + result[k]
        carry = result[k]//10
        result[k] = result[k]%10
    
    # remove zero in all high digits
    for l in range(num1Len+num2Len-1):
        if result[0] == 0:
            result = result[1:]
    result[0] = result[0]*sign
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
