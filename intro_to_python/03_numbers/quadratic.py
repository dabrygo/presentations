import abc

class Quadratic(abc.ABC):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def roots(self):
        d = Quadratic.discriminant(self.a, self.b, self.c)
        root1 = (-self.b + self.sqrt(d)) / 2 * self.a
        root2 = (-self.b - self.sqrt(d)) / 2 * self.a
        return root1, root2
    
    @abc.abstractmethod
    def sqrt(self, n):
        pass

    @staticmethod
    def discriminant(a, b, c):
        return b**2 - 4*a*c


class Real(Quadratic):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

    def sqrt(self, n):
        import math
        return math.sqrt(n)


class HelpfulReal(Quadratic):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

    def sqrt(self, n):
        import math
        d = self.discriminant(self.a, self.b, self.c)
        if d < 0:
            raise Exception(f"Negative discriminant {d} for ({self.a}, {self.b}, {self.c})")
        return math.sqrt(n)


class Complex(Quadratic):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

    def sqrt(self, n):
        import cmath
        return cmath.sqrt(n)


# Real solution
real = Real(1, 0, -1)
print(real.roots())

# DomainError if roots complex
try:
    real = Real(1, 0, 1)
    print(real.roots())
except ValueError as e:
    print(e)

# Custom error if roots complex
try:
    real = HelpfulReal(1, 0, 1)
    print(real.roots())
except Exception as e:
    print(e)

# Complex can solve real roots
complex_ = Complex(1, 0, -1)
print(complex_.roots())

# Complex can solve complex roots
complex_ = Complex(1, 0, 1)
print(complex_.roots())
