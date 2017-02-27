# Chapter 10 - Some simple algorithms and data structres

# The 0th order goal of studying this is to learn how to cast novel problems 
# to known problems that are accessibl

##################################################################################
# 10.1 - Search Algorithms

######################################
# 10.1.1 - Linear Search & Using Indirection to Access Elements

# We'll see two implementations of:
'''
def search(L, e):
	"""Assumes L is a list.
	Returns True if e is in L and False otherwise"""
'''

# The "for i in L" shorthand notation is actually this function:
# It is efficient up to O(len(L))
'''
def search(L, e):
	"""Assumes L is a list.
	Returns True if e is in L and False otherwise"""
	for i in range(len(L)):
		if L[i] == e:
			return i
	return False


targetMin = int(raw_input('enter the min of your range of numbers: '))
targetMax = int(raw_input('enter the max of your range of numbers: '))
targetNum = int(raw_input('enter your target Num: '))
targetList = []
for e in range(targetMin, targetMax+1):
	targetList.append(e)
	#	print e

foundIt = search(targetList, targetNum)
if foundIt == False:
	print "Didn't find the number"
elif type(foundIt) == int:
	print "Found the number as position ",foundIt
else:
	print "something weird happened"

"""
Think about how to do this with object oriented programming.  
Need to create a template and then:
-  set the truth value for found / not found
- the index location for found
- the number of iterations it took to find
... for each instantiation of the variable.  
Basically we're using OOP to pass a bunch of variables about this back and forth.

"""
'''

# This is a linear operation because of "Indirection" - lists contains pointers to
# variables. The pointers (addresses) can be calculated in constant time.
# Once those are calculated, the value is also accessed in constant time.
# So the complexity is set by the size of the search space, len(L)

######################################
# 10.1.2 - Binary search and Exploiting Assumptions

# If we assume a list is in ascending order, we can do much better than a linear
# time search algorithm because we can exploit the ordering to get to a specific
# value range in the list and see whether our value exists in it or now

# E.g., Ascending order list: start at the first spot and go until we hit our
# target number or a number greater than our target, whichever comes first.
# This doesn't actually improve the worst case, it just affects complexity
# when the target actually exists.

######################################
# 10.1.1 Iterative Search again (for ordered list)

'''
def orderedSearch(L,e):
	"""Assumes L is a list, the elements of which are in ascending order.
	Returns True if e is in L and False otherwise"""
	for i in range(len(L)):
		# This works because L is indexex by the natural numbers
		# print "position: ",i," value: ",L[i]
		if L[i] == e:
			return i
		if L[i] > e:
			print "Leaving search after ",i+1," iterations through loop because have reached a value that is greater than the target value"
			return False
	return False

targetMin = int(raw_input('enter the min of your range of numbers: '))
targetMax = int(raw_input('enter the max of your range of numbers: '))
targetNum = int(raw_input('enter your target Num: '))
targetList = []
for e in range(targetMin, targetMax+1):
	targetList.append(e*2)	#	Do this to fill with even numbers.
	# print e
	#print len(targetList)

foundIt = orderedSearch(targetList, targetNum)
if foundIt == False:
	print "Didn't find the number"
elif type(foundIt) == int:
	print "Found the number as position ",foundIt
else:
	print "something weird happened"
'''

######################################
# 10.1.1 Binary Search
# E.g., Ascending order list: bisection search, where we choose a midpoint in 
# the list and then find whether it is greater or less than our number, and
# continue to bisect until we reach our number or exhaust the list.

