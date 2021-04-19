from functools import lru_cache, cache
from timeit import timeit

# Original recursive version, however cached
@cache
def how_sum(target_sum, numbers):
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    
    for n in numbers:
        res = how_sum(target_sum - n, numbers)
        if res or res == []:
            return res + [n]
        
    return None

def how_sum_memo(target_sum, numbers, memo = None):
    if memo is None:
        memo = {}

    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    
    for n in numbers:
        res = how_sum_memo(target_sum - n, numbers, memo)
        if res or res == []:
            memo[target_sum] = res + [n]
            return memo[target_sum]
    
    memo[target_sum] = None
    return None

def how_sum_tab(target_sum, numbers):
    # init table: +1 due to starting from 0
    table = [None] * (target_sum + 1)
    table[0] = []
    
    for i in range(target_sum + 1):
        # only update possible variations
        if table[i] is None:
            continue
        
        for n in numbers:
            next_possible = i + n
            if next_possible <= target_sum: # do not overflow the table
                table[next_possible] = table[i] + [n]
    return table[target_sum]

if __name__ == '__main__':
    samples = [(8, (1, 2, 4)), (50, (1, 2, 4)), (100, (1, 2, 4, 25)), (300, (5, 3, 4, 7))]
    for num in samples:
        print(f'how_sum{num} == {how_sum(*num)})')
        print('how_sum_cache{} took {:.6f} sec'.format(num, timeit(lambda: how_sum(*num), number=1)))
        print('how_sum_memo{} took {:.6f} sec'.format(num, timeit(lambda: how_sum_memo(*num), number=1)))
        print('how_sum_tab{} took {:.6f} sec'.format(num, timeit(lambda: how_sum_tab(*num), number=1)))
        print('--------------------------------')