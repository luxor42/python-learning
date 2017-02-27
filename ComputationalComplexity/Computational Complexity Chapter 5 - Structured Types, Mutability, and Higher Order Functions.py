 # Chapter 5: Strucutred Types, Mutability, and Higher Order Functions

# Exercise 5.1a - playing with Tuples
'''
x = (1,)	# Notice the comma!  That's ho you make a singleton tuple, else it's just a string.
print x

x = (1)
print x
'''

'''
t1 = (1,'two',3)
t2 = (t1, 3.25)
print t1
print t2
print(t1 + t2)
print(t1 + t2)[3]
print(t1 + t2)[2:5]
'''


# Exercise 5.1.b - Print the common divisors of 
'''
def findDivisors(n1,n2):
	"""Assumes that n1 and n2 are positive ints
		Returns a tuple containing all common divisors of n1 & n2"""
	divisors = ()	#	The empty tuple
	for i in range(1, min(n1,n2) + 1):	#	+1 because it is "up to but not including the given int"
		if n1 % i == 0 and n2 % i == 0:
			divisors = divisors + (i,)
	return divisors

def totalDivisors(divisors):
	total = 0
	for d in divisors:
		total += 1
	return total

a = int(raw_input("Enter first number: "))
b = int(raw_input("Enter second number: "))
x = findDivisors(a,b)
print 'Divisors are: ' + str(x)
print 'There are ' + str(totalDivisors(x)) + ' total divisors'
'''

# Exercise 5.1.c - Multiple assignment when the function returns a specified number of values.
'''
def findDivisors(n1,n2):
	"""Assumes that n1 and n2 are positive ints
		Returns a tuple containing all common divisors of n1 & n2"""
	divisors = ()	#	The empty tuple
	for i in range(1, min(n1,n2) + 1):	#	+1 because it is "up to but not including the given int"
		if n1 % i == 0 and n2 % i == 0:
			divisors = divisors + (i,)
	return divisors

def findExtremeDivisors(n1,n2):
	"""Assumes that n1 and n2 are positive ints
		Returns a tuple containing the smaller common divisor > 1
		and the largest common divisors of n1 and n2"""	
	divisors = ()	#	The empty tuple
	minVal, maxVal = None, None
	for i in range(2, min(n1,n2) + 1):
		if n1 % i == 0 and n2 % i == 0:
			#	divisors = divisors + (i,)
			if minVal == None or i < minVal:
				minVal = i
			if maxVal == None or i > maxVal:
				maxVal = i
	return (minVal, maxVal)

a = int(raw_input("Enter first number: "))
b = int(raw_input("Enter second number: "))
minVal, maxVal = findExtremeDivisors(a,b)
x = findDivisors(a,b)
print 'Min and Max divisors are: ' + str(minVal) + " and " + str(maxVal)
print 'All divisors are ' + str(x)
'''

# Exercise 5.2.a - Lists use square brackets [] and tuples use parentheses ()
'''
L = ['I did it all',4,'the nookie']
for l in range(len(L)):
	print L[l]

print [1,2,3,4][1:3][1]
# Uses brackets in 3 different ways but is well-defined.  The first bracket set is the list.
'''

# Exercise 5.2.b - Demonstratin that identical lists actually have unique IDs, mutability, aliasing
'''
Techs = ['MIT','Caltech']
Ivys = ['Harvard','Yale','Brown']
print 'Techs: ',Techs,' and Techs list has ID ',id(Techs)
print 'Ivys: ',Ivys,' and Ivys list has ID ',id(Ivys)
Univs = [Techs,Ivys]
Univs1 = [['MIT','Caltech'],['Harvard','Yale','Brown']]

print 'Univs = ', Univs, ' and in-memory ID: ',id(Univs)
print 'Univs1 = ', Univs1, ' and in-memory ID: ',id(Univs1)
print 'Ids of Univs[0]: ',id(Univs[0]),' and Univs[1] ',id(Univs[1])
print 'Ids of Univs1[0]: ',id(Univs1[0]),' and Univs1[1] ',id(Univs1[1])
print Univs == Univs1

Techs.append('RPI')
print 'Appended RPI to Techs'
print 'After append, Techs: ',Techs,' and Techs list has ID ',id(Techs)
print 'After append, Univs: ',Univs,' and Techs list has ID ',id(Univs)
print 'After append, Univs1: ',Univs1,' and Techs list has ID ',id(Univs1)
# Recall that Univs is constructured from the Techs lists per se, where Univs1 was just the universities
# So Univs changes when Techs changes, but Univs1 doesn't change.
'''

