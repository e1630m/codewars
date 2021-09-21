from itertools import permutations as ip


def sort_perm(s):  # fastest
    s = sorted(list(s))
    perms = [''.join(s)]
    last_idx = len(s) - 1
    while s:
        i = j = k = last_idx
        while i and s[i - 1] >= s[i]:
            i -= 1
        if i <= 0:
            break
        while s[j] <= s[i - 1]:
            j -= 1
        s[i - 1], s[j] = s[j], s[i - 1]
        while i < k:
            s[i], s[k] = s[k], s[i]
            i += 1
            k -= 1
        perms.append(''.join(s))
    return perms


def itertools_perm(s):
    return list(set(''.join(tup) for tup in ip(s, len(s))))


def recur_perm(s):  # slowest
    if len(s) == 1:
        return [s]
    perms = []
    for i, c in enumerate(s):
        for perm in recur_perm(s[:i] + s[i + 1:]):
            perms.append(c + perm)
    return list(set(perms))
