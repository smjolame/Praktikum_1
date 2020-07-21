import os
import pathlib
os.environ['MATPLOTLIBRC'] = (pathlib.Path(__file__).absolute().parent.parent.parent / 'default' / 'matplotlibrc').__str__()
os.environ['TEXINPUTS'] =  (pathlib.Path(__file__).absolute().parent.parent.parent / 'default').__str__() + ':'
import numpy as np
from uncertainties import ufloat
from scipy import stats
import json
import matplotlib.pyplot as plt

# Messwerte einlesen
for farbe in [1,2,3]:

    e,g1,g2 = np.genfromtxt('data/bessel{}.csv'.format(farbe), delimiter=',', unpack=True)

    # Abstand der Linsenpositionen berechnen
    d = g2-g1

    # Brennweite berechnen
    f = (e**2 - d**2)/(4*e)
    f_mean = ufloat(np.mean(f),stats.sem(f))

    # Ergebnisse Speichern JSON
    Ergebnisse = json.load(open('data/Ergebnisse.json','r'))
    if not 'Bessel{}'.format(farbe) in Ergebnisse:
        Ergebnisse['Bessel{}'.format(farbe)] = {}
    Ergebnisse['Bessel{}'.format(farbe)]['f_mean[cm]'] = '{}'.format(f_mean)
    json.dump(Ergebnisse,open('data/Ergebnisse.json','w'),indent=4)

    # Ergebnisse Speichern Tabelle
    data = list(zip(e,g1,g2,d,f))
    np.savetxt('data/bessel{}_tabelle.csv'.format(farbe), data, header='e[cm],g1[cm],g2[cm],d[cm],f[cm]', fmt='%i,%2.1f,%2.1f,%2.1f,%2.2f')