# -*- coding: utf-8 -*-
"""
Bibliothek der wichtigsten Funktionon in Design for Six Sigma

"""

""" Bibliotheken importieren"""
import numpy as np
import scipy as sp
#import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import skew, t, norm, chi2, f
from scipy.io import loadmat
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')
from prettytable import PrettyTable

# Berechnung der Warscheinlichkeit aus der Anzahl moeglicher und guenstiger
# Faelle
def P(Mm,Mg):
    """ 
    Mm - Anzahl moeglicher Ereignisse
    Mg - Anzahl guensitger Ereignisse
    
    Berechnet die Warscheinlichkeit eines guenstigen Ereignisses
    """
    return Mg/Mm

# Kombination ohne Wiederholung
def anzKombination(N,K):
    return sp.special.comb(N,K)

def strProzent(x):
    return str(round(x*100,4))+'%'


# Konfidenzbereich hinzufuegen

class DataSet:
    def __init__(self,name,messgroese,einheit):
        '''
        

        Parameters
        ----------
        name : TYPE
            DESCRIPTION.
        messgroese : TYPE
            DESCRIPTION.
        einheit : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        '''
        self.name = name
        self.messgroese = messgroese
        self.einheit = einheit
        
        self.X_min = 0                          #Minimaler Wert 
        self.X_max = 0                          #Maximaler Wert
        self.N = 0
        
        self.X_mean = 0                         #Mittelwert der Stichprobe
        self.X_med = 0                          #Median der Stichprobe
        
        self.X_var = 0                          #Varianz
        self.X_std = 0                          #Standardabweichung
        self.X_iqr = 0
        
        self.X_skew_mom = 0
        self.X_skew_qua = 0
        
        self.X_freq = 0
        self.X_rel_freq = 0
        self.X_sum_freq = 0
        self.X_rel_sum_freq = 0
        
        self.class_data = 0
        self.class_data_n = 0
        
        self.hist_binCenter = 0
        self.hist_data = 0
        self.hist_edges = 0
        
        self.discard_min = 0                    # Ausschussgrenze minimal
        self.discard_max = 0                    # Ausschussgrenze maximal
        
    def read_m(self,mfile):
        self.mfile = mfile
        print("Einlesen fuer " +self.name+ " der Datei "+mfile)
        
        """Daten aus dem .mat-file"""
        # np.rshape
        try:
            readFile = loadmat(self.mfile)
            readFile_keys = list(readFile.keys())[3:]
        except:
            print('mFile read: faild')
        else:
            print('mFile read: found keys: ' + str(readFile_keys))
            print('mFile read: read sucsess')
        data = np.empty([0,1])
        for i,key in enumerate(readFile_keys):
            data_read = np.reshape(readFile[key],(-1,1))
            data = np.concatenate((data,data_read), axis=0)
        print('mFile read: concatenate all data')
        
        self.data = data
        
        self.calc_Datenumpfang()
        
        """Lagekennwerte"""
        self.clac_LMM()
        
        """Streuungskennwerte"""

        self.calc_SSVI()
        
        """Schiefe"""
        self.calc_schiefe()
        
        """  absolute und relative Häufigkeit"""
        """  absolute und relative Summenhäufigkeit"""
        self.calc_haufigkeit()
        
        self.X_delta = self.X_max - self.X_min
        
        
        
        
    def print_info(self):
        pt = PrettyTable()
        pt.field_names = ['Bezeichnung','Wert']
        pt.align['Bezeichnung'] = 'r'
        pt.align['Wert'] = 'l'
        pt.add_row(['Arithmetischer Mittelwert', self.X_mean])
        pt.add_row(['Median', self.X_med ])
        pt.add_row(['Spannweite', self.X_delta ])
        pt.add_row([' ',' '])
        pt.add_row(['Varianz', self.X_var])
        pt.add_row(['Standardabweichung', self.X_std])
        pt.add_row([' ',' '])
        pt.add_row(['Inter-Quartil-Range', self.X_iqr])
        pt.add_row(['Quartilkoeffizient der Schiefe', self.X_skew_qua ])
        pt.add_row(['Momentenkoeffizient der Schiefe', self.X_skew_mom ])
        #pt.add_row([' ',' '])
        #pt.add_row(['Absolute Häufigkeit hA(x): ', self.X_freq])
        #pt.add_row(['RelativeHaeufigkeit h(x): ', self.X_rel_freq ])
        #pt.add_row(['Absolute Summenhäufigkeit HA(x): ',self.X_sum_freq])
        #pt.add_row(['Relative Summenhäufigkeit H(x): ',self.X_rel_sum_freq])
        print(pt)
        
    def print_q(self):
        pt = PrettyTable()
        pt.field_names = ['Bezeichnung','Wert']
        pt.add_row(['Quartile bei 25%',self.X_q25])
        pt.add_row(['Quartile bei 50%',self.X_q50])
        pt.add_row(['Quartile bei 75%',self.X_q75])
        print(pt)
        
        
        
    def plot_info(self):
        yLimDelta =  self.X_max - self.X_min
        yLimMin = self.X_min - yLimDelta * 0.1
        yLimMax = self.X_max + yLimDelta * 0.1
        xLimMin = 0
        xLimMax = 0.6
        data = self.data
        N =self.N
        
        strMessgroese = self.messgroese
        strEinheit = self.einheit
        """ Grafische Darstellung der einzelnen Messwete als Streudiagramm """
        fig = plt.figure(1, figsize=(12, 4))
        ax1, ax2 = fig.subplots(1,2)
        n = np.arange(1,N+1)
        ax1.plot(n,data, 'bo', Linewidth = 2, label = 'Stichproben')
        ax1.grid(True, which='both', axis='both', linestyle='--')
        ax1.axis([1, N, yLimMin, yLimMax])
        ax1.legend(loc='upper right')
        ax1.set_xlabel('Stichprobe n')
        ax1.set_ylabel(strMessgroese+' '+strEinheit)
        
        """ Erstellen eines Boxplt """
        ax2.boxplot(data)
        ax2.grid(True, which='both', axis='both', linestyle='--')
        ax2.set_xlabel('Messreihe ')
        ax2.set_ylabel(strMessgroese+' '+strEinheit)
        ax2.axis([0, 2, yLimMin, yLimMax])
        
    
        
        """ Grafische Darstellung der relativen Häufigkeiten als Histogramm """
        fig = plt.figure(2, figsize=(12, 4))
        ax1, ax2 = fig.subplots(1,2)
        ax1.hist(data, int(np.sqrt(N)*1.3), facecolor='b')
        #ax1.hist(data, self.Klassengrenzen, histtype='bar' , color='b', weights=np.ones(N)/N, rwidth=1)
        ax1.grid(True, which='both', axis='both', linestyle='--')
        ax1.set_xlabel(strMessgroese+' '+strEinheit)
        ax1.set_ylabel('Relative Häufigkeit h(m)')
        ax1.axis([yLimMin, yLimMax, xLimMin, xLimMax])
        
        xplot = np.linspace(yLimMin,yLimMax,100)
        self.data_predict = norm.pdf(xplot,self.X_mean,self.X_std)
        ax1.plot(xplot,self.data_predict,'r')
        
        """ Grafische Darstellung der relativen Summenhäufigkeit """
        Xsort = np.sort(np.reshape(data,-1))
        Psum = np.arange(1,N+1)/N
        ax2.step(Xsort,Psum, color='b', where='post', linewidth=2)
        ax2.grid(True, which='both', axis='both', linestyle='--')
        ax2.set_xlabel(strMessgroese+' '+strEinheit)
        ax2.set_ylabel('Relative Summenhäufigkeit H(m)')
        ax2.axis([yLimMin, yLimMax, 0, 1])
        
    def plot_summLine(self):
        yLimDelta =  self.X_max - self.X_min
        yLimMin = self.X_min - yLimDelta * 0.1
        yLimMax = self.X_max + yLimDelta * 0.1
        fig = plt.figure(1, figsize=(6, 4))
        f, ax = plt.subplots()
        Xsort = np.append(np.append(48,np.sort(self.data)),54)
        Psum = np.append(np.append([0,],np.arange(1,self.N+1)/self.N),1)
        ax.step(Xsort,Psum, color='b', where='post', linewidth=2)
        ax.grid(True, which='both', axis='both', linestyle='--')
        ax.set_xlabel(self.messgroese+' '+self.einheit)
        ax.set_ylabel('Relative Summenhäufigkeit H(m)')
        ax.axis([yLimMin, yLimMax, 0, 1])
        
        #plot Quartile
        plt.axvline(x=self.X_q25,color='r', linestyle='--', label='vline1.5custom')
        plt.axvline(x=self.X_q50,color='r', linestyle='--', label='vline1.5custom')
        plt.axvline(x=self.X_q75,color='r', linestyle='--', label='vline1.5custom')
        
    
    def calc_koefiBereich(self,gamma):
        '''
        Bestimmen des Konfidenzbereich von Mittelwert und Standardabweichung

        Returns
        -------
        None.

        '''
        N = self.N
        xquer = self.X_mean
        s = self.X_std
        
        self.gamma = gamma
        
        c1 = t.ppf((1-gamma)/2,N-1)
        c2 = t.ppf((1+gamma)/2,N-1)
        self.X_mean_c1 = xquer - c2*s/np.sqrt(N)
        self.X_mean_c2 = xquer - c1*s/np.sqrt(N)
        c1 = chi2.ppf((1-gamma)/2,N-1)
        c2 = chi2.ppf((1+gamma)/2,N-1)
        self.X_std_c1 = s*np.sqrt(N/c2)
        self.X_std_c2 = s*np.sqrt(N/c1)
        
    def print_koefiBereich(self):
        pt = PrettyTable()
        pt.field_names = ['Wert','Konfidenzbereich bei gamma = ' + strProzent(self.gamma)]
        pt.align['Wert'] = 'r'
        pt.align['Konfidenzbereich'] = 'l'
        pt.add_row(['Mittelwert', str(round(self.X_mean_c1,3))+' <= '+str(round(self.X_mean,3))+' <= '+str(round(self.X_mean_c2,3)) ])
        pt.add_row(['Mittelwert', str(round(self.X_std_c1,3))+' <= '+str(round(self.X_std,3))+' <= '+str(round(self.X_std_c2,3)) ])
        
        print(pt)
        
        
    """Bestimmung Datenumfang"""
    def calc_Datenumpfang(self):
        self.X_min = np.amin(self.data)
        self.X_max = np.amax(self.data)
        self.N = self.data.shape[0]
        return
    
    """Berechnen der Lagekennwerte Mittelwert und Median"""
    def clac_LMM(self):
        self.X_mean = np.mean(self.data)
        self.X_med = np.median(self.data)
        return
        
    """ Berechnen der Streuungskennwerte Stadardabweichung, Varianz und """
    """ Inter-Quartil-Range, bei Varianz muss die Anzahl der Freiheitsgrade"""
    """ auf N - 1 angepasst werden"""
    def calc_SSVI(self):
        self.X_var = np.var(self.data, ddof=1)
        self.X_std = np.std(self.data,ddof=1)
        self.X_q25 = np.quantile(self.data,0.25)
        self.X_q50 = np.quantile(self.data,0.50)
        self.X_q75 = np.quantile(self.data,0.75)
        self.X_iqr = self.X_q75 - self.X_q25
        return
        
    """Berechnen der Schiefe"""
    def calc_schiefe(self):
        self.X_skew_mom = skew(self.data)
        self. X_skew_qua = (np.quantile(self.data,0.75) - 2*np.quantile(self.data,0.5) + np.quantile(self.data,0.25))/self.X_iqr
        return
    
    def calc_haufigkeit(self):
        """
        Berechnung der absoluten und relativen Häufigkeit sowie der absoluten
        und relativen Summenhäufigkeit

        Returns
        -------
        None.

        """
        self.X_freq, self.Klassengrenzen = np.histogram(self.data, bins=np.arange(np.floor(self.X_min)-0.5, np.ceil(self.X_max)+1.5))
        self.X_rel_freq = self.X_freq/self.N
        self.X_sum_freq = np.cumsum(self.X_freq)
        self.X_rel_sum_freq = self.X_sum_freq/self.N
        Klassenmitten = np.arange(np.floor(self.X_min),np.ceil(self.X_max)+1)
        
    def calc_ausschuss(self,min,max):
        self.discard_min = min
        self.discard_max = max
        
        self.discard_min_p = test = norm.cdf((min-self.X_mean)/self.X_std)
        self.discard_max_p = test = 1-norm.cdf((max-self.X_mean)/self.X_std)
        self.discard_min_max_p = self.discard_min_p + self.discard_max_p
        
        return self.discard_min_max_p
    
    def print_ausschuss(self):
        pt = PrettyTable()
        pt.field_names = ['Grenzen','Warscheinlichkeit']
        pt.add_row(['//'+str(round(self.discard_min,4))+'//]-------------',strProzent(self.discard_min_p)])
        pt.add_row(['-------------[//'+str(round(self.discard_max,4))+'//',strProzent(self.discard_max_p)])
        pt.add_row(['//'+str(round(self.discard_min,4))+'//]---[//'+str(round(self.discard_max,4))+'//',strProzent(self.discard_min_max_p)])

        print(pt)
        
    def calc_ausschuss_toleranz(self,soll,toleranz):
        p = soll/100*toleranz
        min_val = soll-toleranz
        max_val = soll+toleranz
        
        self.calc_ausschuss(min_val,max_val)
        
        
    def sortKlass(self,class_n):
        '''
        Sortiert in Klassen ein

        Parameters
        ----------
        class_n : TYPE
            DESCRIPTION.

        Returns
        -------
        class_data : TYPE
            DESCRIPTION.

        '''
        #Daten holen
        data=self.data
        X_min = self.X_min
        X_delta = self.X_delta
        count = self.N
        
        #Besimme der Klassenbreite
        class_range = X_delta/class_n
        class_borders = np.zeros(class_n)
        #Klassengrenzen nach oben errechnen
        for i,border in enumerate(class_borders):
            class_borders[i] = X_min+(i+1)*class_range
        #class_borders = np.insert(class_borders, 0, self.X_min)
        #Klassen einteilen
        class_data = [0] * class_n
        class_data_n = [0] * class_n
        for i in range(class_n):
            class_current = np.where(data<=class_borders[i])[0]
            class_data[i] = data[class_current]
            class_data_n[i] = len(class_data[i])
            data = np.delete(data,class_current)
            
        self.class_data = class_data
        self.class_borders = class_borders
        self.class_data_n = class_data_n
        self.class_data_p = [x / count for x in class_data_n]
        return class_data
        
    def histogram(self,bins_n):
        '''
        Generiert Histogrammdaten

        Parameters
        ----------
        bins_n : TYPE
            Klassenanzahl.

        Returns
        -------
        hist_data_rel : TYPE
            Relative Haufigkeitsverteilung.

        '''
        
        data = self.data
        hist_rel,hist_edges =  np.histogram(data, bins=bins_n, density=True)
        hist_abs,hist_edges =  np.histogram(data, bins=bins_n, density=False)
        self.hist_binCenter = [(hist_edges[i]+hist_edges[i+1])/2 for i in range(len(hist_edges)-1)]
        self.hist_rel = hist_rel
        self.hist_abs = hist_abs
        self.hist_edges = hist_edges
        return hist_rel
    
    def histogram_tabel(self):
        pt =PrettyTable()
        pt.add_column(self.messgroese,self.hist_binCenter)
        pt.add_column('Rel',self.hist_abs)
        pt.add_column('Abs',self.hist_rel)
        
        print(pt)
        

#Guetefunktion

#Annahmebereich


#Glasfaser = read_mfile('Glasfaser','01_DataUebung/Glasfaser.mat','Glasfaserduchmesser','d/mymD')
#Glasfaser.histogram(10)
#Glasfaser.histogram_tabel()

name = 'Durchfluss'
messgroese = 'Durchflussmessung Q_IST'
einheit = 'm^3/h'

Durchflussmessung = DataSet(name,messgroese,einheit)
Durchflussmessung.read_m('00_Musterklausuren/00_Klausur_Daten/Durchflussmessung.mat')
Durchflussmessung.plot_info()








