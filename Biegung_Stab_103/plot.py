import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit



I_q=(0.01**4)/12    #Flaechentraegheit Quadtrat in Meter
I_r=(np.pi*0.01**4)/64  #Flaechentraegheit Kreis in Meter
m_ein=1.169+0.0406 #Masse bei einseitiger Einspannung in Kg
m_bei=0.0406+1.169+1.169+1.168+1.170 #Masse bei beidseitiger Einspannung in Kg
L_bei=0.55 #Laenge des Stabes bei beidseitiger Einpannung in Meter
L_ein=0.482 #Laenge des Stabes einseitige Einspannung in Meter

#ab hier alle x in m und alle D in m

x1,D_01,D_m1 =np.genfromtxt('data/ein_k.csv',delimiter=',', unpack=True)
x1=x1*10**(-2)
D_01=D_01*10**(-3)
D_m1=D_m1*10**(-3)
D1=D_01-D_m1










x2,D_02,D_m2 =np.genfromtxt('data/ein_a.csv',delimiter=',', unpack=True)
x2=x2*10**(-2)
D_02=D_02*10**(-3)
D_m2=D_m2*10**(-3)

D2=D_02-D_m2









x3,D_03_l,D_03_r =np.genfromtxt('data/bei_k_o.csv',delimiter=',', unpack=True)
x3,D_m3_l,D_m3_r =np.genfromtxt('data/bei_k_m.csv',delimiter=',', unpack=True)
x3=x3*10**(-2)
D_03_l=D_03_l*10**(-3)
D_03_r=D_03_r*10**(-3)
D_m3_l=D_m3_l*10**(-3)
D_m3_r=D_m3_r*10**(-3)

x3_l=0.275-x3
x3_r=0.275+x3
x3_l_flip=np.flip(x3_l)



D3_l=D_03_l-D_m3_l
D3_r=D_03_r-D_m3_r
D3_l_flip=np.flip(D3_l)







x4,D_04_l,D_04_r =np.genfromtxt('data/bei_a_o.csv',delimiter=',', unpack=True)
x4,D_m4_l,D_m4_r =np.genfromtxt('data/bei_a_m.csv',delimiter=',', unpack=True)
x4=x4*10**(-2)
D_04_l=D_04_l*10**(-3)
D_04_r=D_04_r*10**(-3)
D_m4_l=D_m4_l*10**(-3)
D_m4_r=D_m4_r*10**(-3)

x4_l=0.275-x4
x4_r=0.275+x4
x4_l_flip=np.flip(x4_l)

D4_l=D_04_l-D_m4_l
D4_r=D_04_r-D_m4_r
D4_l_flip=np.flip(D4_l)






def D_ein_k(x,E):
    return m_ein*9.81*(L_ein*x**2-((x**3)/3))/(E*2*I_r)
def D_ein_a(x,E):
    return m_ein*9.81*(L_ein*x**2-((x**3)/3))/(E*2*I_q)
def D_bei_k_l(x,E):
    return m_bei*9.81*(L_bei**2*x*3-4*x**3)/(E*48*I_r)  #beidseitig kupfer für 0<x<L/2
def D_bei_k_r(x,E):
    return m_bei*9.81*(4*x**3-12*L_bei*x**2+9*L_bei**2*x-L_bei**3)/(E*48*I_r) #beidseitig kupfer für L/2<x<L
def D_bei_a_l(x,E):
    return m_bei*9.81*(L_bei**2*x*3-4*x**3)/(E*48*I_q)  # beidseitig alu für 0<x<L/2
def D_bei_a_r(x,E):
    return m_bei*9.81*(4*x**3-12*L_bei*x**2+9*L_bei**2*x-L_bei**3)/(E*48*I_q) #beidseitig alu für L/2<x<L




#fit einseitig kupfer
params_ein_k, cov_ein_k=curve_fit(D_ein_k,x1,D1)
err_ein_k = np.sqrt(np.diag(cov_ein_k))

