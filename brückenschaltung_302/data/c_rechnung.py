import numpy as np 
from scipy.stats import sem

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


Rxm=np.mean(Rx)
Rxs=sem(Rx)
Lxm=np.mean(Lx)
Lxs=sem(Lx)
print(f"Rxm={Rxm}, Rxs={Rxs}, Lxm={Lxm}, Lxs={Lxs}")
rxm=np.mean(rx)
rxs=sem(rx)
lxm=np.mean(lx)
lxs=sem(lx)
print(f"rxm={rxm}, rxs={rxs}, lxm={lxm}, lxs={lxs}")