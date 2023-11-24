n=int(input())
A=[]
for i in range(n):
    b=[]
    for j in range(n):
        print('Введите [',i,',',j,'] элемент')
        b.append(int(input()))
    A.append(b)
for i in range(n):
    for j in range(n):
        print(A[i][j], end=' ')
    print()
S=0
k=0
for i in range(len(A)):
    for j in range(i+1, len(A)):
        S += A[i][j]
        k += 1
print('Сумма всех элементов:', S, 'Число элементов:', k)

            
            
