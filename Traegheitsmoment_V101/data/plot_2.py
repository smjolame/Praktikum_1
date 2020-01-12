import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
from scipy import stats
from scipy.optimize import curve_fit

#konstanten

m = 1.1180
R = 0.0375
h = 0.0300

def I_st(m,R):
    return m/2*R**2
def I_at(m,R,h):
    return m*((R**2)/4+(h**2)/12)

D = ufloat(0.022435,0.001026)
I_eig = ufloat(0.00276,0.00015)

T_s = np.genfromtxt('data/sym.txt', delimiter=',',unpack=True)
T_a = np.genfromtxt('data/asym.txt', delimiter=',',unpack=True)

I_se = ((T_s**2)*D)/(2*np.pi)**2 - I_eig 
I_ae = ((T_a**2)*D)/(2*np.pi)**2 - I_eig


print(np.mean(I_se))

print(np.mean(I_ae))

print(I_st(1.1180,0.0375))
print(I_at(1.1180,0.0375,0.0300))









