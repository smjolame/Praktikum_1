import matplotlib.pyplot as plt
import numpy as np
x1, y1= np.genfromtxt('data/lange_Spule.txt',delimiter=',', unpack=True)
x2 , y2 = np.genfromtxt('data/kurze_Spule.txt',delimiter=',', unpack=True)
x3 , y3 = np.genfromtxt('data/dicke_Spule.txt',delimiter=',', unpack=True)
x4 , y4 =np.genfromtxt('data/Hysteresekurve.txt',delimiter=',', unpack=True)
print(x1,y1)



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

plt.plot(x4, y4,'bx', label='Hysteresekurve')
plt.xlabel(r'$x \:/\: \si{\cm}$')
plt.ylabel(r'$B \:/\: \si{\milli\tesla}$')
plt.legend(loc='best')
plt.grid()
plt.savefig('build/Hysteresekurve.pdf')
plt.clf()
