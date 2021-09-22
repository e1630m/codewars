def possibles(m, r, c):
    if m[r][c]:
        return None
    vert, hori = m[r], [m[i][c] for i in range(9)]
    sqr, sqc = r // 3 * 3, c // 3 * 3
    square = [m[i + sqr][j + sqc] for i in range(3) for j in range(3)]
    return [i for i in range(1, 10) if i not in vert + hori + square]


def one_way_positions(p):
    sole_possibility = []
    for r in range(9):
        for c in range(9):
            if p[r][c] is not None and len(p[r][c]) == 1:
                sole_possibility.append([r, c])
    return sole_possibility


def sudoku(puz):
    p = [[possibles(puz, r, c) for c in range(9)] for r in range(9)]
    queue = one_way_positions(p)
    while queue:
        for i, (r, c) in enumerate(queue[::-1]):
            queue[-i - 1].pop()
            puz[r][c] = p[r][c][0]
        p = [[possibles(puz, r, c) for c in range(9)] for r in range(9)]
        queue = one_way_positions(p)
    return puz


puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
print(sudoku(puzzle))
