import numpy as np

a=np.array([3,2.9,2.9333,2.95,2.96,2.96667,2.714,2.975,2.97778,2.98])
b=a**2


var=-(np.sum(a)/10)**2+np.sum(b)/10
print(var)
std=np.sqrt(var)
print(std)