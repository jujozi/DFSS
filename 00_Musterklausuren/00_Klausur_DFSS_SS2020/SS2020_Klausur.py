"""
Design for Six Sigma

Musterklausur

SS2020

"""

#Bibliotheken importieren
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
from scipy.stats import skew
from scipy.io import loadmat
from IPython import get_ipython
from prettytable import PrettyTable
get_ipython().run_line_magic('matplotlib', 'inline')
import dsff_bib as dfss

"""
Beschreibung der Aufgabe
Stadtwerke und Gasversorger müssen für die Abrechnung von Gas Zähler einsetzen, die in re-
gelmäßigen Abständen kalibriert werden. Dazu werden Prüfstände eingesetzt, wie sie in der
folgenden Abbildung gezeigt sind.

In diesen Prüfständen werden sogenannte kritische Düsen eingesetzt. N unterschiedliche Düsen
erzeugen jeweils einen Volumenstrom Q n , zusammen ergibt sich der für die Kalibrierung not-
wendigen Volumenstrom Q.

Die Düsen weisen einen Druck p D und eine Temperatur T D auf.

Statistische Auswertung einer Wiederholmessung
Zunächst wird an einer einzelnen Düse eine Wiederholmessung durchgeführt. Die Düse hat
einen nominalen Durchfluss von Q NOM = 0.5 m3/h. Mit einem Referenzmessgerät wird der Ist-
wert Q IST des Volumenstroms bestimmt. Die Daten sind in der Datei Durchflussmessung.mat
gespeichert.
"""

name = 'Fraesteile'
messgroese = 'Durchflussmessung Q_IST'
einheit = 'm^3/h'

Durchflussmessung = dfss.DataSet(name,messgroese,einheit)
Durchflussmessung.read_m('00_Musterklausuren/00_Klausur_Daten/Durchflussmessung.mat')

'''
a) Stellen Sie für die Messreihe die Häufigkeitsverteilung als Histogramm dar.
'''
Durchflussmessung.print_info()
Durchflussmessung.plot_info()
'''
b) Schätzen Sie auf Basis der Stichprobe den Mittelwert und die Standardabweichung der
Durchflussmessung. Geben Sie für γ = 95 % den Konfidenzbereich für beide Größen an.
Gehen Sie dabei von einer normalverteilten Grundgesamtheit aus.
'''
Durchflussmessung.calc_koefiBereich(0.94)
Durchflussmessung.print_koefiBereich()
'''
c) Plausibilisieren Sie die geschätzten Größen, in dem Sie die geschätzte Wahrscheinlich-
keitsdichte zusammen mit einem Histogramm der Stichprobenwerte darstellen.
'''

'''
d) Besitzt der Düsenprüfstand einen systematischen Messfehler? Beantworten Sie die Frage
mit einem geeigneten Hypothesentest. Begründen Sie Ihr Vorgehen.
'''

'''
e) Welche Abweichung ∆Q des Düsenprüfstandes könnten Sie mit einer Wahrscheinlichkeit
von 95 % erkennen? Beantworten Sie die Frage, in dem Sie die Gütefunktion des Tests
darstellen und auswerten.
'''











