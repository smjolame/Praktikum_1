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
# params, pcov = curve_fit(f,U,np.sqrt(I))
# a1 = params[0]
# b1 = params[1]
# #Fehler
# a_err = np.absolute(pcov[0][0])**0.5
# b_err = np.absolute(pcov[1][1])**0.5

params, pcov = curve_fit(f,U,np.sqrt(I))
a1=ufloat(params[0],np.absolute(pcov[0][0])**0.5)
b1=ufloat(params[1],np.absolute(pcov[1][1])**0.5)


U_lin = np.linspace(np.min(U),np.max(U), 100)

print('ay =',a1)
print('by =',b1)
#print('ay_err =',a_err)
#print('by_err =',b_err)
print('Uy_g =', -b1/a1)
#print('Uy_gerr =', -a_err/b_err)
#Json
#Ergebnisse = json.load(open('data/Ergebnisse.json','r'))
#if not 'reg_yellow' in Ergebnisse:
#    Ergebnisse['reg_yellow'] = {}
#Ergebnisse['reg_yellow']['ay']= a1
#Ergebnisse['reg_yellow']['by']= b1
#Ergebnisse['reg_yellow']['U_g']= -b1/a1
#json.dump(Ergebnisse,open('data/Ergebnisse.json','w'),indent=4)
plt.xlabel(r'U\,/\,V')
plt.ylabel(r'$\sqrt{I}\,/\,\sqrt{mA}$')
plt.plot(U, np.sqrt(I)*10**6, 'bx', label='Messwerte')
plt.plot(U_lin, f(U_lin, a1.n, b1.n)*10**6, label='Ausgleichsgerade' )
plt.legend()
plt.grid()
plt.savefig('build/yellow.pdf')