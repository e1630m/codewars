def get_edges(w, h):
    t = [(0, i) for i in range(w)]
    l = [(i, 0) for i in range(1, h)]
    r = [(i, w - 1) for i in range(1, h)]
    b = [(h - 1, i) for i in range(1, w - 1)]
    return t + l + r + b


def fully_blocked(m, edges, ans=True):
    for y, x in edges:
        if m[y][x] == ' ':
            ans = False
    return ans


def find_start_pos(m, w, h):
    ans = []
    for tx in range(w): 
        for ty in range(h):
            if m[ty][tx] == 'k':
                ans.append((tx, ty))
    if len(ans) > 1:
        raise ValueError('There should not be multiple Kates')
    elif len(ans) == 0:
        raise ValueError('There should be one Kate')
    return ans


def check_neighbors(m, x, y, w, h):
    valid = []
    lowest = float('inf')
    for dx, dy in ((0, -1), (0, 1), (1, 0), (-1, 0)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < w and 0 <= ny < h:
            if not m[ny][nx]:
                valid.append((nx, ny))
            else:
                lowest = min(lowest, m[ny][nx])
    return valid, lowest


def has_exit(maze):
    if len(maze[0]) == 1:
        return True
    w, h = len(maze[0]), len(maze)
    x, y = find_start_pos(maze, w, h)[0]
    edges = get_edges(w, h)
    if fully_blocked(maze, edges):
        return False
    m = [[w * h + 2 if c == '#' else 0 for c in l] for l in maze]
    m[y][x] = 1
    nxt = check_neighbors(m, x, y, w, h)[0]
    while nxt:
        x, y = nxt.pop(0)
        valid, lowest = check_neighbors(m, x, y, w, h)
        m[y][x] += lowest + 1
        if valid:
            for move in valid:
                nxt.append(move)
        if (y, x) in edges:
            return True
    return False
