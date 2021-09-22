def decomp(n):
    primes = sieve(n)
    count = {i: 0 for i in primes}
    for prime in sieve(n):
        exp, tmp = 0, n
        while tmp:
            tmp //= prime
            exp += tmp
        count[prime] = exp
    return ''.join(f'{str(k) + ("^" + str(v) if v > 1 else "")} * '
                   for k, v in count.items() if v)[:-3]


def sieve(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    i = 2
    while i * i <= n:
        if primes[i]:
            for non_primes in range(i * i, n + 1, i):
                primes[non_primes] = False
        i += 1
    return (i for i, b in enumerate(primes) if b)
