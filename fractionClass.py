

def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm % oldn
    return n


class Fraction:

    def __init__(self, top, bottom):
        """Fraction Constructor"""
        if bottom == 0:
            raise ValueError("Denominator cannot be zero!")
        if not isintance(top, int) or not isinstance(bottom,int):
            raise TypeError("Numerator and Denominator must be type int!")
        
        self.common = gcd(top, bottom)
        self.num = top // self.common
        self.den = bottom // self.common   

    def __str__(self):       
        return str(self.num) + "/" + str(self.den)

    def __add__(self, other):
        """Overloaded add function"""
        newNum = self.num * other.den + self.den * other.num
        newDen = self.den * other.den

        return Fraction(newNum, newDen)

    def __sub__(self, other):
        """Overloaded subtraction function"""
        newNum = self.num * other.den - self.den * other.num
        newDen = self.den * other.den

        return Fraction(newNum, newDen)

    def __mul__(self, other):
        """Overloaded multiplication function"""
        newNum = self.num * other.num
        newDen = self.den * other.den

        return Fraction(newNum, newDen)

    def __floordiv__(self, other):
        """Overloaded division function"""
        newNum = self.num * other.den
        newDen = self.den * other.num

        return Fraction(newNum, newDen)

    def __truediv__(self, other):
        """Overloaded division function"""
        newNum = self.num * other.den
        newDen = self.den * other.num

        return Fraction(newNum, newDen)

    """
    @staticmethod
    def gcd(a, b):
        if b != 0:
            return Fraction.gcd(b, a % b)
        else:
            return abs(a)
    """


f1 = Fraction(-3,2)
f2 = Fraction(1,-2)
print(f1 * f2)

