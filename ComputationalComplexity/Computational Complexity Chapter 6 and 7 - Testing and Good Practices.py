# Computational Complexity Chapter 6 and 7.py

'''
Unit Testing = individual units of code (e.g. functions) work propertly
Integration Testing = whether a program as a whole behaves as intended

Often useful to write "stubs" - pieces of code, such as other functions or classes, that are called by the unit being tested.
Stubs are simple stand-ins for things that may be much more complex or not yet exist.

'''

# Chapter 6
# Exercise 6.1

# Bugs in this program:
# Aliasing Bug!!!
# Variable re-initialized every time a loop was run
# Didn't add parantheses to actually invoke a function (as opposed to refer to it)

'''
def isPal(x):
	"""Assumes x is a list
		Returns True is the list is a palindrome; False otherwise"""
	print "x is : ",x
	#	temp = x  	# This was the source of the aliasing bug
	temp = x[:]
	print "temp is : ",temp
	#	temp.reverse initially didn't put () after reverse call
	temp.reverse()
	""" THIS LINE ALSO REVERSES X, BECAUSE X IS JUST A NAME FOR THE SAME DATA AS TEMP.  
	ALIASING BUG!!! """
	print "x is: ",x," and temp is ",temp
	if temp == x:
		return True
	else:
		return False


def silly(n):
	"""Assumes n is an int > 0
	Gets n inputs from user
	Print 'Yes' if the sequence of inputs forms a palindrome;
		'No' otherwise"""
	result = []
	for i in range(n):
		#	result = []   This should have been placed outside of the for loop
		elem = raw_input('Enter element: ')
		result.append(elem)
	print result
	if isPal(result):
		print 'Yes'
	else:
		print 'No'

silly(2)
#elem = raw_input("Enter an element: ")
#isPal(elem)
'''

# Chapter 7

'''
Exceptions deal with situations in which a program has attempted to execute a statement with no appropriate semantics
Exceptions can be handled by creation of a 'try block'
The except statement following the try can except a tuple of statements or you can write multiple except statements for each block
e.g. try:
		[code]
	 except thisError:
	 	[code]
	 except thatError:
	 	[code]
	 except (theseErrors, thoseErrors):
	 	[code]

# Programs can be called to raise exceptions if particular cases are met -- thing of function arguments not matching assumptions!


'''

'''
try:
	successFailureRatio = numSuccesses/float(numFailures)
	print 'The success/failure ratio is',successFailureRatio
except ZeroDivsionError:
	print 'Nofailures so the success/failure ratio is undefined.'
print 'Now here'
'''

'''
def sumDigits(s):
	"""Assumes s is a string
		Returns the sum of the decimal digits in s
			For example, if s is 'a2b3c' it returns 5"""
	intSum = 0
	print s
	for i in range(len(s)):
		print intSum,"+",s[i],
		try:
			intSum += int(s[i])
			print "=",intSum
		except ValueError:	#I used TypeError at first because i didn't know what error would be thrown
			print 'that was a letter not a number doofus'
	print "Total sum of digits is "

sumDigits('a2b3c')
'''

#	Exercise 7.1.1
#	Original program is below, but it fell apart on 
#	val=int(raw_input('Enter an integer: '))
#	print 'The square of the number you entered is', val**2

'''
while True:	# This while loop keeps asking for a new integer until an integer is given
	val=raw_input('Enter an integer: ')
	try:
		val = int(val)
		print 'The square of the number you entered is', val**2	
		break # exits the while looop
	except ValueError:
		print val,' is not an integer'
'''

'''The above code is much more verbose.
It could be put in a function so it doesn't have to be written every time we want to check
if an input value, is an integer else throw an Error Message a ValueError.

Or we could generalize further:
Write a function that checks if an input value is [[whatever type]] and throws [[whatever message]] for [[whatever error]] 
'''

'''
def ReadVal(valType, requestMessage, errorMessage):
	while True:
		val = raw_input(requestMessage + '')
		try:
			val = valType(val)
			return val
		except ValueError:
			print val, errorMessage


val = ReadVal(int, 'Enter an integer: ','is not an integer. Try again.')
print val**2
'''

# Definition: Polymorphism: works for arguments of many different types

#	Exercise 7.1.2
#	Implement the following function specification

'''
def findAnEven(l):
	"""Assumes l is a list of integers
		Returns the first even number in l
		Raises ValueError if l does not contain an even number"""
	print l
	num = 0
	if type(l) is not list:
		raise TypeError('The parameter passed to findAnEven is not a list.  It is a ',type(l))

	for i in range(len(l)):
		if l[i] % 2 == 0:
			num = l[i]
			print num
			break
	if num == 0:
		raise ValueError('no even number was in the list passed to findAnEven')
	else:
		return num


#l = [1,3,4,6,8,20]
l = (1,2,3)
l = [1,3,5]
findAnEven(l)
print "we're done!"
'''

#	Exercise 7.2.1
#	Implement getRatios - finds ratios of two equal-length lists
#	Shows how try blocks can keep code readable by pushing the complexity into the "Except" conditions

'''
def getRatios(vect1, vect2):
	"""Assumes: vect1 and vect2 are lists of equal length of numbers
		Returns: a list containing the meaningful values of vect1[i]/vect2[i]"""
	ratios = []
	for index in range(len(vect1)):
		try:
			ratios.append(float(vect1[index])/float(vect2[index]))
		except ZeroDivisionError:
			ratios.append(float('nan')) #nan = Not a Number
		except:
			raise ValueError('getRatios called with bad arguments')	# A very general error because 'except' happens with any error
	return ratios

def readVal(valType, requestMessage, errorMessage):
	while True:
		val = raw_input(requestMessage + '')
		try:
			val = valType(val)
			return val
		except ValueError:
			print val, errorMessage

def populateList(n):
	val = []
	var = ""
	message = ""

	for i in range(n):
		message = 'Enter integer #' + str(i) + ": "
		#	print message 
		val.append(readVal(int, message ,'is not an integer. Try again.'))
	return val


try:
	print getRatios([1.0,2.0,7.0,6.0],[1.0,2.0,0.0,3.0])
	print getRatios([],[])
	print getRatios([1.0, 2.0], [3.0])
except ValueError, msg:
	print msg

"""
n = readVal(int,"Enter how many integers you want in each list: ", 'is not an integer. Try again.')	
print "populating list Val1: "
val1 = populateList(n)
print "populating list Val2: "
val2 = populateList(n)
print val1
print val2
print getRatios(val1, val2)
"""

'''

#	Exercise 7.2.2
#	Implementation of getGrades 
#	Notice that we can define our own error message
#	Also see text for assert / assertions -- used to confirm that a value (or statement) is true else throws an exception

import os

def getGrades(fname):
	try:
		gradesFile = open(fname, 'r') #open file for reading
	except IOError:
		raise ValueError('getGrades coupld not open ' + fname)
	grades = []
	for line in gradesFile:
		try:
			print line
			grades.append(float(line))
		except:
			raise ValueError('Unable to convert line to float')
	return grades

try:
	grades = getGrades(os.path.dirname(os.path.realpath(__file__)) + '/quiz1grades.txt')
	grades.sort()
	median = grades[len(grades)//2]
	print 'Median grade is', median
except ValueError, errorMsg:
	print 'Whoops.', errorMsg


