import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
from scipy import stats
from scipy.optimize import curve_fit

#konstanten
k_m = 109
k_e = 16
A = 48*10**(-6)
x = 0.03

def Qm(T):
    return k_m * A * (T/x)

def Qe(T):
    return k_e * A * (T/x)

print(Qm(7.11))
print(Qm(4.80))
print(Qm(3.55))
print(Qm(2.93))
print(Qm(2.61))

print(Qe(12.65))
print(Qe(13.52))
print(Qe(12.57))
print(Qe(11.77))
print(Qe(11.21))
