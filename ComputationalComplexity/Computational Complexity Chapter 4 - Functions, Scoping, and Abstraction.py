# Computational Complexity with Python, Chapter 4: Functions, Scoping, and Abstraction
# See page 50 for some interesting discussion of scope of variables and how functions (as objects) get bound to variables

# Exercise 4.1a - Write a function isIn that accepts two strings as arguments and returns True if either string occurs anywhere in the other
# Hint: you might want to use the bult-in str option 'in'.

'''
def isIn(a,b):
	if(a in b or b in a):
		return True
	else:
		return False

strFirst = "" 
strSecond = ""
while(1==1):
	strFirst = raw_input("Enter your first string: ")
	if(strFirst == 'exit'): break
	strSecond = raw_input("Enter your second string: ")
	if(strSecond == 'exit'): break
	if isIn(strFirst,strSecond):
		print "Yes, ",strFirst," or ",strSecond," is a substring of the other"
	else:
		print "No, those are not substrings of each other"
print "Goodbye!"
'''


# Exercise 4.2a - Generalize the bisect-method root work from Chapter 3 into a function that accepts arbitrary value, root, and tolerance.
'''
def findRealRoot(x, power, epsilon):
	"""This is a function docString. ssumes x and epsilon int or float, power an int,
			epsilon > 0 & power >= 1
		Returns float y such that y**power is within epsilon f x.
			If such a float does not exist, it returns None"""
	guesses = 0
	if x < 0 and power%2 == 0:
		return None

"""	
#	This doesn't work for cases where the target is between (-1, 1) because then abs(root) > abs(target).
#	In other words, the low or high is not the target but is the root, and we don't yet know the root.
#	So we just put the low or high at -1 or 1, knowing that it's an overestimation, because we don't have a better guess.
#	if(x < 0):
#		low = x
#		high = 0.0
#	else:
#		low = 0.0
#		high = x
"""
	if(abs(x)<=1):
		low = -1.0
		high = 1.0
	else:
		low = min(0.0,x)
		high = max(0.0,x)
	#this is just a faster way to write the above
		#low = min(-1.0, x)
		#high = max(1.0, x)
	guess = (low + high) / 2.0
		#print 'high = ', str(high), 'low = ', str(low), ' guess = ', str(guess)
		#	exit()
	while(abs(guess**power - x) >= epsilon):
		if(guess**power - x < 0):
			low = guess
		else:
			high = guess
		guesses += 1
		guess = (low + high) / 2.0
		# print guess
		#print 'new high: ',high," new low: ",low,", new guess: ",guess
		if(guesses >= 25): exit();
	print "It took ",guesses," tries",# to find an acceptable value.",
	print "(",guess,")^",power," is ",guess**power,", within ",epsilon," of ",x
	return guess

def testFindRoot():
	epsilon = 0.00001
	for x in (0.25, -0.25, 2, -2, 8, -8):
		for power in range(1,4):
			print 'Testing x = ' + str(x) + ' and power = ' + str(power)
			result = findRealRoot(x, power, epsilon)
			if result == None:
				print ' No root :-( '
			#else:
			#	print ' ', result**power, '~=', x,

def testFindRootAuto():
	target = float(raw_input('Enter a target: '))
	power = int(raw_input('Enter an integer power: '))
	guess = raw_input('Enter a guess of its root, or "auto" to use targer / 2: ')
	epsilon = float(raw_input('Enter your tolerance, such as 0.01: '))
	if(guess == "auto"):
		guess = target/2.0
	else:
		guess = float(guess)
	findRealRoot(target, power, epsilon)

testFindRoot()
#	findRealRoot(25,2,0.01)
#	findRealRoot(-0.001,3,0.00001)
#testFindRootAuto()
'''

# Exercise 4.3a - Recursion and factorials.  Recursion is just processing all the inductive steps.

'''
# Iterative calculation of a factorial
import time
def factI(n):
	"""Assumes that n>0 and is an integer.
	Returns n!"""
	value = 1
	while(n > 1):
		value *= n
		n = n-1
	return value

def factR(n):
	"""Assumes that n>9 and is an integer.
	Returns n!"""
	# Tell the program what to do in the base case.  This will generally be a simple assignment.
	if n==1:
		return n
	# Tell the function what to do otherwise. This will involve the function calling itself.
	# In thise case, n! = n*(n-1)!.  And (n-1)! = (n-1)*(n-2)!.  So we want to multiply n by all the successive factorial values until n = 1.
	else:
		return n*factR(n-1)

t=0
t = time.time()

n=int(raw_input('Enter a number: '))
x = factI(n)
print n,"! is ",x

elapsed = time.time() - t
print elapsed

t=0
t = time.time()

n=int(raw_input('Enter a number: '))
x = factR(n)
print n,"! is ",x

elapsed = time.time() - t
print elapsed
'''

# Exercise 4.3b - Fibonacci numbers recursively. Also, a test for its effectivness.
# Interesting note: this runs super slow for > 50 results, where as iteration would run very fast.
# The main benefit of recursion is the simplicity of writing the code?

