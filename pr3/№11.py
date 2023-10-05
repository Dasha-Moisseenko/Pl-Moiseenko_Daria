a=int(input())
k=0
for i in range(1,1000):
    if a>1:
        if a%i==0:
            k+=1
if k==2:
    print(a,'простое')
else:
    print(a,'непростое')
        
