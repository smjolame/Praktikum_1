import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
from scipy import stats
from scipy.optimize import curve_fit


def D(F,r,phi):
    return F*r/phi
def reg(x,a,b):
    return a*x+b
def I_symz(m,R):
    return m/2*R**2
def I_asymz(m,R,h):
    return m*((R**2)/4+(h**2)/12)



phi, F = np.genfromtxt('data/feder.txt', delimiter=',',unpack=True)

D=D(F,0.1,phi*np.pi/180)
D_err=stats.sem(D)
D=np.mean(D)
data = [D,D_err]
D_u=ufloat(D,D_err)
np.savetxt('D.txt',data,fmt="%1.6f")

print(D_u)
print(D_err)

def I(T):
    return D*T**2/(4*np.pi**2)

r , T = np.genfromtxt('data/eigentr.txt',delimiter=',',unpack=True)
r=r*10**(-2)

params, cov = curve_fit(reg,r**2,T**2)
I_D_err=np.sqrt(cov[1,1])
I_D=ufloat(params[1],I_D_err)/(4*np.pi**2)
print(I_D)    

x=np.linspace(r[0],r[np.size(r)-1])

plt.plot(r**2,T**2,'rx',label='Quadtrat der Messwerte')
plt.plot(x**2,reg(x**2,params[0],params[1]),'b-',label='Ausgleichsgerade')
plt.grid()
plt.xlabel(r'r')  #!!!!
plt.ylabel(r'T')  #!!!!
plt.legend()