'''
def fib(n):
	"""n is an integer.
	Returns the n'th number of the Fibonacci sequence"""
	print "computing fib(",n,"), yay"
	"""
	This print command demonstrates the fundamental idea of recursion.
	fib(5) calls fib(4) and fib(3)
		But fib(4) calls fib(3) and fib(2)
			and fib(3) calls fib(2) and fib(1)
				and fib(2) calls fib(1) and fib(0), which both our basecases so don't call anything else
			and fib (2) calls fib(1) and fib(2), which both hit our casecases so don't call anything else
		But fib(3) calls fib(2) and fib(1)
			and fib(2) calls fib(1) and fib(0), which hit our basecases so don't call anything else
	So we have 5 calling 4 -> 3
		and 4 calling 3 --> 2
			and 3 calling 2-->1
				and 2 calling 1, 0
		and 3 calling 2 --> 1
				and 2 calling 1, 0
		and 2 calling 1, 0

	fib(2) is fib(1),fib(0)
	fib(3) is fib(2),fib(1) --> fib(2)[,fib(1),fib(0)],fib(1)   
		// above, fib(2) doesn't expand, fib(2) just continues to call fib(1) and fib(0) before it reaches the base case
	fib(4) ia fib(3),fib(2) --> fib(3)[,fib(2),fib(1)],fib(2) --> fib(3)[,fib(2),[[fib(1),fib(0)]],fib(1)],fib(2),[fib(1),fib(0)]
		--> 3, 2, 1, 0, 1, 2, 1, 0

	So we'd expect the print statement above for fib(5) to read:
	5 is (4),(3) --> (4),[3,2],(3),[2,1] --> (4),[3],[[2,1]],[2],[[1,0]],(3),[2],[[1,0]],[1] -->(4),[3],[[2]],[[[1,0]]],[[1]],[2],[[1]],[[0]],(3),[2],[[1]],[[0]],[1]
		4,3,2,1,0
		1,2,1,0
		3,2,1,0,1

	"""
	value = 0
	# We define two base cases because we are taking sums of (n-1) and (n-2).  
	if n==0 or n==1:
		return 1
		# You don't want to define these separately because there should only be 1 return statement,
		# which applies if either base case is reached.
	# Define the recursive case.  Rembmer, recursion avoids having to use loops.
	# fib(n) = fib(n-1) + fib(n-2). 
	# 
	else:
		return fib(n-1) + fib(n-2)

def testFib(n):
	"""n is an integer >= 0.
	Returns a test of the first n Fibonacci numbers"""
	for i in range(n+1):
		print i,"th: ",fib(i)

n = int(raw_input("How many Fibbonacci numbers do you want to see?: "))
testFib(n)
'''


# Exercise 4.3c - Checking to see if a word is a palindrome.
#	A palindrome is the same forward and backward, so we want to go 

'''
def isPalindrome(word):
	"""Assumed word is a string.  It ignores word casing and non-letters.
	Returns TRUE if word is the same forward as backward, otherwise returns False"""
	
	def toChars(word):
		word = word.lower()	# sets lower case
		word_letters = ''
		for c in word:
			if c in 'qwertyuiopasdfghjklzxcvbnm':
				word_letters += c
		return word_letters

	def isPal(word):
		print word
		if(len(word) <= 1):
			return True
		else:
			return word[0]==word[-1] and isPal(word[1:-1])
			# This is a clever way to continue decrementing that length of the word we're sending to the checker
			# The last letter will always return TRUE, but if any ends of the word don't match then it'll return FALSE
			# making the entire boolean expression falses

	return isPal(toChars(word))

word = raw_input("Enter your sentence: ")
print isPalindrome(word)
'''

# Exercise 4.4a - Global Variables, Fibonacci example

'''
def fib(n):
	"""n is an integer.
	Returns the n'th number of the Fibonacci sequence"""
	global numFibCalls
	numFibCalls += 1
	value = 0
	if n==0 or n==1:
		return 1
	else:
		return fib(n-1) + fib(n-2)

def testFib(n):
	for i in range(n+1):
		global numFibCalls
		numFibCalls = 0
		print 'fib of ', i ,'=', fib(i)
		print '\t','fib called', numFibCalls, 'times.'
			# The numFibCalls variable is updated when fib() is called
		#	print i, "th: ", fib(i)

n = int(raw_input("How many Fibbonacci numbers do you want to see?: "))
testFib(n)
'''

# Exercise 4.5a - Modules
# import looks at the relative directory of this file first of all

'''
import circle
pi = 3.0
print pi
print circle.pi
	# module.variable or module.function is used to refere to variables and functions that come from those modules.
	# It is possible to bind all module names locally so you don't need the "module." to call it, but that is highly confusing
print circle.area(3)
print circle.circumference(3)
print circle.sphereSurface(3)
'''

# Exercise 4.6 - I/O to files
# The standard output director is the pwd where the file is run from

path = '/Volumes/git/Dropbox/python'
nameHandle = open(path + '/family.txt','w')
for i in range(2):
	name = raw_input('Enter name: ')
	nameHandle.write(name + '\n')
nameHandle.close()

nameHandle = open(path + '/family.txt','r')
for line in nameHandle:
	#	print line
	print line[:-1]	# The difference with normal 'print' is that this doesn't print the last character, i.e. the line break
nameHandle.close()

nameHandle = open(path + '/family.txt','a')
nameHandle.write('Ryan\n')
nameHandle.close()

nameHandle = open(path + '/family.txt','r')
for line in nameHandle:
	#	print line
	print line[:-1]
nameHandle.close()

nameHandle = open(path + '/family.txt','r')
print nameHandle.read()
nameHandle.close()

