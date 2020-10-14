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
    def __init__(self,name,mfile):
        self.name = name
        self.mfile = mfile
        
        print("Einlesen fuer " +name+ " der Datei "+mfile)

    """Einlesen und Umsortieren der Daten aus dem .mat-file"""
    def read_mat(matname):
        data = loadmat(matname)['data']
        return np.array(data).reshape(data.shape[0]*data.shape[1])
    
    """Bestimmung Datenumfang"""
    def calc_Datenumpfang(X):
        X_min = np.amin(X)
        X_max = np.amax(X)
        N = X.shape[0]
        return
    
    """Berechnen der Lagekennwerte Mittelwert und Median"""
    def clac_LMM(X):
        X_mean = np.mean(X)
        print(' ')
        print('Arithmetischer Mittelwert: ', X_mean)
        X_med = np.median(X)
        print('Median:', X_med )
        
    """ Berechnen der Streuungskennwerte Stadardabweichung, Varianz und """
    """ Inter-Quartil-Range, bei Varianz muss die Anzahl der Freiheitsgrade"""
    """ auf N - 1 angepasst werden"""
    def calc_SSVI(X):
        X_var = np.var(X, ddof=1)
        print(' ')
        print('Varianz: ', X_var)
        X_std = np.std(X,ddof=1)
        print('Standardabweichung: ', X_std)
        X_iqr = np.quantile(X,0.75) - np.quantile(X,0.25)
        print('Inter-Quartil-Range: ', X_iqr)
        
    """Berechnen der Schiefe"""
    def calc_schiefe(X):
        X_skew_mom = skew(X)
        print(' ')
        print('Momentenkoeffizient der Schiefe:', X_skew_mom )
        X_skew_qua = (np.quantile(X,0.75) - 2*np.quantile(X,0.5) + np.quantile(X,0.25))/X_iqr
        print('Quartilkoeffizient der Schiefe:', X_skew_qua )















