from dive import Dive
from window import Ui_Dive
from add import Ui_AddDive
from stats import Ui_Stats
from about import Ui_About
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from sys import exit, argv
from math import ceil, trunc
import sqlite3

global db
db = Dive()

class StartQT4( QMainWindow ):
	def __init__( self, parent = None ):
		QWidget.__init__( self, parent )

		# Initate the GUI
		self.ui = Ui_Dive()
		self.ui.setupUi( self )
		
		self.showapp = True
		
		#Get Dives
		self.updateListDives()
		
		#add shortcut keys
		if hasattr( QKeySequence, "Quit" ):
			self.quit_shortcut = QShortcut( QKeySequence( QKeySequence.Quit ), self )
		else:
			self.quit_shortcut = QShortcut( QKeySequence( "Ctrl+Q" ), self )
		if hasattr( QKeySequence, "New" ):
			self.new_shortcut = QShortcut( QKeySequence( QKeySequence.New ), self )
		else:
			self.new_shortcut = QShortcut( QKeySequence( "Crtl+N"), self.add )
		if hasattr( QKeySequence, "Stats" ):
			self.stats_shortcut = QShortcut( QKeySequence( QKeySequence.Stats ), self )
		else:
			self.stats_shortcut = QShortcut( QKeySequence( "Ctrl+S" ), self )
		
		#Connect Quit Actions
		QObject.connect( self.ui.Quit, SIGNAL( "activated()" ), qApp, SLOT( 'quit()' ) )
		QObject.connect( self.quit_shortcut, SIGNAL( "activated()" ), qApp, SLOT( 'quit()' ) )
		
		#Add
		QObject.connect( self.ui.AddDive, SIGNAL( "activated()" ), self.add )
		QObject.connect( self.new_shortcut, SIGNAL( "activated()"), self.add )
		
		#Misc
		QObject.connect( self.ui.ListDives, SIGNAL( "itemClicked( QListWidgetItem* )" ), self.updateDiveInfo )
		QObject.connect( self.ui.ListDives, SIGNAL( "itemSelectionChanged()" ), self.updateDiveInfo )
		QObject.connect( self.ui.Delete, SIGNAL( "clicked()" ), self.remove )
		QObject.connect( self.ui.Stats, SIGNAL( "activated()" ), self.stats )
		QObject.connect( self.stats_shortcut, SIGNAL( "activated()" ), self.stats )
		QObject.connect( self.ui.About, SIGNAL( "activated()" ), self.about )
		QObject.connect( self.ui.Edit, SIGNAL( "clicked()" ), self.edit )
	
	def updateListDives( self ):
		try:
			dvList = db.listDives()
			if self.ui.ListDives.count() != 0:
				self.ui.ListDives.clear()
			for dive in dvList:
				self.ui.ListDives.addItem( str( dive['number'] ) + ' - ' + dive['location'] )
		except sqlite3.Error, e:
			QMessageBox.critical( self, "Error", str( e ).capitalize() )
	
	def remove( self ):
		try:
			db.removeDive( self.dive['number'] )
			QMessageBox.information( self, "Succes", "The dive has succesfully been deleted." )
			self.updateListDives()
		except:
			QMessageBox.critical( self, "Error", "Couldn't remove the selected dive." )
	
	def updateDiveInfo( self ):
		try:
			# Extract number from number + string configuration and typecast it to a int
			number = int( self.ui.ListDives.currentItem().text().split( '-' )[0] )
		
			#Make degree symbol posible ;)
			degree = unichr(176).encode("latin_1")
		
			self.dive = db.fetchDive( number )
		
			#Global and Extra Information
			self.ui.INumber.setText( str( self.dive['number'] ) )
			self.ui.IDate.setText( self.dive['divedate'].split("-")[2]+"-"+self.dive['divedate'].split("-")[1]+"-"+self.dive['divedate'].split("-")[0] )
			self.ui.ILead.setText( str( self.dive['lead'] ) + " Kg" )
			self.ui.ISight.setText( str( self.dive['sight'] ) + " Meter" )
			self.ui.ITemperature.setText( str( self.dive['temperature']) + " " + degree +"C" )
			self.ui.IBarIn.setText( str( self.dive['bar_in'] ) )
			self.ui.IBarOut.setText( str( self.dive['bar_out'] ) )
			self.ui.IBarUseage.setText( str( db.usage( self.dive['number'] ) ) )
			self.ui.ITimeIn.setText( str( self.dive['time_in'] ) )
			self.ui.ITimeOut.setText( str( self.dive['time_out'] ) )
		
			#Graph
			self.ui.ITime.setText( str( trunc( ceil( self.dive['time'] ) ) ) + "min" )
			self.ui.IDepth.setText( str( self.dive['depth'] ) + "m" )
			
			#Notes
			self.ui.INotes.clear()
			self.ui.INotes.insertPlainText( str( self.dive['notes'] ) )
		except sqlite3.Error, e:
			QMessageBox.critical( self, "Error", str( e ).capitalize() )
	
	def add( self ):
		Add( self )
	
	def edit( self ):
		Edit( self )
	
	def stats( self ):
		Stats( self )
	
	def about( self ):
		About( self )

