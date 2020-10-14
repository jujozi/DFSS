#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Anwendungsbeispiel der Bibliothek dfss

"""

""" Bibliotheken importieren"""
import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import skew
from scipy.io import loadmat
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')
import dsff_bib as dfss


""" Test """
print("Anwendungsbeispiel der Bibliothek der Vorlesung DFSS")

""" Import einer Matlab .mat Datei"""

X=dfss.read_mat('Klebermenge')