'''

def binarySearchForLoop(L,e):
	"""Assumes L is a list, the elements of which are in ascending order.
	Returns True if e is in L and False otherwise"""
	counter = 0
	topMarker = len(L)-1
	bottomMarker = 0
	i = int(len(L)/2)
	while L[i] != e and bottomMarker != topMarker:
		counter += 1
		print "Counter: ",counter,"Checking position: ",i," value there: ",L[i]," bottomMarker: ",bottomMarker," topMarker: ",topMarker
		if L[i] < e:
			if i == topMarker: 
				# If our value at index is less than target then we need to move our bottom
				# to the lower index because true value is more than tracker. We know the
				# value must be higher than current location of the tracker.
				# However if tracker is already at the max mark then the sought
				# variable must not be in the list at any index.
				return False
			else:
				bottomMarker = i+1
				# We already know that L[i] != e from the while loop conditions
				# If L[i] < e, then the bottom market is at least 1 value larger
				# than the current indexer
		if L[i] > e:
			topMarker = i
		i = (topMarker+bottomMarker)//2
		print "Updated: bottomMarker: ",bottomMarker," topMarker: ",topMarker		
		# This works because L is indexed by the natural numbers

	if L[i] == e:
		print "-- FOUND!  position: ",i," value there: ",L[i]," bottomMarker: ",bottomMarker," topMarker: ",topMarker
		return i
	else:
		return False
"""		Because of the change above where we quit if the index is already at the topMarker,
		this algorithm is robust to the corner case of our target being L's max or min 
	elif L[i-1] == e:
		print "-- FOUND!  position: ",i-1," value there: ",L[i-1]," bottomMarker: ",bottomMarker," topMarker: ",topMarker
		return i-1
	elif L[i+1] == e:		
		print "-- FOUND!  position: ",i+1," value there: ",L[i+1]," bottomMarker: ",bottomMarker," topMarker: ",topMarker
		return i+1
"""		

#	Accomplish this with recursion because we're calling with a shortened list

def searchAbstract(L, e):
	"""Assumes L is a list, the elements of which are in ascending order.
	Returns True if e is in L and False otherwise"""
	def BinarySearchRecursion(L,e, low, high):
		global counter
		counter = counter+1
		print "On try #",counter," low: ",low," high: ",high
		# Remember recursion won't have loops so we will need to bring the
		# logic of our while loop directly in as an if statement
		# Recursion will also return via a function call. 


		# Define the base case - the value to return when no more recursion is required
		# because we've reached some desired stop condition.
		# In this case it's when we have a list equal to len 1 w/o finding answer
		

		# Step 1 -- defines our first stop condition for recursion
		# -- when we have scanned the whole list 
		# Handle the case where we've exhausted searching the list
		# Returns true means we found the value in the last possible place

		if high == low:
			if L[low] == e:
				return low
			else:
				return False

		i = (high+low)//2	#	Truncates the decimal (i.e. rounds down)

		# Step 2 -- defines our second stop condition for recursion
		# -- we have found the target we're seraching for

		if L[i] == e:	# This logic was handled in while loop; needs to be stated here
			return i
		elif L[i] > e:  # Step 3 -- moves high closer to low and invokes recursion
			if i==low:	# Handles target not being in list. Says value at index is
						# bigger than target so target should be lower down the index.
						# but we can't go lower down if i==low, so we know it's
						# not in the list.
						# We could have put "if i==high" in the L[i]<e condition for
						# an identical effect.
				return False
			else:
				# Could also have defined high = i-1 and passed high
				# we want i-1 because we've checked that it's not at i and we know it's <i
				return BinarySearchRecursion(L,e, low, i-1)
		elif L[i] < e:
			return BinarySearchRecursion(L,e, i+1, high)
			# we want i+1 because we've checked it's not at i and we know it's > i

	global counter
	counter = 0
	if len(L) == 0:
		return False
	else:
		return BinarySearchRecursion(L, e, 0, len(L) -1)
		# use high = L-1 because we're zero-indexed (did same thing in for loop search)

counter = 0
targetMin = int(raw_input('enter the min of your range of numbers: '))
targetMax = int(raw_input('enter the max of your range of numbers: '))
targetNum = int(raw_input('enter your target Num: '))
targetList = []
for e in range(targetMin, targetMax+1):
	targetList.append(e)	#	Do this to fill with even numbers.
	# print e
	#print len(targetList)
#	print targetList


foundIt = binarySearchForLoop(targetList, targetNum)
# foundIt = searchAbstract(targetList, targetNum)
#	print foundIt
if type(foundIt) == int:
	print "Found the number as position ",foundIt
elif foundIt == False:
	print "Didn't find the number"
else:
	print "something weird happened"

'''

