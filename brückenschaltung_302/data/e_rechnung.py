import numpy as np 
import matplotlib.pyplot as plt 

f0  = 250 #Hz  Berechneter Wert der Minimalfrequenz
Us=2.5 #V
R=664 #Ohm
C=994 #nF
R´=500 #Ohm
f, Ubr =np.genfromtxt('e.txt', delimiter=',', unpack=True)


U=(Ubr/Us) #V

Omega=(f/f0)

f0_t=1/(C*R)  #theoretischer Wert der Minimalfrequenz
Omega_t=(f/f0_t)  #Theoretischer Wert des Frequnzverhältnisses

U_t=sqr(((Omega_t**2-1)**2)/(9*(1-Omega_t**2)**2+9*Omega_t**2))