def solution(l, ans=''):
    tmp = 0
    for i, cur in enumerate(l[1:]):
        if cur - l[i] != 1:
            ans += ',' if ans != '' else ''
            if tmp == i:
                ans += str(l[tmp])
            else:
                if tmp + 1 < i:
                    ans += str(l[tmp]) + '-' + str(l[i])
                else:
                    ans += ','.join(str(i) for i in l[tmp:i + 1])
            tmp = i + 1
    ans += ',' if ans != '' else ''
    if tmp + 2 < len(l):
        ans += str(l[tmp]) + '-' + str(l[-1])
    else:
        ans += ','.join(str(i) for i in l[tmp:])
    return ans
