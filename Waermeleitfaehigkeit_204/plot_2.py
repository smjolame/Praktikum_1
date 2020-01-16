import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
from scipy import stats
from scipy.optimize import curve_fit

T1,T2,T3,T4,T5,T6,T7,T8,t = np.genfromtxt('data/GLXportRun1.txt', unpack=True, delimiter='  ')

plt.plot(t,T5, 'rx', label='T5')
plt.plot(t,T8, 'bx', label='T8')

plt.grid()
plt.xlabel(r'$t\:/\:\si{\s}$')
plt.ylabel(r'$T\:/\:\si{\celsius}$')
plt.legend()
plt.savefig('data/T5T8')





