def last_survivors(s, a='abcdefghijklmnopqrstuvwxyza'):
    s, d = [c for c in s], {k: s.count(k) for k in a[:-1]}
    while any(v > 1 for v in d.values()):
        to_remove = [k for k, v in d.items() if v > 1][0]
        for i in range(2):
            del s[s.index(to_remove)]
        s.append(a[a.index(to_remove) + 1])
        d = {k: s.count(k) for k in a[:-1]}
    return ''.join(s)
