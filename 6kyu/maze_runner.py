def maze_runner(maze, directions):
    w, h = len(maze[0]), len(maze)
    for tx in range(w):
        for ty in range(h):
            if maze[ty][tx] == 2:
                x, y = tx, ty
                break
    d = {'N': (0, -1), 'S': (0, 1), 'E': (1, 0), 'W': (-1, 0)}
    while directions:
        dx, dy = d[directions.pop(0)]
        nx, ny = x + dx, y + dy
        if not 0 <= nx < w or not 0 <= ny < h or maze[ny][nx] == 1:
            return 'Dead'
        if maze[ny][nx] == 3:
            return 'Finish'
        x, y = nx, ny
    return 'Lost'
