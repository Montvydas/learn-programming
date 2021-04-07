from functools import lru_cache, cache
from timeit import timeit

# Original recursive version, however cached
@cache
def best_sum(target_sum, numbers):
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    
    min_entries = None
    
    for n in numbers:
        res = best_sum(target_sum - n, numbers)
        if res or res == []:
            res = res + [n]
        
            if min_entries is None or len(min_entries) > len(res):
                min_entries = res[:]
    
    return min_entries

def best_sum_memo(target_sum, numbers, memo = None):
    if memo is None:
        memo = {}
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    
    min_entries = None
    
    for n in numbers:
        res = best_sum_memo(target_sum - n, numbers, memo)
        if res or res == []:
            res = res + [n]
        
            if min_entries is None or len(min_entries) > len(res):
                min_entries = res[:]
    
    memo[target_sum] = min_entries
    return min_entries

def best_sum_tab(target_sum, numbers):
    pass

if __name__ == '__main__':
    samples = [(8, (1, 2, 4)), (50, (1, 2, 4)), (100, (1, 2, 4, 25)), (300, (5, 3, 4, 7))]
    for num in samples:
        print(f'best_sum{num} == {best_sum(*num)})')
        print('how_sum_cache{} took {:.6f} sec'.format(num, timeit(lambda: best_sum(*num), number=1)))
        print('best_sum_memo{} took {:.6f} sec'.format(num, timeit(lambda: best_sum_memo(*num), number=1)))
        print('best_sum_tab{} took {:.6f} sec'.format(num, timeit(lambda: best_sum_tab(*num), number=1)))
        print('--------------------------------')