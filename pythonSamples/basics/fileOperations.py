#Object oriented advanced
""" Here we will use concepts of Inheritance and then make the vehicles of 2 different types Cars and Bikes
 and store them into a list and try to print it 
    In addition to this car and bike info will be read from files as input
"""

import time

#General central logger function
def log(str):
	print str;

log("Program started : " + str(int(time.time())) + "\n")

class Vehicle(object):
	make = None
	model = None

	def __init__(self,make,model):
		self.make = make
		self.model = model

	def displayVehicle(self):
		print "This is " + self.make + " - " + self.model;

	def getMake(self):
		return self.make
	
	def getModel(self):
		return self.model


class Car(Vehicle):
	
	#this below with __ double underscore serves purpose similar to static variable in java	
	__vehicleType = "Car"

	doors=None
	type=None
	def __init__(self, make, model, doors, type):
		Vehicle.__init__(self, make, model)
		self.doors=doors
		self.type=type

	def displayVehicle(self):
		make = super(Car,self).getMake()
		model = super(Car,self).getModel()
		log(self.__vehicleType + " : " + make + " " + model + " " + str(self.doors) + "door " + self.type)


class Bike(Vehicle):

	__vehicleType = "Bike"
	type=None
	
	def __init__(self,make,model,type):
		Vehicle.__init__(self,make,model)
		self.type=type

	def displayVehicle(self):
		make = super(Bike,self).getMake()
		model = super(Bike,self).getModel()
		log(self.__vehicleType + " : " + make + " " + model + " " + self.type)


#resultant collection of all vehicles, initially empty
vehicles = []

log("Reading from cars file...");
#open cars file for reading
fileCars = open("resources/cars.txt","r")

#read line by line , split and make car objects and load up the vehicles list
for carEntry in fileCars:
	carParams = carEntry.rstrip().split(",")
	c = Car(carParams[0],carParams[1],carParams[2],carParams[3])
	vehicles.append(c)

log("Reading from bike file...")
#open bikes file for reading
fileBikes = open("resources/bikes.txt","r")

#read line by line, split and make bikes and append to existing vehicles list
for bikeEntry in fileBikes:
	bikeParams = bikeEntry.rstrip().split(",")
	b = Bike(bikeParams[0],bikeParams[1],bikeParams[2])
	vehicles.append(b)

numOfVehicles = "\nVehicles created : " + str(len(vehicles))
log(numOfVehicles);

#iterate the list and call display method on each vehicle
for j in range (len(vehicles)):
	v = vehicles[j]
	v.displayVehicle()

log("\nEnd of program : " + str(int(time.time())))	
