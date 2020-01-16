import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
from scipy import stats
from scipy.optimize import curve_fit

T1,T2,T3,T4,T5,T6,T7,T8,t = np.genfromtxt('data/GLXportRun3.txt', unpack=True, delimiter='  ')

plt.plot(t,T7, 'rx', label='T7_2')
plt.plot(t,T8, 'bx', label='T8_2')

plt.grid()
#plt.xlabel(r'$t\:/\:\si{\s}$')
#plt.ylabel(r'$T\:/\:\si{\celsius}$')
plt.legend()
plt.savefig('data/T7T8')