import numpy as np 
from scipy.stats import sem


#Wert 19
R2, R3, R4 ,C4 =np.genfromtxt('d_wert19.txt', delimiter=',', unpack=True)

Rx=R2*(R3/R4) #Ohm

print(Rx)

Lx=R2*R3*C4/1000000 #mH
print(Lx)

Rxm=np.mean(Rx)
Rxs=sem(Rx)
Lxm=np.mean(Lx)
Lxs=sem(Lx)
print(f"Rxm={Rxm}, Rxs={Rxs}, Lxm={Lxm}, Lxs={Lxs}")