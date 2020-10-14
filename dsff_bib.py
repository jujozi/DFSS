# -*- coding: utf-8 -*-
"""
Bibliothek der wichtigsten Funktionon in Design for Six Sigma

"""

""" Bibliotheken importieren"""
import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import skew
from scipy.io import loadmat
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')

class read_mfile:
    def __init__(self,name,mfile,messgroese,einheit):
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
        
        
        
        
        
    def print_info(self):
        print(' ')
        print('Arithmetischer Mittelwert: ', self.X_mean)
        print('Median:', self.X_med )
        print(' ')
        print('Varianz: ', self.X_var)
        print('Standardabweichung: ', self.X_std)
        print('Inter-Quartil-Range: ', self.X_iqr)
        print(' ')
        print('Quartilkoeffizient der Schiefe:', self.X_skew_qua )
        print('Momentenkoeffizient der Schiefe:', self.X_skew_mom )
        print(' ')
        print('Absolute Häufigkeit hA(x): ', self.X_freq)
        print('RelativeHaeufigkeit h(x): ', self.X_rel_freq )
        print('Absolute Summenhäufigkeit HA(x): ',self.X_sum_freq)
        print('Relative Summenhäufigkeit H(x): ',self.X_rel_sum_freq)
        
        
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
        

    """Einlesen und Umsortieren der Daten aus dem .mat-file"""
    def read_mat(self):
        data = loadmat(self.mfile)['data']
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
        self.X_iqr = np.quantile(self.data,0.75) - np.quantile(self.data,0.25)
        return
        
    """Berechnen der Schiefe"""
    def calc_schiefe(self):
        self.X_skew_mom = skew(self.data)
        self. X_skew_qua = (np.quantile(self.data,0.75) - 2*np.quantile(self.data,0.5) + np.quantile(self.data,0.25))/self.X_iqr
        return
    
    """ Berechnung der absoluten und relativen Häufigkeit sowie der absoluten"""
    """ und relativen Summenhäufigkeit"""
    def calc_haufigkeit(self):
        self.X_freq, self.Klassengrenzen = np.histogram(self.data, bins=np.arange(np.floor(self.X_min)-0.5, np.ceil(self.X_max)+1.5))
        self.X_rel_freq = self.X_freq/self.N
        self.X_sum_freq = np.cumsum(self.X_freq)
        self.X_rel_sum_freq = self.X_sum_freq/self.N
        Klassenmitten = np.arange(np.floor(self.X_min),np.ceil(self.X_max)+1)
        
        
    















