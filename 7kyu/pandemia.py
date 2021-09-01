def infected(s):
    population = len(s) - s.count('X')
    if not population:
        return 0
    spreaded = ''
    for continent in s.split('X'):
        if '1' in continent:
            spreaded += '1' * len(continent)
        else:
            spreaded += continent
    return spreaded.count('1') / population * 100
