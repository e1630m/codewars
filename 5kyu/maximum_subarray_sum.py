def max_sequence(a):
    return 0 if all(n < 0 for n in a) else [] if not a else max(
        sum(a[i:j]) for i in range(len(a)) for j in range(i + 1, len(a) + 1))
