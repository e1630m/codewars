def check(n, p):
    m = str(n)
    count = {i: m.count(str(i)) for i in range(10)}
    num_digits, most_freq = sum(count.values()), max(count.values())

    t_zero = num_digits - most_freq - 1 == 0 and most_freq == count[0]
    same = num_digits == most_freq
    seq_inc = m in '1234567890'
    seq_dec = m in '9876543210'
    palin = m[:len(m) // 2] == m[::-1][:len(m) // 2]
    matched = sum(n == i for i in p)

    return any([t_zero, same, seq_inc, seq_dec, palin, matched])


def is_interesting(n, p):
    if n + 2 < 100:
        return 0
    if n > 99 and check(n, p):
        return 2
    return any([check(n + 1, p), check(n + 2, p)])
