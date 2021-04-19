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
    # init table: +1 due to starting from empty string. All values are initialised to 0
    # Then set value at location 0 to be 1 since char of length zero ('') can be created in one way
    # Example word "purple":
    # ----------------------------
    # |  | p | u | r | p | l | e |
    # ----------------------------
    target_length = len(target)
    table = [0] * (target_length + 1)
    table[0] = 1
    
    for i in range(target_length + 1):
        # Excluding this would still work, but not worth doing this 
        # since adding 0 to anything will not change the number
        if table[i] == 0:
            continue

        for w in words:
            # skip w characters ahead of i
            next_possible = i + len(w)
            # do not overflow the list AND substring from the target starting at i starts with w
            if next_possible < target_length + 1 and target[i:].find(w) == 0:
                table[next_possible] += table[i] # Update next possible with what we got in current i position
    return table[target_length]

if __name__ == '__main__':
    samples = [('enterapotentpot', ('a', 'p', 'ent', 'enter', 'ot', 'o', 't')), 
               ('skateboard', ('s', 'k', 'b', 'sk', 'rd', 'boa', 'ate')),
               ('abcdef', ('ab', 'abc', 'cd', 'ef', 'abcd')),
               ('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ('e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee')),
               ]
    for num in samples:
        print(f'count_construct{num} == {count_construct_tab(*num)})')
        print('count_construct_cache{} took {:.6f} sec'.format(num, timeit(lambda: count_construct(*num), number=1)))
        print('count_construct_memo{} took {:.6f} sec'.format(num, timeit(lambda: count_construct_memo(*num), number=1)))
        print('count_construct_tab{} took {:.6f} sec'.format(num, timeit(lambda: count_construct_tab(*num), number=1)))
        print('--------------------------------')