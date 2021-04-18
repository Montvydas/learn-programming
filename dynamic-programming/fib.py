from functools import lru_cache, cache
from timeit import timeit

# Original recursive version, however cached
# @lru_cache(maxsize=5)
@cache
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

def fib_memo(n, memo = None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n == 1 or n == 2:
        return 1
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

def fib_tab(n):
    # init table: +1 due to starting from 0
    table = [0] * (n + 1)
    table[1] = 1
    
    for i in range(n + 1):
        if i + 1 <= n: # Avoid index out of boundaries
            table[i + 1] += table[i]
        if i + 2 <= n:
            table[i + 2] += table[i]
    return table[n]

if __name__ == '__main__':
    samples = [15, 30, 50, 100, 200, 500]
    for num in samples:
        print(f'fib({num}) == {fib(num)})')
        print('fib_cache({}) took {:.6f} sec'.format(num, timeit(lambda: fib(num), number=1)))
        print('fib_memo({}) took {:.6f} sec'.format(num, timeit(lambda: fib_memo(num), number=1)))
        print('fib_tab({}) took {:.6f} sec'.format(num, timeit(lambda: fib_tab(num), number=1)))
        print('--------------------------------')
    