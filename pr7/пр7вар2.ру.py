#второй вариант номер 1

import math
def s(x):
    s = ((x**2*(3**(1/2)))/4)
    return s
x = int(input('x:'))
print(6*s(x))

#второй вариант номер 2

import math
def s(x, y):
    s = x*y
    return s
A=[]
for i in range(3):
    print('Введите стороны', i, '-го прямоугольника:')
    a = int(input('a:'))
    b = int(input('b:'))
    A.append(s(a, b))
for i in range(3):
    print('площадь', i, '-го прямоугольника: {:.2f}'.format(A[i]))
    
