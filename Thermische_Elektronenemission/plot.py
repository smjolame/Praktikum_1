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
def approx(I_s,a,b,U):
    return I_s-a*np.e**(-b*U)
def I(U,a,n):
    return a*U**n
def j(U,c,k):
    return c*np.e**(k*U)
U_max, I_max = np.genfromtxt('data/max.txt',delimiter=',',unpack=True) #U in V, I in mA
U_nmax, I_nmax = np.genfromtxt('data/nmax.txt',delimiter=',',unpack=True)  #U in V, I in mA

epsilon0=8.85418782    #F/m
e0=1.6021892*10**(-19)  #C
m0=9.109534*10**(-34)  #kg
h=6.62607015*10**(-34) #J*s
k_B=1.380662*10**(-23) #J/K

#a)
gebiet=21

def Saettignug(U,Is,a,b):
    return (Is-a*np.e**(-b*U))
sa1, cov1 = curve_fit(Saettignug,U_max[18:],I_max[18:],p0=[2.3,2.5,0])
sa2, cov2 = curve_fit(Saettignug,U_nmax[10:20],I_nmax[10:20],p0=[0.2,10,0])
Is1=sa1[0]
Is2=sa2[0]
Is1=ufloat(Is1,np.sqrt(cov1[0][0]))
Is2=ufloat(Is2,np.sqrt(cov2[0][0]))
print(Is1,Is2)


#b)

params, cov =curve_fit(I,U_max[:gebiet],I_max[:gebiet])
n=ufloat(params[1],np.sqrt(cov[1][1]))
print(n)

x1=np.linspace(U_max[18],300)
x2=np.linspace(U_nmax[10],100)
x=np.linspace(0,U_max[:gebiet])
plt.plot(U_max,I_max,'kx')
plt.plot(x,I(x,*params))
plt.plot(x1,Saettignug(x1,*sa1))

plt.clf()
plt.plot(U_nmax,I_nmax,'bx')
plt.plot(x2,Saettignug(x2,*sa2))



#c)
I_max=I_max*10**(-3)
R_innen=10**6
U_korr=U_max-R_innen*I_max



#nicht machbar

#d)
#Messung 1
V_f1=5   #V
I_f1=2.3   #A
#Messung 2
V_f2=4   #V
I_f2=1.8   #A

sigma=5.7*10**(-12)  #W/(cm^2 K^4)
aether=0.28   
f=0.32  #cm^2
N_wl=1  #W

def T(I,U):
    return ((I*U-N_wl)/(f*aether*sigma))**(1/4)
T1=T(I_f1,V_f1)
T2=T(I_f2,V_f2)
print(T1,T2)
#passt

#e)
def phi(Is,T):
    return-k_B*T/e0*np.log(Is*h**3/(4*np.pi*f*e0*m0*k_B**2*T**2))

phi1=phi(1.6,T1)
phi2=phi(0.227,T2)
print(phi1,phi2)
W1=e0*phi1
W2=e0*phi2
print(W1,W2)

W=ufloat(np.mean([W1,W2]),sem([W1,W2]))
print(W)








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