##################################################################################
# 10.2 - Sorting Algorithms
# Standard implementations of sorting are very good: ~O(n*log(n)), n = len(List to sort)
# Just use L.sort() or sorted(L).
# Recall that L.sort() will mutate the list while sorted(L) will return a sorted
# version of the list while NOT mutating L itself.
# Sorting is worth studying because it is great practice for understanding complexity.

######################################
# 10.2.1 - Selection Sort and Loop Invariants
# Create a "prefix" list that is initially empty but will get populated by appending
# the smallest element of the main list (called "suffix" list)

'''
def sortAbstract(L,sortType):
	"""Assumes that L is a list.  Assumes that sortType is one of our types.
	Returns a sorted version of list L using the sort type specified."""

	def selectionSortRecursive(prefixList, suffixList):
		"""Implements list sort via recusion. Runs 1 depth of recursion per list member, which runs out of space quickly!!"""

		# Ending condition is that we no longer have a suffixlist.
		if len(suffixList) == 0:
			return prefixList

		# If we haven't reached that condition than keep on recursing...
		"""		
		try:
			print type(suffixList)
			print min(suffixList)
		except:
			print "failed for some reason"
		"""

		# Recursive action is to shorten the suffix list and put its smallest element in the next place in the prefix list.
		x = min(suffixList)
		#	print type(x)
		#	print x
		#	exit()
		prefixList.append(x)
		suffixList.remove(x)
		#	doesn't matter if there is more than 1 item with this value
		selectionSort(prefixList, suffixList)

		return prefixList

	def selectionSortLoops(L):
		"""Implements list sort via a loop.
		We start at the 0th position and swap the 0th for the next element if the next element is smaller.
		We continue through the loop comparing 0th to 1st, 0st to 2nd. Then again 1st to 2nd, 1st to 3rd, etc.
		We're guaranteed to have smallest element in L[suffixList:len(L) at position L[suffuixList] aftereach pass."""
		
		suffixStart = 0
		temp = 0

		while suffixStart != len(L):	# Could also do a for loop since we know how much we're iterating
			# The double for loop makes it slightly more obvious this is an n^2 complexity with list length
			for i in range(suffixStart,len(L)):
				if L[i] < L[suffixStart]:
					temp = L[i]  
					#Python lets us do "L[suffixStart], L[i] = L[i], L[suffixStart]"" to avoid 3 lines and a temp
					#but that's no more efficient and is obscure to non-python users
					L[i] = L[suffixStart]
					L[suffixStart] = temp
			
			suffixStart += 1
		return L

######################################
# 10.2.1 - Merge sort
# 10.2.2 - Functions as parameters

# Assumes we already have two ordered lists
# Compares them element-by-element and results in a single merged, sorted list.
# The magic is in getting to lists that are sorted as quickly as possible.

######################################

# Complexity discussion for mergesort:
# The "merge" section involves comparing at most len(max(L1,L2)) elements, where L1 & L2 are our lists.
# So merging two sorted lists is linear in the length of the lists.

# The number of merges that we have to do is equal to the number of recursions that we have to do. 
# We'll do log base 2 of len(L) recursions because we're breaking the list in half - so O(log(len(L))).

# So overall complexity of O(len(L)*log(len(L)) --> O(n*log n) usually written. A list with n elements.

# MASSIVELY FASTER BUT YOU HAVE TO HAVE ENOUGH MEMORY because we make len(L) copies of the list.
# Insertion sort makes no copies of the list at all.  It is "in-place" sorting."""

	def merge(left, right, compare):
		"""Assumes left and right are sorted lists.  Compares them using the operator defined at compare.
		Returns a single sorted list containing the individual elements of left and right."""

		result = []
		i = 0
		j = 0
		while i < len(left) and j < len(right):
			if compare(left[i], right[j]):
					# If "compare" is "<" operator then saying "if left[i] < right[i]:"
					# We will define our own compare functions below
				result.append(left[i])	# Use the append operator so we don't have to keep track of placement in results list
				i = i+1 	# Move to the next element in the left list
			else:
				result.append(right[j])
				j = j+1 	# Move to the next element in the right list
		# Termination of this loop means that we're left with more elements in one of the list
		# Since we were comparing elements of each list and the lists were in order
		# All of the remaining values in whichever list is left can all be appended to the results list

		# Since we don't know which list retains elements let's just make two while loops, only one of which will ever run
		while i < len(left):
			result.append(left[i])
			i = i+1

		while j < len(right):
			result.append(right[j])
			j = j+1

		# We return a sorted list.  
		return result

	import operator
	def mergeSort(L, compare = operator.lt):
		"""Key insight is that if two lists start sorted then you can just compare their first elements
		and put the smaller of the two in another list. Repeat until the smaller list is gone and you will have a single sorted list."""
		
		# When the list returned by merge function is the length of L then we have a sorted L.
		# However we are only sure something is sorted in a list if there is just 1 thing in that list
		# So we want to only start building up our comparisons of lists once we have lists of length L
		# As in binary search, split the lists in 2 until each piece is at most len(1)

		# When our list is length 1 then it is by definition sorted.
		if len(L) <= 1:
			return L

		# If our list is longer than 1 then split it up and run it through the merge
		else:
			middle = len(L)/2
			left = mergeSort(L[:middle], compare)
			right = mergeSort(L[middle:], compare)

			# The first values that get sent to merge will be of length 1. 
			# merge() will then return a sorted version of each smaller list to the particulare iteration of MergeSort that called it
			# merge() will dutifully combine those next two larger lists into 1
			return merge(left, right, compare)
	
	#	Here we are creating functions that will be used as operators in the merge() function above
	def lastNameFirstName(name1, name2):
		import string
		name1 = string.split(name1, ' ')
		name2 = string.split(name2, ' ')
		if name1[1] != name2[1]:
			return name1[1] < name2[1]
			# Recall that the operators are looking for the truth value of a comparison so we are returning to them that truth value
			# Is equivalent to making a new operator that is "last names less than" and "first names less than" 
		else: # last name's the same, sort by first name
			return name1[0] < name2[0]

	def firstNameLastName(name1, name2):
		import string
		name1 = string.split(name1, ' ')
		name2 = string.split(name2, ' ')
		if name1[0] != name2[0]:
			return name1[0] < name2[0]
		else: 
			return name1[1] < name2[1]


	if sortType == 'selection-recursive':
		# Prefix list starts empty
		# Suffix list starts equal to the original list
		prefixList = []
		suffixList = L
		return selectionSortRecursive(prefixList, suffixList)

	if sortType == 'selection-loop':
		return selectionSortLoops(L)

	if sortType == 'merge-nums':
		return mergeSort(L)

	if sortType == 'merge-names-last':
		return mergeSort(L, lastNameFirstName)

	if sortType == 'merge-names-first':
		return mergeSort(L, firstNameLastName)

	else:
		print sortTpe," is an invalid sort type"
		return False

# import hashlib -- originally had idea of pulling list from hashed inputs
# but then realized I'd need to randomly specify element lengths so I might as well
# just use a python's own random number generator

import random
listLength = int(raw_input('enter your list length: '))
listMax = int(eval(raw_input('enter a max range for random list generation: ')))
	#	print listMax
	#	exit()
	#	listMax = int(raw_input('enter a max range for random list generation: '))
listTarget = []
for e in range(listLength):
	listTarget.append(random.randrange(0, listMax))
print listTarget

	#	print type(listTarget)
	#	print min(listTarget)
#	print sortAbstract(listTarget,'selection-loop')
#	print sortAbstract(listTarget,'selection-recursive')
print sortAbstract(listTarget,'merge-nums')

L = ['Chris Terman', 'Tom Brady', 'Eric Grimson', 'Gisele Bundchen']
print "Sort by last names: ",  sortAbstract(L,'merge-names-last')
print "Sort by first names: ", sortAbstract(L,'merge-names-first')
'''

