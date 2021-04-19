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

def can_construct_memo(target, words, memo = None):
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
    # init table: +1 due to starting from empty string
    # Example word "purple":
    # ----------------------------
    # |  | p | u | r | p | l | e |
    # ----------------------------
    target_length = len(target)
    table = [False] * (target_length + 1)
    table[0] = True
    
    for i in range(target_length + 1):
        # only update possible variations
        if table[i] is False:
            continue
            
        for w in words:
            # skip w characters ahead of i
            next_possible = i + len(w)
            # do not overflow the list AND substring from the target starting at i starts with w
            if next_possible < target_length + 1 and target[i:].find(w) == 0:
                table[next_possible] = True
    return table[target_length]

if __name__ == '__main__':
    samples = [('skateboard', ('sk', 'rd', 'boa', 'ate')),
               ('abcdef', ('ab', 'abc', 'cd', 'def', 'abcd')),
               ('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ('e', 'ee', 'eee', 'eeee')),
               ]
    for num in samples:
        print(f'can_construct{num} == {can_construct_tab(*num)})')
        print('can_construct_cache{} took {:.6f} sec'.format(num, timeit(lambda: can_construct(*num), number=1)))
        print('can_construct_memo{} took {:.6f} sec'.format(num, timeit(lambda: can_construct_memo(*num), number=1)))
        print('can_construct_tab{} took {:.6f} sec'.format(num, timeit(lambda: can_construct_tab(*num), number=1)))
        print('--------------------------------')