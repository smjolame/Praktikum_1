import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


def func(T,a,b):
    return a * T + b

t,U=np.genfromtxt('data/a.txt',delimiter=',', unpack=True)


i=np.linspace(0,2.5,1000)

popt,pcov=curve_fit(func,t,np.log(U))
print(popt)
plt.plot(t,np.log(U),'rx')
plt.plot(t,func(t,popt[0],popt[1]))
plt.grid()
plt.clf()
plt.savefig('bulid/a.pdf')



f1,A=t,U=np.genfromtxt('data/b.txt',delimiter=',', unpack=True)
plt.plot(f1,A)
plt.grid()
plt.clf()

f2,a,b=np.genfromtxt('data/c.txt',delimiter=',', unpack=True)
plt.plot(f2,A)
plt.grid()
plt.clf()