#fit einseitig alu
params_ein_a, cov_ein_a=curve_fit(D_ein_a,x2,D2)
err_ein_a = np.sqrt(np.diag(cov_ein_a))

#fit beidseitig links kupfer
params_bei_k_l, cov_bei_k_l=curve_fit(D_bei_k_l,x3_l_flip,D3_l_flip)
err_bei_k_l = np.sqrt(np.diag(cov_bei_k_l))


#fit beidseitig rechts kupfer
params_bei_k_r, cov_bei_k_r=curve_fit(D_bei_k_r,x3_r,D3_r)
err_bei_k_r = np.sqrt(np.diag(cov_bei_k_r))

#fit beidseitig links alu
params_bei_a_l, cov_bei_a_l=curve_fit(D_bei_a_l,x4_l_flip,D4_l_flip)
err_bei_a_l = np.sqrt(np.diag(cov_bei_a_l))

#fit beidseitig rechts alu
params_bei_a_r, cov_bei_a_r=curve_fit(D_bei_a_r,x4_r,D4_r)
err_bei_a_r = np.sqrt(np.diag(cov_bei_a_r))



###################################################################################################
#ab hier wieder in D mm und x meter
x_t=np.linspace(0,0.45)
x_t_l=np.linspace(0.15,0.27)
x_t_r=np.linspace(0.28,0.40)
x1=x1*10**(2)
D_01=D_01*10**(3)
D_m1=D_m1*10**(3)
D1=D_01-D_m1

x2=x2*10**(2)
D_02=D_02*10**(3)
D_m2=D_m2*10**(3)
D2=D_02-D_m2


x3=x3*10**(2)
D_03_l=D_03_l*10**(3)
D_03_r=D_03_r*10**(3)
D_m3_l=D_m3_l*10**(3)
D_m3_r=D_m3_r*10**(3)

x3_l=27.5-x3
x3_r=27.5+x3
x3_l_flip=np.flip(x3_l)



D3_l=D_03_l-D_m3_l
D3_r=D_03_r-D_m3_r
D3_l_flip=np.flip(D3_l)

D3_xlr=np.append(x3_l_flip,x3_r)
D3_lr=np.append(D3_l_flip,D3_r)



x4=x4*10**(2)
D_04_l=D_04_l*10**(3)
D_04_r=D_04_r*10**(3)
D_m4_l=D_m4_l*10**(3)
D_m4_r=D_m4_r*10**(3)

x4_l=27.5-x4
x4_r=27.5+x4
x4_l_flip=np.flip(x4_l)

D4_l=D_04_l-D_m4_l
D4_r=D_04_r-D_m4_r
D4_l_flip=np.flip(D4_l)

D4_xlr=np.append(x4_l_flip,x4_r)
D4_lr=np.append(D4_l_flip,D4_r)
#plots

plt.plot(x1,D1,'rx',label='Messwerte1')
plt.grid()
plt.legend()
plt.plot(x_t*10**2,D_ein_k(x_t,params_ein_k)*10**3)


plt.show()
plt.clf()



plt.plot(x2,D2,'rx',label='Messwerte2')
plt.grid()
plt.legend()
plt.plot(x_t*10**2,D_ein_a(x_t,params_ein_a)*10**3)

plt.show()
plt.clf()


plt.plot(D3_xlr,D3_lr,'rx',label='Messwerte3')
plt.grid()
plt.legend()
plt.plot(x_t_l*10**2,D_bei_k_l(x_t_l,params_bei_k_l)*10**3)
plt.plot(x_t_r*10**2,D_bei_k_r(x_t_r,params_bei_k_r)*10**3)


plt.show()
plt.clf()


plt.plot(D4_xlr,D4_lr,'rx',label='Messwerte4')
plt.grid()
plt.legend()
plt.plot(x_t_l*10**2,D_bei_a_l(x_t_l,params_bei_a_l)*10**3)
plt.plot(x_t_r*10**2,D_bei_a_r(x_t_r,params_bei_a_r)*10**3)


plt.show()
plt.clf()

