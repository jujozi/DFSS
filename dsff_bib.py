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


"""Einlesen und Umsortieren der Daten aus dem .mat-file"""
def read_mat(matname):
    data = loadmat(matname)['data']
    return np.array(data).reshape(data.shape[0]*data.shape[1])













