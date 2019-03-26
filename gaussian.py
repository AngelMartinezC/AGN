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
from lmfit import Model
from scipy.integrate import trapz, simps


class spectrum:
	
	
	def __init__(self,data,header=False):
		
		self.data = data
		self.header = header
	
	
	def read(self,data,header):
		
		if isinstance(data,str):
			array = fits.getdata(self.data,0)
			x, y = [], []  #Wavelength and flux
			for i in range(len(array)):
				y.append(array[i][0])
				x.append(10**array[i][1])	
				
			if header == True:
				header = fits.getheader(data,0)
				return np.array(x), np.array(y), header
			else:
				return np.array(x), np.array(y)
		else:
			print('Not Valid ... Exiting')
			exit()


	def plot(self):
		
		if self.header == True:
			x_axis, y_axis, head = self.read(self.data,self.header)
		else:
			x_axis, y_axis = self.read(self.data,self.header)
		
		plt.figure(figsize=(8,5))
		plt.plot(x_axis,y_axis)
		plt.grid()
		plt.ylabel(r'Flux $[10^{17}$ erg cm$^{-2}$ s$^{-1}$ $\AA^{-1}$]')
		plt.xlabel(r'Wavelength [$\AA$]')
		plt.show()


	def limits(self,wavelength1,wavelength2,statistics=False,plot=False,ax=None,
		savefig=False,show_model=False):
		
		
		if self.header == True:
			x_axis, y_axis, head = self.read(self.data,self.header)
		else:
			x_axis, y_axis = self.read(self.data,self.header)
		
		
		def gaussian(x, amp, cen, wid):
			return (amp/(np.sqrt(2*np.pi)*wid))*np.exp(-(x-cen)**2/(2*wid**2))


		def eqw(lambda1,lambda2,topflux,bottomflux):
			a = topflux-bottomflux
			sigma = (lambda1-lambda2)/2.35
			A = a*sigma*np.sqrt(2*np.pi)/topflux
			return A


		def plot_fit(ax):
			if ax is None:
				ax = plt.gca()
			ax.plot(x_range,y_range+mini,'o-',label='Spectrum')
			ax.plot(X,Y+mini,label='Gaussian function')
			ax.plot(x_range,result.best_fit+mini,'o--',label='Gaussian Fit')
			plt.ylabel(r'Flux $[10^{17}$ erg cm$^{-2}$ s$^{-1}$ $\AA^{-1}$]')
			plt.xlabel(r'Wavelength [$\AA$]')
			plt.legend()
			plt.grid()
			if savefig == True:
				plt.savefig('gaussian.png')
			else:
				pass
			plt.show()


		def statistics_fit():
			maxy = max(y_axis[x1-1:x2+1])
			miny = min(y_axis[x1-1:x2+1])
			equi = eqw(wavelength1,wavelength2,maxy,miny)
			print('\nStatistics\n')
			print(' Min Value:  {0:.3f}  Flux'.format(mini))
			print(' Max Value:  {0:.3f}  Flux'.format(maxy))
			print(' Lambda1:    {0:.3f}  Å'.format(x_range[0]))
			print(' Lambda2:    {0:.3f}  Å\n'.format(x_range[-1]))
			print(" Equivalent Width:  {}\n".format(equi))
			print(" Area:")
			print("   Trapezoid:   {}\n   Simpson:     {}".format(trapz(Y,X), simps(Y,X)))
			
		
		x1 = np.where(abs(x_axis-wavelength1+1) <= 1)[0][0]
		x2 = np.where(abs(x_axis-wavelength2-2) <= 1)[0][0]
		
		if y_axis[x1] <= y_axis[x2]:
			mini = y_axis[x1]
		else:
			mini = y_axis[x2]

		x_range = x_axis[x1-1:x2+1]
		y_range = y_axis[x1-1:x2+1]-mini

		gmodel = Model(gaussian)
		result = gmodel.fit(y_range,x=x_range,amp=1000,cen=x_range[0],wid=1.5)
		
		amp = result.best_values['amp']
		cen = result.best_values['cen']
		wid = result.best_values['wid']
		X = np.linspace(x_range[0],x_range[-1],1000)
		Y = gaussian(X, amp=amp, cen=cen, wid=wid)
		
		
		if show_model == True:
			print(gmodel.param_names)
			print(result.fit_report(show_correl=False))
			result.plot()
			print(result.best_values)
		else:
			pass
			
		
		if plot == True:
			plot_fit(ax)
		else:
			pass
		
		
		if statistics == True:
			statistics_fit()
		else:
			pass
		
		
		if self.header == True:
			return trapz(Y,X),result.best_fit,x_axis,y_axis,X,Y,head
		else:
			return trapz(Y,X),result.best_fit,x_axis,y_axis,X,Y



if __name__=='__main__':

	data = 'example/spec-1070-52591-0072.fits'

	x1 = 6740
	x2 = 6754

	data = spectrum(data,header=False)
	data.plot()
	A=data.limits(x1,x2,statistics=True,plot=True,savefig=True)
	print('Area    {}'.format(A[0]))
	
	
	


