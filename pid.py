# -*- coding: utf-8 -*-
"""PID.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Co4eNxG5eyVG-ru779KgNQ8-4f4W8LVX
"""

#More information: http://en.wikipedia.org/wiki/PID_controller
#references: - PID Controller Implementation in Software, Phil's lab
#            - Goal to goal turtlesim, Anis Koubaa

class PID:
	"""
	PID control
	"""

	def __init__(self, p=5/16, i=0.0, d=0.0, Derivator=0, Integrator=0, Integ_max=200, Integ_min=-200):

		self.const_p=p
		self.const_i=i
		self.const_d=d
		self.Derivator=Derivator
		self.Integrator=Integrator
		self.Integ_max=Integ_max
		self.Integ_min=Integ_min
		self.err=0.0
		self.set_point=0.0
		

	def error_update(self, err):
		"""
		PID output value for input 
		"""

		self.error = err

		self.P_cmd = self.const_p * self.err
		self.D_cmd = self.const_d * ( self.err - self.Derivator)
		self.Derivator = self.error

		self.Integrator = self.Integrator + self.err

		if self.Integrator > self.Integ_max:
			self.Integrator = self.Integ_max
		elif self.Integrator < self.Integ_min:
			self.Integrator = self.Integ_min

		self.I_cmd = self.Integrator * self.const_i

		PID = self.P_cmd + self.I_cmd + self.D_cmd

		return PID

	def setPoint(self,set_point):
		
		self.set_point = set_point
		self.Integrator=0
		self.Derivator=0

	def setIntegrator(self, Integrator):
		self.Integrator = Integrator

	def setDerivator(self, Derivator):
		self.Derivator = Derivator

	def setp_const(self,P):
		self.const_p=P

	def seti_const(self,I):
		self.const_i=I

	def setd_const(self,D):
		self.const_d=D
		
	def getError(self):
		return self.err	

	def getPoint(self):
		return self.set_point
        	
	def getDerivator(self):
		return self.Derivator

	def getIntegrator(self):
		return self.Integrator

