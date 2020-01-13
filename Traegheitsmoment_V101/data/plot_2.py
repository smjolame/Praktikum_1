import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
from scipy import stats
from scipy.optimize import curve_fit

#konstanten

m = 1.1180
R = 0.0375
h = 0.0300

def I_st(m,R):
    return m/2*R**2
def I_at(m,R,h):
    return m*((R**2)/4+(h**2)/12)

D = ufloat(0.022435,0.001026)
I_eig = ufloat(0.00276,0.00015)

T_s = np.genfromtxt('data/sym.txt', delimiter=',',unpack=True)
T_a = np.genfromtxt('data/asym.txt', delimiter=',',unpack=True)

I_se = ((T_s**2)*D)/(2*np.pi)**2 - I_eig 
I_ae = ((T_a**2)*D)/(2*np.pi)**2 - I_eig


print(np.mean(I_se))
I_exsym=np.mean(I_se)
print(np.mean(I_ae))
I_exasym=np.mean(I_ae)
I_sym=I_st(1.1180,0.0375)
I_asym=I_at(1.1180,0.0375,0.0300)
print(I_st(1.1180,0.0375))
print(I_at(1.1180,0.0375,0.0300))

I1=-I_exsym+I_sym
I2=-I_exasym+I_asym




Tr_1=ufloat(-0.00252,0.00014)
Tr_2=ufloat( -0.00224,0.00013)
Th_1= 0.00027633977142385086
Th_2= 0.0005880247884968426

I3=-Tr_1+Th_1
I4=-Tr_2+Th_2

print([I1,I2,I3,I4])
