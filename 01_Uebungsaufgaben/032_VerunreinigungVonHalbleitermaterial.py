"""
Design for Six Sigma
Teil B: Statistische Grundlagen

Uebungen

3.2
Verunreinigung von Halbleitermaterial

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
Gegeben sind Messwerte für die Verunreinigung von Materialien zur Halbleiterfertigung. Die Mess-
werte sind als Daten verfügbar (Halbleitermaterial.mat).
"""



Halbleiter = dfss.read_mfile('Halbleiter','01_DataUebung/Halbleitermaterial.mat','Verunreinigung','M/ppm')

'''
a) Geben Sie für die Messung alle Lage- und Streuungswerte an. Geben Sie für alle Kennwerte auch
die entsprechende Formel an.
- Arithmetischer Mittelwert
- Median
- Spannweite
'''

'''
b) Stellen Sie die relative Summenhäufigkeit als Liniendiagramm dar. Eine Einteilung der Daten in
Klassen soll dabei nicht durchgeführt werden.

c) Berechnen Sie die Quartile der Messwerte, also 25%, 50% und 75% Quartil. Tragen Sie die
Werte in die Grafik aus Aufgabenteil b) ein. Berechnen Sie den Quartilkoeffizient der Schiefe.
Was können Sie über die Schiefe der Verteilung aussagen?
'''

Halbleiter.print_info()
Halbleiter.print_q()
Halbleiter.plot_summLine()







