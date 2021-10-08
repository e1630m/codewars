def hand(h, cc):
    s, r = '♠ ♥ ♦ ♣'.split(), '2 3 4 5 6 7 8 9 10 J Q K A'.split()[::-1]
    a, o = h + cc, lambda x: sorted(x, key=lambda x: r.index(x))
    ro = o(ca for ca in [card[:-1] for card in h + cc])
    cs = {suit: [c[-1] for c in a].count(suit) for suit in s}
    cr = {rank: [c[:-1] for c in a].count(rank) for rank in r}
    fl = [o(c[:-1] for c in a if k in c) for k, v in cs.items() if v > 4]
    st = [r[i:i + 5] for i in range(9) if all(list(cr.values())[i:i + 5])]
    sf = [s for s in st if ''.join(s) in ''.join(fl[0])] if fl and st else 0
    if sf: return 'straight-flush', sf[0]
    if fk := [rank for rank, count in cr.items() if count >= 4]:
        return 'four-of-a-kind', fk + [c for c in ro if c not in fk][:1]
    tk = [rank for rank, count in cr.items() if count == 3]
    p = [rank for rank, count in cr.items() if count == 2]
    if tk and p or len(tk) > 1:
        return 'full house', tk[:1] + p[:1] if p else tk
    t = 'nothing|pair|two pair|three-of-a-kind'.split('|')
    return (('flush', fl[0][:5]) if fl else ('straight', st[0]) if st
        else (t[3], tk[:1] + [c for c in ro if c not in tk][:2]) if tk
        else (t[1], p + [c for c in ro if c not in p][:3]) if len(p) == 1
        else (t[2], o(p)[:2] + [c for c in ro if c not in p][:1]) if p
        else (t[0], ro[:5]))
