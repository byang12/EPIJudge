from typing import List

from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    # TODO - you fill in here.
    if n == 1 or n == 0:
        return []    
    if n == 2:
        return [2]
    primes = [2]
    for i in range(3,n+1):
        prime_flag = 1
        for j in primes:
            if i%j == 0:
                prime_flag = 0
                break
        if prime_flag:
            primes.append(i)
                
    return primes


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
