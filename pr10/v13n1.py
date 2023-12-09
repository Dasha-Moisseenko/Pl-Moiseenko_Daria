def v(m):
    y = []
    for i in range(len(m)):
        if i % 2 == 1:  
            b = min(m[i])
            y.append(b)
    return y
def b(n):
    with open(n, 'r') as file:
        ls = file.readlines()
        matrix = [[int(k) for k in l.split()] for l in ls]
    return matrix

def z(r, n):
    with open(n, 'w') as file:
        file.write(' '.join(map(str, r)) + '\n')

c = 'Daria1.txt'
c2 = 'Daria2.txt'

matrix = b(c)
p = v(matrix)
z(p, c2)
