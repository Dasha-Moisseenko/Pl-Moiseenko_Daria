lst=[0,1]
n=int(input("введите число"))
k=int(input("ведите число"))-1
for i in range(1,n+1):
    lst.append(lst[-2]+lst[-1])
print(sum(lst[k: len(lst)]))
