def mayor_numero(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


print(mayor_numero(3, 5, 2))
