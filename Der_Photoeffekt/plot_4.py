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

def f(x,a,b):
    return a*x + b

c = 299792458 #m/s
h = 6.626 *10**(-34) #Js
e0 = -1.602 *10**(-19) #C

lamb = np.array([578,546,434])
lamb = lamb*10**(-9)
U = uarray([-0.66, -0.48,-1.28],[0.31,0.19,0.35])
nu = c/lamb
params, pcov = curve_fit(f,nu, unp.nominal_values(U), sigma=unp.std_devs(U))
a=ufloat(params[0],np.absolute(pcov[0][0])**0.5)
b=ufloat(params[1],np.absolute(pcov[1][1])**0.5)

nu_lin = np.linspace(np.min(nu),np.max(nu), 100)

print(nu)
a_th = h/e0
abw = (a-a_th)*100/a_th 
print('Experimentel: h/e_0 =',a,', b =', b)
print('Theorie: h/e_0 =',a_th)
print('Abweichung:',abw,'%')

plt.xlabel(r'$v \,/\, Hz$')
plt.ylabel(r'$U \,/\, V$')
plt.plot(nu, unp.nominal_values(U), 'bx', label='Messwerte')
plt.plot(nu_lin, f(nu_lin,a.n,b.n), 'r-', label='Ausgleichsgerade')
plt.legend()
plt.grid()
plt.savefig('build/grenz.pdf')
