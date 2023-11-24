#третий вариант номер 1

import math
def z(x, y):
    z = math.sqrt(x**2+y**2)
    return z
A = []
for i in range(2):
    print('Введите катеты', i, '-го треугольника')
    a = int(input('a:'))
    b = int(input('b:'))
    A.append(z(a, b))
for i in range(2):
    print('Гипотенуза', i, '-го треугольника {:2f}'.format(A[i]))
if A[0]>A[1]:
    print('Гипотенуза 0-го треугольника больше:', A[0], 'а гипотенуза 1-го меньше:', A[1])
else: print('Гипотенуза 1-го треугольника больше:', A[1], 'а гипотенуза 0-го меньше:', A[0])


#третий вариант номер 2
s='седьмая практическая работа'
ss=s.split()
r=''.join([''.join(sorted(s)) for s in ss])
print(r)

    
