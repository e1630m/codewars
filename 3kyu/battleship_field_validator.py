def get_size(m, r, c, h, w):
    if c < w and ((r > 0 and m[r - 1][c + 1]) or
        (r < h and ((m[r + 1][c] and m[r][c + 1]) or m[r + 1][c + 1]))):
        return -1
    if r < h and m[r + 1][c] == 1:
        return 1 + get_size(m, r + 1, c, h, w)
    if c < w and m[r][c + 1] == 1:
        return 1 + get_size(m, r, c + 1, h, w)
    return 1


def validate_battlefield(m):
    s = {i: 0 for i in range(5)}
    h, w = len(m) - 1, len(m[0]) - 1
    for row in range(h + 1):
        for col in range(w + 1):
            if (m[row][col]
                and not (row > 0 and m[row - 1][col]) 
                and not (col > 0 and m[row][col - 1])):
                    size = get_size(m, row, col, h, w)
                    s[size] = s.get(size, 0) + 1
    return all(s[i] == 5 - i for i in range(1, 5))
