import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
from scipy import stats
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp

A1,A2,T21,A5,A6,T65 = np.genfromtxt('data/amp_werte.txt', delimiter=',',unpack=True)
A7,A8,T78 = np.genfromtxt('data/amp2_werte.txt',delimiter=',',unpack=True)
#konstanten
p_m= 8520
c_m= 385
x= 0.03
p_a= 2800
c_a= 830
p_e= 8000
c_e= 400


a1 = ufloat(4.3,0.1511897262823546)
a2 = ufloat(12.716666666666667,0.09688194419555772)
t21 = ufloat(14.333333333333334,0.881917103688197)
a5 = ufloat(7.7316666666666665,0.16872890814689848)
a6 = ufloat(15.69,0.1347528602046477)
t65 = ufloat(7.333333333333333,0.33333333333333337)
a7 = ufloat(19.384999999999998,0.11994790535895172)
a8 = ufloat(2.8987499999999997,0.10472931378877008)
t78 = ufloat(55.75,4.479118216792229)

#print(np.mean(A7))
#print(stats.sem(A7))
#print(np.mean(A8))
#print(stats.sem(A8))
#print(np.mean(T78))
#print(stats.sem(T78))


#print(np.mean(A1))
#print(stats.sem(A1))
#
#print(np.mean(A2))
#print(stats.sem(A2))
#
#print(np.mean(t21))
#print(stats.sem(t21))
#
#print(np.mean(A5))
#print(stats.sem(A5))
#
#print(np.mean(A6))
#print(stats.sem(A6))
#
#print(np.mean(t65))
#print(stats.sem(t65))
k21 = p_m*c_m*(x**2)/(2*t21*(unp.log(a2/a1)))
k65 = p_a*c_a*(x**2)/(2*t65*(unp.log(a6/a5)))
k78 = p_e*c_e*(x**2)/(2*t78*(unp.log(a7/a8)))
print(np.mean(k21))
print(np.mean(k78))
print(np.mean(k65))
