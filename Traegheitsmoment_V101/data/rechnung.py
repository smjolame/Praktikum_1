import matplotlib as plt
import numpy as np
from uncertainties import ufloat
from scipy import stats
from scipy.optimize import curve_fit

def D(F,r,phi):
    return F*r/phi
def reg(x,a,b):
    return a*x+b

phi, F = np.genfromtxt('data/feder.txt', delimiter=',',unpack=True)

D=D(F,0.1,phi*np.pi/180)

D_err=stats.sem(D)
D=np.mean(D)
D_data=np.array([D,D_err])
np.savetxt('D.txt',D_data,fmt="%1.6f")

print(D)
print(D_err)

r , T = np.genfromtxt('data/eigentr.txt',delimiter=',',unpack=True)
r=r*10**(-2)

params, cov = curve_fit(reg,r**2,T**2)
I_D=params[1]/(4*np.pi**2)
I_D_err=np.sqrt(cov[1,1])
print(I_D)
print(I_D_err)



