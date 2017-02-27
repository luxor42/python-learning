# Chapter 9 - A simplistic introduction to algorithmic complexity

"""
Measure COMPLEXITY in numbers of operations required to complete the program.
Basis of comparison isn't total number of operations but the time to completion
based upon size of the input. 
"""

# Exercise 9.1.1 - Linear search

'''
def LinearSearch(L, x):
	for e in L:
		if e == x:
			return True
	return False

L = range(1,100)
x = 250
print LinearSearch(L, x)
'''
			
""" Distinct best, worst, average (Expected) cases for algorithms:
Best case = minimum over all possible inputs of a given size
	- for LinearSearch, this does not depend on the size of L.
Worst case = maximum over all possible inputs of a given size
	- for LinearSearch, this scales linearly with the size of L.
Average case = expected running time over all with a given size.

Generally we're designing algorithms to reduce the worst case // minimize the upper bound of all worst cases
"""

# Exercise 9.1.2 - Iterative implementation of the factorial function
#	It takes 2 steps for initial assignment + return.  Then 5*n steps
#   Total # of steps is 2 + 5n.  As n increases, 2 << 5n, so we just say "5n" as worse case.

'''
def fact(n):
	"""Assumes n is a natural number
	Returns n!"""
	answer = 1
	while n > 1:
		answer = n*answer
		n = n -1
	return answer

target = int(raw_input("Enter your target num: "))
print fact(target)
'''

# Exercise 9.1.3 - Exhaustive v. bisection approximation for square root
# Bisection approximation scales very much sub-linearly. 
# Multiplicative constants of its relative efficiency are irrelevant

'''
def squareRootExhaustive(x, epsilon):
	"""Assumes x and epsilon are positive floats and epsilon < 1
	Returns a y such that y*y is within epsilon of x"""
	counter = 0
	step = epsilon**2
	ans = 0.0
	while abs(ans**2 - x) >= epsilon and ans*ans <= x:
		ans += step
		counter += 1
	if ans*ans > x:
		raise ValueError
	return {'ans':ans, 'counter':counter}

def squareRootBi (x, epsilon):
	"""Assumes x and epsilon are positive floats & epsilon < 1
	Returns a y such that y*y is within epsilon of x"""
	counter = 0
	low = 0.0
	high = max(1.0, x)
	ans = (high + low) / 2.0
	while abs(ans**2 - x) >= epsilon:
		if ans**2 < x:
			low = ans
		else:
			high = ans
		ans = (high + low) / 2.0
		counter += 1
	return {'ans':ans, 'counter':counter}

target = int(raw_input("Enter the number to find square root of: "))
epsilon = float(raw_input("Enter a tolerance level: "))
result = squareRootExhaustive(target, epsilon)
print result['ans']
print result['counter']

result = squareRootBi(target, epsilon)
print result['ans']
print result['counter']
'''

# Exercise 9.2.1
# Asymptotic notation describes the complexity of an algorithm as its inputs approach infinity.
# As x --> inf, and gets >> 10 in the example below, non-constant terms dominate quickly.
# Total time below: 1000 + x + 2*x^2.  The 2*x^2 will dominate.
# f(x) O(x^2) ... "f(x) grows no faster than the polynomial x^2 in an asymptotic case"

'''
def f(x):
	"""Assume x is an int > 0"""
	ans = 0
	#Loop that takes constant time .... + 1000 to the efficiency
	for i in range(1000):
		ans += 1
	print 'Number of additions so far', ans

	#Loop that takes time x .... + x to the efficiency
	for i in range(x):
		ans += 1
	print 'Number of additions so far', ans

	#Next loops take time x**2 .... + 2x**2 to the efficiency.  
	for i in range(x):
		#ans +=1 
		for j in range(x):
			ans += 1
			ans += 1
	print 'Number of additions so far', ans
	return ans
'''

""" Section 9.3 - Important complexity cases """

'''
O(n) --> linear time
O(n log n) --> log-linear time
O(n**k) --> polynomial running time.  k is a constant.
O(c**n) --> exponential running time.  c is constant, n is input size.
'''

