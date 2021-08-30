def digital_root(n):  # submitted
    s = str(n)
    while 1:
        sumdigit = sum(int(c) for c in s)
        if sumdigit < 10:
            return sumdigit
        s = str(sumdigit)


def recursive_digital_root(n):
    if n < 10:
        return n
    sumdigit = 0
    while n > 10:
        n, r = divmod(n, 10)
        sumdigit += r
    return recursive_digital_root(sumdigit + n)


for i in (16, 942, 132189, 493193):
    print(digital_root(i) == recursive_digital_root(i))
