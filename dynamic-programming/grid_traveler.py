from functools import lru_cache, cache
from timeit import timeit

# Original recursive version, however cached
@cache
def travel_grid(n, m):
    if n == 0 or m == 0:
        return 0
    if n == 1 or m == 1:
        return 1    
    return travel_grid(n - 1, m) + travel_grid(n, m - 1)

def travel_grid_memo(n, m, memo = None):
    if memo is None:
        memo = {}
    key = (n ,m)
    if key in memo:
        return memo[key]
    if n == 0 or m == 0:
        return 0
    if n == 1 or m == 1:
        return 1
    memo[(n ,m)] = travel_grid_memo(n - 1, m, memo) + travel_grid_memo(n, m - 1, memo)
    return memo[key]

def travel_grid_tab(cols, rows):
    # init table: +1 because index is equal to numbers of cols/rows
    table = [[0 for i in range(cols + 1)] for j in range(rows + 1)]
    table[1][1] = 1
    for row in range(rows + 1):
        for col in range(cols + 1):
            if row + 1 <= rows: # Avoid out of index error
                table[row + 1][col] += table[row][col]
            if col + 1 <= cols:
                table[row][col + 1] += table[row][col]
    return table[rows][cols]


if __name__ == '__main__':
    samples = [(15, 15), (30, 30), (50, 50), (200, 200)]
    for num in samples:
        print(f'travel_grid{num} == {travel_grid(*num)})')
        print('travel_grid_cache{} took {:.6f} sec'.format(num, timeit(lambda: travel_grid(*num), number=1)))
        print('travel_grid_memo{} took {:.6f} sec'.format(num, timeit(lambda: travel_grid_memo(*num), number=1)))
        print('travel_grid_tab{} took {:.6f} sec'.format(num, timeit(lambda: travel_grid_tab(*num), number=1)))
        print('--------------------------------')
    