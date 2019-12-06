import numpy as np 
import scipy.constants as const

def B(N,I,l):
    return (const.mu_0*N*I/l)
    

l=B(300,1,0.163)
k=B(100,1,0.053)
d=B(3400,0.25,0.092)


def Bh(N,I,R):
    return (const.mu_0*N*I/((5/4)**(3/2)*R))
    
p=Bh(100,5,0.0625)
print(l)
print(k)
print(d)
print(p)