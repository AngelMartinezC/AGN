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


name = 'example/spec-1070-52591-0072.fits'

def read_fits(name):
  if isinstance(name,str):
    array = fits.getdata(name,0)
    header = fits.getheader(name,0)
    new_data = np.transpose(np.array([i for i in array]))
    return new_data, header
  else:
    return "Not valid"


hdudata, hduheader = read_fits(name)
x_axis = 10**hdudata[1]    # Wavelength in log10(AA)
y_axis = hdudata[0]        # Spectral flux


plt.plot(x_axis,y_axis)
plt.show()






