from planner import Dive, Dives
from window import Ui_Logbook
from add import Ui_AddDive
from edit import Ui_EditDive
import sys, datetime, time
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from os import path

global dives
dives = Dives()

class StartQT4( QMainWindow ):
	def __init__( self, parent = None ):
		QWidget.__init__( self, parent )

		# Initate the GUI
		self.ui = Ui_Logbook()
		self.ui.setupUi( self )
		
		self.showapp = True
		
		#Load dives data file
		dives.load()
		self.loadDives()

		#add shortcut key
		if hasattr( QKeySequence, "Quit" ):
			self.quit_shortcut = QShortcut( QKeySequence( QKeySequence.Quit), self )
		else:
			self.quit_shortcut = QShortcut( QKeySequence( "Ctrl+Q" ), self )

		self.new_shortcut = QShortcut( QKeySequence( "Ctrl+N" ), self )

		#Connect some actions
		#Quiters
		QObject.connect( self.ui.Quit, SIGNAL( "activated()" ), qApp, SLOT( 'quit()' ) )
		QObject.connect( self.quit_shortcut, SIGNAL( "activated()" ), qApp, SLOT( 'quit()' ) )
		QObject.connect( self.ui.AddDive, SIGNAL( "activated()" ), self.add )
		QObject.connect( self.ui.Stats, SIGNAL( "activated()" ), self.stats )
		QObject.connect( self.ui.About, SIGNAL( "activated()" ), self.about )
		QObject.connect( self.ui.License, SIGNAL( "activated()" ), self.license )
		QObject.connect( self.ui.ListDives, SIGNAL( "itemClicked( QListWidgetItem* )" ), self.update )
		QObject.connect( self.ui.Delete, SIGNAL( "clicked()" ), self.remove )
		QObject.connect( self.ui.Edit, SIGNAL( "clicked()" ), self.edit )
	
	def loadDives( self ):
		dvlist = sorted( dives.getList(), key=lambda dive: dive.number )
		if self.ui.ListDives.count() != 0:
			self.ui.ListDives.clear()
		for item in dvlist:
			self.ui.ListDives.addItem( str( item.number ) + '-' +item.location )
	
	def stats( self ):
		QMessageBox.information( self, "Your Statistics", "You have made a total of " + str( dives.totalDives() ) + " dives!\nYour total dive time is " + str( dives.totalDiveTime() ) + "!\nYour average divetime is " + str( dives.averageTime() ) + " minutes.\nYour maximum depth is " + str( dives.maxDepth() ) + " meters!\nYour average depth is " + str( dives.averageDepth() ) + " meters.\nYour average air usage is " + str( dives.averageUsage() ) + ' bar/' )
	
	def about( self ):
		QMessageBox.information( self, "About", "This program is written by Tom Sleebe\nIt is written in Python with PyQt gui framework.\nThis was a project for the fun of it ;)" )
	
	def license( self ):
		QMessageBox.information( self, "License", "This program is licensed under the GPL License\nE.g You can do what you want with it.\nAlthough you must keep in mind that the creator is in no case responsible for any damage through the usage of this program.\nThis program is written in the hope that it will be usefull,\nhowever there is no guarantee that it will be." )
	
	def update( self ):
		# Extract number from number + string configuration and typecast it to a int
		number = int( self.ui.ListDives.currentItem().text().split( '-' )[0] )
		#Make degree symbol posible ;)
		degree = unichr(176).encode("latin_1")
		
		
		#get the dive to show:
		self.dive = dives.getDive( number )
		
		self.ui.INumber.setText( str( self.dive.number ) )
		self.ui.IDate.setText( str( self.dive.date ) )
		self.ui.ILocation.setText( self.dive.location )
		if type( self.dive.tIn ) != int:
			self.ui.ITimeIn.setText( str( self.dive.tIn.tm_hour ) + ":" + str( self.dive.tIn.tm_min ) )
		else:
			self.ui.ITimeIn.setText( str( self.dive.tIn ) )
		if type( self.dive.tOut ) != int:
			self.ui.ITimeOut.setText( str( self.dive.tOut.tm_hour ) + ":" + str( self.dive.tOut.tm_min ) )
		else:
			self.ui.ITimeOut.setText( str( self.dive.tOut ) )
		self.ui.ISight.setText( str( self.dive.sight ) + ' Meters' )
		self.ui.ILead.setText( str( self.dive.weight ) + ' Kg' )
		self.ui.ITemperature.setText( str( self.dive.temparature ) +' '+ degree + 'C' )
		self.ui.IDepth.setText( str( self.dive.depth ) + 'm' )
		self.ui.ITime.setText( str( self.dive.time ) + 'min' )
		self.ui.INotes.clear()
		self.ui.INotes.insertPlainText( self.dive.notes )
		self.ui.IBarIn.setText( str( self.dive.barIn ) )
		self.ui.IBarOut.setText( str( self.dive.barOut ) )

	def remove( self ):
		try:
			dives.remove( self.dive.number )
			self.loadDives()
			dives.save()
			QMessageBox.information( self, "Succes", "The dive has succesfully been removed" )
		except:
			QMessageBox.critical( self, "Error", "Something went wrong!" )
	
	def add( self ):
		Add( self )
	
	def edit( self ):
		Edit( self )

