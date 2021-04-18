from functools import lru_cache, cache
from timeit import timeit

# Original recursive version, however cached
@cache
def all_construct(target, words):
    if target == '':
        return [[]]

    result = []
    for w in words:
        if target.find(w) == 0:
            res = all_construct(target[len(w):], words)
            
            if res or res == [[]]:
                [r.append(w) for r in res]
                [result.append(r) for r in res]
    
    return result

def all_construct_memo(target, words, memo = None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == '':
        return [[]]

    result = []
    for w in words:
        if target.find(w) == 0:
            res = all_construct_memo(target[len(w):], words, memo)
            
            if res or res == [[]]:
                [r.append(w) for r in res]
                [result.append(r) for r in res]
    
    memo[target] = result
    return result

def all_construct_tab(target, words):
    pass

if __name__ == '__main__':
    samples = [('enterapotentpot', ('a', 'p', 'ent', 'enter', 'ot', 'o', 't')), 
               ('skateboard', ('s', 'k', 'b', 'sk')), 
               ('skateboard', ('s', 'k', 'b', 'sk', 'rd', 'boa', 'ate')), 
               ('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ('e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee')),
               ]
    for num in samples:
        print(f'all_construct{num} == {all_construct(*num)})')
        print('all_construct_cache{} took {:.6f} sec'.format(num, timeit(lambda: all_construct(*num), number=1)))
        print('all_construct_memo{} took {:.6f} sec'.format(num, timeit(lambda: all_construct_memo(*num), number=1)))
        # print('all_construct_tab{} took {:.6f} sec'.format(num, timeit(lambda: all_construct_tab(*num), number=1)))
        print('--------------------------------')