######################################
# 10.2.3 - Sorting in Python.  Iterable objects v. functions.

# Python generally uses timsort, a more efficient version of merge sort that assumes lists are generally sorted
# Its worst case converges to merge sort but its best case is much beter

'''
L =[3,5,2,'banana', 'apple']
D = {'a':12, 'c':5, 'b':'dog'}
print 'Here is your original L: ',L
print 'Here is a sorted version of L: ',sorted(L)
print 'Here is L again, see that it was not mutated: ',L
L.sort()
print 'We ran L.sort() and now L is mutated: ',L
print 'Running sorted(D) gives a sorted list of the keys of the dictionary which allows you to pull values later if you want: ',sorted(D)
print 'Running D.sort() gives an error because dictionaries are meant to have no concept of comparitive value of items, just key-->value pairs  : '
print D.sort()
'''

##################################################################################
# 10.3 - Hash Tables

# We know that we can sort in O(n*log(n)) time and search a sorted list in in O(log(n)) time
# so the worst we expect to find k objects in a list is O(n*log n + k*log n)

# A hash table is a dictionary that contains pre-processed data allowing instantaneous looked.
# The search terms are known in advance and "hashed" i.e. transformed somehow into an integer that is a key in a list
# The value in the list can be an actual value of interest but is usually itself a pointer to something else.
# We'll use lists here which is simple but inefficient -- we'll search the final list in linear time for the original search term.

