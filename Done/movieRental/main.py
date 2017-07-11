# program manages video rentals, overdue fees, and keeps an inventory of products

from videoRentalStore import *

myStore = videoRentalStore('MovieBuster')

print('==========================================\nWelcome to ' + myStore.storeName + '\n==========================================')
while True:
	myStore.displayMenu()