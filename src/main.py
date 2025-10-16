from format_hint import format_hint
from solver import solver
def solve_nanogram(hint) -> list[list[str]]:
    size, row_hints, col_hints = format_hint(hint)
    return solver(size, row_hints, col_hints)

ans = solve_nanogram(open("../hint.txt", "r"))
for row in ans:
    print(" ".join(row))