#############################################################################
# Exercise 9.3.1 O(1) --> constant time.
# Asympototic complexity is independent of the inputs.
# e.g.  finding length of a Python list.  multiplying 2 numbers. """


#############################################################################
# Exercise 9.3.2 - # O(log n) --> logarithmic complexity.  
# Don't really care about the base of the log
# because log_2(x) = log_10(x)/log_10(2) = k * log_10(x)


# Example: notice that we have 1 more iteration per 10x increase the input
# This complexity is this O(log(i))
'''
def intToStr(i):
	"""Assumes i is a nonnegative int
	Returns a decimal string representation of i"""
	digits = '0123456789'
	if i == 0:
		return '0'
	result = ''
	while i > 0:
		result = digits[i%10] + result
		i = i//10
	return result
'''

# Example: 
# the "result" above is on the order of log(i) almost as a definitional thing
# representing the number in base 10 requires 1 more digit for every 10x growth
# Ths addDigits below loops over the string representation of the number
# so the for loop is also log(n) in length.  Because it called intToStr(),
# the total complexity is proportaional to O(log(n)) + O(log(n)), or just O(log(n)) 
# Note that we're measuring complexity by MAGNITUDE OF NUMBER not LENGHT OF STRING

'''
def addDigits(n): 
	"""Assumes n is a nonnegative int
	Returns the sum of the digits in n"""
	stringRep = intToStr(n)
	val = 0
	for c in stringRep:
		val += int(c)
	return val

target = int(raw_input("Enter the number to compute on: "))
print intToStr(target)
print addDigits(target)
'''


#############################################################################
# Exercise 9.3.3 - Linear Complexity
# Usually an algorithm is linear because it touches
# Each element of the list some constant (>0) number of times
# Above, addDigits is linear in the length of the string stringRep

# Below, using recursion reduces the computational complexity to linear
# Because we make as many calls as the magnitude of x.
# Complexity of the function is O(x)

# HOWEVER!  We create a new stack frame each call preceeding data frames.
# "Space complexity" is O(x) <-- memory required to implement scales linearly 
'''
def factorial(x):
	"""Assumes that x is a positive int
		Returns x!"""
	if x == 1:
		return 1
	else:
		return x*factorial(x-1)

target = int(raw_input("Enter the number to find the factorial of: "))
print factorial(target)
'''

################################################################################
# Note 9.3.4 - Log-Linear complexity
# Means that algorithm scales with O(n * log(n)), for example
# where n is the length of a list rather that will be sorted.
# Interpret this as having two parts to the complexity: one that
# scans and the other that does something.  THe scan is O(n)
# and the thing it does is O(log(n)) for each scane, so the total
# time complexity if O(n*log(n))

################################################################################
# Exercise 9.3.5 - Polynomial Complexity
# Frequently quadratic, growing with square of the input
# Generally because the entire list is scanned as a pointer
# advances over the list ... n*(n+(n-1)+(n-2)+(n-3)+...
# so maybe actually n^2/2, but that's as bad as n^2

'''
def isSubset(L1, L2):
	"""Assumes L1 and L2 are lists. Returns True if each element in L1 is also
	in L2 and False otherwise.
	The complexity here is O(len(L1)) * O(len(L2))
	"""
	for e1 in L1:
		#	print e1
		matched = False
		#	print matched
		for e2 in L2:
			#	print e2
			if e1 == e2:
				matched = True
				#	print matched
				break
		if not matched:
			#	print matched
			return False	# Break out of the program the first time there's no match
	return True	#	If we've gotten to this point then we matched all L1 to L2 elements

L1 = raw_input("Enter a bunch of letters L1: ")
L2 = raw_input("Enter a bunch more letters L2: ")
if isSubset(L1,L2) == True:
	print "L1 letters are a subset of L2!"
else:
	print "L1 letters are not a subset of L2!"
'''

#	In this example the *worst case* is n^2. Could be much better

# Exercise 9.3.5.2 - List intersection

