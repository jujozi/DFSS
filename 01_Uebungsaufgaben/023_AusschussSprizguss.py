"""
Design for Six Sigma
Teil B: Statistische Grundlagen

Uebungen

2.3
Ausschuss einer Spritzgussmaschine

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
In einer Kunststofffabrik werden Kleinteile im Spritzgussverfahren hergestellt. Die eingesetzte Ma-
schine fertigt mit einer Wahrscheinlichkeit von 7 % Ausschuss. Um die Anzahl ausgelieferter Aus-
schussteile zu minimieren, durchlaufen alle Kleinteile eine automatisierte Prüfung. Durch die zweite
Maschine zur Überprüfung werden Ausschussteile mit 78 % Wahrscheinlichkeit ausgesondert. Fehler-
lose Kleinteile werden nur mit 1.5 % Wahrscheinlichkeit fälschlicherweise aussortiert.
"""
P_ausschuss= 0.07
P_ausschuss_erkannt = 0.78
P_ausschuss_erkannt_falsch = 0.015

"""
a) Erstellen Sie einen Ereignisbau und bezeichnen die Sie unterschiedlichen Ereignisse.
"""
#Siehe Aufschrieb
"""
b) Wie viel Prozent Ausschuss wird die Ware haben, die die Kontrolle mit positiver Prüfung durch-
laufen hat?
"""
P_ausschuss_NachKontrolle = P_ausschuss*(1-P_ausschuss_erkannt)
print('Ausschuss nach Kontrolle: '+str(P_ausschuss_NachKontrolle))
"""
c) Wie viel Prozent fehlerlose Teile enthält der Behälter, in dem die Maschine den Ausschuss sam-
melt?
"""
P_fehlerlos_inAusschuss = (1-P_ausschuss)*P_ausschuss_erkannt_falsch
print('fehlerlose Teile im Ausschuss nach Kontrolle: '+str(P_fehlerlos_inAusschuss))
"""
d) Ein Unternehmen kauft zur Weiterverarbeitung die hergestellten Kleinteile. Bei der Eingangskon-
trolle werden 100 Teile überprüft. Mit wie vielen fehlerhaften Teilen rechnen Sie?
"""
N=100
N_defekt = P_ausschuss_NachKontrolle * N
print('Defekte Teile in Stichprobe: '+str(N_defekt))


