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
def gerade(x,a,b):
    return a*x+b
#Spezifische Elektronenladung
def spez(a,U):
    return a**2*8*U

k_l = 0.05/8 #Kästchenlänge (m)

L = 0.175 #Wirkungsbereich des B Feldes (m)
mu_0 = 4*np.pi*10**(-7) #magn.Konst.
N = 20 #Anzahl Windungen der Spulen
R = 0.282 #Radius der Spulen (m)
U_1 = 250 #Spannug erste Versuchsdurchführung (V)
U_2 = 380 #Spannug zweite Versuchsdurchführung (V)
I_hor = 0.7 #Strom zum kompensieren des Erdmagnetfeldes (A)
phi = np.radians(58) #Inklinationswinkel (rad)
#Magnetfeld einer Helmholtzspule
def B(I):
    return mu_0*8*N*I/(np.sqrt(125)*R)

I_1, K_1 = np.genfromtxt('data/250V.txt',delimiter=',',unpack=True)
I_2, K_2 = np.genfromtxt('data/380V.txt',delimiter=',',unpack=True)
D_1 = K_1*k_l #Ablenkung der Elektronen
D_2 = K_2*k_l


 
V_1 = D_1/(D_1**2+L**2) #Verhältnis zum Bestimmen der Steigung
V_2 = D_2/(D_2**2+L**2)


#Curve Fits
pa_1 , cov_1 = curve_fit(gerade, B(I_1),V_1)
pa_2 , cov_2 = curve_fit(gerade, B(I_2),V_2)

a_1 = ufloat(pa_1[0],np.absolute(cov_1[0][0])**0.5)
b_1 = ufloat(pa_1[1],np.absolute(cov_1[1][1])**0.5)

a_2 = ufloat(pa_2[0],np.absolute(cov_2[0][0])**0.5)
b_2 = ufloat(pa_2[1],np.absolute(cov_2[1][1])**0.5)

spez_1=spez(a_1,U_1)
spez_2=spez(a_2,U_2)

spez=np.mean([spez_1,spez_2])

spez_l=17.5882001076*10**10 #Literaturwer spez Ladung
abw_spez=abw(spez_l,spez)
print(abw_spez)
#Plots
plt.plot(B(I_1)*10**3,V_1,'kx',label='Messwerte bei U=250V')
plt.plot(B(I_2)*10**3,V_2,'bx',label='Messwerte bei U=380V')
plt.plot(B(I_1)*10**3,gerade(B(I_1),noms(a_1),noms(b_1)),label='Ausgleichsgerade 250V')
plt.plot(B(I_2)*10**3,gerade(B(I_2),noms(a_2),noms(b_2)),label='Ausgleichsgerade 380V')
plt.xlabel(r'$B \:/\: \si{\milli\tesla}$')
plt.ylabel(r'$\frac{D}{L^2+D^2} \:/\: \si[per-mode=reciprocal]{\per\m}$')
plt.grid()
plt.legend()
plt.savefig('build/Kurve.pdf')

##Erdmagnetfeld

B_hor=B(I_hor)

B_tot=B_hor/np.cos(phi) #Totalintensität Erdmagnetfeld
B_l=4.91941*10**(-5)
abw_B=abw(B_l,B_tot)
print(abw_B)

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
