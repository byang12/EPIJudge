import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def even_odd(A: List[int]) -> None:
    # TODO - you fill in here.
    i = 0
    j = len(A) - 1
    while i < j:
        if (A[i]%2)&(A[j]%2): #both odd
            j = j-1
        elif (A[i]%2)&~(A[j]%2): # i odd j even
            A[i], A[j] = A[j], A[i]
            i = i + 1
            j = j - 1
        elif ~(A[i]%2)&(A[j]%2): # i even j odd
            i = i + 1
            j = j - 1
        else: #i even j even
            i = i + 1


@enable_executor_hook
def even_odd_wrapper(executor, A):
    before = collections.Counter(A)

    executor.run(functools.partial(even_odd, A))

    in_odd = False
    for a in A:
        if a % 2 == 0:
            if in_odd:
                raise TestFailure('Even elements appear in odd part')
        else:
            in_odd = True
    after = collections.Counter(A)
    if before != after:
        raise TestFailure('Elements mismatch')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_array.py',
                                       'even_odd_array.tsv', even_odd_wrapper))
