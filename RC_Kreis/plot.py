import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

#a)
def func(T,a,b):
    return a * T + b

t,U=np.genfromtxt('data/a.txt',delimiter=',', unpack=True)


i=np.linspace(0,2.5,1000)

popt,pcov=curve_fit(func,t,np.log(U))
print(popt)
plt.plot(t,np.log(U),'rx')
plt.plot(t,func(t,*popt))
plt.grid()

plt.savefig('build/a.pdf')
plt.clf()

#b)


f1,A=np.genfromtxt('data/b.txt',delimiter=',', unpack=True)

f1_t=np.linspace(0,1000,10000)

def Amp(w,U_0,R,C):
    return U_0/(np.sqrt(1+w**2*R**2*C**2))

params, cov_matrix=curve_fit(Amp,f1,A)

plt.plot(f1,A,'rx')
plt.plot(f1,Amp(f1,*params))
plt.grid()
plt.savefig('build/b.pdf')






#c)

f2,a,b=np.genfromtxt('data/c.txt',delimiter=',', unpack=True)



plt.plot(f2,A)
plt.grid()
plt.clf()
