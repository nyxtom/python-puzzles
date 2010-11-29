def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def binet(n):
    phi = (1 + 5**0.5) / 2
    return round((phi**n - (1 - phi)**n) / 5**0.5)

def rangefib(start, stop, step=1):
    a, b = start, 0
    list = []
    while True:
        b, a = binet(a), a + step
        if b < stop:
            list.append(b)
        else:
            break
    return list
