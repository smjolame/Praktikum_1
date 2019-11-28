import numpy as np 

#Wert 13
R2, R3, R4 =np.genfromtxt('a_wert13.txt', delimiter=',', unpack=True)

Rx=R2*(R3/R4) #Ohm
print(Rx)

#Wert 12
r2, r3, r4=np.genfromtxt('a_wert12.txt', delimiter=',',unpack=True)

rx=r2*(r3/r4) #Ohm
print(rx)

