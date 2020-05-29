import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as const
from scipy.optimize import curve_fit
from uncertainties import ufloat
from uncertainties.unumpy import uarray
from uncertainties import unumpy as unp

Ergebnisse = json.load(open('data/Ergebnisse.json','r')
if not 'Name' in Ergebnisse:
    Ergebnisse['Name'] = {}
Ergebnisse['Name']['Name des Wertes']=Wert

json.dump(Ergebnisse,open('data/Ergebnisse.json','w'),indent=4)
