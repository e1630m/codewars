def pig_it(t):
    return ' '.join(w[1:] + w[0] + 'ay' if w not in '?!.' else w for w in t.split())
