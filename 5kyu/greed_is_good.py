def score(dice):
    d = [i for i in dice[:]]
    counts = {i: d.count(i) for i in range(1, 7)}
    s = 0
    for k, v in counts.copy().items():
        if v >= 3:
            multiplier = 100 if k > 1 else 1000
            s += k * multiplier
            counts[k] -= 3
    return s + counts[1] * 100 + counts[5] * 50
