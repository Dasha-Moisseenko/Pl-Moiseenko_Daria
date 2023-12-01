def f():
    z1 = z2 = 0    
    def n(z1, z2):
        c = int(input("Введите натуральное число: "))        
        if c == 0:
            return z2
        if c > z1:
            return n(c, z1)
        elif c > z2:
            return n(z1, c)
        else:
            return n(z1, z2)
    r = n(z1, z2)
    return r

r = f()
print("Второе по величине число:",r)
