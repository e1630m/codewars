def solution(n: int) -> str:
    roman = 'I V X L C D M'.split()
    ans = ''
    for i in range(1, 6, 2):
        n, tmp = divmod(n, 10)
        q, r = divmod(tmp, 5)
        if r < 4:
            ans += r * roman[i - 1] + roman[i] * q
        else:
            ans += roman[i + q] + roman[i - 1]
    ans += n * roman[-1]
    return ans[::-1]
