


import math
x=1.825*10**2
y=18.225
z=-3.298*10**-2
s=((math.fabs(x**(y/x)-(math.sqrt(y/x)**(1/3))))+((y-x)*(((math.cos(y))-(z/(y-x)))/(1+(y-x)**2))))
print("s={0:.6f}".format(s))