# Exercise 5.2.c - List concatenation
'''
L1 = [1,2,3]
L2 = [4,5,6]
L3 = L1 + L2	#	This assignment doesn't affect L1 or L2
print 'L3 = ',L3
L1.extend(L2)	#	The elements of the list L2 are added to L1
print 'L1 = ',L1
L1.append(L2)	#	The  list L2 is put into L1 as a new element
print 'L1 = ',L1
'''

# Exercise 5.2.d - Cloning to avoid brain explosion of iterating and concurrently mutating lists

'''
def removeDupsImproperly(L1,L2):
	"""Accepts to lists, L1 & L2
		Returns a list that is elements in L1 that are not also in L2"""
	for e in L1:
		if e in L2:
			L1.remove(e)
	return L1

def removeDupsProperly(L1,L2):
	"""Accepts to lists, L1 & L2
		Returns a list that is elements in L1 that are not also in L2"""
	for e in L1[:]:	# This is a "slice" of the list, i.e. a new variable that is the substring
		if e in L2:
			L1.remove(e)
	return L1

L1 = [1,2,3,4]
L2 = [1,2,5,6]
print removeDupsImproperly(L1, L2)
print removeDupsProperly(L1, L2)
'''

# Exercise 5.2.e - Element-by-element list operations.
# Frighteningly similar to R's vectors.
# The book warns against over-using lists for elegance & subtlty b/c it's hard to understand
'''
L = [x**2 for x in range(1,7)]
print L

mixed = [1,2,'a',3,4.0]
print[x**2 for x in mixed if type(x) == int]
'''

# Exercise 5.3.a - Functions as objects - Passing functions as paramaters of other functions
'''
def applyToEach(X, f):
	"""Accepts a list L and a function f
		Mutates the list L by applying the function f to each element of the list L"""
	print id(X)
	for i in range(len(X)):
		X[i] = f(X[i])
	# Note that we are mutating the same List; we can confirm that via the IDs
	# Lists are not just variables but represent a unique state of memory

L = [ 1, -2, 3.33]
print id(L)
print 'L = ', L
print 'Apply abs to each element of L: '
applyToEach(L, abs)
print 'L = ',L
print 'Apply int to each element of L: '
applyToEach(L, int)
print 'L = ',L
'''

# Exercise 5.3.b - the "map" higher-order function for unary operations

def factR(n):
	"""Assumes that n>9 and is an integer.
	Returns n!"""
	# Tell the program what to do in the base case.  This will generally be a simple assignment.
	if n==1:
		return n
	# Tell the function what to do otherwise. This will involve the function calling itself.
	# In thise case, n! = n*(n-1)!.  And (n-1)! = (n-1)*(n-2)!.
	# So we want to multiply n by all the successive factorial values until n = 1.
	else:
		return n*factR(n-1)

L = [1,2,3]
print 'L = ',L
print "Factorial of L's elements map(factR,[1,2,3]): ",
print map(factR,[1,2,3])

L1 = [1,28,36]
L2 = [2,57,9]
print 'L1 is ',L1,' and L2 is ',L2," so map(min,L1,L2) is: ",
print map(min,L1,L2)
#	Does an element-by-element comparison to return list [min(1,2),min(28,57),min(36,9)]


# Exercise 5.5.a - Dictionaries - unordered & not accessible via an index.
# Dictionaries are actually hash tables (to be explored later) so are super fast
'''
monthNumbers = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May'}
print 'The third month is ', monthNumbers[3]
dist = monthNumbers['Apr'] - monthNumbers['Jan']
print 'Apr and Jan are ',dist,' months apart'

print monthNumbers.keys()
x= monthNumbers.keys()
print x.sort()	#	This is None because monthNumbers has no awareness of internal structure
keys = []
for e in monthNumbers:
	keys.append(e)
keys.sort()		#	However, the list keys is sortable so this returns the sorted list
print keys
'''

