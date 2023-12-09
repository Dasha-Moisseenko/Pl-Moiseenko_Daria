def v(m):
    s = 0
    k = 0
    for i in range(len(m)):
        for j in range(i+1, len(m)):
            if m[i][j] > 0:
                s += m[i][j]
                k += 1
    return s, k
c = "Daria1.txt"
c2 = "Daria2.txt"

m = []
with open(c, 'r') as file:
    for l in file:
        r = [int(x) for x in l.split()]
        m.append(r)

s, k = v(m)

with open(c2, 'w') as file:
    file.write("Сумма: " + str(s) + "\n")
    file.write("Количество: " + str(k))
