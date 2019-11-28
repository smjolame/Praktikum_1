import numpy as np 


#Wert 19
R2, R3, R4 ,C4 =np.genfromtxt('d_wert19.txt', delimiter=',', unpack=True)

Rx=R2*(R3/R4) #Ohm

print(Rx)

Lx=R2*R3*C4 #nH
print(Lx)

