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

def abw(exact,approx):
    return (exact-approx)*100/exact  #Abweichnung

l = 825  #Abstand Spalt und Messgerät in mm
lam = 633*10**(-9) #wellenlänge Laser in m
b_lit = 0.00015 #spaltbreite in m
x , I = np.genfromtxt( 'data/data.txt',delimiter=',',unpack=True)
def B2(phi,A0,b):
    return A0**2*b**2*(lam/(np.pi*b*np.sin(phi)))**2*np.sin(np.pi*b*np.sin(phi)/lam)**2


#Wechsel der Skalierung

I1=I[0:6]
I2=I[6:8]
I3=I[8:16]
I4=I[16:35]
I5=I[35:38]
I6=I[38:40]
I7=I[40:]

I1=I1*0.3*10**(-6)
I2=I2*0.1*10**(-6)
I3=I3*0.03*10**(-6)
I4=I4*10*10**(-9)
I5=I5*0.3*10**(-6)
I6=I6*0.1*10**(-6)
I7=I7*0.03*10**(-6)


I=np.concatenate((I1,I2,I3,I4,I5,I6,I7))

#Dunkelstrom abziehen
I=I-6.4*10*10**(-9)
x=x-27.5

phi=np.arctan(x/l)

plt.plot(phi,I*10**(6),'k.',label='Messwerte')
plt.grid()

#suchen nach Indices, bei den x[i] = 0 ist, da durch x geteilt wird
krit=[]
for i in range(56):
    if phi[i]==0:
        krit.append(i)

#löschen der Werte an den kritischen Punkten
for i in krit:
    I=np.delete(I,i)
    phi=np.delete(phi,i)

phi_lin=np.linspace(np.min(phi),np.max(phi),10000)

params , cov =curve_fit(B2,phi,I,p0=[0.0004,0.00001])
A0=ufloat(params[0],np.sqrt(cov[0][0]))
b=ufloat(params[1],np.sqrt(cov[1][1]))

plt.plot(phi_lin,B2(phi_lin,params[0],params[1])*10**(6),label='Ausgleichskurve')
plt.xlabel(r'$\phi \:/\: \si{\radian}$')
plt.ylabel(r'$I \:/\: \si{\micro\ampere}$')
plt.legend()
plt.savefig('build/graph.pdf')

abw=abw(b_lit,b)
print(abw)
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
