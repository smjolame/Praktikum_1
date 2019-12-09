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

plt.plot(C_k,n(C_k))

f,Ck,ne=np.genfromtxt('data/messwerte_a.txt',delimiter=',',unpack=True)
plt.plot(Ck*10**(-9),ne/2,'rx')
plt.xlabel(r'$C_k \:/\:\si{\farad}$')
plt.ylabel(r'$n_t$')
plt.savefig('build/amplituden.pdf')
