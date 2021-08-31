def find_nb(m, high=100, low=1):
    cube_sum = lambda x: (x * (x + 1) // 2)**2
    while cube_sum(high) < m:
        high *= 2
    mid = (high + low) // 2
    while high - low > 1:
        tmp = cube_sum(mid)
        if tmp > m:
            high = mid
        if tmp < m:
            low = mid
        if tmp == m:
            return mid
        mid = (high + low) // 2
    return high if cube_sum(high) == m else -1
