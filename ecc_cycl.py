#!/usr/bin/python

from opyscad import *
from math import sin, cos, sqrt, pi, floor


class EccCycl(object):
	def __init__(self,
					r = 0,
					R = 0,
					e = 0,
					ch = 0,
					dt = 0.1):
		self.smallGearRadius = r
		self.bigGearRadius = R
		self.eccentricity = e
		self.cycleHeight = ch
		self.dt = dt
		self.bigGearAxisRadius = 0
		self.smallGearAxisRadius = 0
		self.slices = 10
		self.smallGearFn = 60
		self.axisFn = 15

	def bigGear(self, h):
		if not self.checkValues():
			print 'Incorrect values'
			return None
		
		h = float(h)

		nr = self._R / self._r
		n = int(2 * pi / self._dt * nr)
		t = 0
		points = []
		for i in xrange(n):
			t += self._dt
			points.append(self.epitrochoid(t))
			
		res = polygon(points)
		
		res = linear_extrude(height = h, twist = self.twist(h)/nr, slices=self._slices) (res)
		
		if self._axis_R > 0:
			res -= cylinder(h + 2, self._axis_r, fn = self._axisFn) << [0, 0, -1]
		
		return res

	def smallGear(self, h):
		if not self.checkValues():
			print 'Incorrect values'
			return None
		
		res = circle(self._r, fn = self._smallGearFn)
		res <<= [self._e * self._r, 0, 0]
		res = linear_extrude(height = h, twist = -self.twist(h), slices = self._slices) (res)
		
		if self._axis_r > 0:
			res -= cylinder(h + 2, self._axis_r, fn=self._axisFn) << [0, 0, -1]
		
		return res
	
	def epitrochoid(self, t):
		r = self._r
		R = self._R

		e = self._e * r

		m = r / R
		
		x = R * (m + 1) * cos(m * t) - e * cos((m + 1) * t)
		y = R * (m + 1) * sin(m * t) - e * sin((m + 1) * t)
		
		xf = R * (m + 1) * cos(m * t) * m - e * cos((m + 1) * t) * (m + 1)
		yf = R * (m + 1) * sin(m * t) * m - e * sin((m + 1) * t) * (m + 1)
		
		m = sqrt(xf*xf + yf*yf)
		
		x -= xf / m * r
		y -= yf / m * r
		
		return [x, y]
		
	@property
	def smallGearRadius(self):
		return self._r
	
	@smallGearRadius.setter
	def smallGearRadius(self, val):
		self._r = float(val)
	
	@property
	def bigGearRadius(self):
		return self._R
	
	@bigGearRadius.setter
	def bigGearRadius(self, val):
		self._R = float(val)
		
	@property
	def eccentricity(self):
		return self._e
	
	@eccentricity.setter
	def eccentricity(self, val):
		self._e = float(val)
		
	@property
	def cycleHeight(self):
		return self._cycleHeight
	
	@cycleHeight.setter
	def cycleHeight(self, val):
		self._cycleHeight = float(val)
		
	@property
	def dt(self):
		return self._dt
	
	@dt.setter
	def dt(self, val):
		self._dt = float(val)
		
	@property
	def bigGearAxisRadius(self):
		return self._axis_R
	
	@bigGearAxisRadius.setter
	def bigGearAxisRadius(self, val):
		self._axis_R = float(val)
		
	@property
	def smallGearAxisRadius(self):
		return self._axis_r
	
	@smallGearAxisRadius.setter
	def smallGearAxisRadius(self, val):
		self._axis_r = float(val)
		
	@property
	def slices(self):
		return self._slices
	
	@slices.setter
	def slices(self, val):
		self._slices = int(val)
		
	@property
	def smallGearFn(self):
		return self._smallGearFn
	
	@smallGearFn.setter
	def smallGearFn(self, val):
		self._smallGearFn = int(val)
		
	@property
	def axisFn(self):
		return self._axisFn
	
	@axisFn.setter
	def axisFn(self, val):
		self._axisFn = int(val)
		
	def setRnN(self, R, n):
		self.bigGearRadius = R
		self.smallGearRadius = self._R / n
	
	def checkValues(self):
		if self._r <= 0 \
			or self._R <= 0 \
			or self._e <= 0 \
			or self._dt <= 0 \
			or self._cycleHeight <= 0:
			return False
		if (self._R / self._r) != floor(self._R / self._r):
			return False
		
		return True
	
	def twist(self, h):
		return h / self._cycleHeight * 360.0
		
	
	
