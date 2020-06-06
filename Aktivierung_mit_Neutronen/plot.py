import matplotlib.pyplot as plt
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

def gerade(x,a,b):
    return a*x+b
def T(lamb):
    return np.log(2)/lamb
def abw(exact,approx):
    return (exact-approx)*100/exact  #Abweichnung

T_V_t=224.58
T_R_1_t=42.3
T_R_2_t=260.4


#Bestimmung der Untergrundrate
N_U = np.array([129, 143, 144, 136, 139, 126, 158]) #Impulse pro 300 sek
#Vanadium
N_U_30 = N_U/10 #Impulse pro 30 sek
N_U_30_err = sem(N_U_30)
N_U_30 = np.mean(N_U_30)
N_U_30 = ufloat(N_U_30,N_U_30_err)
#Rhodium
N_U_15 = N_U/20 #Impulse pro 15 sek
N_U_15_err = sem(N_U_15)
N_U_15 = np.mean(N_U_15)
N_U_15 = ufloat(N_U_15,N_U_15_err)


#Halbwertszeit Vanadium
t_V ,N_V_roh = np.genfromtxt('data/Vanadium.dat',delimiter=',',unpack=True)


N_V_roh_err = np.sqrt(N_V_roh)
N_V_roh = uarray(N_V_roh,N_V_roh_err)
N_V = N_V_roh - N_U_30
#curve fit
#E=15 # Wert bis zur doppelten Halbwertszeit
V_params ,V_cov=curve_fit(gerade, t_V,noms(unp.log(N_V)),sigma=stds(unp.log(N_V)))
#V_params_2,V_cov_2=curve_fit(gerade, t_V[:E],noms(unp.log(N_V[:E])),sigma=stds(unp.log(N_V[:E])))
#plot
plt.plot(t_V,noms(N_V),'bx',label='bereinigte Messwerte')
plt.errorbar(t_V,noms(N_V),yerr=stds(N_V),fmt='bx',label='Unsicherheit der bereinigten Messwerte')
plt.plot(t_V,np.e**gerade(t_V,*V_params),label='Ausgleichsgerade')
plt.yscale('log')
plt.grid()
plt.legend()
plt.xlabel(r'$t \:/\: \si{\s}$')
plt.ylabel(r'$N \:/\: \si{\frac{1}{30\s}}$')
plt.savefig('build/Vanadium.pdf')
plt.clf()

#Halberwertszeit
a_V = ufloat(V_params[0],np.sqrt(V_cov[0][0]))
b_V = ufloat(V_params[1],np.sqrt(V_cov[1][1]))
T_V = T(-a_V)
#a_V_2 = ufloat(V_params_2[0],np.sqrt(V_cov_2[0][0]))
#b_V_2 = ufloat(V_params_2[1],np.sqrt(V_cov_2[1][1]))
#T_V_2=T(-a_V_2)
print(T_V_2)
#Halbertszeit Rhodium
t_R ,N_R_roh = np.genfromtxt('data/Rhodium.dat',delimiter=',',unpack=True)

N_R_roh_err = np.sqrt(N_R_roh)
N_R_roh = uarray(N_R_roh,N_R_roh_err)
N_R = N_R_roh - N_U_15
#curve fit
I=14  #geschätze Grenze Links
G=17 #geschätze Grenze/Übergang rechts
#rechter Bereich
R_params2 , R_cov2 = curve_fit(gerade,t_R[G:],noms(unp.log(N_R[G:])),sigma=stds(unp.log(N_R[G:])))
a_2=ufloat(R_params2[0],np.sqrt(R_cov2[0][0]))
b_2=ufloat(R_params2[1],np.sqrt(R_cov2[1][1]))
N_R_1=gerade(t_R,a_2,b_2)

#linker Bereich
R_params1 , R_cov1 = curve_fit(gerade,t_R[:I],noms(unp.log(N_R[:I]-unp.exp(N_R_1[:I]))),sigma=stds(unp.log(N_R[:I]-unp.exp(N_R_1[:I]))))

a_1=ufloat(R_params1[0],np.sqrt(R_cov1[0][0]))
b_1=ufloat(R_params1[1],np.sqrt(R_cov1[1][1]))

#Halbertszeit
T_R_1=T(-a_1)
T_R_2=T(-a_2)

#plot
plt.plot(t_R,noms(N_R),'kx')
plt.errorbar(t_R,noms(N_R),yerr = stds(N_R),fmt = 'kx',label='bereinigte Messwerte')
plt.plot(t_R[:I+1],np.e**gerade(t_R[:I+1],*R_params1),'r',label='Ausgleichsgerade bereinigter schneller Zerfall')
plt.plot(t_R,np.e**gerade(t_R,*R_params2),label='Augleichsgerade langsamer Zerfall')
plt.plot(t_R[:I],np.e**noms(unp.log(N_R[:I]-unp.exp(N_R_1[:I]))),'bx')
plt.errorbar(t_R[:I],np.e**noms(unp.log(N_R[:I]-unp.exp(N_R_1[:I]))),yerr=np.e**stds(unp.log(N_R[:I]-unp.exp(N_R_1[:I]))),fmt = 'bx',label='bereinigter schneller Zerfall')
plt.yscale('log')
plt.grid()
plt.legend(fontsize='small')
plt.xlabel(r'$t \:/\: \si{\s}$')
plt.ylabel(r'$N \:/\: \si{\frac{1}{15\s}}$')
plt.savefig('build/Rhodium.pdf')



abw_V=abw(T_V_t,T_V)
abw_R_1=abw(T_R_1_t,T_R_1)
abw_R_2=abw(T_R_2_t,T_R_2)


##Halberwertszeit
#a_R=ufloat(R_params[0],np.sqrt(R_cov[0][0]))
#T_R=T(-a_R)
#print(T_R)




##Curvefit
#def BeispielFunktion(x,a,b):
#    return a*x+b 
#params, cov = curve_fit(BeispielFunktion, x-Werte, y-Werte,sigma=fehler_der_y_werte,p0=[schätzwert_1,#schätzwert_2])
#a = ufloat(params[0],np.absolute(cov[0][0])**0.5)
#b = ufloat(params[1],np.absolute(cov[1][1])**0.5)
#
#


print(f"Halbertszeit Vanadium{T_V}")
print(f"Geradenparameter a Vanadium{a_V}")
print(f"Geradenparameter b Vanadium{b_V}")
print(f"Halbwertszeit Rhodium schnell{T_R_1}")
print(f"Halbertszeit Rhodium langsam{T_R_2}")
print(f"a Rhodium schnell{a_1}")
print(f"b Rhodium schnell{b_1}")
print(f"a Rhodium langsam{a_2}")
print(f"b Rhodium langsam{b_2}")
print(f"Abweichung T_V {abw_V}")
print(f"Abweichung T_R_{abw_R_1}")
print(f"Abweichung T_R_2{abw_R_2}")
