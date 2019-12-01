import numpy as np 
import matplotlib.pyplot as plt 

f0  = 250 #Hz  Berechneter Wert der Minimalfrequenz
Us=2.5 #V
R=664 #Ohm
C=994*10**(-9) #F
R_s=500 #Ohm
f, Ubr =np.genfromtxt('e.txt', delimiter=',', unpack=True)


U=(Ubr/Us) 

Omega=(f/f0)

f0_t=1/(2*np.pi*C*R)  #theoretischer Wert der Minimalfrequenz
print(f0_t)
f_t=np.linspace(0,30100,10000)
Omega_t=(f_t/f0_t)  #Theoretischer Wert des Frequnzverhältnisses


U_t=np.sqrt(((Omega_t**2-1)**2)/(9*(1-Omega_t**2)**2+9*Omega_t**2))