# Find the greatest common denominator of two numbers

def euclid(x, y):
    assert x >= 0 and y >= 0, f"x={x} and y={y} cannot be negative"
    while y != 0:
        r = x % y
        x = y
        y = r
    return x

print(euclid(2, 4))
print(euclid(18, 27))
print(euclid(7, 11))
