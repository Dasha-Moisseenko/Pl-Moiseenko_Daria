#Первый вариант номер 2

n=int(input('Введите количество строк:'))
m=int(input('Введите количество столбцов:'))
A=[]
for i in range(n):
    b=[]
    for j in range(m):
        print('Введите [',i,',',j,'] элемент')
        b.append(int(input()))
    A.append(b)
for i in range(n):
    for j in range(m):
        print(A[i][j], end=' ')
    print()
max=A[i][j]
for i in range(n):
    for j in range(m):
        if max<A[i][j]:
            max=A[i][j]
print('Максимльное значение:',max)
max=A[0][0]
print(max)
min=A[i][j]
for i in range(n):
    for j in range(m):
        if min>A[i][j]:
            min=A[i][j]
print('Минимальное значение:', min)
min=A[i][-1]
print(min)

        
