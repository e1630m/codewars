class Permscraper:
    def __init__(self, clue):
        self.clue, self.lenc = clue, len(clue)
        self.size, self.plus = self.lenc // 4, self.lenc // 4 + 1
        self.perms = self.gen_perms(tuple([i for i in range(1, self.plus)]))
        self.t, self.r = clue[:self.size], clue[self.size:self.size * 2]
        self.b = clue[self.size * 3 - 1:self.size * 2 - 1:-1]
        self.l = clue[self.size * 4 - 1:self.size * 3 - 1:-1]
        self.c = self.gen_cdict()


    def gen_perms(self, t):
        if len(t) < 2:
            return (t, )
        permutations = []
        for i, c in enumerate(t):
            for perm in self.gen_perms(t[:i] + t[i + 1:]):
                permutations.append((c, ) + perm)
        return permutations

    def gen_cdict(self):
        cdict = {i: set() for i in range(self.plus)}
        for p in self.perms:
            cdict[0].add(p)
            cdict[self.count(p)].add(p)
        return cdict

    def count(self, line):
        return sum(h >= max(line[:i + 1]) for i, h in enumerate(line))

    def get_pboard(self):
        r, c, m = [], [], lambda sets: map(lambda x: tuple(reversed(x)), sets)
        for i in range(self.size):
            r.append(self.c[self.l[i]].intersection(set(m(self.c[self.r[i]]))))
            c.append(self.c[self.t[i]].intersection(set(m(self.c[self.b[i]]))))
        return r, c

    def solve(self):
        pr, pc = self.get_pboard()
        while any(len(row) > 1 for row in pr):
            for i in range(self.size):
                for j in range(self.size):
                    intxn = set(r[j] for r in pr[i]).intersection(
                            set(c[i] for c in pc[j]))
                    pr[i] = [r for r in pr[i] if r[j] in intxn]
                    pc[j] = [c for c in pc[j] if c[i] in intxn]
        return tuple(tuple(r[0]) for r in pr)


def solve_puzzle(clues):
    return Permscraper(clues).solve()
