def iq_test(num):
    idx_e = idx_o = 0
    num_e = num_o = 0
    for i, n in enumerate(int(n) for n in num.split()):
        if n % 2:
            num_o += 1
            if not idx_o:
                idx_o = i + 1
        else:
            num_e += 1
            if not idx_e:
                idx_e = i + 1
    if num_e > num_o:
        return idx_o
    return idx_e
