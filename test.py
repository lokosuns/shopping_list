class Calculator:

    def __init__(self, num):
        self.num = num
        self.buffer = []

    def plus(self, value):
        self.buffer.append(
            ('plus', value)
        )
        return self

    def minus(self, value):
        self.buffer.append(
            ('minus', value)
        )
        return self

    def calc(self):
        for oper, value in self.buffer:
            if oper == 'plus':
                self.num += value
            elif oper == 'minus':
                self.num -= value
        return self.num

print(Calculator(10).plus(5).minus(7).calc())