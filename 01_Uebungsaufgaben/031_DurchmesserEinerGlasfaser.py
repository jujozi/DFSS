"""
Design for Six Sigma
Teil B: Statistische Grundlagen

Uebungen

3.1
Durchmesser einer Glasfaser

"""

#Bibliotheken importieren
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew
from scipy.io import loadmat
from IPython import get_ipython
from prettytable import PrettyTable
get_ipython().run_line_magic('matplotlib', 'inline')
import dsff_bib as dfss

"""
Gegeben sind Messwerte für den Durchmesser einer Glasfaser. Die Messwerte sind als Daten verfügbar
(Glasfaser.mat).
"""
Glasfaser = dfss.read_mfile('Glasfaser','01_DataUebung/Glasfaser.mat','Glasfaserduchmesser','d/mymD')


"""
b) Teilen Sie die Daten in 10 Klassen ein und erstellen Sie eine Tabelle mit absoluter Häufigkeit.
Stellen Sie folgende die relative Häufigkeitsverteilung und die relative Summenhäufigkeit in
MATLAB als Säulendiagramm dar.
"""

Glasfaser.histogram(10)
Glasfaser.histogram_tabel()

'''
c) Berechnen Sie die Quartile der Messwerte, also 25%, 50% und 75% Quartil. Geben Sie für alle
Kennwerte auch die entsprechende Formel an und berechnen Sie den Quartilkoeffizient der
Schiefe. Was können Sie über die Schiefe der Verteilung aussagen?
'''
Glasfaser.print_info()
Glasfaser.plot_info()
Glasfaser.print_q()

'''
d) Stellen Sie den Box-Plot in MATLAB dar. Interpretieren Sie den Box-Plot. Was können Sie am
Box-Plot ablesen?
'''






