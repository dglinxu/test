def zdgys(x, y):
    x, y = (y, x) if x > y else (x, y)
    for i in range(x, 0, -1):
        if x % i == 0 and y % i == 0:
            return i


def zxgys(x, y):
    return x*y//(zdgys(x, y))


print(zdgys(9, 6), zxgys(9, 6))


def gcd(x, y):
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor


def lcm(x, y):
    return x * y // gcd(x, y)


print(gcd(9, 6), lcm(9, 6))
