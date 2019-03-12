# coding: utf-8
"""
Code to find temperature and density of the narrow line region of an 
AGN given its lines ratio of the ions O[III] or N[II] with the ions 
O[II] or S[II].

Usage:
  Select one of the 

Example:
>>> import fivel_class as f
>>> 


Author: Angel Daniel Martinez Cifuentes
Date: 11 march, 2019

"""

import numpy as np


class agn:
	
	def __init__(self, J1=122.72, J2=1.36, ion1="OIII",ion2="SII",show=True):
		self.J1 = J1
		self.J2 = J2
		self.ion1 = ion1
		self.ion2 = ion2
		self.show = show

	# Physical constants
	h = 6.62607004e-34  # Planck constant
	c = 2.99792458e8    # Light speed
	k = 1.38064852e-23  # Boltzmann constant
	T = 1000

	# Values for the ions [Osterbrock, 2006]
	values = {'OIII':{'Ods':0.58, 'Lds':4363,'Ads':1.6, 'g':3.00,
					  'Ops':0.29, 'Lps':2321, 'Aps':2.3e-1,
					  'Odp1':2.29, 'Ldp1':4959, 'Adp1':6.8e-3,
					  'Odp2':2.29, 'Ldp2':5007, 'Adp2':2.0e-2},
			  'NII' :{'Ods':0.83, 'Lds':5755,'Ads':1.0, 'g':3.86,
					  'Ops':0.29, 'Lps':3063, 'Aps':3.3e-2,
					  'Odp1':2.64, 'Ldp1':6548, 'Adp1':9.8e-4,
					  'Odp2':2.64, 'Ldp2':6583, 'Adp2':3.0e-3},
			  'SII' :{'Oab':2.76, 'Oag':4.14, 'Obg':7.47,
					  'Aab':8.8e-4, 'Aag':2.6e-4, 'Lab':6731,
					  'Lag':6716},
			  'OII' :{'Oab':0.536, 'Oag':0.804, 'Obg':1.17,
					  'Aab':1.6e-4, 'Aag':3.6e-5, 'Lab':3726,
					  'Lag':3729}}

	# Exponential function

	def E(self,val,T):
		h = 6.62607004e-34  # Planck constant
		c = 2.99792458e8    # Light speed
		k = 1.38064852e-23  # Boltzmann constant
		y = np.exp(-h*c*10**10/(k*T*val))
		return y


	def ratio(self,J, Ne=10, T=1000, ion='OIII'):

		"""
		 Función que contiene las razones para los iones dados
		 [OIII, NII, SII, OII]. 
		
		 Seleccionar ION estudiar y su peso razón entre líneas
		 de cada uno de de ellos
		"""
		
		gd, gs = 5, 1    # Statistical Weigths
		gb, gg = 4, 6    # Statistical Weigths
		V = 8.6e-6    
		dic = self.values[ion]
		
		###########################################################
		
		if ion=='OIII' or ion=='NII':
			
			g = dic['g']
			Ods,  Lds,  Ads  = dic['Ods'], dic['Lds'], dic['Ads']
			Ops,  Lps,  Aps  = dic['Ops'], dic['Lps'], dic['Aps']
			Opd1, Lpd1, Adp1 = dic['Odp1'], dic['Ldp1'], dic['Adp1']
			Opd2, Lpd2, Adp2 = dic['Odp2'], dic['Ldp2'], dic['Adp2']
			
			f1 = gd*Adp2*Lds/(gs*Ads*Lpd2)
			f2 = gs*(Ads+Aps)/(g*V*Ops)
			f3 = gs*Ads/(g*V*Opd2)
			f4 = gd*Adp2/(g*V*Opd2)
			
			sol = []

			def funct(T,J):
				fac = f1*self.E(-Lds,T)
				y1 = fac*(Ne/(T**0.5) + f2*(1+(f3/f2)*self.E(Lds,T)))# +\
					#Ne/(g*T**0.5)*(Ods/Opd2)*self.E(Lds,T))
				y2 = J*(Ne/(T**0.5)+f4)# + \
				#Ne*Ods/(g*Opd2)*self.E(Lds,T)*self.E(Lpd2,T)*self.E(-Lps,T))
				
				return y1, y2
			
			Te = np.arange(100,1e5,0.1)
			AA = funct(Te,J)[0]
			BB = funct(Te,J)[1]
			idx = np.argwhere(np.diff(np.sign(AA - BB))).flatten()
			
			sol = Te[idx]
			
			return sol[0]
		
		###########################################################
		
		elif ion=='SII' or ion=='OII':
			
			val = self.values[ion]
			C = V/(T**0.5)
			Oab, Oag, Obg = val['Oab'], val['Oag'], val['Obg']
			Aab, Aag = val['Aab'], val['Aag']
			Lab, Lag = val['Lab'], val['Lag']

			ff1 = 1+(Obg/Oab)+(Obg/Oag)
			ff2 = gb/Oab
			ff3 = gg/Oag
			ff3/ff1
			
			up = (ff3/ff1)*Aag*Aab*(gg-J*gb)
			down = C*(J*gb*Aab - gb*Aag)
			
			sol = up/down
			
			return sol


	#def fivel(J1,J2,ion1='OIII',ion2='SII',show=True):
	def fivel(self):
		
		###########################################################
		
		if self.ion1=='OIII' or self.ion1=='NII': #2p2
			X = 1e6 #value of density
			T = self.ratio(J=self.J1,Ne=X,ion=self.ion1)
			
			print("\n Begin of iteration\n")
			
			#Begin of "iteration"
			for i in range(0,4):
				RES = T
				Ne = self.ratio(J=self.J2,T=RES,ion=self.ion2)
				T = self.ratio(J=self.J1,Ne=Ne,ion=self.ion1)
				if self.show:
					print("  Iteration {}\n Ne  {}\n T   {}\n".format(i+1,Ne,RES))
			
		###########################################################
		
		elif self.ion1=='SII' or self.ion1=='OII': #2p3
			X = 12036 #value of Temperature
			Ne = self.ratio(J=self.J2,T=X,ion=self.ion2)
			print("\n Begion of iteration\n")
			
			#Begin of "iteration"
			for i in range(0,4):
				RES = Ne
				T = self.ratio(J=self.J2,Ne=RES,ion=self.ion2)
				Ne = ratio(J=J1,T=T,ion=ion1)
				if show:
					print("  Iteration {}\n Ne  {}\n T   {}\n".format(i+1,RES,T))
		
		#Return Temperature and Density 
		return T, Ne




if __name__=='__main__':

	### NGC 3227
	A = agn(J1=122.72,J2=1.36,ion1='OIII',ion2='SII')
	T, Ne = A.fivel()
	print("Temperature {}\nDensity     {}".format(T,Ne))


	### NGC 1068
	
	A = agn(J1=15.628,J2=1.228,ion1='OIII',ion2='SII')
	T, Ne = A.fivel()
	print("Temperature {}\nDensity     {}".format(T,Ne))
	
	### NGC 5548
	A = agn(J1=65.865,J2=1.523,ion1='OIII',ion2='SII')
	T, Ne = A.fivel()
	print("Temperature {}\nDensity     {}".format(T,Ne))

