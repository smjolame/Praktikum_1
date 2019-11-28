import numpy as np 

#16

R2, R3, R4 =np.genfromtxt('c_wert16.txt', delimiter=',', unpack=True)

Rx=R2*(R3/R4) #Ohm

print(Rx)

L2=20.1 #mH
Lx=L2*(R3/R4) #mH

print(Lx)


#19

r2, r3, r4 =np.genfromtxt('c_wert19.txt', delimiter=',', unpack=True)

rx=r2*(r3/r4) #Ohm
print(rx)

lx=L2*(r3/r4) #mh
print(lx)