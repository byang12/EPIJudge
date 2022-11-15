from test_framework import generic_test


def fibonacci(n: int) -> int:
    # TODO - you fill in here.
	cache = [0,1]
	if n > 1:
		for i in range(2,n+1):
			cache.append(cache[i-1]+cache[i-2])
	return cache[n]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('fibonacci.py', 'fibonacci.tsv',
                                       fibonacci))
