def solution(n, ans=''):
    tmp = 0
    for i, cur in enumerate(n[1:]):
        if cur - n[i] != 1:
            ans += ',' if ans != '' else ''
            if tmp == i:
                ans += str(n[tmp])
            else:
                if tmp + 1 < i:
                    ans += str(n[tmp]) + '-' + str(n[i])
                else:
                    ans += ','.join(str(i) for i in n[tmp:i + 1])
            tmp = i + 1
    ans += ',' if ans != '' else ''
    if tmp + 2 < len(n):
        ans += str(n[tmp]) + '-' + str(n[-1])
    else:
        ans += ','.join(str(i) for i in n[tmp:])
    return ans
