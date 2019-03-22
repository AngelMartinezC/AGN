#-*- coding:utf-8

"""
  Calculation of the area under the spectral flux function
  for an AGN spectrum.
"""


from __future__ import print_function
from __future__ import division


import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
import os


data = 'array.fit' #or in .fits format

def read_fits(name):
  array = 0
