def format_duration(n: int) -> str:
    count = {k: 0 for k in 'year day hour minute second'.split()}
    count['year'], n = divmod(n, 31536000)
    count['day'], n = divmod(n, 86400)
    count['hour'], n = divmod(n, 3600)
    count['minute'], count['second'] = divmod(n, 60)
    ans = ''
    c = {k + 's' if v > 1 else k: v for k, v in count.items() if v}
    nz = len(c)
    for k, v in c.items():
        nz -= 1
        separator = ', ' if nz > 1 else ' and ' if nz else ''
        ans += f'{v} {k}' + separator
    return ans if ans else 'now'
