def tribonacci(signature, n):
    if n <= 3:
        return signature[:n]
    a, b, c = signature
    ans = [a, b, c]
    while len(ans) < n:
        ans.append(ans[-1] + ans[-2] + ans[-3])
    return ans
