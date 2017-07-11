import random

class Harvestable:
	# variables: {'crop name' : [price, cost, value, rarity, [seasons], daysToGrow, daysToRegrow, numHarvested]}
	name = "none"				# name of the crop/animal/etc
	price, cost, value = 0.0	# price or sell mature, cost to purchase new, value of yielded product
	age, grade, rarity = 0		# age in days, grade in quality, rarity in rank
	seasons = []
	daysToGrow, daysToRegrow, numHarvested = 0
	
	# constructor
	def __init__(self,key,D):
		stuff = []
		self.name = str(key)
		stuff = D.get(key)			# {'crop name' : 
		stuff = list(stuff)
		# [price, cost, value, 
		self.price = stuff[0]
		self.cost = stuff[1]
		# rarity, seasons, 
		# daysToGrow, daysToRegrow, numHarvested]}
		
		return None
	
	# methods
	def printList(self, L):
		L = list(L)
		for item in L:
			print(item, end='',sep=', ')
		print()
		return None
		
	# abstract methods
	def plant(self): pass
	def grow(self): pass
	def setAge(self): pass
	def setGrade(self): pass
	
	
if __name__ == '__main__':
	# variables: {'crop name' : 
	# [price, cost, value, 
	# rarity, seasons, 
	# daysToGrow, daysToRegrow, numHarvested]}
	thisCrop = {'turnip':[
	'300','120','500',
	0, [1,2],
	5,0,1
	]}
	test = Harvestable(thisCrop)
	
