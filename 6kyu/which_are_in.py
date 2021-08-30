def in_array(a1, a2):
    arr = []
    for e1 in a1:
        for e2 in a2:
            if e1 in e2 and e1 not in arr:
                arr.append(e1)
                break
    arr.sort()
    return arr
