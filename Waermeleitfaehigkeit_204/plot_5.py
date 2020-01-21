import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
from scipy import stats
from scipy.optimize import curve_fit

T1,T2,T3,T4,T5,T6,T7,T8,t = np.genfromtxt('data/werte1.txt',delimiter='	',unpack=True)

def T_78(T7,T8):
    return T7-T8

def T_21(T2,T1):
    return T2-T1

plt.plot(t,T_78(T7,T8), 'r-', label='$\Delta T$ Edelstahl')
plt.plot(t,T_21(T2,T1), 'b-', label='$\Delta T$ Messing')

plt.grid()
plt.xlabel(r'$t\:/\:\si{\s}$')
plt.ylabel(r'$T\:/\:\si{\celsius}$')
plt.legend()
plt.savefig('build/deltaT.pdf')
