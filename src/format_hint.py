def format_hint(hint) -> tuple[int, list[list[int]], list[list[int]]]:
    lines = hint.readlines()
    size = int(lines[0].strip())
    row_hints = []
    col_hints = []
    for i in range(1, size + 1):
        row_hints.append(list(map(int, lines[i].strip().split())))
    for i in range(size + 1, 2 * size + 1):
        col_hints.append(list(map(int, lines[i].strip().split())))
    return size, row_hints, col_hints