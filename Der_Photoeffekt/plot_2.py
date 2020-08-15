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

U,I = np.genfromtxt('data/green.csv', unpack=True, delimiter=',')
I = I*10**(-9)


#Curvefit
def f(x,a,b):
    return a*x+b 
params, pcov = curve_fit(f,U,np.sqrt(I))
a1=ufloat(params[0],np.absolute(pcov[0][0])**0.5)
b1=ufloat(params[1],np.absolute(pcov[1][1])**0.5)

U_lin = np.linspace(np.min(U),np.max(U), 100)

print('ag =',a1)
print('bg =',b1)
#print('ag_err =',a_err)
#print('bg_err =',b_err)
print('Ug_g =', -b1/a1)
#Json
#Ergebnisse = json.load(open('data/Ergebnisse.json','r'))
#if not 'reg_green' in Ergebnisse:
#    Ergebnisse['reg_green'] = {}
#Ergebnisse['reg_green']['ag']= a1
#Ergebnisse['reg_green']['bgg']= b1
#Ergebnisse['reg_green']['U_g']= -b1/a1
#json.dump(Ergebnisse,open('data/Ergebnisse.json','w'),indent=4)
plt.xlabel(r'U\,/\,V')
plt.ylabel(r'$\sqrt{I}\,/\,mA$')
plt.plot(U, np.sqrt(I)*10**6, 'bx', label='Messwerte')
plt.plot(U_lin, f(U_lin, a1.n, b1.n)*10**6, label='Ausgleichsgerade' )
plt.legend()
plt.grid()
plt.savefig('build/green.pdf')