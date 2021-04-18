from functools import lru_cache, cache
from timeit import timeit

# Original recursive version, however cached
@cache
def count_construct(target, words):
    if target == '':
        return 1
    
    count = 0
    for w in words:
        if target.find(w) == 0:
            count += count_construct(target[len(w):], words)
    
    return count

def count_construct_memo(target, words, memo = None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == '':
        return 1

    count = 0
    for w in words:
        if target.find(w) == 0:
            count += count_construct_memo(target[len(w):], words, memo)
    
    memo[target] = count
    return count

def count_construct_tab(target, words):
    pass

if __name__ == '__main__':
    samples = [('enterapotentpot', ('a', 'p', 'ent', 'enter', 'ot', 'o', 't')), ('skateboard', ('s', 'k', 'b', 'sk', 'rd', 'boa', 'ate')), ('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ('e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'))]
    for num in samples:
        print(f'count_construct{num} == {count_construct(*num)})')
        print('count_construct_cache{} took {:.6f} sec'.format(num, timeit(lambda: count_construct(*num), number=1)))
        print('count_construct_memo{} took {:.6f} sec'.format(num, timeit(lambda: count_construct_memo(*num), number=1)))
        # print('count_construct_tab{} took {:.6f} sec'.format(num, timeit(lambda: count_construct_tab(*num), number=1)))
        print('--------------------------------')