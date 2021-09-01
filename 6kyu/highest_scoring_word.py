def high(x):
    words = {w: sum(ord(c) - 96 for c in w) for w in x.split()}
    return max(words, key=words.get)
