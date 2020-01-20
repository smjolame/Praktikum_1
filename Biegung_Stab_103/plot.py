import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat



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



def g(x,a,b):
    return a*x+b
def lamb1(x):
    return L_ein*x**2-(x**3)/3
def lamb2(x):
    return 3*L_bei**2*x-4*x**3
def lamb3(x):
    return 4*x**3-12*L_bei*x**2+9*L_bei**2*x-L_bei**3
def g1(x,E):
    return x*m_ein*9.81/(2*E*I_r)


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




###################################################################################################
#ab hier wieder in D mm und x meter


D_01=D_01*10**(3)
D_m1=D_m1*10**(3)
D1=D_01-D_m1


D_02=D_02*10**(3)
D_m2=D_m2*10**(3)
D2=D_02-D_m2


D_03_l=D_03_l*10**(3)
D_03_r=D_03_r*10**(3)
D_m3_l=D_m3_l*10**(3)
D_m3_r=D_m3_r*10**(3)

x3_l=0.275-x3
x3_r=0.275+x3
x3_l_flip=np.flip(x3_l)



D3_l=D_03_l-D_m3_l
D3_r=D_03_r-D_m3_r
D3_l_flip=np.flip(D3_l)

D3_xlr=np.append(x3_l_flip,x3_r)
D3_lr=np.append(D3_l_flip,D3_r)




D_04_l=D_04_l*10**(3)
D_04_r=D_04_r*10**(3)
D_m4_l=D_m4_l*10**(3)
D_m4_r=D_m4_r*10**(3)

x4_l=0.275-x4
x4_r=0.275+x4
x4_l_flip=np.flip(x4_l)

D4_l=D_04_l-D_m4_l
D4_r=D_04_r-D_m4_r
D4_l_flip=np.flip(D4_l)

D4_xlr=np.append(x4_l_flip,x4_r)
D4_lr=np.append(D4_l_flip,D4_r)

#fit einseitig kupfer
params_ein_k, cov_ein_k=curve_fit(g,lamb1(x1),D1)
err_ein_k = np.sqrt(np.diag(cov_ein_k))

a_ein_k=ufloat(params_ein_k[0],err_ein_k[0])
b_ein_k=ufloat(params_ein_k[1],err_ein_k[1])
E_ein_k=m_ein*9.81/(2*I_r*a_ein_k)
print(f"a= {a_ein_k}")
print(f"b={b_ein_k}")
print(f"E={E_ein_k}")



#fit einseitig alu
params_ein_a, cov_ein_a=curve_fit(g,lamb1(x2),D2)
err_ein_a = np.sqrt(np.diag(cov_ein_a))

a_ein_a=ufloat(params_ein_a[0],err_ein_a[0])
b_ein_a=ufloat(params_ein_a[1],err_ein_a[1])
E_ein_a=m_ein*9.81/(2*I_q*a_ein_a)
print(f"a={a_ein_a}")
print(f"b={b_ein_a}")
print(f"E={E_ein_a}")

#fit beidseitig links kupfer
params_bei_k_l, cov_bei_k_l=curve_fit(g,lamb2(x3_l_flip),D3_l_flip)
err_bei_k_l = np.sqrt(np.diag(cov_bei_k_l))

a_l_k=ufloat(params_bei_k_l[0],err_bei_k_l[0])
b_l_k=ufloat(params_bei_k_l[1],err_bei_k_l[1])
E_l_k=m_bei*9.81/(48*a_l_k*I_r)
print(f"a={a_l_k}")
print(f"b={b_l_k}")
print(f"E={E_l_k}")

#fit beidseitig rechts kupfer
params_bei_k_r, cov_bei_k_r=curve_fit(g,lamb3(x3_r),D3_r)
err_bei_k_r = np.sqrt(np.diag(cov_bei_k_r))

a_r_k=ufloat(params_bei_k_r[0],err_bei_k_r[0])
b_r_k=ufloat(params_bei_k_r[1],err_bei_k_r[1])
E_r_k=m_bei*9.81/(48*a_r_k*I_r)
print(f"a={a_r_k}")
print(f"b={b_r_k}")
print(f"E={E_r_k}")

E_m_k=(E_l_k+E_r_k)/2
print(f"E_m_k={E_m_k}")

#fit beidseitig links alu
params_bei_a_l, cov_bei_a_l=curve_fit(g,lamb2(x4_l_flip),D4_l_flip)
err_bei_a_l = np.sqrt(np.diag(cov_bei_a_l))

a_l_a=ufloat(params_bei_a_l[0],err_bei_a_l[0])
b_l_a=ufloat(params_bei_a_l[1],err_bei_a_l[1])
E_l_a=m_bei*9.81/(48*a_l_a*I_q)
print(f"a={a_l_a}")
print(f"b={b_l_a}")
print(f"E={E_l_a}")

