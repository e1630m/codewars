def last_survivors(a, n, ans=''):
    for line, num_c in zip(list(zip(*a[::-1])), n):
        i = 0
        while num_c and i < len(line):
            if line[i] != ' ':
                num_c -= 1
            i += 1
        ans += ''.join(c for c in line[i:] if c != ' ')
    return ans
