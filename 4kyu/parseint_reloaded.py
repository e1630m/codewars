def parse_int(string):
    a = {w: i for i, w in enumerate('''
        zero one two three four five six seven eight nine
        ten eleven twelve thirteen fourteen fifteen sixteen 
        seventeen eighteen nineteen'''.split())}
    b = {w: i for i, w in zip(range(20, 101, 10), 'twenty thirty \
        forty fifty sixty seventy eighty ninety hundred'.split())}
    c = {'thousand': 1_000, 'million': 1_000_000}
    d = {**{**a, **b}, **c}
    ans = 0
    for i, chunk in enumerate(string.split('thousand')):
        tmp = 0
        for w in chunk.split():
            if w in d.keys():
                tmp = d[w] * tmp if 'hund' in w else d[w] + tmp
            tmp += sum((d[w]) for w in w.split('-')) if '-' in w else 0
        tmp *= 1000 if 'thou' in string and i == 0 else 1
        ans += tmp
    return 1_000_000 if 'mil' in string else ans
