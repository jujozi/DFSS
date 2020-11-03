"""
Design for Six Sigma
Teil B: Statistische Grundlagen

Uebungen

2.4
Schnelltest fuer Messfuehler

"""

#Bibliotheken importieren
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew
from scipy.io import loadmat
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')
import dsff_bib as dfss

"""
Zum Test eines Messfühlers wurde ein Gerät entwickelt, dass für Schnelltests bei der Fertigung einge-
setzt werden soll. Aus Erfahrung ist bekannt, dass ca. 15 von 10 000 Messfühlern fehlerhaft sind. Das
Gerät zeigt bei einem defekten Messfühler mit einer Wahrscheinlichkeit von 95 % an, dass ein defekter
Messfühler vorliegt. Mit einer Wahrscheinlichkeit von 10% wird ein voll funktionsfähiger Messfühler
als fehlerhaft angezeigt.
"""

N_erfahrung = 10000
N_erfahrung_defekt= 15

P_notOK_D = 0.95
P_notKO_notD = 0.1

P_D = N_erfahrung_defekt/N_erfahrung
P_notD = 1-P_D
"""
a) Erstellen Sie einen Ereignisbau und bezeichnen die Sie unterschiedlichen Ereignisse.
"""
#Siehe Aufschrieb
print('Warscheinlichkeit Defekt: '+ dfss.strProzent(P_D))
print('Warscheinlichkeit nicht Defekt: '+ dfss.strProzent(P_notD))
print('Warscheinlichkeit erkannter Defekt: '+ dfss.strProzent(P_notOK_D))
print('Warscheinlichkeit falsch erkannter Defekt: '+ dfss.strProzent(P_notKO_notD))

"""
b) Wie sicher kann sich der Bediener sein, dass der getestete Messfühler tatsächlich defekt ist, wenn
das Gerät dies anzeigt?
"""
P_m=P_D*P_notOK_D+P_notD*P_notKO_notD
P_g=P_D*P_notOK_D
P_D_notOK = dfss.P(P_m,P_g)
print('Warscheinlichkeit, dass Fuehler wirklich defekt ist: '+dfss.strProzent(P_D_notOK))