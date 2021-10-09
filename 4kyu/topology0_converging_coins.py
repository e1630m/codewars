def converge(g, u1, u2, u3):
    if u1 == u2 == u3:
        return 0
    pos = [{u1}, {u2}, {u3}]
    visited = [pos]
    for i in range(len(g)):
        pos = [{n for new in coin for n in g[new]} for coin in pos]
        if pos[0].intersection(pos[1].intersection(pos[2])):
            return i + 1
        if pos in visited:
            return None
        visited.append(pos)
    return i 
