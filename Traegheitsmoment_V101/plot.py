import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
from scipy import stats
from scipy.optimize import curve_fit


def D(F,r,phi):
    return F*r/phi
def reg(x,a,b):
    return a*x+b
def I_symz(m,d):
    return m/2*(d/2)**2
def I_asymz(m,d,h):
    return m*(((d/2)**2)/4+(h**2)/12)
def V_z(d,h):
    return (d/2)**2*np.pi*h



phi, F = np.genfromtxt('data/feder.txt', delimiter=',',unpack=True) 

##Berechnung von der Winkelrichtgröße 

D=D(F,0.1,phi*np.pi/180)
D_err=stats.sem(D)
D=np.mean(D)
data = [D,D_err]
D_u=ufloat(D,D_err)
np.savetxt('data/D.txt',data,fmt="%1.6f")

print(f"Winkelrichtgröße = {D_u}")


##

##Eigenträgheitsmoment

r , T = np.genfromtxt('data/eigentr.txt',delimiter=',',unpack=True)
r=r*10**(-2)

params, cov = curve_fit(reg,r**2,T**2)
b_err=np.sqrt(cov[1,1])
b=params[1]
b=ufloat(b,b_err)
I_D=b*D_u/(4*np.pi**2)
print(f"Eigenträgheitsmoment = {I_D}")  
print(f"b={b}")  

##

##Trägheitsmoment eines Körpers in Abhängigkeit der Periodendauer
def I(T):
    return (D_u*T**2/(4*np.pi**2))-I_D
##

##Experimentell bestimmte Trägheitsmomente der Puppe
T_f1=np.genfromtxt('data/fig1.txt',unpack=True)
T_f1=ufloat(np.mean(T_f1),stats.sem(T_f1))
T_f2=np.genfromtxt('data/fig2.txt',unpack=True)
T_f2=ufloat(np.mean(T_f2),stats.sem(T_f2))

print(f"Periodendauer bei pos 1: {T_f1}")
print(f"Periodendauer bei pos 2: {T_f2}")

I_f1=I(T_f1)
print(f"Trägheitsmoment Puppe Pos 1: {I_f1}")
I_f2=I(T_f2)
print(f"Trägheitsmoment Puppe Pos 2: {I_f2}")
##

##Theoretische Werte Trägheismoment Puppe
m_puppe=0.168 #Kg
V_arm=V_z(0.013,0.135) #m^3
V_arme=2*V_arm
V_kopf=V_z(0.021,0.05)
V_rumpf=V_z(0.038,0.095)
V_bein=V_z(0.015,0.15)
V_beine=2*V_bein
V_puppe=V_arme+V_beine+V_rumpf+V_kopf
def m_z(V):
    return m_puppe*V/V_puppe
m_arm=m_z(V_arm)
m_bein=m_z(V_bein)
m_kopf=m_z(V_kopf)
m_rumpf=m_z(V_rumpf)
##

V_data_p=np.array([V_kopf,V_rumpf,V_bein,V_arm,V_puppe])
np.savetxt('data/V_puppe.txt',V_data_p*10**6, "%1.3f")

#Pos 1:
I_arm1=I_asymz(m_arm,0.013,0.135)
I_arme1=(I_arm1+m_arm*(0.0675+0.019)**2)*2 #Statz von Steiner
I_bein1=I_symz(m_bein,0.015)
I_beine1=(I_bein1+m_bein*(0.019-0.0075)**2)*2
I_rumpf=I_symz(m_rumpf,0.038)
I_kopf=I_symz(m_kopf,0.021)
I_puppe1=I_arme1+I_beine1+I_rumpf+I_kopf
I_data1=([I_kopf,I_rumpf,I_beine1,I_arme1])
np.savetxt('data/I_Pos1.txt',I_data1)
print(f"Th. Trägheitsmoment Puppe Pos 1: {I_puppe1}")
#Pos 2:
I_arme2=I_arme1
I_bein2=I_asymz(m_bein,0.015,0.15)
I_beine2=(I_bein2+m_bein*np.sqrt((0.075**2+(0.019-0.0075)**2))**2)*2
I_puppe2=I_arme2+I_beine2+I_rumpf+I_kopf
I_data2=([I_kopf,I_rumpf,I_beine2,I_arme2])
np.savetxt('data/I_Pos2.txt',I_data2)
print(f"Th. Trägheitsmoment Puppe Pos 2: {I_puppe2}")
################################################


x=np.linspace(r[0],r[np.size(r)-1])

plt.plot(r**2,T**2,'rx',label='Quadtrat der Messwerte')
plt.plot(x**2,reg(x**2,params[0],params[1]),'b-',label='Ausgleichsgerade')
plt.grid()
plt.xlabel(r'$r^2\:/\: \si{\m^2}$')  
plt.ylabel(r'$T^2\:/\: \si{\s^2}$')  
plt.legend()
plt.savefig('data/Ausgleichsgerade.pdf')



