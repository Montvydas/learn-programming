from functools import lru_cache, cache
from timeit import timeit
from copy import deepcopy

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
    '''
    Complexity is exponential, thus tabulation is not a great solution for this specific problem
    '''
    # init table: +1 due to starting from empty string. All values are initialised to 0
    # Then set value at location 0 to be 1 since char of length zero ('') can be created in one way
    # Example word "purple":
    # ----------------------------
    # |  | p | u | r | p | l | e |
    # ----------------------------
    target_length = len(target)
    # ensure to not create list with the same reference, thus for loop here...
    table = [[] for i in range(target_length + 1)]
    table[0] = [[]]
    
    for i in range(target_length + 1):
        # only update possible variations
        if table[i] == []:
            continue

        for w in words:
            # skip w characters ahead of i
            next_possible = i + len(w)
            # print(i, w, table)
            # do not overflow the list AND substring from the target starting at i starts with w
            if next_possible < target_length + 1 and target[i:].find(w) == 0:
                # deepcopy the current entries into the next spot. Deepcopy to copy the values but not references
                copied_prev = deepcopy(table[i])
                # Append the new w value for every i entry
                [cp.append(w) for cp in copied_prev]
                # AAnd update next entry with the i entry
                table[next_possible] += copied_prev

    return table[target_length]

if __name__ == '__main__':
    samples = [('enterapotentpot', ('a', 'p', 'ent', 'enter', 'ot', 'o', 't')), 
               ('abcdef', ('ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c')),
               ('skateboard', ('s', 'k', 'b', 'sk')), 
               ('skateboard', ('s', 'k', 'b', 'sk', 'rd', 'boa', 'ate')), 
               ('eeeeeeeeeeeeeeeeef', ('e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'))]
    for num in samples:
        print(f'all_construct{num} == {all_construct(*num)})')
        print('all_construct_cache{} took {:.6f} sec'.format(num, timeit(lambda: all_construct(*num), number=1)))
        print('all_construct_memo{} took {:.6f} sec'.format(num, timeit(lambda: all_construct_memo(*num), number=1)))
        print('all_construct_tab{} took {:.6f} sec'.format(num, timeit(lambda: all_construct_tab(*num), number=1)))
        print('--------------------------------')