class Add( QMainWindow ):
	def __init__( self, parent = None ):
		QWidget.__init__( self, parent)
		self.parent = parent

		self.ui = Ui_AddDive()
		self.ui.setupUi( self )
		
		self.ui.IDate.setDateTime( QDateTime.currentDateTime() )
		try:
			if db.query( "SELECT MAX( number ) FROM dive").fetchall()[0][0] == None:
				number = 1
			else:
				number = db.query( "SELECT MAX( number ) FROM dive").fetchall()[0][0]+1
			self.ui.INumber.setText( str( number ) )
		except sqlite3.Error, e:
			QMessageBox.critical( self, "Error", str( e ).capitalize() )
		
		QObject.connect( self.ui.Add, SIGNAL( "clicked()"), self.add )
		QObject.connect( self.ui.Cancel, SIGNAL( "clicked()"), self.close )
		
		self.show()
	
	def add( self ):
		# Set error to None
		error = None
		# Check some requirements
		if self.ui.INumber.displayText() == "":
			error = True
			QMessageBox.critical( self, "Error", "Dive number is required." )
		if self.ui.IDepth.value() == 0.0:
			error = True
			QMessageBox.critical( self, "Error", "Depth is required." )
		if ( self.ui.ITimeIn.time().toString( "HH:mm" ) == "00:00" and self.ui.ITimeOut.time().toString( "HH:mm" ) == "00:00" ) and self.ui.ITime.displayText() == "":
			error = True
			QMessageBox.critical( self, "Error", "Time in/out or dive time is required." )
		if self.ui.ILocation.displayText() == "":
			error = True
			QMessageBox.critical( self, "Error", "Location is required." )
		
		if not error:
			try:
				if self.ui.ITimeIn.time().toString( "HH:mm" ) == "00:00" and self.ui.ITimeOut.time().toString( "HH:mm" ) == "00:00":
					db.insertDive( int( self.ui.INumber.displayText() ), float( self.ui.IDepth.value() ), str( self.ui.IDate.dateTime().toString( "yyyy-MM-dd") ), 0, 0, int( self.ui.ITime.displayText() ), int( self.ui.IBarIn.value() ), int( self.ui.IBarOut.value() ), int( self.ui.ILead.value() ), int( self.ui.ITemperature.value() ), int( self.ui.ISight.value() ), str( self.ui.ILocation.displayText() ), str( self.ui.INotes.toPlainText() ) )
					self.parent.updateListDives()
					QMessageBox.information( self, "Succes", "The dive has succesfully been added" )
					self.close()
				else:
					if self.ui.ITimeOut.time().toString( "HH:mm" ) == "00:00":
						db.insertDive( int( self.ui.INumber.displayText() ), float( self.ui.IDepth.value() ), str( self.ui.IDate.dateTime().toString( "yyyy-MM-dd") ), str( self.ui.ITimeIn.time().toString( "HH:mm") ), '24:00', 0, int( self.ui.IBarIn.value() ), int( self.ui.IBarOut.value() ), int( self.ui.ILead.value() ), int( self.ui.ITemperature.value() ), int( self.ui.ISight.value() ), str( self.ui.ILocation.displayText() ), str( self.ui.INotes.toPlainText() ) )
						self.parent.updateListDives()
						QMessageBox.information( self, "Succes", "The dive has succesfully been added" )
						self.close()
					else:
						db.insertDive( int( self.ui.INumber.displayText() ), float( self.ui.IDepth.value() ), str( self.ui.IDate.dateTime().toString( "yyyy-MM-dd") ), str( self.ui.ITimeIn.time().toString( "HH:mm") ), str( self.ui.ITimeOut.time().toString( "HH:mm") ), 0, int( self.ui.IBarIn.value() ), int( self.ui.IBarOut.value() ), int( self.ui.ILead.value() ), int( self.ui.ITemperature.value() ), int( self.ui.ISight.value() ), str( self.ui.ILocation.displayText() ), str( self.ui.INotes.toPlainText() ) )
						self.parent.updateListDives()
						QMessageBox.information( self, "Succes", "The dive has succesfully been added" )
						self.close()
			except (sqlite3.Error, Exception), e:
				QMessageBox.critical( self, "Error", str( e ).capitalize() )

