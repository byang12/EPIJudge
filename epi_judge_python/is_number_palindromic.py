from test_framework import generic_test
import math

def is_palindrome_number(x: int) -> bool:
    # TODO - you fill in here.
    if x<0:
        return False
    if x == 0:
        return True
    
    numOfDigits = math.floor(math.log10(x)) + 1 # x can not <= 0, otherwise malfunction
    mask = 10**(numOfDigits-1)

    while mask>0:
        MSD = x//mask # Most Significant Digit
        LSD = x%10 # Least Significant Digit
        if not MSD == LSD:
            return False
        x = x % mask # remove MSD
        x = x // 10 # remove LSD
        mask = mask // 100
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
