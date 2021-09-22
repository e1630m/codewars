def battle_codes(let, num, a='abcdefghijklmnopqrstuvwxyz'):
    if not let or not num:
        return 'Peace'
    al, an = [a.index(c) + 1 for c in let], [int(i) for i in num]
    while al and an:
        la, na = al[-1], an[0]
        try:
            an[0], al[-1], al[-2] = an[0] - la, al[-1] - na, al[-2] - na
        except IndexError:
            an[0], al[-1] = an[0] - la, al[-1] - na
        al, an = [i for i in al if i > 0], [i for i in an if i > 0]
    w = ''.join(str(n) for n in an) if an else ''.join(a[c - 1] for c in al)
    return 'Draw' if al == an else w
