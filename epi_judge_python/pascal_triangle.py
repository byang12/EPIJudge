from typing import List

from test_framework import generic_test


def generate_pascal_triangle(n: int) -> List[List[int]]:
    # TODO - you fill in here.
    # ~ Leetcode118 answer
    # ~ numRows = n
    # ~ if numRows == 0:
        # ~ return []
    # ~ elif numRows == 1:
        # ~ return[[1]]
    # ~ elif numRows == 2:
        # ~ return[[1],[1,1]]
    # ~ else:
        # ~ result = [[1],[1,1]]
        # ~ for i in range(2,numRows):
            # ~ currentRow = [1,1]
            # ~ for j in range(1,i):
                # ~ currentRow.insert(-1,result[i-1][j-1]+result[i-1][j])
            # ~ result.append(currentRow)
        # ~ return result
    
    result = [[1]*(i+1) for i in range(n)]
    for i in range(n):
        for j in range(1,i):
            result[i][j] = result[i-1][j-1] + result[i-1][j]
    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pascal_triangle.py',
                                       'pascal_triangle.tsv',
                                       generate_pascal_triangle))
