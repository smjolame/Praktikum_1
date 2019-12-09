import matplotlib.pyplot as plt
import numpy as np

L=23.954*10**(-3)
C=0.7932*10**(-9)
C_sp=0.028*10**(-9)

C_ges=C+C_sp
vp=1/(2*np.pi*np.sqrt(L*C_ges))

def n(C_k):

    vm=1/(2*np.pi*np.sqrt(L*((1/C+2/C_k)**(-1)+C_sp)))
    n=(vp+vm)/(2*(vm-vp))
    return n


C_k = np.linspace(2*10**(-9), 12*10**(-9), 1000)

plt.plot(C_k,n(C_k), label='theoretische Kurve')

f1,Ck,ne=np.genfromtxt('data/messwerte_a.txt',delimiter=',',unpack=True)
plt.plot(Ck*10**(-9),ne/2,'rx', label='gemessene Werte')
plt.xlabel(r'$C_k \:/\:\si{\farad}$')
plt.ylabel(r'$n_t$')
plt.grid()
plt.legend()
plt.savefig('build/amplituden.pdf')
plt.clf()

def Z(w,C_k):
    return (w*L-1/w*(1/C+1/C_k))

def I(w,R,C_k,U):
    return (U*(1/(np.sqrt(4*w**2*C_k**2*R**2*Z(w,C_k)**2+(1/(w*C_k)-w*C_k*Z(w,C_k)**2+w*R**2*C_k)**2))))






Ck, v, U =np.genfromtxt('data/messwerte_b_pi.txt',delimiter=',',unpack=True)
plt.plot(C_k,1/(2*np.pi*np.sqrt(L*((1/C+2/C_k)**(-1)+C_sp))), label='theoretische Kurve')
plt.plot(Ck*10**(-9),v*10**3,'rx',label='gemessene Werte')
plt.ylabel(r'$\nu^-\:/\: \si{\hertz}$')
plt.xlabel(r'$C_k \:/\:\si{\farad}$')
plt.grid()
plt.legend()
plt.savefig('build/frequenzen.pdf')
plt.clf()

f=np.linspace(5,50000,10000)
plt.plot(f,I(2*np.pi*f,73,Ck[0]*10**(-9),U[0]),label='theoretische Kurve')
plt.grid()
plt.plot(37900,0.089,'rx', label='gemessene Werte')
plt.plot(35600,0.098,'rx')
plt.xlabel(r'$\nu^-\:/\: \si{\hertz}$')
plt.ylabel(r'$I \:/\: \si{\ampere}$')
plt.legend()
plt.savefig('build/strom.pdf')
plt.clf()

"""
f=np.linspace(5,50000,10000)
plt.plot(f,I(2*np.pi*f,73,Ck[1]*10**(-9),U[1]))
plt.grid()
plt.savefig('build/strom1.pdf')
plt.clf()

f=np.linspace(5,50000,10000)
plt.plot(f,I(2*np.pi*f,73,Ck[2]*10**(-9),U[2]))
plt.grid()
plt.savefig('build/strom2.pdf')
plt.clf()

f=np.linspace(5,50000,10000)
plt.plot(f,I(2*np.pi*f,73,Ck[3]*10**(-9),U[3]))
plt.grid()
plt.savefig('build/strom3.pdf')
plt.clf()

f=np.linspace(5,50000,10000)
plt.plot(f,I(2*np.pi*f,73,Ck[4]*10**(-9),U[4]))
plt.grid()
plt.savefig('build/strom4.pdf')
plt.clf()

f=np.linspace(5,50000,10000)
plt.plot(f,I(2*np.pi*f,73,Ck[5]*10**(-9),U[5]))
plt.grid()
plt.savefig('build/strom5.pdf')
plt.clf()

f=np.linspace(5,50000,10000)
plt.plot(f,I(2*np.pi*f,73,Ck[6]*10**(-9),U[6]))
plt.grid()
plt.savefig('build/strom6.pdf')
plt.clf()

"""

