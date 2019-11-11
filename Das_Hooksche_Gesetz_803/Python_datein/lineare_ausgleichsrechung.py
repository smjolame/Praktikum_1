import numpy as np 
import matplotlib.pyplot as plt 


D=np.array([3,2.9,2.9333,2.95,2.96,2.96667,2.714,2.975,2.97778,2.98])


x=np.linspace(0.05,0.5,10)


F=np.array([0.15,0.29,0.44,0.59,0.74,0.89,1.04,1.19,1.34,1.49])

m=(np.mean(F*x)-(np.mean(F)*np.mean(x)))/(np.mean(x**2)-(np.mean(x))**2)
b=(np.mean(F)*np.mean(x**2)-np.mean(x*F)*np.mean(x))/(np.mean(x**2)-(np.mean(x))**2)
print("m=")
print(m)
print("b=")
print(b)





import matplotlib.pyplot as plt
import numpy as np



plt.plot(x,F , 'bx')
t=np.linspace(0,0.5,100)
plt.plot(t,m*t+b,'r--')
plt.xlabel(r'$x / \mathrm{m}$')
plt.ylabel(r'$F / \mathrm{N}$')

plt.xlim(0,0.55)
plt.ylim(0,1.6)
plt.savefig('Plot_Ausgleichsrechung.pdf')
