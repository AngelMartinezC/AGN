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

name2 = 'example/spSpec-52591-1070-072.fit'

def read_fit(name):
  if isinstance(name,str):
    array = fits.getdata(name,0)
    header = fits.getheader(name,0)
    #new_data = np.transpose(np.array([i for i in array]))
    return array, header
  else:
    return "Not valid"

def read_fits(name):
  if isinstance(name,str):
    array = fits.getdata(name,0)
    header = fits.getheader(name,0)
    new_data = np.transpose(np.array([i for i in array]))
    return new_data, header
  else:
    return "Not valid"


data, head = read_fit(name2)


print(head['COEFF0'],10**head['COEFF0'])
print(head['Z'])

#print(head)

x_range = ([i+10**head['COEFF0'] for i in range(len(data[0]))])

"""
plt.title('fit')
plt.plot(x_range,data[0])
#plt.xlim(9200,9250)
#plt.plot(data[1])
plt.show()
exit()
"""

hdudata, hduheader = read_fits(name)
x_axis = 10**hdudata[1]    # Wavelength in log10(AA)
y_axis = hdudata[0]        # Spectral flux

print(x_axis[0],x_axis[-1])

plt.title("fits")
plt.plot(x_axis,y_axis)

plt.show()






