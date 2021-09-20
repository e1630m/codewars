def next_bigger(n):
    s = [c for c in str(n)]
    try:
        a = max(i for i in range(1, len(s)) if s[i] > s[i - 1])
        b = max(i for i in range(a, len(s)) if s[i] > s[a - 1])
    except ValueError:
        return -1
    s[b], s[a - 1] = s[a - 1], s[b]
    s[a:] = s[a:][::-1]
    return int(''.join(c for c in s))
