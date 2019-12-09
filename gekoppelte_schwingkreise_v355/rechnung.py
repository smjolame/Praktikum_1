import numpy as np 
 
R=73
C_k=2.19*10**(-9)
L=23.954*10**(-3)
C=0.028*10**(-9)

Ip=1/(R*np.sqrt(4+(R**2*C_k**2)/(L*C)))
print(Ip)
