def dbl_linear(n):
    u, stack = [1], [1]
    limit = n // 2
    while stack:
        t = stack.pop(0)
        tstack = [t * 2 + 1, t * 3 + 1]
        if limit:
            limit -= 1
            stack += tstack
            stack.sort()
        u += tstack
    return sorted(list(set(u)))[n]
