def to_alternating_case(s):
    return ''.join([c.lower() if c.encode().isupper()
                    else c.upper() if c.encode().islower()
                    else c for c in s])
