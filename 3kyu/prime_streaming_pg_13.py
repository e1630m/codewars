from itertools import count


class Primes:
    @staticmethod
    def stream():
        yield from (2, 3, 5, 7)
        sieve = {}
        ps = Primes.stream()
        p = next(ps) and next(ps)
        q = p * p
        for cand in count(9, 2):
            if cand in sieve:
                s = sieve.pop(cand)
            elif cand < q:
                yield cand
                continue              
            else:
                s = count(q + 2 * p, 2 * p)
                p = next(ps)
                q = p * p
            for m in s:
                if m not in sieve:
                    break
            sieve[m] = s


# Timeout
# class Primes:
#     @staticmethod
#     def stream(comp={}, i=2):
#         while 1:
#             if i not in comp:
#                 comp[i * i] = [i]
#                 yield i
#             else:
#                 for p in comp[i]:
#                     comp.setdefault(p + i, []).append(p)
#                 del comp[i]
#             i += 1