######################################
# 10.3.1 - Dictionary hash table w/ classes

class intDict(object):
	"""A dictionary with integer keys"""

	def __init__(self, numBuckets):
		"""Create an empty dictionary.  You remember how to use the 'self' parameter right? """
		self.buckets = []
		self.numBuckets = numBuckets
		for i in range(numBuckets):
			self.buckets.append([])
		
		print self.buckets
		# We're creating a list htat contains numBuckets of empty lists

	def addEntry(self, dictKey, dictVal):
		"""Assumes dictKey an int. Adds an entry."""
		hashBucket = self.buckets[dictKey%self.numBuckets]	# The bucket we're going to be adding to has has index dictKey%self.numBuckets
		for i in range(len(hashBucket)):
			if hashBucket[i][0] == dictKey:			# Once we've found the bucket for that key ...
				hashBucket[i] = (dictKey, dictVal)	# ... add the (key, value) pair to that bucket.
				return 								# Note that all lists are stored as self.buckets[()]. We'll append more typles as we go.
													# So a list can end up with numerous tuples
		hashBucket.append((dictKey, dictVal))		# If we don't find it then add a new hashbucket index for that dictionary key.


	def getValue(self, dictKey):
		"""Assumes dictKey an int. Returns entry associated with the key dictKey."""
		hashBucket = self.buckets[dictKey%self.numBuckets]	# Identify the appropriate hashbucket
		for e in hashBucket:								# Loop through its keys
			if e[0] == dictKey:								# If the inner list at index zero is the key 
				return e[1]									# ... then return the value at inner list index 1.
		return None

	def __str__(self):
		"""recall this is what happens when one tries to print an instance of this variable"""
		result = "{"
		for b in self.buckets:
			for e in b:
				result = result + str(e[0]) + ':' + str(e[1]) + ','
		return result[:-1] + '}' # result[:-1] omits the last comma

import random # a standard libary module we'll discuss in Chapter 12

D = intDict(30)
for i in range(20):
	#choose a random int between 0 and 10**5
	key = random.randint(0, 10**5)
	D.addEntry(key, i)
print 'The value of the intDict is: '
print D

print '\n', 'The buckets are: '
for i in range(D.numBuckets):			#violates abstraction barrier
	print 'bucket ',i,':', D.buckets[i]		
#	for hashBucket in D.buckets: 		#violates abstraction barrier
#		print ' ', hashBucket

############################################################################
# What is the complexity of the method getValue in intDict?
# The exact answer will depend on the expected value of a collision.
# If there are no collisions -- the same it's O(1) because every value is put into its same own bucket
# If everything is in 1 bucket then it's O(n) because we have to search every bucket.
# The EV of length of sampling is the expected (the expected number of repeat indices) / (the number of places to put those indices )







