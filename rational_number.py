def rationalization(num: str):
    isSignPlus = True
    if num[0] == "-":
        isSignPlus = False
        num = num[1:]
    period = ""
    point = ""
    IntNum = ""
    isPeriod = False
    if "(" in num:
        arr = num.split(".")
        IntNum = arr[0]
        for e in arr[1]:
            if isPeriod and e != ")":
                period += e
            if e != "(" and not isPeriod:
                point += e
            else:
                isPeriod = True
        divisor = ""
        for i in range(0, len(period)):
            divisor += "9"
        for i in range(0, len(point)):
            divisor += "0"
        if len(point) == 0:
            point = 0
        else:
            point = int(point)
        divisor = int(divisor)
        IntNum = int(IntNum)
        period = int(period)
        dividend = 0
        if point == 0:
            dividend = period + IntNum * divisor
        else:
            dividend = point * period - point + IntNum * divisor
    else:
        count = abs(num.find('.') - len(num)) - 1
        dividend = int(float(num) * 10 ** count)
        divisor = 10 ** count
    if isSignPlus:
        rational = RationalNum(dividend, divisor)
    else:
        rational = RationalNum(dividend * (-1), divisor)
    rational.abbreviation()
    return rational


class RationalNum(object):
    def __init__(self, m, n):
        if not (type(m) == int and type(n) == int and n != 0):
            raise IOError("числитель, знаменатель - целые числа, знаменатель != 0")
        if n < 0:
            self.m = -1 * m
            self.n = -1 * n
        else:
            self.m = m
            self.n = n

    def abbreviation(self):
        gcd = self.__gcd(self.m, self.n)
        self.m = int(self.m / gcd)
        self.n = int(self.n / gcd)

    def __gcd(self, x, y):
        gcd = 1
        if x % y == 0:
            return y
        for k in range(int(y / 2), 0, -1):
            if x % k == 0 and y % k == 0:
                gcd = k
                break
        return gcd

    def __repr__(self):
        return f"{self.m}/{self.n}"

    def __str__(self):
        return f"{self.m}/{self.n}"

    def __eq__(self, other):  # ==
        return self.m * other.n == other.m * self.n

    def __ne__(self, other):  # !=
        return self.m * other.n != other.m * self.n

    def __lt__(self, other):  # <
        return self.m * other.n < other.m * self.n

    def __le__(self, other):  # <=
        return self.m * other.n <= other.m * self.n

    def __gt__(self, other):  # >
        return self.m * other.n > other.m * self.n

    def __ge__(self, other):  # >=
        return self.m * other.n >= other.m * self.n

    def __add__(self, other):
        return RationalNum(self.m * other.n + other.m * self.n, self.n * other.n)

    def __sub__(self, other):
        return RationalNum(self.m * other.n - other.m * self.n, self.n * other.n)

    def __mul__(self, other):
        return RationalNum(self.m * other.m, self.n * other.n)

    def __truediv__(self, other):
        if other.m == 0:
            raise ZeroDivisionError
        return RationalNum(self.m * other.n, self.n * other.m)

    def __floordiv__(self, other):
        if other.m == 0:
            raise ZeroDivisionError
        return (self.m * other.n) // (other.m * self.n)

    def __mod__(self, other):
        if other.m == 0:
            raise ZeroDivisionError
        return (self.m * other.n) % (other.m * self.n)

    def decimalisation(self):
        dividend = abs(self.m)
        divisor = abs(self.n)
        decimal = str(dividend // divisor) + "."
        list = {}
        index = 0
        dividend = dividend % divisor
        if dividend == 0:
            return str(self.m / self.n)
        list[dividend] = index
        flag = False
        while not flag:
            if dividend == 0:
                break
            digit = dividend * 10 // divisor
            dividend = dividend * 10 - digit * divisor
            if dividend not in list:
                decimal += str(digit)
                index += 1
                list[dividend] = index
            else:
                decimal += str(digit) + ")"
                decimal = decimal[:list.get(dividend) + len(decimal[:decimal.index(".") + 1])] + "(" + decimal[
                                                                                                       list.get(dividend) + len(decimal[:decimal.index(".") + 1]):]
                flag = True
        if self.m < 0:
            decimal = "-" + decimal
        return decimal
