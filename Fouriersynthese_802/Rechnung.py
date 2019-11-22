import numpy as np 
import matplotlib.pyplot as plt

k=np.arange(1,51)


def f(x):
    s=0
    for i in k:
        B=(2*(-1)**(i+1))/i
        s=s+B*np.sin(k*x)
    return s



x=np.linspace(-10,10)
plt.plot(x,f(x))
plt.savefig("plot1.pdf")
plt.show()