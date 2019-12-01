import matplotlib.pyplot as plt
import numpy as np


f0  = 250 #Hz  Berechneter Wert der Minimalfrequenz
Us=2.5 #V
R=664 #Ohm
C=994*10**(-9) #F
R_s=500 #Ohm
f, Ubr =np.genfromtxt('data/e.txt', delimiter=',', unpack=True)


U=(Ubr/Us) #V

Omega=(f/f0)

f0_t=1/(2*np.pi*C*R)  #theoretischer Wert der Minimalfrequenz

f_t=np.linspace(0,30100,10000)
Omega_t=(f_t/f0_t)  #Theoretischer Wert des Frequnzverhältnisses


U_t=np.sqrt(((Omega_t**2-1)**2)/(9*(1-Omega_t**2)**2+9*Omega_t**2))



plt.plot(Omega, U,'rx', label='Messwerte')
plt.xlabel(r'$\Omega$')
plt.ylabel(r'$\frac{U_{\text{Br}}}{U_{\text{S}}}$')
plt.xscale(r'log')
plt.legend()

plt.plot(Omega_t, U_t,'b', label='theoretische Kurve')
plt.xscale('log')
plt.legend()
plt.grid()
plt.savefig('build/e.pdf')


