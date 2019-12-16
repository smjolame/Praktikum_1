import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

#a)
def func(T,a,b):
    return a * T + b

t,U=np.genfromtxt('data/a.txt',delimiter=',', unpack=True)



popt,pcov=curve_fit(func,t,np.log(U))

plt.plot(t,np.log(U),'rx',label='gemessene Werte')
plt.plot(t,func(t,*popt),label='Theorie')
plt.grid()
plt.ylabel(r'$\log(U_c)$')
plt.xlabel(r'$t \:/\: \si{\milli\s}$')

plt.savefig('build/a.pdf')
plt.clf()

a = popt[0]
a_err = np.absolute(pcov[0][0])**0.5
b = popt[1]
b_err = np.absolute(pcov[1][1])**0.5
RC1 = 1/a
RC_err = (a_err/a)*RC1


print(RC1)
print(RC_err)


#b)


fb,A=np.genfromtxt('data/b.txt',delimiter=',', unpack=True)

f_t=np.linspace(100,1200,10000)

#def Amp(f,U_0,R,C):
#    return U_0/(np.sqrt(1+(2*np.pi*f)**2*R**2*C**2))

def Amp2(f,a):
    return 9.2/(np.sqrt(1+(2*np.pi*f)**2*a**2))

#params, cov_matrix=curve_fit(Amp,f1,A)
RC, cov1=curve_fit(Amp2,fb,A)


def A_t(f):
    return 9.2/(np.sqrt(1+(2*np.pi*f)**2*15058**2*(93.2*10**(-9))**2))

plt.plot(fb,A/9.2,'rx',label='gemessene Werte')
#plt.plot(fb,Amp(fb,*params))
plt.plot(f_t,Amp2(f_t,*RC)/9.2,label='Ausgleichskurve')
#plt.plot(f_t,A_t(f_t)/9.2,label='Theorie')
plt.xscale(r'log')
plt.ylabel(r'$\frac{U_c}{U_0}$')
plt.xlabel(r'$f \:/\: \si{\hertz}$')
plt.tight_layout()
plt.legend()
plt.grid()
plt.savefig('build/b.pdf')
print(RC)
plt.clf()



param_a = RC[0]
param_a_err = np.absolute(cov1[0][0])**0.5

print(param_a)
print(param_a_err)



#c)

fc,a,b=np.genfromtxt('data/c.txt',delimiter=',', unpack=True)

def phi(f,a):
    return np.arctan(-(2*np.pi*f)*a)
def phi_t(f):
    return np.arctan(-(2*np.pi*f)*15058*93.2*10**(-9))

def phi1(f):
    return np.arctan(-(2*np.pi*f)*RC)

p=(a/b)*2*np.pi
plt.plot(fc,p,'rx',label='gemessene Werte')

params1, cov3=curve_fit(phi, fc, p)

plt.plot(f_t,phi(f_t,*params1),label='Ausgleichskurve')
#plt.plot(f_t,phi_t(f_t),label='Theorie')
plt.ylabel(r'$\phi \:/\: \si{\radian}$')
plt.xlabel(r'$f \:/\: \si{\hertz}$')

plt.grid()
plt.xscale(r'log')
plt.savefig('build/c.pdf')
plt.clf()


param_c = params1[0]
param_c_err = np.absolute(cov3[0][0])**0.5

print(param_c)
print(param_c_err)

#d)


def phi1(f):
    return np.arctan(-(2*np.pi*f)*RC)

phi=(a/b)*2*np.pi

phi_linspace = np.linspace(0,np.max(phi),100)

def Ap(f):
    return -np.sin(phi1(f))*9.2/(2*np.pi*f*RC)
plt.polar(phi1(fc),A/9.2,'rx',label='Messwerte')


#def Ap_t(f):
#    return -np.sin(phi_t(f))*9.2/(2*np.pi*f*15058*93.2*10**(-9))

plt.polar(phi_linspace,np.cos(phi_linspace),label='Theorie')
plt.legend()
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
#plt.polar(phi_t(f_t),Ap_t(f_t)/9.2)


plt.savefig('build/d.pdf')




#Theoriewert RC
RC_theorie=15058*93.2*10**(-9)
RC_t_err=600*93.2*10**(-9)
print(RC_theorie)
print(RC_t_err)

