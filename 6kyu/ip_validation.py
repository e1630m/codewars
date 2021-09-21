def is_valid_IP(s):
    return all(n.isdigit() and 0 <= int(n) <= 255
               and not (n.startswith('0') and len(n) > 1)
               for n in s.split('.')) and len(s.split('.')) == 4
