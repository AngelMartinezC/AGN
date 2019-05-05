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
			print('Not valid dataset ... Abort')
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


	def limits(self,statistics=False,plot=True,ax=None,
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
		

		def plot_fit(ax,fit,x_range,y_range,X,Y,mini=0,area=0.0,ind=0):
			if ax is None:
				ax = plt.gca()
			ax.plot(x_range,y_range+mini,'o-',color='b')
			ax.plot(X,Y+mini,'-',label='Gaussian function',color='red')
			ax.plot(x_range,fit+mini,'o--',label='Gaussian Fit',color='y')
			plt.title('Area: {0:.3f}'.format(area))
			plt.ylabel(r'Flux $[10^{17}$ erg cm$^{-2}$ s$^{-1}$ $\AA^{-1}$]')
			plt.xlabel(r'Wavelength [$\AA$]')
			plt.legend(loc=2)
			#plt.grid()
			if savefig == True:
				v = ind+1
				plt.savefig(str(v)+'gaussian.png')
			else:
				plt.savefig("temp.png")
				os.system("rm -rf temp.png")

			plt.pause(1) # <-------
			#input("<Hit Enter To Close>")
			plt.waitforbuttonpress(0)
			plt.close()

			plt.show()


		def statistics_fit(y_axis,x_range,y_range,x1,x2,x01,x02,X,Y):
			maxy = max(y_axis[x1-1:x2+1])
			miny = min(y_axis[x1-1:x2+1])
			equi = eqw(x01,x02,maxy,miny)
			print('\nStatistics\n')
			print(' Min Value:  {0:.3f}  Flux'.format(miny))
			print(' Max Value:  {0:.3f}  Flux'.format(maxy))
			print(' Lambda1:    {0:.3f}  Å'.format(x_range[0]))
			print(' Lambda2:    {0:.3f}  Å\n'.format(x_range[-1]))
			print(" Equivalent Width:  {}\n".format(equi))
			print(" Area:")
			print("   Trapezoid:   {}\n   Simpson:     {}".format(trapz(Y,X), simps(Y,X)))
			
		
		def windows(x_axis,y_axis,wavelength1=6734,wavelength2=6760, legend='6716$\AA$',line=4382.4):
			
			xx1 = np.where(abs(x_axis-wavelength1+1) <= 1)[0][0]
			xx2 = np.where(abs(x_axis-wavelength2-2) <= 1)[0][0]
			plt.plot(x_axis[xx1:xx2],y_axis[xx1:xx2],'o-',color='b',label=legend)
			plt.axvline(x=line,linewidth=3,alpha=0.7)
			plt.ylabel(r'Flux $[10^{17}$ erg cm$^{-2}$ s$^{-1}$ $\AA^{-1}$]')
			plt.xlabel(r'Wavelength [$\AA$]')
			plt.grid()
			plt.legend(loc=2)
			print("Please select two regions of the graph ")
			x = plt.ginput(2,show_clicks=True)
			x01 = x[0][0]
			x02 = x[1][0]
			return x01,x02
		
		
		def lines(num=4):

			waves = [[6734,6760,'S[II]: 6716$\AA$',6746.8],[6750,6780,'S[II]: 6731$\AA$',6760.8],
			[4366,4393,'O[III]: 4363$\AA$',4382.4],[4962,4995,'O[III]: 4959$\AA$',4982.0],
			[5012,5050,'O[III]: 5007$\AA$',5030.3]]
			
			x01, x02 = windows(x_axis=x_axis,y_axis=y_axis,wavelength1=waves[num][0],
			wavelength2=waves[num][1],legend=waves[num][2],line=waves[num][3])
			
			x1 = np.where(abs(x_axis-x01+1) <= 1)[0][0]
			x2 = np.where(abs(x_axis-x02-2) <= 1)[0][0]
			
			if y_axis[x1] <= y_axis[x2]:
				mini = y_axis[x1]
			else:
				mini = y_axis[x2]

			x_range = x_axis[x1:x2]
			y_range = y_axis[x1:x2]-mini

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
				
				
			AREA = trapz(Y,X)
			
			if plot == True:
				plot_fit(ax,result.best_fit,x_range,y_range,X,Y,mini,area=AREA,ind=num)
			else:
				#pass
				plt.show()
			
			
			if statistics == True:
				statistics_fit(y_axis,x_range,y_range,x1,x2,x01,x02,X,Y)
			else:
				pass
			
			if self.header == True:
				return AREA,result.best_fit,x_axis,y_axis,X,Y,head
			else:
				return AREA,result.best_fit,x_axis,y_axis,X,Y
		
		area = []
		for i in range(0,5):
			area.append(lines(i)[0])
		
		return area



if __name__=='__main__':

	data = '../data/spec-1070-52591-0072.fits'
	
	def message():
		print('-------------------------------------------------------')
		print(' Code to calculate the fluxes of a set of given lines\n')
		print('  The user have to select two points of the graphic')
		print('  corresponding to the value of two wavelengths over')
		print('  which will be performed a gaussian fit\n')
		input('  < Press enter to continue > ')
		print(' ')
	
	message()
	
	data = spectrum(data,header=False)
	#data.plot()
	A=data.limits(statistics=False,plot=True,savefig=False)
	print('\n Area\n  6716:   {0:.3f}\n  6731:   {1:.3f}\
	\n  4363:   {2:.3f}\n  4959:   {3:.3f}\
	\n  5007:   {4:.3f}'.format(A[0],A[1],A[2],A[3],A[4]))
	
	
	

