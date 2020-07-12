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
def approx(I_s,a,b,U):
    return I_s-a*np.e**(-b*U)
U_max, I_max = np.genfromtxt('data/max.txt',delimiter=',',unpack=True)
U_nmax, I_nmax = np.genfromtxt('data/nmax.txt',delimiter=',',unpack=True)

epsilon0=8.85418782
e0=1.6021892*10**(-19)
m0=9.109534*10**(-34)

def j(V,x,a)=4/9*epsilon0*np.sqrt(2e0/m0)*V**x/a**2


pa_nmax, cov_nmax = curve_fit(approx,U_nmax,I_nmax)
print(pa_nmax[0])

plt.plot(U_max,I_max,'kx')
#plt.plot(U_nmax,I_nmax,'kx')
#plt.plot(U_nmax,approx(*pa_nmax,U_nmax))
plt.show()








#Plots###############


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
#
#json.dump(Ergebnisse,open('data/Ergebnisse.json','w'),indent=4)
