from test_framework import generic_test


def is_palindrome_number(x: int) -> bool:
    # TODO - you fill in here.
    if x<0:
        return False
    result  = 0
    remains = x
    while remains>0:
        result = result*10 + remains%10
        remains = remains//10
    if result != x:
        return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
