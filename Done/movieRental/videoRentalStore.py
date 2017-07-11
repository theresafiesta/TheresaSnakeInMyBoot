import sys
	
class videoRentalStore:
	
	# attributes
	titles = {
		"Men in Black":"Action",
		"Men in Black 2":"Action",
		"Sherlock Holmes":"Mystery",
		"Dude Where's My Car":"Comedy",
		"Mulan":"Family",
		"The Notebook":"Romance"
	}
	accounts = {}	# name : feebalance
	fees = {}	
	BASE_FEE = 1.00;
	DAILY_FEE = 0.30;
	checkedOut = {}	# title:name
	storeName = ""
	
	def __init__(self, store):
		self.storeName = store
		return None
		
	def displayMenu(self):
		ans = input('[*] please select from the menu: ' +
		'\n\t1. view all titles' +
		'\n\t2. view by genre' +
		'\n\t3. rent a movie' +
		'\n\t4. return a rental' +
		'\n\t5. register new customer' +
		'\n\t6. view customer accounts' +
		'\n\t7. quit\n==> ')
		ans = int(ans)
		if ans == 1: self.viewTitles()
		elif ans == 2: self.viewByGenre()
		elif ans == 3: self.rent()
		elif ans == 4: self.returnRental()
		elif ans == 5: self.addCustomer()
		elif ans == 6: self.viewAccounts()
		elif ans == 7: sys.exit()
		else: print('[*] error: invalid selection. ')
		return None
		
	def viewTitles(self):
		available = []
		num = 1
		print("\n\tAvailable Titles:")
		for key in self.titles.keys():
			if key not in self.checkedOut.keys():
				available.append(key)
		for i in available:
			print("\t\t" + str(num) + ". " + str(i))
			num += 1
		print()
		return None
		
	def viewByGenre(self):
		genres = []
		num = 1
		print('\t[*] select genre to view titles: ')
		# display each genre by putting titles values into array once
		for key in self.titles.keys():
			if self.titles.get(key) not in genres:
				genres.append(str(self.titles.get(key)))
		# print out genre selection
		for item in genres:
			print('\t\t' + str(num) + ". " + str(item))
			num += 1
		ans = input('\t\t==> ')
		ans = int(ans)
		# print out all titles not checked out for the specified genre
		num = 1
		print('\n\tAvailable Titles in ' + str(genres[ans-1]))
		for key in self.titles.keys():
			if str(self.titles.get(key)) == str(genres[ans-1]) and key not in self.checkedOut.keys():	
				print("\t\t" + key)	
		print()
		return None
		
	def selectTitle(self):
		available = []
		num = 1
		selection = ""
		print("\n\tAvailable Titles:")
		for key in self.titles.keys():
			if key not in self.checkedOut.keys():
				available.append(key)
		for i in available:
			print("\t\t" + str(num) + ". " + str(i))
			num += 1
		ans = input("\t[*] choose title to check out:\n\t==>")
		ans = int(ans)
		selection = str(available[ans])
		return selection
		
		
	def addCustomer(self):
		name = input('[*] enter customer name: ')
		cust = {name : 0.00}
		if name not in self.accounts.keys():
			self.accounts.update(cust)
			print("[*] Added " + name + " to accounts.")
		else:
			print('[*] error: customer name already exists!')
		print()
		return None
		
	def addThisCustomer(self, name):
		cust = {name : 0.00}
		if name not in self.accounts.keys():
			self.accounts.update(cust)
			print("\t[*] Added " + name + " to accounts.")
		else:
			print('\t[*] error: customer name already exists!')
		return None
		
	def custLookup(self, name):
		acct = self.accounts.get(name)
		rentals = []
		# return a list of titles checked out by this customer
		for key in self.checkedOut.keys():
			if name == self.checkedOut.get(key):
				rentals.append(str(key))
		return rentals
		
	def viewAccounts(self):
		print('\t[*] Customer Accounts: ')
		for (i,j) in self.accounts.items():
			print('\t\t' + i,j)
		print()
		return None
		
	def rent(self):
		name = input('\t[*] enter customer name: \n\t==> ')
		#title = input('\t[*] enter movie to rent: \n\t==> ')
		title = self.selectTitle()
		rental = {title : name}
		# make sure cust is in accounts
		if name in self.accounts.keys():
			# make sure they dont have a substantial outstanding balance
			fee = self.accounts.get(name)
			if fee < 1.50:				
				# add to checkedOut list if the title is available for checkout
				if title not in self.checkedOut.keys():
					self.checkedOut.update(rental)
					print("\t[*] " + name + " checked out " + title + "\n")
				else:
					print("\t[*] " + title + " not available.\n")
			else:
				print("\t[*]" + name + " has an outstanding balance of $" + fee + ". Cannot checkout.\n")
		else:
			print("\t[*]" + name + " not found.")
			ans = input("\n\t[*] add " + name + " to accounts?\n\t==> ")
			if ans == 'yes' or ans == 'y':
				self.addThisCustomer(name)
				self.rentForCust(name, title)
			else:
				print("\t[*] customer not added to accounts. Cannot checkout.")	
		return None
		
	def rentForCust(self, name, title):
		# make sure cust is in accounts
		rental = {title:name}
		if name in self.accounts.keys():
			# make sure they dont have a substantial outstanding balance
			fee = self.accounts.get(name)
			if fee < 1.50:				
				# add to checkedOut list
				if title not in self.checkedOut:
					self.checkedOut.update(rental)
					print("\t[*] " + name + " checked out " + title + "\n")
				else:
					print("\t[*] " + title + " not available.\n")
			else:
				print("\t[*]" + name + " has an outstanding balance of $" + fee + ". Cannot checkout.\n")
		else:
			print("\t[*]" + name + " not found.")
			ans = input("\n\t[*] add " + name + " to accounts?\t==> ")
			if(ans == 'yes'):
				self.addCustomer()
				self.rentForCust(name, title)
			else:
				print("\t[*] customer not added to accounts. Cannot checkout.\n")	
		return None
		
	def returnRental(self):
		name = input("\t[*] enter customer name: \n\t==> ")
		num = 1
		# get current items checked out
		rentals = self.custLookup(name)
		print("\t[*] items currently checked out:")
		for i in range(len(rentals)):
			print("\t\t" + str(num) + ". " + str(rentals[i]))
			num += 1
		# return an item
		ans = input("\t[*] enter item to return:\n\t==> ")
		ans = int(ans)
		if ans <= (len(rentals)):
			self.checkedOut.pop(str(rentals[ans-1]))
			print("\t[*] " + str(name) + " returned " + str(rentals[ans-1]) + "\n")
		else:
			print("\t[*] error: invalid entry.\n")
		return None
		
		
	def payLateFee():
		pass
		