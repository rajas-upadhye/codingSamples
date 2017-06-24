#Create list of 100 coin tosses and calculate the number of Heads (H) and Tails (T) toss results
#Also lambda function is used here as alternative
import random

tossOptions = ['H','T']

#just a function to make a random choice between heads and tails
def coinToss():
	return random.choice(tossOptions)

#using basic function calling
def populateList():
	list = [ ]
	for i in range(100):
		tossResult = coinToss()
		list.append(tossResult)

	return list

#using lambda / anonymous function to get random toss 
def populateListLambda():
	list = [ ]
	for i in range(100):
		tossResult = lambda : random.choice(tossOptions)
		list.append(tossResult())

	return list

#now linearly access list and count number of H and T, we can use simple variables to keep track
def countTossResults(tosses):
	countH = 0
	countT = 0
	for i in range(len(tosses)):
		if tosses[i] == 'H':
			countH+=1
		else:
			countT+=1

	result = []
	result.append(countH)
	result.append(countT)
	return result

#populate the toss list
tosses1 = populateList()
tosses2 = populateListLambda()

result1 = countTossResults(tosses1)
print "Toss results 1: Heads {} and Tails {}".format(result1[0],result1[1])

result2 = countTossResults(tosses2)
print "Toss results 2: Heads {} and Tails {}".format(result2[0],result2[1])
