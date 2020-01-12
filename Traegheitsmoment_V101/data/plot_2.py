import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
from scipy import stats
from scipy.optimize import curve_fit



def I_symz(m,R):
    return m/2*R**2
def I_asymz(m,R,h):
    return m*((R**2)/4+(h**2)/12)

T = np.genfromtxt('data/sym.txt', delimiter=',',unpack=True)
I = np.genfromtxt('data/asym.txt', delimiter=',',unpack=True)



print(np.mean(T))
print(stats.sem(T))
print(np.mean(I))
print(stats.sem(I))









