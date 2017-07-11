"""
Codewars
"""

import random
from debug import *

class KungFoo:
	# variables
	debug = ""
	
	# constructor
	def __init__(self):
		self.debug = debug()
		self.debug.beach("===============================================\n"+"   KungFoo from Codewars with Minerva12345!\n"+"===============================================\n\n")
		return None
		
	#Given a list of strings and an integer, return the FIRST longest combination of strings (i.e., concatenated)
	def findLongestPairInList(self,L,x):
		y = 0	# index of item in outer for loop
		i = 0	# index to be added to y in order to concatenate current with the next index 
		longest = ""	# the longest string combo of x items in sequence in L
		current = ""
		L = list(L)
		
		# set up the first string
		for i in range(0,x):
			longest += L[i]
		longest = str(longest)
		
		# check initial longest to make sure i am not an idiot
		initial = "initial longest string is =>\t" + longest
		self.debug.info(initial)
		
		# compare against other combos until a lesser is found, then return
		for item in L:
			if y < (len(L) - x):
				while i < x:	# to concatenate x strings in L	
					if (y+i) < len(L):	# do not go out of bounds of L
						current += L[y+i]	# concatenate at the collective index (current item index + value of i as index)
						#self.debug.log(("L[" + str(i+y) +"]"),str(L[y+i]))
						#self.debug.log("new current",current)
						i += 1
					else: break
					
				# log the sctrings real quick to make sure i am not dumb
				current = str(current)
				longest = str(longest)
				self.debug.log("current",current)
				self.debug.log("longest",longest)
				
				# compare the two string combos
				if longest > current: 
					self.debug.show((longest + " > " + current))
					self.debug.success(("Longest combination of " + str(x) + " strings in list: " + longest))
					break
				elif longest < current:
					self.debug.show((longest + " < " + current))
					longest = current
				elif longest == current:
					self.debug.show((longest + " == " + current))
					longest = current
				else:
					self.debug.warn("there's problem with longest and current values!")
				
				# increment/reinitialize
				i = y
				y += 1
				current = ""	
		return None
		
if __name__ == "__main__":
	test = KungFoo()
	
	L = ['how','now','brown','cowabunga','mooalicious','you','candy','land','man','can']
	x = 3
	test.findLongestPairInList(L,x)
