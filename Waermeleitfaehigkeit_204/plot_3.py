import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
from scipy import stats
from scipy.optimize import curve_fit

x,T1,T2,T3,T4,T5,T6,T7,T8,t = np.genfromtxt('data/werte2.txt',delimiter='	',unpack=True)

plt.plot(t,T1, 'r.', label='T1_2')
plt.plot(t,T2, 'b.', label='T2_2')

plt.grid()
#plt.xlabel(r'$t\:/\:\si{\s}$')
#plt.ylabel(r'$T\:/\:\si{\celsius}$')
plt.legend()
plt.savefig('data/T1T2.pdf')