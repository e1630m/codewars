def rgb(r, g, b):
    n = [i if 0 <= i <= 255 else 255 * (i > 0) for i in (r, g, b)]
    h = lambda x: hex(x)[2:].zfill(2)
    return ''.join(c.upper() if c.isalpha() else c for i in n for c in h(i))
