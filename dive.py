import sqlite3
from os import path
from math import trunc
from datetime import time

class Dive:
	def __init__( self ):
		"""
		Database class
		__init__ creates a db connection and cursor.
		If db doesn't exists it will be created with the table in it.
		"""
		#Path var
		dbfile = path.join( path.dirname( path.dirname( path.realpath( __file__ ) ) ), "dive/dive.db")
		if path.exists( dbfile ):
			#Database file exists, only make connection
			self.conn = sqlite3.connect( dbfile )
			self.conn.row_factory = sqlite3.Row
		else:
			#Database file doesn't exists, make connection and create tables
			self.conn = sqlite3.connect( dbfile )
			self.conn.row_factory = sqlite3.Row
			self.conn.execute( """CREATE TABLE dive (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			number INTEGER UNIQUE,
			depth DOUBLE,
			divedate DATE,
			time_in TIME,
			time_out TIME,
			time DOUBLE,
			bar_in INTEGER,
			bar_out INTEGER,
			lead INTEGER,
			location STRING,
			temperature INTEGER,
			sight INTEGER,
			notes TEXT
			)
			""")		
		
		self.cursor = self.conn.cursor()
	
	def query( self, query = None ):
		""" 
		Method to do anykind of query
		"""
		if query == None:
			print "Please specify a query"
		else:
			self.cursor.execute( query )
			self.conn.commit()
			return self.cursor
	
	def fetchDive( self, diveNumber ):
		""" 
		Fetch a dive. And return the information
		"""
		data = self.cursor.execute( "SELECT * FROM dive WHERE number =" + str( diveNumber ) ).fetchall()
		return data[0]
	
	def listDives( self ):
		"""
		Fetch all data from the dives table.
		"""
		data = self.cursor.execute( "SELECT * FROM dive ORDER BY number" ).fetchall()
		return data
	
	def maxDepth( self ):
		maxDepth = self.cursor.execute( "SELECT MAX( depth ) FROM dive" ).fetchall()
		return maxDepth[0][0]
	
	def averageDepth( self ):
		averageDepth = self.cursor.execute( "SELECT AVG( depth ) FROM dive" ).fetchall()
		return averageDepth[0][0]
	
	def totalTime( self ):
		totalTime = self.cursor.execute( "SELECT SUM( time )/60 FROM dive" ).fetchall()
		time = str( totalTime[0][0] )
		Hours = time.split(".")[0]
		Minutes = float( "0."+ time.split(".")[1] )
		Minutes *= 60
		Minutes = trunc(round( Minutes ) )
		if len( str( Minutes ) ) == 1:
			Minutes = "0" + str( Minutes )
		if len( Hours ) == 1:
			Hours = "0" + Hours
		totaltime = Hours + ":" + str( Minutes )
		return totaltime
	
	def averageTime( self ):
		averageTime = self.cursor.execute( "SELECT AVG( time ) FROM dive" ).fetchall()
		return averageTime[0][0]
	
	def totalDives( self ):
		totalDives = self.cursor.execute( "SELECT COUNT(*) FROM dive" ).fetchall()
		return totalDives[0][0]
		
	def totalLocations( self ):
		totalLocations = self.cursor.execute( "SELECT COUNT( DISTINCT( location ) ) FROM dive" ).fetchall()
		return totalLocations[0][0]
	
	def averageUsage( self ):
		averageUsage = self.cursor.execute( "SELECT AVG( bar_in - bar_out ) FROM dive WHERE bar_in != 0 AND bar_out != 0" ).fetchall()
		return averageUsage[0][0]
	
	def usage( self, diveNumber ):
		usage = self.cursor.execute( "SELECT (bar_in - bar_out) AS usage FROM dive WHERE number="+str( diveNumber ) ).fetchall()
		return usage[0][0]
	
	def insertDive( self, number=0, depth=0.0, divedate="", time_in=0, time_out=0, time=0, bar_in=0, bar_out=0, lead=0, temperature=0, sight=0, location='', notes='' ):
		if number <= 0:
			raise Exception( 'Dive number is required.' )
		if depth <= 0.0:
			raise Exception( 'Dive depth is required.' )
		if ( time_in <= 0 and time_out <= 0 ) and time <= 0:
			raise Exception( 'Please fill in time in and time out or divetime field.' )
		if divedate == '':
			raise Exception( 'Dive date is required.' )
		if time_in > 0 or time_out > 0:
			self.cursor.execute( """ INSERT INTO dive ( number, depth, divedate, time_in, time_out, time, bar_in, bar_out, lead, temperature, sight, location, notes ) VALUES (
				"""+str( number )+""", """+str( depth )+""", STRFTIME( '%Y-%m-%d', '"""+str( divedate )+"""'), STRFTIME( '%H:%M', '"""+str( time_in )+"""'), STRFTIME( '%H:%M', '"""+str( time_out )+"""'), round(strftime('%s', '"""+time_out+"""') - strftime('%s', '"""+time_in+"""'))/3600*60, """+str( bar_in )+""", """+str( bar_out )+""", """+str( lead )+""", """+str( temperature )+""", """+str( sight )+""", '"""+self.escaped(location)+"""', " """+self.escaped(notes)+""" ")""" )
			self.conn.commit()
		else:
			self.cursor.execute( """ INSERT INTO dive ( number, depth, divedate, time_in, time_out, time, bar_in, bar_out, lead, temperature, sight, location, notes) VALUES 
				("""+str( number )+""", """+str( depth )+""", STRFTIME( '%Y-%m-%d', '"""+str( divedate )+"""'), 0, 0, """+str( time )+""", """+str( bar_in )+""", """+str( bar_out )+""", """+str( lead )+""", """+str( temperature )+""", """+str( sight )+""", '"""+self.escaped(location)+"""', '"""+self.escaped(notes)+"""' )""" )
			self.conn.commit()
	
	def removeDive( self, diveNumber ):
		self.cursor.execute( "DELETE FROM dive WHERE number="+str( diveNumber ) )
		self.conn.commit()
	
	def close( self ):
		self.cursor.close()
	
	def escaped( self, value ):
		return value.replace( "'", "''" )