class Edit( QMainWindow ):
	def __init__( self, parent = None ):
		QWidget.__init__( self, parent )
		self.parent = parent
		
		self.ui = Ui_AddDive()
		self.ui.setupUi( self )
		
		#Connect buttons
		QObject.connect( self.ui.Add, SIGNAL( "clicked()"), self.edit )
		QObject.connect( self.ui.Cancel, SIGNAL( "clicked()"), self.close )
		
		#Edit the add window to edit stuff
		self.ui.Add.setText( "Edit" )
		self.setWindowTitle( "Edit dive" )
		
		if not hasattr( self.parent, "dive"):
			QMessageBox.critical( self, "Error", "Please select a dive first." )
			self.close()
			return
			
		#Set Values
		self.ui.INumber.setText( str( self.parent.dive['number'] ) )
		self.ui.ILocation.setText( str( self.parent.dive['location'] ) )
			
		self.ui.IDate.setDateTime( QDateTime( QDate( int( self.parent.dive['divedate'].split("-")[0]), int( self.parent.dive['divedate'].split("-")[1]), int( self.parent.dive['divedate'].split("-")[1])), QTime(0, 0, 0) ) )
		if self.parent.dive['time_in'] != 0:
			self.ui.ITimeIn.setTime( QTime( int( self.parent.dive['time_in'].split(":")[0] ), int( self.parent.dive['time_in'].split(":")[1] ), 0 ) )
		else:
			self.ui.ITimeIn.setTime( QTime( 0, 0, 0 ) )
		if self.parent.dive['time_out'] != 0:
			self.ui.ITimeOut.setTime( QTime( int( self.parent.dive['time_out'].split(":")[0] ), int( self.parent.dive['time_out'].split(":")[1] ), 0 ) )
		else:
			self.ui.ITimeOut.setTime( QTime( 0, 0, 0 ) )
			
		self.ui.IBarIn.setValue( self.parent.dive['bar_in'] )
		self.ui.IBarOut.setValue( self.parent.dive['bar_out'] )
		self.ui.ITemperature.setValue( self.parent.dive['temperature'] )
		self.ui.ISight.setValue( self.parent.dive['sight'] )
		self.ui.ILead.setValue( self.parent.dive['lead'] )
		self.ui.IDepth.setValue( self.parent.dive['depth'] )
		self.ui.ITime.setText( str( self.parent.dive['time'] ) )
		self.ui.INotes.setPlainText( str( self.parent.dive['notes'] ) )
		
		self.show()
	
	def edit( self ):
		# Set error to None
		error = None
		# Check some requirements
		if self.ui.INumber.displayText() == "":
			error = True
			QMessageBox.critical( self, "Error", "Dive number is required." )
		if self.ui.IDepth.value() == 0.0:
			error = True
			QMessageBox.critical( self, "Error", "Depth is required." )
		if ( self.ui.ITimeIn.time().toString( "HH:mm" ) == "00:00" and self.ui.ITimeOut.time().toString( "HH:mm" ) == "00:00" ) and self.ui.ITime.displayText() == "":
			error = True
			QMessageBox.critical( self, "Error", "Time in/out or dive time is required." )
		if self.ui.ILocation.displayText() == "":
			error = True
			QMessageBox.critical( self, "Error", "Location is required." )
		
		if not error:
			try:
				if self.ui.ITimeIn.time().toString( "HH:mm" ) == "00:00" and self.ui.ITimeOut.time().toString( "HH:mm" ) == "00:00":
					db.query( """UPDATE dive SET number='"""+str(self.ui.INumber.displayText() )+"""', depth='"""+str( float( self.ui.IDepth.value()) )+"""', divedate='"""+str( self.ui.IDate.dateTime().toString( "yyyy-MM-dd") )+"""', time_in='0', time_out='0', time='"""+str( float( self.ui.ITime.displayText() ) )+"""', bar_in='"""+str( self.ui.IBarIn.value() )+"""', bar_out='"""+str( self.ui.IBarOut.value() )+"""', lead='"""+str( self.ui.ILead.value() )+"""', temperature='"""+str( self.ui.ITemperature.value() )+"""', sight ='"""+str( self.ui.ISight.value() )+"""', location='"""+db.escaped( str( self.ui.ILocation.displayText() ) )+"""', notes='"""+db.escaped( str( self.ui.INotes.toPlainText() ) )+"""' WHERE number = """+str( self.parent.dive['number'] ) )
					
					self.parent.updateListDives()
					QMessageBox.information( self, "Succes", "The dive has succesfully been edited" )
					self.close()
				else:
					if self.ui.ITimeOut.time().toString( "HH:mm" ) == "00:00":
						db.query( """UPDATE dive SET number='"""+str(self.ui.INumber.displayText() )+"""', depth='"""+str( float( self.ui.IDepth.value()) )+"""', divedate='"""+str( self.ui.IDate.dateTime().toString( "yyyy-MM-dd") )+"""', time_in='"""+str( self.ui.ITimeIn.time().toString( "HH:mm") )+"""', time_out='24:00', time=round(strftime('%s', '24:00') - strftime('%s', '"""+str( self.ui.ITimeIn.time().toString( "HH:mm") )+"""'))/3600*60, bar_in='"""+str( self.ui.IBarIn.value() )+"""', bar_out='"""+str( self.ui.IBarOut.value() )+"""', lead='"""+str( self.ui.ILead.value() )+"""', temperature='"""+str( self.ui.ITemperature.value() )+"""', sight ='"""+str( self.ui.ISight.value() )+"""', location='"""+db.escaped( str( self.ui.ILocation.displayText() ) )+"""', notes='"""+db.escaped( str( self.ui.INotes.toPlainText() ) )+"""' WHERE number = """+str( self.parent.dive['number'] ) )
						
						self.parent.updateListDives()
						QMessageBox.information( self, "Succes", "The dive has succesfully been edited" )
						self.close()
					else:
						db.query( """UPDATE dive SET number='"""+str(self.ui.INumber.displayText() )+"""', depth='"""+str( float( self.ui.IDepth.value()) )+"""', divedate='"""+str( self.ui.IDate.dateTime().toString( "yyyy-MM-dd") )+"""', time_in='"""+str( self.ui.ITimeIn.time().toString( "HH:mm") )+"""', time_out='"""+str( self.ui.ITimeOut.time().toString( "HH:mm") )+"""', time=round(strftime('%s', '"""+str( self.ui.ITimeOut.time().toString( "HH:mm") )+"""') - strftime('%s', '"""+str( self.ui.ITimeIn.time().toString( "HH:mm") )+"""'))/3600*60, bar_in='"""+str( self.ui.IBarIn.value() )+"""', bar_out='"""+str( self.ui.IBarOut.value() )+"""', lead='"""+str( self.ui.ILead.value() )+"""', temperature='"""+str( self.ui.ITemperature.value() )+"""', sight ='"""+str( self.ui.ISight.value() )+"""', location='"""+db.escaped( str( self.ui.ILocation.displayText() ) )+"""', notes='"""+db.escaped( str( self.ui.INotes.toPlainText() ) )+"""' WHERE number = """+str( self.parent.dive['number'] ) )
					
						self.parent.updateListDives()
						QMessageBox.information( self, "Succes", "The dive has succesfully been edited" )
						self.close()
			except ( sqlite3.Error, ValueError ), e:
				QMessageBox.critical( self, "Error", str( e ).capitalize() )

