from functools import lru_cache, cache
from timeit import timeit

# Original recursive version, however cached
@cache
def can_sum(target_sum, numbers):
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False

    return any([can_sum(target_sum - n, numbers) for n in numbers])

def can_sum_memo(target_sum, numbers, memo = None):
    if memo is None:
        memo = {}
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False
    
    for n in numbers:
        if can_sum_memo(target_sum - n, numbers, memo):
            memo[target_sum] = True
            return True

    memo[target_sum] = False
    return False

def can_sum_tab(target_sum, numbers):
    # init table: +1 due to starting from 0
    table = [False] * (target_sum + 1)
    table[0] = True
    
    for i in range(target_sum + 1):
        # only update possible variations
        if table[i] == False:
            continue

        for n in numbers:
            next_possible = i + n
            if next_possible < target_sum + 1:
                table[next_possible] = True
    return table[target_sum]

if __name__ == '__main__':
    samples = [(8, (1, 2, 4)), (50, (1, 2, 4)), (99, (32, 18, 6)), (300, (7, 14))]
    for num in samples:
        print(f'can_sum{num} == {can_sum(*num)})')
        print('can_sum_cache{} took {:.6f} sec'.format(num, timeit(lambda: can_sum(*num), number=1)))
        print('can_sum_memo{} took {:.6f} sec'.format(num, timeit(lambda: can_sum_memo(*num), number=1)))
        print('can_sum_tab{} took {:.6f} sec'.format(num, timeit(lambda: can_sum_tab(*num), number=1)))
        print('--------------------------------')
    