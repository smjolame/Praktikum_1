import numpy as np
import math

x , y =np.genfromtxt('data/Hysteresekurve.txt',delimiter=',', unpack=True)

def z(I):
    return 595*I/((2*math.pi*0.185)-0.003)

h=-z(x)


m1=(y[4]-y[3])/(h[4]-h[3])
m2=(y[16]-y[15])/(h[16]-h[15])    


k1=y[3]-m1*h[3]
t1=-k1/m1
k2=y[15]-m2*h[15]
t2=-k2/m2

print(t1)
print(t2)