from get_compulsory import get_compulsory
def solver(size : int , row_hints : list[list[int]], col_hints : list[list[int]]) -> list[list[str]]:
    grid = [[" "] * size for _ in range(size)]
    prev_grid = None
    while grid != prev_grid:
        prev_grid = [row[:] for row in grid]
        for i in range(size):
            grid[i] = get_compulsory(row_hints[i], grid[i])
        for j in range(size):
            col = [grid[i][j] for i in range(size)]
            new_col = get_compulsory(col_hints[j], col)
            for i in range(size):
                grid[i][j] = new_col[i]
    return grid