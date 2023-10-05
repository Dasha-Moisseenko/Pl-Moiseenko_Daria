import math
x=12.3*10**(-1)
y=15.4
z=0.252*10**3
s=((y**(x+1))/((math.sqrt(math.fabs(y-2)))+3))+((x+(y/2))/(2*(math.fabs(x+y))))*((x+1)**(-1/(math.sin(z))))
print("s={0:.6f}".format(s))
