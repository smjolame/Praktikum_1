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

l,u1,t1,u2,t2 = np.genfromtxt('data/impulsecho.txt', delimiter=',', unpack=True)

l = l/1000

params,pcov = curve_fit(f,l,t2/2)
a = params[0]
b = params[1]

#Fehler berechnen
a_err = np.absolute(pcov[0][0])**0.5
b_err = np.absolute(pcov[1][1])**0.5

a_c = ufloat(a,a_err)
b_c = ufloat(b,b_err)

x_linspace = np.linspace(np.min(l),np.max(l),100)
plt.plot(x_linspace, f(x_linspace,*params), 'b-', label='Ausgleichskurve')
plt.plot(l, t2/2, 'ro', label='Messwerte')
plt.xlabel(r'$l \:/\: \si{\meter}$')
plt.ylabel(r'$t \:/\: \si{\micro\second}$')
plt.legend()
plt.savefig('build/impulsecho.pdf')
print('a und b bei echo impuls')
print(a_c)
print(b_c)
print(c(a_c))

plt.clf()

G = np.log(u2/u1)

params2,pcov2 = curve_fit(f,l,G)
a2 = params2[0]
b2 = params2[1]

#Fehler berechnen
a2_err = np.absolute(pcov2[0][0])**0.5
b2_err = np.absolute(pcov2[1][1])**0.5
Ergebnisse = json.load(open('data/Ergebnisse.json','r'))
if not 'Impuls2' in Ergebnisse:
    Ergebnisse['Impuls2'] = {}
Ergebnisse['Impuls2']['a[A]'] = a2
Ergebnisse['Impuls2']['a_err[A]'] = a2_err
Ergebnisse['Impuls2']['b[V]'] = b2
Ergebnisse['Impuls2']['b_err[V]'] = b2_err
json.dump(Ergebnisse,open('data/Ergebnisse.json','w'),indent=4)

x_linspace2 = np.linspace(0,np.max(l),100)
plt.plot(x_linspace2, f(x_linspace2,*params2), 'b-', label='Ausgleichskurve')
# Plot der Daten
plt.plot(l,G , 'ro', label='Messwerte')

# Achsenbeschriftung
plt.xlabel(r'$l \:/\: \si{\meter}$')
plt.ylabel(r'$\ln(\frac{U_\text{R}}{U_\text{A}})')
plt.legend()
plt.savefig('build/alpha.pdf')
##Curvefit
#def BeispielFunktion(x,a,b):
#    return a*x+b 
#params, cov = curve_fit(BeispielFunktion, x-Werte, y-Werte,sigma=fehler_der_y_werte,p0=[schätzwert_1,#schätzwert_2])
#a = ufloat(params[0],np.absolute(cov[0][0])**0.5)
#b = ufloat(params[1],np.absolute(cov[1][1])**0.5)
#
#
##Json
#Ergebnisse = json.load(open('data/Ergebnisse.json','r'))
#if not 'Name' in Ergebnisse:
#    Ergebnisse['Name'] = {}
#Ergebnisse['Name']['Name des Wertes']=Wert
