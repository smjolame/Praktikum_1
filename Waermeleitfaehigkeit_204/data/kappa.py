import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
from scipy import stats
from scipy.optimize import curve_fit

A1,A2,T21,A5,A6,T65 = np.genfromtxt('data/amp_werte.txt', delimiter=',',unpack=True)

#konstanten
p= 8520
c= 385
x= 0.03

a1 = ufloat(4.3,0.1511897262823546)
a2 = ufloat(12.716666666666667,0.09688194419555772)
t21 = ufloat(14.333333333333334,0.881917103688197)
a5 = ufloat(7.7316666666666665,0.16872890814689848)
a6 = ufloat(15.69,0.1347528602046477)
t65 = ufloat(7.333333333333333,0.33333333333333337)

def ln(a1,a2):
    return np.log(a1/a2)

print(np.mean(ln(a1,a2)))




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
#k21 = p*c*(x**2)/(2*t21*(np.log(a2/a1)))
#k65 = p*c*(x**2)/(2*t65*(np.log(a6/a5)))

#print(np.mean(k21))
#print(stats.sem(k21))
#
#print(np.mean(k65))
#print(stats.sem(k65))