from operator import __add__, __sub__, __mul__, __truediv__


class Calculator(object):
    def __init__(self):
        self.o = {'+': __add__, '-': __sub__, '*': __mul__, '/': __truediv__}

    def calc(self, s, op='*/'):
        i = 1
        while i < len(s) - 1:
            if s[i] in op:
                s[i - 1] = str(self.o[s[i]](float(s[i - 1]), float(s[i + 1])))
                del s[i:i + 2]
                i -= 2
            i += 1
        return self.calc(s, op='+-') if op == '*/' else s[0]

    def parenthesis_calc(self):
        start = [i for i, e in enumerate(self.s) if e == '('][-1]
        end = [i for i, e in enumerate(self.s[start:]) if e == ')'][0] + start
        self.s[start] = self.calc(self.s[start + 1:end])
        del self.s[start + 1: end + 1]

    def evaluate(self, string):
        self.s = string.split(' ')
        while '(' in self.s:
            self.parenthesis_calc()
        self.s = self.calc(self.s)
        return float(self.s)
