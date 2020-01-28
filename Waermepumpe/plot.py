import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
from scipy import stats
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp


t , T_1 , T_2 , p_a , p_b , P = np.genfromtxt('data/daten.txt',delimiter=',', unpack =True)
p_a=(p_a+1)*10**5 #Atmosphärendruck pascal aufaddiert
p_b=(p_b+1)*10**5
t=t*60  #Zeit in Sekunden
T_1=T_1+273.15 #Temp in Kelvin
T_2=T_2+273.15
N=ufloat(np.mean(P),stats.sem(P)) #watt
cm_w=4.18*0.997*3000  #wärmekapazität wasser J/K
R=8.314462618  # allgm Gaskonstante  J/(mol*K)
rho_0=5.510 #kg/m^3
kappa=1.14
p_0=100000  #atmosphärendruck in Pascal

#funktionen
def a(t,A,B,C):
    return A*t**2+B*t+C
def da(t,A,B):
    return 2*A*t+B
def dm(dT,L):
    return ((cm_w+750)*dT/L)


#Fit temp
##########################################
params_T1 ,  cov_T1 =curve_fit(a,t,T_1)
params_T2 ,  cov_T2 =curve_fit(a,t,T_2)

A1=ufloat(params_T1[0],np.sqrt(np.absolute(cov_T1[0,0])))
B1=ufloat(params_T1[1],np.sqrt(np.absolute(cov_T1[1,1])))
C1=ufloat(params_T1[2],np.sqrt(np.absolute(cov_T1[2,2])))

A2=ufloat(params_T2[0],np.sqrt(np.absolute(cov_T2[0,0])))
B2=ufloat(params_T2[1],np.sqrt(np.absolute(cov_T2[1,1])))
C2=ufloat(params_T2[2],np.sqrt(np.absolute(cov_T2[2,2])))


t_lin=np.linspace(np.min(t),np.max(t))

#Plots
############################################
plt.plot(t,T_1,'rx',label='Temp. T1')
plt.plot(t,T_2,'bx',label='Temp. T2')
plt.plot(t_lin,a(t_lin,*params_T1),'r-',label='Ausgleich T1')
plt.plot(t_lin,a(t_lin,*params_T2),'b-',label='Ausgleich T2')
plt.ylabel(r'$T \:/\: \si{\kelvin}$')
plt.xlabel(r'$t \:/\: \si{\s}$')

plt.grid()
plt.legend()
plt.savefig('build/temp.pdf')

plt.clf()

##########################################
#minute 4(t[5]), 9(t[10]), 14(t[15]), 18(t[19])

dt=np.array([5,10,15,19])

#Ableitung an den Stellen bei T1:
da1 = da(t[dt],A1,B1)

#Ableitung an den Stellen bei T2:
da2 = da(t[dt],A2,B2)


#güteziffer
###############################################
#ideal
v_id=T_1[dt]/(T_1[dt]-T_2[dt])

#real
v_re=(cm_w+750)*da1/N 



#massendurchsatz
######################################
T_lin=np.linspace(np.min(1/T_1),np.max(1/T_1))

def l(t,a,b):
    return (a*t+b)

params_L, cov_L=curve_fit(l,1/T_1,np.log(p_b/p_0))

plt.plot(1/T_1,np.log(p_b/p_0),'rx',label='Messwerte')
plt.plot(T_lin,l(T_lin,*params_L),'r-',label='Ausgleichsgerade')
plt.xlabel(r'$\frac{1}{T_1} \:/\:  \frac{1}{\si{\s}}$')
plt.ylabel(r'$\ln\left(\frac{p_b}{p_0}\right)$')
plt.legend()
plt.tight_layout()
plt.grid()
plt.savefig('build/L.pdf')


a=ufloat(params_L[0],np.sqrt(np.absolute(cov_L[0,0])))
L=-a*R #J/mol



dm=dm(da2,L) #mol/s
dm=dm*0.121 #mit kg/mol multipliziert -> #kg/s



rho=rho_0*273.15*p_a[dt]/(T_2[dt]*p_0)
N_mech=1/(kappa-1)*(p_b[dt]*(p_a[dt]/p_b[dt])**(1/kappa)-p_a[dt])/rho*dm #watt

print(f"Wärmekapazität Wasser {cm_w}")
print(f"Parameter T1: A1: {A1}, B1: {B1}, C1: {C1}")
print(f"Parameter T2: A2: {A2}, B2: {B2}, C2: {C2}")
print(f"Ausgewählte Zeiten {t[dt]}")
print(f"Steigungen für T1: {da1}")
print(f"Steigungen für T2: {da2}")
print(f"Güteziffer ideal: {v_id}")
print(f"Güteziffer real: {v_re}")
print(f"Steigung für Wärmedruck: {a}")
print(f"Verdampfungswärme: {L} J/mol")
print(f"Massendurchsatz: {dm} kg/s")
print(f"Kompressorleistung: {N_mech} watt")
print(f"Temperaturn an den Zeitpunkten T1: {T_1[dt]}")
print(f"Temperaturn an den Zeitpunkten T2: {T_2[dt]}")
print(f"Leistung des Kompressores: {N}")
print(f"Steigung der Geraden: {a}")

#abweichung
def ab(soll,ist):
    return (soll-ist)/soll*100
print(f"Abweichung {ab(v_id,v_re)}")