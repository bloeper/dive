from datetime import datetime
import time as t
import pickle, math
from os import path

class Dive:
	"""
	Dive class, this contains all specific data of 1 dive. 
	So you could read all the information about it back.
	"""
	def __init__( self, number = 0, depth = 0, date = 0, tIn = 0, tOut = 0, time = 0, weight = 0, location = '', temparature = 0, sight = 0, notes = '' ):
		self.number = number
		self.depth = depth
		self.date = date
		if (tIn is not 0 and tOut is not 0):
			self.tIn = t.strptime( tIn , '%H:%M' )
			self.tOut = t.strptime( tOut, '%H:%M' )
		else:
			self.tIn = 0
			self.tOut = 0
		self.weight = weight
		self.location = location
		self.temparature = temparature
		self.sight = sight
		self.notes = notes
		
		if self.tIn == 0 and self.tOut == 0:
			self.time = time
		else:
			self.time = self.calcTime( self.tIn, self.tOut)
	
	def setTimeIn( self, timeString ):
		self.tIn = t.strptime( timeString, '%H:%M' )
	
	def setTimeOut( self, timeString ):
		self.tOut = t.strptime( timeString, '%H:%M' )
		
	def calcTime( self, tIn, tOut ):
		""" 
		Calculate the divetime in minutes.
		This is done by substracting the time in of timeout.
		"""
		hours = tOut.tm_hour - tIn.tm_hour
		minutes = tOut.tm_min - tIn.tm_min
		minutes += hours * 60
		return minutes
	
	def __repr__( self ):
		degree = unichr(176).encode("utf_8")
		return 'Dive number: %d\nYou dived @ %s on %s.\nYour maximum depth was %d meters with %d kg of lead you had a sight of %d meters.\nDive time %d minutes the water temperature was %d%sC\nPersonal Notes:\n%s' % ( self.number, self.location, self.date, self.depth, self.weight, self.sight, self.time, self.temparature, degree, self.notes )

class Dives( Dive ):
	"""
	Contains a list of all the dives you've logged.
	It can also calculated some things about all the dives.
	"""
	def __init__( self ):
		self.dives = []
	
	#Handlers 
	def add( self, dive ):
		self.dives.append( dive )
	
	def __add__( self, dive ):
		self.dives.append( dive )
	
	def remove( self, number ):
		for dive in self.dives:
			if dive.number == number:
				self.dives.remove( dive )
				return
	
	def __sub__( self, number ):
		for dive in self.dives:
			if dive.number == number:
				self.dives.remove( dive )
				return
	
	def getDive( self, number ):
		for dive in self.dives:
			if dive.number == number:
				return dive
	
	# Some stats about dives.
	def totalDives( self ):
		return len( self.dives )
	
	def totalDiveTime( self ):
		"""
			Returns the total logged dive time in Hours:Minutes format.
			Function needs a lot of optimalisation
		"""
		time = 0.0
		for dive in self.dives:
			time += dive.time
		timeH = time / 60
		decimals = str( timeH ).split('.')[1]
		decimals = '0.' + decimals
		decimals = float( decimals ) * 60
		timeH = math.trunc( timeH )
		timeM = math.trunc( decimals )
		total = str( timeH ) + ':' + str( timeM )
		return total
	
	def maxDepth( self ):
		maxDepth = 0.0
		for dive in self.dives:
			if dive.depth >= maxDepth:
				maxDepth = dive.depth
		
		return maxDepth
	
	def averageTime( self ):
		time = 0.0
		for dive in self.dives:
			time += dive.time
		average = time / self.totalDives()
		return average
	
	def averageDepth( self ):
		depth = 0.0
		for dive in self.dives:
			depth += dive.depth
		
		average = depth / self.totalDives()
		return average
	
	#For the gui ;)
	def getList( self ):
		return self.dives
	
	#Save and load function
	def save( self ):
		pickle.dump( self.dives, open( path.join( path.dirname( path.dirname( path.realpath( __file__ ) ) ), "dive/dives.dat"), "wb" ) )
	
	def load( self ):
		try:
			data = pickle.load( open( path.join( path.dirname( path.dirname( path.realpath( __file__ ) ) ), "dive/dives.dat"), "rb" ) )
			data = sorted(data, key=lambda dive: dive.number)
			for item in data:
				self.dives.append( item )
		except:
			pass
