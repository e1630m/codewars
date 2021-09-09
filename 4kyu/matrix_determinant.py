def determinant(m, ans=0):
    if len(m) == 1:
        return m[0][0]
    tbt = lambda x: x[0][0] * x[1][1] - x[0][1] * x[1][0]
    if len(m) == 2:
        return tbt(m)
    e = lambda x: enumerate(x)
    d = lambda x, col: [[v for i, v in e(l) if i != col] for l in x[1:]]
    for i, sm in enumerate([d(m, n) for n in range(len(m[0]))]):
        ans += m[0][i] * determinant(sm)  * (-1 if i % 2 else 1)
    return ans
