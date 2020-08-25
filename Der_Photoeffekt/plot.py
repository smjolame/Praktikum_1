import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as const
import json
from scipy.optimize import curve_fit
from uncertainties import ufloat
from uncertainties.unumpy import uarray
from uncertainties import unumpy as unp
from uncertainties.unumpy import (nominal_values as noms,std_devs as stds)
from scipy.stats import sem

#def abw(exact,approx):
#   return (exact-approx)*100/exact  #Abweichnung

U,I = np.genfromtxt('data/yellow.csv', unpack=True, delimiter=',')
I = I*10**(-9)


#Curvefit
def f(x,a,b):
    return a*x+b 


params, pcov = curve_fit(f,U[17:],np.sqrt(I[17:]))
a1=ufloat(params[0],np.absolute(pcov[0][0])**0.5)
b1=ufloat(params[1],np.absolute(pcov[1][1])**0.5)


U_lin = np.linspace(5,-1, 100)

print('ay =',a1)
print('by =',b1)

print('Uy_g =', -b1/a1)

plt.xlabel(r'U\,/\,V')
plt.ylabel(r'$\sqrt{I}\,/\,\sqrt{mA}$')
plt.plot(U, np.sqrt(I)*10**6, 'bx', label='Messwerte')
plt.plot(U_lin, f(U_lin, a1.n, b1.n)*10**6, label='Ausgleichsgerade' )
plt.legend()
plt.grid()
plt.savefig('build/yellow.pdf')