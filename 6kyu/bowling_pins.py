def bowling_pins(arr, ans=''):
    line_num = 4
    pin_num = 10
    while line_num:
        line = ''
        l_pad, l_break = ' ' * (4 - line_num), '\n' if line_num > 1 else ''
        for i in range(line_num):
            pad = ' ' if line_num - 1 > i else ''
            pin = ' ' if pin_num in arr else 'I'
            line += pin + pad
            pin_num -= 1
        ans += l_pad + line[::-1] + l_pad + l_break
        line_num -= 1
    return ans
