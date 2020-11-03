"""
Design for Six Sigma
Teil B: Statistische Grundlagen

Uebungen

2.1 Auswahl Multimeter
In einer Schachtel liegen 10 Multimeter, darunter 3 defekte Multimeter.

"""

""" Bibliotheken importieren"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew
from scipy.io import loadmat
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')
import dsff_bib as dfss

"""
In einer Schachtel liegen 10 Multimeter, darunter 3 defekte Multimeter.
"""

N = 10          # Gesamtanzahl
N_Defekt = 3    # Defekte Geraete
k = 2           # Anzahl der Ziehungen

N_m = N         #Anzahl der moeglichen Faelle
N_g = N-3       #Anzahl der gunstigen Faelle

"""
a) Wie groß ist die Wahrscheinlichkeit, lauter brauchbare Multimeter zu bekommen, wenn zwei Mul-
timeter nacheinander zufällig und ohne Zurücklegen entnommen werden?
"""

Mm_a = dfss.anzKombination(N_m,k)
Mg_a = dfss.anzKombination(N_g,k)

P_a = dfss.P(Mm_a,Mg_a)

print('Warscheinlichkeit der Aufgabe 2.1(a: '+str(P_a))


"""
b) Wie groß ist die Wahrscheinlichkeit, wenn die Packung 19 Multimeter enthält, 8 Multimeter defekt
sind und 5 Artikel zufällig und ohne Zurücklegen herausgegriffen werden?
"""
N = 19          # Gesamtanzahl
N_Defekt = 8    # Defekte Geraete
k = 5        # Anzahl der Ziehungen

N_m = N         #Anzahl der moeglichen Faelle
N_g = N-3       #Anzahl der gunstigen Faelle

Mm_b = dfss.anzKombination(N_m,k)
Mg_b = dfss.anzKombination(N_g,k)

P_b = dfss.P(Mm_b,Mg_b)

print('Warscheinlichkeit der Aufgabe 2.1(b: '+str(P_b))
