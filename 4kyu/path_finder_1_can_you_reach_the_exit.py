def path_finder(maze):
    if maze == '.':
        return True
    m = [[0 if i == '.' else len(maze) + 1 for i in l] for l in maze.split()]
    h, w = len(m), len(m[0])
    nxt = [(0, 0)]
    while nxt:
        row, col = nxt.pop(0)
        for (i, j) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = row + i, col + j
            if 0 <= nr < h and 0 <= nc < w:
                if not m[nr][nc]:
                    m[nr][nc] = m[row][col] + 1
                    nxt.append((nr, nc))
    return True if m[-1][-1] else False
