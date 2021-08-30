def getCount(s):
    return sum(1 for c in s if c in 'aeiou')
