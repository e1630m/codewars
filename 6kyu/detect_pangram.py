def is_pangram(s):
    return all(c >= 1 for c in (s.lower().count(a)
                                for a in 'abcdefghijklmnopqrstuvwxyz'))
