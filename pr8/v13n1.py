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
for i in range(len(A)):
    if i%2==1:
        c=min(A[i])
        A.append(c)
print('Минимальное значение:', c) 

