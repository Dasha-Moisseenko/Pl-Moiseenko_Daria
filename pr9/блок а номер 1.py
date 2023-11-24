import math

def f(a, b):
    if b == 0:
        return 1
    else:
        return (a ** b) / math.factorial(b)

a = 3
b = 8
print(f(a, b))
