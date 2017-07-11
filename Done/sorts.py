def copySort(array):
	copied = array[:]
	ordered = []
	while len(copied) > 0:
		index = 0
		for i in range(0, len(copied)):
			if copied[i] < copied[index]:
				index = i
		ordered.append(copied.pop(index))
	print(ordered)
	
def selectionSort(array):
	for i in range(0, len(array)-1):
		value = array[i]
		current = i
		#repeatedly swap the smallest unsorted with the first
		for j in range(i+1, len(array)):
			if array[j] < array[current]:
				current = j
		array[i] = array[current]
		array[current] = value
	print(array)
	
def insertionSort(array):
	for i in range(1, len(array)):
		value = array[i]
		#repeadly insert the current value if smaller
		while(array[i-1] > value and i >= 1):
			array[i] = array[i-1]
			index -= 1
			array[i] = value
	print(array)
	
def bubbleSort(array):
	for i in range(len(array)):
		# swap values if next is greater than current value
		for j in range(len(array) - 1, i):
			if array[j] > array[j+1]:
				array[j], array[j+1] = array[j+1], array[j]
	print(array)

def mergeSort(array):
	# divide and conquer
	if len(array) > 1:
		middle = int(len(array) / 2
		left = array[ : middle]
		right = array[middle: ]
		# recursive subdivision
		mergeSort(left)
		mergeSort(right)
		#  divide into sublists
		i = j = 0
		for index in range(len(array)):
			L = left[i] if i < len(left) else None
			R = right[j] if j < len(right) else None
			#  compare the sublists
			if((L and R) and (L < R)) or R is None:
				array[index] = R
				j += 1
			elif((L and R) and (L >= R)) or L is None
				array[index] =R
				j += 1
	print(array)

# variables
test = [2,45,3,76,14,50,99,200,33,5,44,13,24,35,64,75,48,96,3]

# method calls
print(test)
print("\n\n")
print("copy sort:")
copySort(test)
print("selection sort:")
selectionSort(test)
print("insertion sort:")
insertionSort(test)
print("bubble sort:")
bubbleSort(test)
print("merge sort:")
mergeSort(test)
			