#Object oriented advanced
""" Here we will use concepts of Inheritance and then make the vehicles of 2 different types Cars and Bikes
 and store them into a list and try to print it """

import time

#General central logger function
def log(str):
	print str;

log("Program started : " + str(int(time.time())))

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

#list of makes and models for cars bikes and trucks
carMakes=['Honda','Toyota','Hyundai','Nissan','Audi','BMW']
carModels = ['Civic','Corolla','Tucson','Altima','Q3','X1']

#loop cars list and make cars 
for i in range(len(carMakes)):
	c = Car(carMakes[i],carModels[i],4,"Sedan")
	vehicles.append(c)

bikeMakes = ['Kawasaki','Yamaha']
bikeModels = ['Ninja','F15']

#loop bikes list and make bikes
for i in range(len(bikeMakes)):
	b = Bike(bikeMakes[i],bikeModels[i],"Sports")
	vehicles.append(b)

numOfVehicles = "Vehicles created : " + str(len(vehicles))
log(numOfVehicles);

#iterate the list and call display method on each vehicle
for j in range (len(vehicles)):
	v = vehicles[j]
	v.displayVehicle()

log("End of program : " + str(int(time.time())))	
