import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as const
import json
from scipy.optimize import curve_fit
from uncertainties import ufloat
from uncertainties.unumpy import uarray
from uncertainties import unumpy as unp
from uncertainties.unumpy import (nominal_values as noms,std_devs as stds)

def abw(exact,approx):
    return (exact-approx)*100/exact  #Abweichnung

def f(x,a,b):
    return a*x + b 

def f2(x,a):
    return a*x 

def c(a):
    return 1/a * 10**6 #m/s


L,T2 = np.genfromtxt('data/durchschallung.txt',delimiter=',', unpack=True)

L = L/1000

params,pcov = curve_fit(f,L,T2)
a2 = params[0]
b2 = params[1]

#Fehler berechnen
a2_err = np.absolute(pcov[0][0])**0.5
b2_err = np.absolute(pcov[1][1])**0.5

a2_c = ufloat(a2,a2_err)
b2_c = ufloat(b2,b2_err)

x_linspace = np.linspace(np.min(L),np.max(L),100)
plt.plot(x_linspace, f(x_linspace,*params), 'b-', label='Ausgleichskurve')
plt.plot(L, T2, 'ro', label='Messwerte')
plt.xlabel(r'$l \:/\: \si{\meter}$')
plt.ylabel(r'$t \:/\: \si{\micro\second}$')
plt.legend()
plt.savefig('build/durchschallung.pdf')
print('a und b bei durchschallung')
print(a2_c)
print(b2_c)
print('schallgeschwindigkeit')
print(c(a2_c))
