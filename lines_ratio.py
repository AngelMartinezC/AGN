#-*- coding:utf-8

"""
Lines ratio
===========

  Code to calculate Temperature [K] and particle density [part cm^-3] from a 
  given fits data set from SSDS (Sloan Digital Sky Survey)


Needed packages:
----------------

  - lmfit:       For Gaussian fit   -  https://github.com/lmfit/lmfit-py
  - astropy:     To read Fits file  -  https://github.com/astropy/astropy
  - scipy:       For integration    -  https://github.com/scipy/scipy
  - numpy        Numerical Python   -  https://github.com/numpy/numpy
  - matplotlib   Plotting library   -  https://github.com/matplotlib/matplotlib
  - gaussian     For graphics          (same path)
  - fivel        To make iterations    (same path)


Usage:
------
  If the program is called as a module, the calling proccedure is like:
  
  >>> import lines_ratio as lr
  >>>
  >>> name = 'some .fits file'
  >>> T,Ne = lr.calculation(name)
  
  The user will be asked for the ions to make the calculations if they are
  not specified. Avaliable ions are (O[III] or N[II]) and (S[II] or O[II])
  It returns T and Ne, the temperature and particle density in [K] and
  [part cm^-3] respectively of the narrow line region from an AGN.
  
  
"""

from gaussian import spectrum
from fivel import agn


def calculation(name=None, ion1=None, ion2=None, statistics=False, header=False, plot=True, savefig=False, ax=None, show_model=False, iteration=True, plot_spectrum=False,z = 0.00420765,**kwargs):
	
	
	if not name:
		print('Please provide a .fits file from SDSS. ')
		print('Exiting...')
		exit()

	def message():
		print('-------------------------------------------------------')
		print(' Code to calculate the Temperature and Density of a set of given lines\n')
		print('  The user have to select two points of the graphic')
		print('  corresponding to the value of two wavelengths over')
		print('  which will be performed a gaussian fit\n')
		print('  The user will be asked for the lines to work with:')
		print('   Avaliable ions: ')
		print('     O[III] or N[II]\n     S[II]  or O[II]')
		print('  \n  After selecting the two points, press enter to pass the next flux\n')
		input('  < Press enter to continue > ')
		print(' ')

	message()
	
	if not ion1:
		i1 = float(input("  Type the number of the ion1\n    1:   O[III]\n    2:   N[II]\n"))
		if i1 == 1:
			ion1 = 'OIII'
		elif i1 == 2:
			ion1 = 'NII'
		else: 
			print("Number not defined")
			print("Exiting")
			exit()
	
	if not ion2:
		i2 = float(input("  Type the number of the ion2\n    1:   S[II]\n    2:   O[II]\n"))
		if i2 == 1:
			ion2 = 'SII'
		elif i2 == 2:
			ion2 = 'OII'
		else: 
			print("Number not defined")
			print("Exiting")
			exit()
	
	data = spectrum(data=name,header=header,z=z)
	
	if plot_spectrum is True:
		data.plot()
	
	A = data.limits(statistics=statistics,plot=plot,savefig=savefig,ax=ax,show_model=show_model)

	F6716, F6731 = A[0], A[1]
	F4363, F4959, F5007 = A[2], A[3], A[4]

	F2 = F6716/F6731
	F1 = (F5007 + F4959)/F4363


	A = agn(J1=F1,J2=F2,ion1=ion1,ion2=ion2,show=iteration)
	T, Ne = A.fivel()
	
	return T, Ne
	





if __name__=='__main__':
	
	name = 'data/spec-1070-52591-0072.fits'
	z = 0.00420765
	#name = 'data/spec-1369-53089-0157.fits'
	
	T, Ne = calculation(name,z=z)
	print("  Temperature  {}\n  Density      {}".format(T,Ne))

