import numpy as np 
from scipy.stats import sem

#Wert 9
R2, R3, R4 , C2=np.genfromtxt('b_wert9.txt', delimiter=',', unpack=True)

Rx=R2*(R3/R4) #Ohm

print(Rx)

Cx=C2*(R4/R3) #nF

print(Cx)

Rxm=np.mean(Rx)
Rxs=sem(Rx)
Cxm=np.mean(Cx)
Cxs=sem(Cx)
print(f"Rxm={Rxm}, Rxs={Rxs}, Cxm={Cxm}, Cxs={Cxs}")