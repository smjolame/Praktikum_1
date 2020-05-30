import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as const
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

#Bestimmung der Untergrundrate
N_U = np.array([129, 143, 144, 136, 139, 126, 158]) #Impulse pro 300 sek
#Vanadium
N_U_30 = N_U/10 #Impulse pro 30 sek
N_U_30_err = sem(N_U_30)
N_U_30 = np.mean(N_U_30)
N_U_30 = ufloat(N_U_30,N_U_30_err)
print(N_U_30)
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
V_params ,V_cov=curve_fit(gerade, t_V,np.log(noms(N_V)),sigma=np.log(stds(N_V)))
#plot
plt.plot(t_V,noms(N_V),'bx')
plt.errorbar(t_V,noms(N_V),yerr=stds(N_V),fmt='bx')
plt.plot(t_V,np.e**gerade(t_V,*V_params))
plt.yscale('log')
plt.clf()

#Halberwertszeit
a_V = ufloat(V_params[0],np.sqrt(V_cov[0][0]))
T_V = T(-a_V)
print(T_V)


#Halbertszeit Rhodium
t_R ,N_R_roh = np.genfromtxt('data/Rhodium.dat',delimiter=',',unpack=True)

N_R_roh_err = np.sqrt(N_R_roh)
N_R_roh = uarray(N_R_roh,N_R_roh_err)
N_R = N_R_roh - N_U_15
#curve fit
I=20   #geschätze Grenze/Übergang
#rechter Bereich
R_params2 , R_cov2 = curve_fit(gerade,t_R[I:],np.log(noms(N_R[I:])),sigma=np.log(stds(N_R[I:])))
a_2=ufloat(R_params2[0],np.sqrt(R_cov2[0][0]))
b_2=ufloat(R_params2[1],np.sqrt(R_cov2[1][1]))
N_R_1=gerade(t_R,a_2,b_2)

#linker Bereich
R_params1 , R_cov1 = curve_fit(gerade,t_R[:I],np.log(noms(N_R[:I]-N_R_1[:I])),sigma=np.log(stds(N_R[:I]-N_R_1[:I])))

a_1=ufloat(R_params1[0],np.sqrt(R_cov1[0][0]))
b_1=ufloat(R_params1[1],np.sqrt(R_cov1[1][1]))

#Halbertszeit
T_R_1=T(-a_1)
T_R_2=T(-a_2)
print(T_R_1)
print(T_R_2)
#plot
plt.plot(t_R,noms(N_R),'bx')
plt.errorbar(t_R,noms(N_R),yerr = stds(N_R),fmt = 'bx')
plt.plot(t_R,np.e**gerade(t_R,*R_params1))
plt.plot(t_R,noms(N_R),'bx')
plt.errorbar(t_R,noms(N_R),yerr = stds(N_R),fmt = 'kx')
plt.plot(t_R,np.e**gerade(t_R,*R_params2))
plt.yscale('log')
plt.show()

#Halberwertszeit
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

#Ergebnisse = json.load(open('data/Ergebnisse.json','r')
#if not 'Name' in Ergebnisse:
#    Ergebnisse['Name'] = {}
#Ergebnisse['Name']['Name des Wertes']=Wert
#
#json.dump(Ergebnisse,open('data/Ergebnisse.json','w'),indent=4)
