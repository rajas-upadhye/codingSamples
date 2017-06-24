# Using map , filter and reduce in some basic examples

import random
from functools import reduce

def generateList(capacity , rangeStart , rangeEnd):
	"""
	resultList = []
	for i in range(capacity):
		currentChoice = random.randint(rangeStart,rangeEnd)
		resultList.append(currentChoice)
	return resultList
	"""
	
	#single line magic
	return list(random.randint(rangeStart,rangeEnd) for i in range(capacity))
	
print("Sample 1 \n\n")
#generate list of 100 random ints with range of 1 to 1000
sampleList = generateList(50,1,1000)
print("Generated List of {} numbers is :".format(len(sampleList)))
print(sampleList)

#FILTER : lets filter elements in list divisible by 5
filteredListDivBy5 = list(filter((lambda x : x%5 == 0),sampleList))
print("Divisible by 5 numbers are: ")
print(filteredListDivBy5)


"""
	Now we will generate list of 100 numbers ranging from 1,200
	use map to classify numbers <= 100 and > 100
	use filter to filter only even numbers
	use reduce to calculate sum of all filtered numbers
"""
print("\n\n Sample 2 \n\n")
#generate list
numbersList = generateList(10,1,200)
print(numbersList)

#map
numbersDoubled = list(map(lambda x : x * 2 , numbersList))
print("After mapping...")
print(numbersDoubled)

#filter
evenNumbers= list(filter((lambda x : x%2 == 0),numbersDoubled))
print("After filtering even numbers : ")
print(evenNumbers)

#reduce
countEvenNumbers = reduce((lambda x,y : x+y),evenNumbers)
print("After reducing the even numbers sum : {} \n".format(countEvenNumbers))
