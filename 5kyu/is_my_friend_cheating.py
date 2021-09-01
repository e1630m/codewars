def remov_nb(n):
    nsum = int(0.5 * n * (n + 1))
    ans = []
    for i in range(nsum // n, n):
        q, r = divmod(nsum - i, i + 1)
        if not r and q <= n:
            ans.append((i, q))
    return ans
