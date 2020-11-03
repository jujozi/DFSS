"""
Design for Six Sigma
Teil B: Statistische Grundlagen

Uebungen

2.5
Fertigung von Drucksensoren

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
In einem Werk werden Drucksensoren gefertigt. Ob ein Teil die Qualitätskontrolle besteht, ist von den
Neuteiltoleranzen bei der Druckmessung und der Stärke der Temperaturdrift abhängig. Beide Eigen-
schaften können als unabhängig angenommen werden. Als Neuteiltoleranz wird bei Raumtemperatur
eine maximale Abweichung von ± 1 % akzeptiert. Bei Änderung der Temperatur im Bereich von
- 20 ... 120 °C darf der Messwert maximal um ± 2 % streuen. Nach der Fertigung durchlaufen Stich-
proben eine Qualitätskontrolle, in der die Neuteilcharakteristik des Drucksensors und das Temperatur-
verhalten getrennt ermittelt werden. Hierbei wird festgestellt, dass von 100 vermessenen Drucksensoren
4 außerhalb der Neuteiltoleranz liegen, 7 die Toleranzgrenzen der Temperaturdrift nicht einhalten. Ein
Vergleich zeigt, dass nur bei einem Sensor beide Toleranzgrenzen verletzt wurden.
"""
N= 100

P_notN = 0.04
P_notT = 0.07
P_notTN= 0.01

"""
a) Erstellen Sie einen Ereignisbau und bezeichnen die Sie unterschiedlichen Ereignisse.
"""
#Siehe Aufschrieb

"""
b) Es wird zufällig ein Drucksensor ausgewählt. Mit welcher Wahrscheinlichkeit handelt es sich bei
dem Sensor um ein defektes Bauteil?
"""
# moegliches Ereignis alle also
P_m = 1
# guenstiges Ereigniss sind alle drei Defekte

P_g = P_notN+P_notT-P_notTN

P_defekt = P_g

print('Warscheinlichkeit fuer ein defektes Teil: '+dfss.strProzent(P_defekt))


"""
c) Es werden 25 Drucksensoren aus der Produktion entnommen. Mit wie vielen defekten Druck-
sensoren rechnen Sie in Ihrer Stichprobe? Wie viele Sensoren erwarten Sie, die ausschließlich auf
Grund ihrer Neuteiltoleranzen aussortiert werden?
"""
N_sampel = 25

N_defektSampel= N_sampel*P_defekt
print('Erwartete Anzahl an defekten Sensoren in einer Stichprobe von '+str(N_sampel)+': '+str(round(N_defektSampel,2)))
N_defektSampel_N = N_sampel * (P_notN-P_notTN)
print('Erwartete Anzahl an defekten Sensoren in einer Stichprobe von '+str(N_sampel)+' augrund der Neutoleranz: '+str(round(N_defektSampel_N,2)))
print('Das sind '+dfss.strProzent((P_notN-P_notTN)))