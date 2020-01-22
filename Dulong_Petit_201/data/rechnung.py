import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
from scipy import stats
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp

k=np.genfromtxt('data/kupfer.txt',delimiter=',',unpack=True)
z=np.genfromtxt('data/zinn.txt',delimiter=',',unpack=True)
g=np.genfromtxt('data/graphit.txt',delimiter=',',unpack=True)

#daten
c_w=4.18  #joule/(gram*kelvin)
m_k=237.87 #g
m_z=204.5 #g
m_g=110 #g
#Massen für Kupfer
k1=k[:3:2,:]
k2=k[1:4:2,:]
k_m=k1-k2



np.savetxt('data/k_m.txt',np.transpose(k_m),fmt='%.2f')

#Massen für Zinn
z1=z[:3:2,:]
z2=z[1:4:2,:]
z_m=z1-z2

np.savetxt('data/z_m.txt',np.transpose(z_m),fmt='%.2f')

#Masse Graphit
g_m=np.array([g[0]-g[1],g[2]-g[3]])

np.savetxt('data/g_m.txt',g_m,fmt='%.2f')


#Bestimmung der spezifischen Wärmelapazität des derivatgefässes
wasser=np.genfromtxt('data/wasser.txt',delimiter=',',unpack=True)
wasser_m=np.array([wasser[0]-wasser[1],wasser[2]-wasser[3]])
np.savetxt('data/wasser_m.txt',wasser_m,fmt='%.2f')
c_g=(c_w*wasser_m[0]*(73.3-44.9)-c_w*wasser[1]*(44.9-20.7))/(44.9-20.7)
print(f"Wärmekapazität Wasser:{c_g}")



#spezifische wärme kapazität der stoffe
def c(m_w,m_k,T_k,T_w,T_m,):
    return (c_w*m_w+c_g)*(T_m-T_w)/(m_k*(T_k-T_m))
#kupfer
c_k=c(k_m[1,:],m_k,k[4,:],k[5,:],k[6,:])
x1=np.mean(c_k)
x2=stats.sem(c_k)
c_k_u=ufloat(x1,x2)

#graphit
c_g=c(g_m[1],m_g,g[4],g[5],g[6])#


#zinn
c_z=c(z_m[1,:],m_z,z[4,:],z[5,:],z[6,:])
x1=np.mean(c_z)
x2=stats.sem(c_z)
c_z_u=ufloat(x1,x2)

print(f"Wärmekapzität Kupfer:{c_k}")
print(f"Wärmekapzität Kupfer:{c_k_u}")
print(f"Wärmekapzität Graphit:{c_g}")
print(f"Wärmekapzität Zinn:{c_z}")
print(f"Wärmekapzität Zinn:{c_z_u}")


#mischwärme
#kupfer
t_k=k[6,:]
x1=np.mean(t_k)
x2=stats.sem(t_k)
t_k=ufloat(x1,x2)
#zinn
t_z=z[6,:]
x1=np.mean(t_z)
x2=stats.sem(t_z)
t_z=ufloat(x1,x2)
#graphit
t_g=g[6]



#Wärmekapazität volumen
def c_p(a,k,M,rho,c,T):
    return c*M-(9*(a*10**(-6))**2*k*10**9*T*M/(rho*10**6))
#kupfer
a_k=16.8
k_k=136
rho_k=8.96
M_k=63.5

c_p_k=c_p(a_k,k_k,M_k,rho_k,c_k,k[6])

#zinn
a_z=27
k_z=55
rho_z=7.28
M_z=118.7

c_p_z=c_p(a_z,k_z,M_z,rho_z,c_z,k[6])

#graphit
a_g=8
k_g=33
rho_g=2.25
M_g=12

c_p_g=c_p(a_g,k_g,M_g,rho_g,c_g,t_g)



print(f"Wärmekapazität Kupfer Volumen:{c_p_k}")
print(f"Wärmekapazität Zinn Volumen:{c_p_z}")
print(f"Wärmekapazität Graphit Volumen:{c_p_g}")

x1=np.mean(c_p_k)
x2=stats.sem(c_p_k)
c_p_k=ufloat(x1,x2)
print(f"Wärmekapazität Kupfer Volumen:{c_p_k}")

x1=np.mean(c_p_z)
x2=stats.sem(c_p_z)
c_p_z=ufloat(x1,x2)

print(f"Wärmekapazität Zinn Volumen:{c_p_z}")