'''
def makeIntersection(L1, L2):
	"""Assumes L1 and L2 are lists.
	Returns a string that includes unique elements in both L1 and L2."""
	# Find elements in both lists.  Running time is O(len(L1))*O(len(L2))
	i = 0
	tmp = []
	for e1 in L1:
		for e2 in L2:
			if e1 == e2:
				tmp.append(e1)
	# Remove duplicates.  The "not in" built-in function is as bad as
	# the long-hand loop above in complexity.  
	L3 = []
	for e in tmp:
		if e not in L3:
			L3.append(e)
	return L3

L1 = raw_input("Enter a bunch of letters L1: ")
L2 = raw_input("Enter a bunch more letters L2: ")
print "Intersection of those lists is: "
print makeIntersection(L1,L2)
'''

# Overall complexity is max{O(find common), O(remove duplicates)}
# the length of tmp is at most min(L1,L2) so O(find common) dominates.

################################################################################
# Exercise 9.3.6 - Exponential Complexity
"""
BLUF is that we loop over a list that is 2^n where n is the length of our list,
so the complexity is O(2*n).  For every extra n it will take 2 times as long.
"""

# Find the power set of a list
# The power set contains 2^n elements because (informally) each element will either
# be or not be in an element of the power set.  There are 2 possible states for 
# each element, and the states are independent. So 2^n elements in power set.
# We can explain that "present" / "not present" state by using the binary rep-
# resentation of the number to return the set elements.

# E.g. 11.  11%%2=1, so right most digit is a 1
	# To see if we can fit another digit to the left, see is 11 / 2 > 1.  
	# Keep doing that division until we get a number < 2.
	# If it's 0 then stop, if 1 then append 1 at left and stop
	# 11%%2 = 1 means it's an odd number whereas all other 2^n are even, so right most digit is odd.
	# 11 // 2 = get the base number when 11 / 2, so 11 // 2 = 5.
# 5%%2 = 1, so the next digit is 1.
	# 5 // 2 = 2
# 2%%2 = 0.
	# 2 // 2 = 1
# 1 % 2 = 1.  
# So binary representation is 1011.
#  5 = 		    1*2^2 + 0*2^1 + 1*2^0 =     4 + 0 + 1 =  5
# 11 =  1*2^3 + 0*2^2 + 1*2^1 + 1*2^1 = 8 + 0 + 2 + 1 = 11
# 12 =  1*2^3 + 1*2^2 + 0*2&1 + 0*2^1 = 8 + 4 + 0 + 0 = 12

def getBinary(n):
	"""Accept a number.  Return its binary equivalent."""
	binRep = ''
	while n > 1:
		#	print n
		binRep = str(n % 2) + binRep # Append to the left the next digif
		#	print binRep
		n = n // 2
	binRep = str(n % 2) + binRep
	return binRep

def getPowerSet(L):
	"""Accepts a list L and returns the power set of L,
	a list composed of all unique lists created from elements of L."""
	# There will be 2^n sets in the power set.
	# To construct each set, loop through a binary representation of numbers between 0 and 2^|L|.  
	# Loop through elements in the string up to index of the length of the returned binary string.	
	# In the first iteration, we'll have length 0 so binary representation is 0 and we have no values
	# In the second iteration, we've have (1) so the first element is present. 
	# In the third iteration will have (1,0) so the second element is present but not the first.
	# etc etc etc
	# If the binary string element's value at an index is 1 then include the element at that index in the set
	# If it's 0 then don't include the element at the index in the set.
	powerSet = []
	print L
	print type(L)
	print len(L)
	#	exit()
	for i in range(0, 2**len(L)):
		strBinRep = getBinary(i)  # Get the binary representation of the number between 0, 2^n
		#	print 'num: ' + str(i) + ', binary: ', strBinRep
		#raise ValueError("here we are")
		#exit()
		tmp = []				  # This is where we'll store the list for each iteration
		for j in range(0,len(strBinRep)):  # Cycle through the 1's and 0's in strBinRep
			# print 'at interior placement ' + str(j)
			#	print L[j]
			if strBinRep[j] == '1':
				tmp.append(L[j])  # Populate our tmp set w/ that L's value at that index if that location in the binary set is 1
		powerSet.append(tmp)
	return powerSet


target = raw_input('enter a few letters in order: ')
targetList = []
for e in target:
	targetList.append(e)
print "power set is: " + str(len(getPowerSet(targetList))) + " characters long"



##