class Add( QMainWindow ):
	def __init__( self, parent = None ):
		QWidget.__init__( self, parent)
		self.parent = parent

		self.ui = Ui_AddDive()
		self.ui.setupUi( self )
		
		self.ui.IDate.setDateTime( QDateTime.currentDateTime() )
		#Set Divenumber to next number (isn't required)
		self.ui.INumber.setText( str( dives.totalDives() + 1 ) )
		
		QObject.connect( self.ui.Add, SIGNAL( "clicked()"), self.add )
		QObject.connect( self.ui.Cancel, SIGNAL( "clicked()"), self.close )
		
		self.show()
	
	def add( self ):
		# Check if the folowing fields are filled in, if not leave a nice error ;)
		if self.ui.INumber.displayText() == "":
			QMessageBox.critical( self, "Error", "You need to fill in a divenumber." )
		elif self.ui.ITime.displayText() == "" and (self.ui.ITimeIn.time().toString( "HH:mm" ) == "00:00" or self.ui.ITimeOut.time().toString( "HH:mm" ) == "00:00" ):
			QMessageBox.critical( self, "Error", "You need to fill in time in & out or divetime." )
		elif self.ui.ILocation.displayText() == "":
			QMessageBox.critical( self, "Error", "You need to fill in the dive location." )	
		elif (self.ui.ITimeIn.time().toString( "HH:mm" ) != "00:00" or self.ui.ITimeOut.time().toString( "HH:mm" ) != "00:00" ):
			try:
				if self.ui.ITime.displayText() == "":
					self.ui.ITime.setText( "0" )
				newDive = Dive( int( self.ui.INumber.displayText() ), float( self.ui.IDepth.displayText() ), str( self.ui.IDate.dateTime().toString( "dd-MM-yyyy" ) ), str(self.ui.ITimeIn.time().toString( "HH:mm") ) , str( self.ui.ITimeOut.time().toString( "HH:mm") ), int( self.ui.ITime.displayText() ), int( self.ui.ILead.value() ), str( self.ui.ILocation.displayText() ), int( self.ui.ITemperature.displayText() ), int( self.ui.ISight.value() ), str( self.ui.INotes.toPlainText() ), int( self.ui.IBarIn.displayText() ), int( self.ui.IBarOut.displayText() ) )
				dives.add( newDive )
				dives.save()
				QMessageBox.information( self, "Succes", "The dive has succesfully been added" )
				self.parent.loadDives()
				self.close()
			except:
				QMessageBox.critical( self, "Error", "Sorry couldn't add the dive :('" )
		else:
			try:
				newDive = Dive( int( self.ui.INumber.displayText() ), float( self.ui.IDepth.displayText() ), str( self.ui.IDate.dateTime().toString( "dd-MM-yyyy" ) ), 0 , 0, int( self.ui.ITime.displayText() ), int( self.ui.ILead.value() ), str( self.ui.ILocation.displayText() ), int( self.ui.ITemperature.displayText() ), int( self.ui.ISight.value() ), str( self.ui.INotes.toPlainText() ), int( self.ui.IBarIn.displayText() ), int( self.ui.IBarOut.displayText() ) )
				dives.add( newDive )
				dives.save()
				QMessageBox.information( self, "Succes", "The dive has succesfully been added" )
				self.parent.loadDives()
				self.close()
			except:
				QMessageBox.critical( self, "Error", "Sorry couldn't add the dive :('" )

