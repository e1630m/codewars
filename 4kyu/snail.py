def snail(m):
    if (n := len(m)) < 2:
        return m[0]
    eaten = []
    for _ in range(n // 2):
        for _ in range(4):
            for i in range(len(m[0]) - 1):
                eaten.append(m[0][i])
            m = [[i for i in l] for l in list(zip(*m))[::-1]]
        m = [l[1:-1] for l in m[1:-1]]
    return eaten + ([m[0][0]] if n % 2 else [])