#fit beidseitig rechts alu
params_bei_a_r, cov_bei_a_r=curve_fit(g,lamb3(x4_r),D4_r)
err_bei_a_r = np.sqrt(np.diag(cov_bei_a_r))

a_r_a=ufloat(params_bei_a_r[0],err_bei_a_r[0])
b_r_a=ufloat(params_bei_a_r[1],err_bei_a_r[1])
E_r_a=m_bei*9.81/(48*a_r_a*I_q)
print(f"a={a_r_a}")
print(f"b={b_r_a}")
print(f"E={E_r_a}")

E_m_a=(E_l_a+E_r_a)/2
print(f"E_m_a={E_m_a}")


#Abweichungen
E_k=(1.23*10**8-E_ein_k)/(1.23*10**8)*100
print(f"E_abweichnung= {E_k}")
E_a=(0.71*10**8-E_ein_a)/(0.71*10**8)*100
print(f"E_abweichnung= {E_a}")
E_k=(1.23*10**8-E_m_k)/(1.23*10**8)*100
print(f"E_abweichnung= {E_k}")
E_a=(0.71*10**8-E_m_a)/(0.71*10**8)*100
print(f"E_abweichnung= {E_a}")


#plots
x1_t_ein=np.linspace(np.min(lamb1(x1)),np.max(lamb1(x1)))
x2_t_ein=np.linspace(np.min(lamb1(x2)),np.max(lamb1(x2)))
x3_t_bei_l=np.linspace(np.min(lamb2(x3_l_flip)),np.max(lamb2(x3_l_flip)))
x3_t_bei_r=np.linspace(np.min(lamb3(x3_r)),np.max(lamb3(x3_r)))
x4_t_bei_l=np.linspace(np.min(lamb2(x4_l_flip)),np.max(lamb2(x4_l_flip)))
x4_t_bei_r=np.linspace(np.min(lamb3(x4_r)),np.max(lamb3(x4_r)))



plt.plot(lamb1(x1),D1,'rx',label='Messwerte')
plt.grid()

plt.plot(x1_t_ein,g(x1_t_ein,*params_ein_k),label='Ausgleichskurve')

plt.xlabel(r'$\lambda \:/\: \si{\cubic\meter}$')
plt.ylabel(r'$D \:/\: \si{\milli\meter}$')
plt.legend()
plt.savefig('build/ein_k.pdf')
#
plt.clf()



plt.plot(lamb1(x2),D2,'rx',label='Messwerte')
plt.grid()

plt.plot(x2_t_ein,g(x2_t_ein,*params_ein_a),label='Ausgleichsgerade')

plt.xlabel(r'$\lambda \:/\: \si{\cubic\meter}$')
plt.ylabel(r'$D \:/\: \si{\milli\meter}$')
plt.legend()
plt.savefig('build/ein_a.pdf')
plt.clf()


plt.plot(lamb2(x3_l_flip),D3_l_flip,'rx',label='Messwerte')
plt.grid()

plt.plot(x3_t_bei_l,g(x3_t_bei_l,*params_bei_k_l),label='Ausgleichsgerade links')

plt.xlabel(r'$\lambda_l\:/\: \si{\cubic\meter}$')
plt.ylabel(r'$D \:/\: \si{\milli\meter}$')
plt.legend()
plt.savefig('build/bei_k_l.pdf')

plt.clf()



plt.plot(lamb3(x3_r),D3_r,'rx',label='Messwerte')
plt.grid()
plt.plot(x3_t_bei_r,g(x3_t_bei_r,*params_bei_k_r),label='Ausgleichsgerade rechts')
plt.xlabel(r'$\lambda_r \:/\: \si{\cubic\meter}$')
plt.ylabel(r'$D \:/\: \si{\milli\meter}$')

plt.legend()
plt.savefig('build/bei_k_r.pdf')

plt.clf()



plt.plot(lamb2(x4_l_flip),D4_l_flip,'rx',label='Messwerte')
plt.grid()

plt.plot(x4_t_bei_l,g(x4_t_bei_l,*params_bei_a_l),label='Ausgleichsgerade links')

plt.xlabel(r'$\lambda_l \:/\: \si{\cubic\meter}$')
plt.ylabel(r'$D \:/\: \si{\milli\meter}$')
plt.legend()
plt.savefig('build/bei_a_l.pdf')

plt.clf()



plt.plot(lamb3(x4_r),D4_r,'rx',label='Messwerte')
plt.grid()
plt.plot(x4_t_bei_r,g(x4_t_bei_r,*params_bei_a_r),label='Ausgleichsgerade rechts')
plt.xlabel(r'$\lambda_r \:/\: \si{\cubic\meter}$')
plt.ylabel(r'$D \:/\: \si{\milli\meter}$')

plt.legend()
plt.savefig('build/bei_a_r.pdf')

plt.clf()









