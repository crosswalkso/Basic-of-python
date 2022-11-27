class Calculator:
    def __init__(self, start):
        self.result = start
        print(self.result)

    def add(self, num):
        self.result += num
        print(self.result)

    def sub(self, num):
        self.result -= num
        print(self.result)


cal1 = Calculator(3)
cal2 = Calculator(2)
