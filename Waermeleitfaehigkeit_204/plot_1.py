import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
from scipy import stats
from scipy.optimize import curve_fit

T1,T2,T3,T4,T5,T6,T7,T8,t = np.genfromtxt('data/werte1.txt',delimiter='	',unpack=True)


plt.plot(t,T1, 'r.', label='T1')
plt.plot(t,T4, 'b.', label='T4')

plt.grid()
#plt.xlabel(r'$t\:/\:\si{\s}$')
#plt.ylabel(r'$T\:/\:\si{\celsius}$')
plt.legend()
plt.savefig('data/T1T4.pdf')




