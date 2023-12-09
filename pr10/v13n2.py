with open('Daria1.txt', 'r') as file:
    a = [[int(k) for k in line.split(',')] for line in file]

def f(m):
    ml = m[0][0]
    mnl = m[0][0]
    for r in m:
        for el in r:
            if el > ml:
                ml = el
            if el < mnl:
                mnl = el
    return ml, mnl

def s(m):
    ml, mnl = f(m)
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == ml:
                m[i][j] = mnl
            elif m[i][j] == mnl:
                m[i][j] = ml
    return m

h = s(a)

with open('Daria2.txt', 'w') as file:
    for r in h:
        file.write(','.join([str(k) for k in r]) + '\n')
