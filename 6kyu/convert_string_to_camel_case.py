def to_camel_case(text, ans=''):
    for i, c in enumerate(text):
        if i > 0 and text[i - 1] in '-_':
            ans += c.upper()
        elif c not in '-_':
            ans += c
    return ans
