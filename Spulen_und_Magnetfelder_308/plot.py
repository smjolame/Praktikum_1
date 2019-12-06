import matplotlib.pyplot as plt
import numpy as np
import math
x1, y1= np.genfromtxt('data/lange_Spule.txt',delimiter=',', unpack=True)
x2 , y2 = np.genfromtxt('data/kurze_Spule.txt',delimiter=',', unpack=True)
x3 , y3 = np.genfromtxt('data/dicke_Spule.txt',delimiter=',', unpack=True)
x4 , y4 =np.genfromtxt('data/Hysteresekurve.txt',delimiter=',', unpack=True)
x5 , y5 =np.genfromtxt('data/H_abstand6.txt', delimiter=',',unpack=True)
x6 , y6 =np.genfromtxt('data/H_abstand12.txt', delimiter=',',unpack=True)
x7 , y7 =np.genfromtxt('data/H_abstand18.txt', delimiter=',',unpack=True)


def z(I):
    return 595*I/((2*math.pi*0.185)-0.003)

h=-z(x4)



plt.plot(x1, y1,'bx', label='Lange Spule')
plt.xlabel(r'$x \:/\: \si{\cm}$')
plt.ylabel(r'$B \:/\: \si{\milli\tesla}$')
plt.legend(loc='best')
plt.grid()
plt.savefig('build/lange_Spule.pdf')
plt.clf()

plt.plot(x2, y2,'bx', label='Kurze Spule')
plt.xlabel(r'$x \:/\: \si{\cm}$')
plt.ylabel(r'$B \:/\: \si{\milli\tesla}$')
plt.legend(loc='best')
plt.grid()
plt.savefig('build/kurze_Spule.pdf')
plt.clf()

plt.plot(x3, y3,'bx', label='Dicke Spule')
plt.xlabel(r'$x \:/\: \si{\cm}$')
plt.ylabel(r'$B \:/\: \si{\milli\tesla}$')
plt.legend(loc='best')
plt.grid()
plt.savefig('build/dicke_Spule.pdf')
plt.clf()

t1=np.linspace(h[3],h[4])
t2=np.linspace(h[15],h[16])
m1=(y4[4]-y4[3])/(h[4]-h[3])
m2=(y4[16]-y4[15])/(h[16]-h[15])
plt.plot(h, y4,'b.', label='Hysteresekurve')
plt.xlabel(r'$H \:/\: \si{\ampere}\si{\m}^{-1}$')
plt.ylabel(r'$B \:/\: \si{\milli\tesla}$')
plt.plot(0, 430,'rx', label='Remanenz')
plt.plot(0, 550,'rx')
plt.plot(t1,m1*t1+y4[3]-m1*h[3], 'g--', label='Nullpunkt$\equiv$Koerzitivfeldstärke')
plt.plot(t2,m2*t2+y4[15]-m2*h[15], 'g--')
plt.legend(loc='best')
plt.grid()




plt.savefig('build/Hysteresekurve.pdf')





plt.clf()

plt.plot(x5, y5,'bx', label='Spulenabstand: 6,25 \si{\centi\m}')
plt.xlabel(r'$x \:/\: \si{\cm}$')
plt.ylabel(r'$B \:/\: \si{\milli\tesla}$')
plt.legend(loc='best')
plt.grid()
plt.savefig('build/H_abstand6.pdf')
plt.clf()

plt.plot(x5[0:7], y5[0:7],'bx', label='Spulenabstand: 6,25 \si{\centi\m}(Vergrößert)')
plt.xlabel(r'$x \:/\: \si{\cm}$')
plt.ylabel(r'$B \:/\: \si{\milli\tesla}$')
plt.legend(loc='best')
plt.grid()
plt.savefig('build/H_abstand6_k.pdf')
plt.clf()

plt.plot(x6, y6,'bx', label='Spulenabstand: 12,50 \si{\centi\m}')
plt.xlabel(r'$x \:/\: \si{\cm}$')
plt.ylabel(r'$B \:/\: \si{\milli\tesla}$')
plt.legend(loc='best')
plt.grid()
plt.savefig('build/H_abstand12.pdf')
plt.clf()

plt.plot(x7, y7,'bx', label='Spulenabstand: 18,75 \si{\centi\m}')
plt.xlabel(r'$x \:/\: \si{\cm}$')
plt.ylabel(r'$B \:/\: \si{\milli\tesla}$')
plt.legend(loc='best')
plt.grid()
plt.savefig('build/H_abstand18.pdf')
plt.clf()