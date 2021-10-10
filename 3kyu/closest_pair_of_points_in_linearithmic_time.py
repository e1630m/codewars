def d(x, y):
    return (x[0] - y[0])**2 + (x[1] - y[1])**2


def closest_pair(p):
    if (lp := len(p)) == 2:
        return p
    elif lp < 33:
        pair, dist = (p[0], p[1]), d(p[0], p[1])
        for i in range(lp - 1):
            for j in range(i + 1, lp):
                if (td := d(p[i], p[j])) < dist:
                    pair, dist = (p[i], p[j]), td
        return pair
    p, c = sorted(p), lp // 2
    f, b = closest_pair(p[:c + 1]), closest_pair(p[c:])
    fd, bd = d(f[0], f[1]), d(b[0], b[1])
    pair, dist = (f if fd < bd else b), min(fd, bd)
    cp = sorted([pos for pos in p if (p[c][0] - pos[0]) ** 2 < dist],
                key=lambda x: x[1])
    for i, np in enumerate(cp):
        while (i := i - 1) >= 0 and (np[1] - cp[i][1])**2 < dist:
            if d(np, cp[i]) < dist:
                pair, dist = (np, cp[i]), d(np, cp[i])
    return pair
