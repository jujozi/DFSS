"""
Design for Six Sigma
Teil B: Statistische Grundlagen

Uebungen

2.2
System mit vier Teilsystemen
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
System besteht aus vier Komponenten, von denen jede entweder funktioniert oder defekt ist. Die Wahr-
scheinlichkeit, dass Komponente 1 defekt ist, liegt bei 5 %, die Wahrscheinlichkeit, dass Komponente
2 defekt ist, liegt bei 10 %. Für die Komponenten 3 und 4 gilt eine Fehlerwahrscheinlichkeit von 3 %.
Das System ist gerade noch funktionsfähig, wenn mindestens 2 Komponenten fehlerfrei sind.
"""

N = 4
Nfunktion = 2

Prop_1 = 0.05
Prop_2 = 0.10
Prop_3 = 0.03
Prop_4 = 0.03

Prop_1_workling = 1-Prop_1
Prop_2_workling = 1-Prop_2
Prop_3_workling = 1-Prop_3
Prop_4_workling = 1-Prop_4

"""
a) Wie groß ist die Wahrscheinlichkeit, dass ein System völlig einwandfrei ist? Wie groß ist die Wahr-
scheinlichkeit, dass das System gerade noch funktionsfähig ist?

"""

P_fehlerfrei= Prop_1_workling*Prop_2_workling*Prop_3_workling*Prop_4_workling

print('Warscheinlichkeit fuer fehlerfreien Betrieb'+str(P_fehlerfrei))

P_lim= Prop_1*Prop_2*Prop_3_workling*Prop_4_workling + Prop_1*Prop_2_workling*Prop_3*Prop_4_workling +  Prop_1*Prop_2_workling*Prop_3_workling*Prop_4 +Prop_1_workling*Prop_2*Prop_3*Prop_4_workling +Prop_1_workling*Prop_2*Prop_3_workling*Prop_4 +Prop_1_workling*Prop_2_workling*Prop_3*Prop_4

print('Watscheinlichkeit fuer gerade noch funkionsfaehig: '+str(P_lim))
print('')

"""
b) Es werden 100 Systeme als Stichprobe analysiert. Mit wie vielen defekten Komponenten 1 rechnen
Sie? Wie viele völlig einwandfreie und wie viele gerade noch funktionsfähigen Systeme erwarten
Sie in Ihrer Stichprobe?
"""
N=100

N_defekt1 = N*Prop_1
N_einwandfrei = N*P_fehlerfrei
N_lim = N*P_lim


print('defekte Komponenten 1: '+str(N_defekt1))
print('völlig einwandfrei: '+str(N_einwandfrei))
print('gerade noch funktionsfähig: '+str(N_lim))


