# -*- coding: utf-8 -*-
"""
Bibliothek der wichtigsten Funktionon in Design for Six Sigma

"""

""" Bibliotheken importieren"""
import numpy as np
import scipy as sp
#import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import skew
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



class read_mfile:
    """
    Einlesen einer Matlab-Datei
    """
    def __init__(self,name,mfile,messgroese,einheit):
        """
        Name,mfile,messgroese,einheit
        """
        self.name = name
        self.mfile = mfile
        
        self.messgroese = messgroese
        self.einheit = einheit
        
        print("Einlesen fuer " +name+ " der Datei "+mfile)
        
        """Daten aus dem .mat-file"""
        self.data = self.read_mat()
        
        self.X_min = 0
        self.X_max = 0
        self.N = 0
        self.calc_Datenumpfang()
        
        """Lagekennwerte"""
        self.X_mean = 0
        self.X_med = 0
        self.clac_LMM()
        self.X_delta = self.X_max - self.X_min
        
        """Streuungskennwerte"""
        self.X_var = 0
        self.X_std = 0
        self.X_iqr = 0
        self.calc_SSVI()
        
        """Schiefe"""
        self.X_skew_mom = 0
        self. X_skew_qua = 0
        self.calc_schiefe()
        
        """  absolute und relative Häufigkeit"""
        """  absolute und relative Summenhäufigkeit"""
        self.X_freq = 0
        self.X_rel_freq = 0
        self.X_sum_freq = 0
        self.X_rel_sum_freq = 0
        self.calc_haufigkeit()
        
        self.class_data = 0
        self.class_data_n = 0
        
        self.hist_binCenter = 0
        self.hist_data = 0
        self.hist_edges = 0
        
        
        
        
        
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
        """ Grafische Darstellung der einzelnen Messwete als Streudiagramm """
        fig = plt.figure(1, figsize=(12, 4))
        ax1, ax2 = fig.subplots(1,2)
        n = np.arange(1,self.N+1)
        ax1.plot(n,self.data, 'bo', Linewidth = 2, label = 'Stichproben')
        ax1.grid(True, which='both', axis='both', linestyle='--')
        ax1.axis([1, self.N, yLimMin, yLimMax])
        ax1.legend(loc='upper right')
        ax1.set_xlabel('Stichprobe n')
        ax1.set_ylabel(self.messgroese+' '+self.einheit)
        
        """ Erstellen eines Boxplt """
        ax2.boxplot(self.data)
        ax2.grid(True, which='both', axis='both', linestyle='--')
        ax2.set_xlabel('Messreihe ')
        ax2.set_ylabel(self.messgroese+' '+self.einheit)
        ax2.axis([0, 2, yLimMin, yLimMax])
        
        
        """ Grafische Darstellung der relativen Häufigkeiten als Histogramm """
        fig = plt.figure(2, figsize=(12, 4))
        ax1, ax2 = fig.subplots(1,2)
        ax1.hist(self.data, self.Klassengrenzen, histtype='bar' , color='b', weights=np.ones(self.N)/self.N, rwidth=1)
        ax1.grid(True, which='both', axis='both', linestyle='--')
        ax1.set_xlabel(self.messgroese+' '+self.einheit)
        ax1.set_ylabel('Relative Häufigkeit h(m)')
        ax1.axis([yLimMin, yLimMax, 0, 0.6])
        
        """ Grafische Darstellung der relativen Summenhäufigkeit """
        Xsort = np.append(np.append(48,np.sort(self.data)),54)
        Psum = np.append(np.append([0,],np.arange(1,self.N+1)/self.N),1)
        ax2.step(Xsort,Psum, color='b', where='post', linewidth=2)
        ax2.grid(True, which='both', axis='both', linestyle='--')
        ax2.set_xlabel(self.messgroese+' '+self.einheit)
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
        

    def read_mat(self):
        """Einlesen und Umsortieren der Daten aus dem .mat-file"""
        readFile = loadmat(self.mfile)
        try:
            data = readFile['values']
        except:
            print('mFile read faild: No values found')
        return np.array(data).reshape(data.shape[0]*data.shape[1])
    
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
        



#Glasfaser = read_mfile('Glasfaser','01_DataUebung/Glasfaser.mat','Glasfaserduchmesser','d/mymD')
#Glasfaser.histogram(10)
#Glasfaser.histogram_tabel()











