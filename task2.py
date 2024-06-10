def calculate(c1, b1):
    c = c1
    b = 0
    t = 0

    while c > 0:
        t += 2 * c
        b += c
        c = 0
        if b >= b1:
            c = 2 * (b // b1)
            b = b % b1

    return t

c1 = 10
b1 = 5

print(calculate(c1, b1))