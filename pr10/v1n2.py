#Первый вариант номер 2
n=open('Daria-Moiseenko_yb-32_1.txt')
z2=open('Daria-Moiseenko_yb-32_2.txt','w')
A = []
for i in n:
    p = [int(y) for y in i.split()]
    A.append(p)

max = 0
for i in range(len(A)):
    for j in range(len(A[i])):
        if max<A[i][j]:
            max=A[i][j]
z2.write('Максимльное значение:' + str(max) + '\n')
min=A[i][j]
for i in range(len(A)):
    for j in range(len(A[i])):
        if min>A[i][j]:
            min=A[i][j]
z2.write('Минимальное значение:' + str(min))
