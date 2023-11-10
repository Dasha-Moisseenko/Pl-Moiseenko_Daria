#ВАРИАНТ 2


#1
n=int(input('введите n ' ))
a = [ int(input('введите числа массива ')) for i in range(n) ] 
print(a.index(min(a))) 
#2
a1=[1,3434,-17,53,54,-22,-44]
a2=[];a3=[] 
for i in a1: 
    if i>0:
        a2.append(i)
    elif i<0:
        a3.append(i)
print(a2)
print(a3)
