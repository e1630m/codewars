def sieve(comp={}, i=2):
    while 1:
        if i not in comp:
            comp[i * i] = [i]
            yield i
        else:
            for p in comp[i]:
                comp.setdefault(p + i, []).append(p)
            del comp[i]
        i += 1


def getPrimes(start, finish):
    low = min(start, finish)
    high = max(start, finish)
    primes = []
    for p in sieve():
        primes += [p] if low <= p <= high else []
        if p > high:
            break
    return primes


def isPrime(n):
    if n < 4:
        return False if n < 2 else True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, n**0.5 + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True