class Edit( QMainWindow ):
	def __init__( self, parent = None ):
		QWidget.__init__( self, parent)
		self.parent = parent

		self.ui = Ui_EditDive()
		self.ui.setupUi( self )
		
		QObject.connect( self.ui.Edit, SIGNAL( "clicked()"), self.edit )
		QObject.connect( self.ui.Cancel, SIGNAL( "clicked()"), self.close )
		
		self.show()
		
		if not hasattr( self.parent, "dive"):
			QMessageBox.critical( self, "Error", "Please select a dive first." )
			self.close()
		else:
			self.ui.INumber.setText( str( self.parent.dive.number ) )
			self.ui.IDate.setDateTime( QDateTime( QDate( int( self.parent.dive.date.split("-")[2]), int( self.parent.dive.date.split("-")[1]), int( self.parent.dive.date.split("-")[0])), QTime(0, 0, 0) ) )
			self.ui.ILocation.setText( str( self.parent.dive.location ) )
			self.ui.IDepth.setText( str( self.parent.dive.depth ) )
			if self.parent.dive.tIn != 0:
				self.ui.ITimeIn.setTime( QTime( int( self.parent.dive.tIn.tm_hour ), int( self.parent.dive.tIn.tm_min ), 0 ) )
			else:
				self.ui.ITimeIn.setTime( QTime( 0, 0, 0 ) )
			if self.parent.dive.tOut != 0:
				self.ui.ITimeOut.setTime( QTime( int( self.parent.dive.tOut.tm_hour ), int( self.parent.dive.tOut.tm_min ), 0 ) )
			else:
				self.ui.ITimeOut.setTime( QTime( 0, 0, 0 ) )
			self.ui.ITime.setText( str( self.parent.dive.time ) )
			self.ui.ILead.setValue( int( self.parent.dive.weight ) )
			self.ui.ISight.setValue( int( self.parent.dive.sight ) )
			self.ui.ITemperature.setText( str( self.parent.dive.temparature ) )
			self.ui.INotes.setText( str( self.parent.dive.notes ) )
			self.ui.IBarIn.setText( str( self.parent.dive.barIn ) )
			self.ui.IBarOut.setText( str( self.parent.dive.barOut ) )
	
	def edit( self ):
		if self.ui.INumber.displayText() == "":
			QMessageBox.critical( self, "Error", "You need to fill in a divenumber." )
		elif self.ui.ITime.displayText() == "" and (self.ui.ITimeIn.time().toString( "HH:mm" ) == "00:00" or self.ui.ITimeOut.time().toString( "HH:mm" ) == "00:00" ):
			QMessageBox.critical( self, "Error", "You need to fill in time in & out or divetime." )
		elif self.ui.ILocation.displayText() == "":
			QMessageBox.critical( self, "Error", "You need to fill in the dive location." )	
		elif (self.ui.ITimeIn.time().toString( "HH:mm" ) != "00:00" or self.ui.ITimeOut.time().toString( "HH:mm" ) != "00:00" ):
			
			try:
				self.parent.dive.number = int( self.ui.INumber.displayText() )
				self.parent.dive.depth = float( self.ui.IDepth.displayText() )
				self.parent.dive.date = str( self.ui.IDate.dateTime().toString( "dd-MM-yyyy" ) )
				self.parent.dive.setTimeIn( str( self.ui.ITimeIn.time().toString( "HH:mm") ) )
				self.parent.dive.setTimeOut( str( self.ui.ITimeOut.time().toString( "HH:mm") ) )
				self.parent.dive.time = self.parent.dive.calcTime( self.parent.dive.tIn, self.parent.dive.tOut )
				self.parent.dive.weight = int( self.ui.ILead.value() )
				self.parent.dive.location = str( self.ui.ILocation.displayText() )
				self.parent.dive.temparature = int( self.ui.ITemperature.displayText() )
				self.parent.dive.sight = int( self.ui.ISight.value() )
				self.parent.dive.notes = str( self.ui.INotes.toPlainText() )
				self.parent.dive.barIn = int( self.ui.IBarIn.displayText() )
				self.parent.dive.barOut = int( self.ui.IBarOut.displayText() )
			
				dives.save()
				QMessageBox.information( self, "Succes", "The dive has succesfully been saved" )
				self.parent.loadDives()
				self.close()
			except:
				QMessageBox.critical( self, "Error", "Sorry couldn't save the dive :(" )
		else:
			try:
				self.parent.dive.number = int( self.ui.INumber.displayText() )
				self.parent.dive.depth = float( self.ui.IDepth.displayText() )
				self.parent.dive.date = str( self.ui.IDate.dateTime().toString( "dd-MM-yyyy" ) )
				self.parent.dive.tIn = 0
				self.parent.dive.tOut = 0
				self.parent.dive.time = int( self.ui.ITime.displayText() )
				self.parent.dive.weight = int( self.ui.ILead.value() )
				self.parent.dive.location = str( self.ui.ILocation.displayText() )
				self.parent.dive.temparature = int( self.ui.ITemperature.displayText() )
				self.parent.dive.sight = int( self.ui.ISight.value() )
				self.parent.dive.notes = str( self.ui.INotes.toPlainText() )
				self.parent.dive.barIn = int( self.ui.IBarIn.displayText() )
				self.parent.dive.barOut = int( self.ui.IBarOut.displayText() )
			
				dives.save()
				QMessageBox.information( self, "Succes", "The dive has succesfully been saved" )
				self.parent.loadDives()
				self.close()
			except:
				QMessageBox.critical( self, "Error", "Sorry couldn't save the dive :(" )
			
if __name__ == "__main__":
	app = QApplication( sys.argv )
	myapp = StartQT4( )

	if myapp.showapp:
		myapp.show()
	sys.exit( app.exec_() )
