def solution(n):
    if n <= 0:
        return 0
    ans = []
    for i in (3, 5, 15):
        q, r = divmod(n, i)
        ans.append(i * q * (q + 1) // 2 if r else i * q * (q - 1) // 2)
    return ans[0] + ans[1] - ans[2]
