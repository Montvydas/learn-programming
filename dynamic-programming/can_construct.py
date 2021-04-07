from functools import lru_cache, cache
from timeit import timeit

# Original recursive version, however cached
@cache
def can_construct(target, words):
    if target == '':
        return True
    
    for w in words:
        if target.find(w) == 0:
            if can_construct(target[len(w):], words) is True:
                return True
    
    return False

def can_construct_memo(target, words, memo = {}):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == '':
        return True
    
    for w in words:
        if target.find(w) == 0:
            if can_construct_memo(target[len(w):], words, memo) is True:
                memo[target] = True
                return True
    
    memo[target] = False
    return False

def can_construct_tab(target, words):
    pass

if __name__ == '__main__':
    samples = [("skateboard", ("sk", "rd", "boa", "ate")), ("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ("e", "ee", "eee", "eeee"))]
    for num in samples:
        print(f'can_construct{num} == {can_construct(*num)})')
        print('can_construct_cache{} took {:.6f} sec'.format(num, timeit(lambda: can_construct(*num), number=1)))
        print('can_construct_memo{} took {:.6f} sec'.format(num, timeit(lambda: can_construct_memo(*num), number=1)))
        print('can_construct_tab{} took {:.6f} sec'.format(num, timeit(lambda: can_construct_tab(*num), number=1)))
        print('--------------------------------')