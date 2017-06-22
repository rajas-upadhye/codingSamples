#Object oriented basics with Collection
# Here we will store list of vehicles

class Vehicle:
	make = None
	model = None

	def __init__(self,make,model):
#		print "Constructing vehicle..."
		self.make = make
		self.model = model

	def displayVehicle(self):
		print "This is " + self.make + " - " + self.model;

def log(str):
	print str;


#list of makes and models
makes=['Honda','Toyota','Hyundai','Nissan','Audi','BMW']
models = ['Civic','Corolla','Tucson','Altima','Q3','X1']
vehicles = []

#loop around both lists above 
for i in range(len(makes)):
	v = Vehicle(makes[i],models[i])
	vehicles.append(v)

numOfVehicles = "Vehicles created : " + str(len(vehicles))
log(numOfVehicles);

#iterate the list and call display method on each vehicle
for j in range (len(vehicles)):
	v = vehicles[j]
	v.displayVehicle()


log("End of program")	
