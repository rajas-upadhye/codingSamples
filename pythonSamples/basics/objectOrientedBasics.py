#Object oriented basics

class Vehicle:
	make = None
	model = None

	def __init__(self,make,model):
		print "Constructing vehicle..."
		self.make = make
		self.model = model

	def displayVehicle(self):
		print "Vehicle is " , self.make , " - " , self.model;



v = Vehicle("Honda","Civic");
v.displayVehicle();

def log(str):
	print str;

log("End of program")	
