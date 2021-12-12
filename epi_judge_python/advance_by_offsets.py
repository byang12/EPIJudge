from typing import List
from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:
    # TODO - you fill in here.
    furest_reach = 0
    max_step = len(A) - 1
    i = 0
    while i<=furest_reach and furest_reach<=max_step:
        furest_reach = max(furest_reach,A[i]+i)
        i = i + 1
    return furest_reach>=max_step


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