class Stats( QMainWindow ):
	def __init__( self, parent = None ):
		QWidget.__init__( self, parent)
		self.parent = parent

		self.ui = Ui_Stats()
		self.ui.setupUi( self )
		
		try:
		
			if db.totalDives() > 0:
				#Setup information
				self.ui.ITotalDives.setText( str( db.totalDives() ) )
				self.ui.IAvgAir.setText( str( db.averageUsage() ) + " bar" )
				self.ui.IAvgTime.setText( str( db.averageTime() ) + " min" )
				self.ui.ITotalTime.setText( str( db.totalTime() ) )
				self.ui.ITotalLocations.setText( str( db.totalLocations() ) )
				self.ui.IMaxDepth.setText( str( db.maxDepth() ) + " meters" )
				self.ui.IAvgDepth.setText( str( db.averageDepth() ) + " meters" )
			else:
				#No dives yet, so set text to default values
				self.ui.ITotalDives.setText( str( db.totalDives() ) )
				self.ui.IAvgAir.setText( "0 bar" )
				self.ui.IAvgTime.setText( "0 min" )
				self.ui.ITotalTime.setText( "00:00" )
				self.ui.ITotalLocations.setText( "0" )
				self.ui.IMaxDepth.setText( "0 meters" )
				self.ui.IAvgDepth.setText( "0 meters" )
		except sqlite3.Error, e:
			QMessageBox.critical( self, "Error", str( e ).capitalize() )
		
		QObject.connect( self.ui.Ok, SIGNAL( "clicked()"), self.close )
		
		self.show()

class About( QMainWindow ):
	def __init__( self, parent = None ):
		QWidget.__init__( self, parent)
		self.parent = parent

		self.ui = Ui_About()
		self.ui.setupUi( self )
		
		QObject.connect( self.ui.Ok, SIGNAL( "clicked()"), self.close )
		
		self.show()
	
if __name__ == "__main__":
	app = QApplication( argv )
	myapp = StartQT4( )

	if myapp.showapp:
		myapp.show()
	db.close()
	exit( app.exec_() )
