# Example 3.1

# Fun discovery: In python3, print is a function print(), so most of the commands won't work in python 3
# Find the cube root of a perfect cube
'''
x = int(raw_input('Enter an integer: '))
ans = 0
while ans**3 < abs(x):
		#print "Value of the decrementing function abs(x) - ans**3 is",abs(x)-ans**3
		ans = ans + 1
if ans**3 != abs(x):
	print x, 'is not a perfect cube'
else:
	if x < 0:
		ans = -ans
	print 'cube root of', x, 'is', ans
print 'tried ',ans,' tries'
exit()
'''

# Example 3.1b
# Just for fun instruction
'''
max = int(raw_input('Enter a positive integer: '))
i = 0
while i < max:
	i = i + 1
print i
'''

# Example 3.1c - Finger Exercise
# Write a program that asks the user to enter an integer and prints two integers, root and pwr, such that 0 < pwr < 6 and root**pwr is equal to the integer entered by the user. If no such integer exists, it should print a message to that effect
'''
user_int = int(raw_input('Enter a posiive integer: '))
print 'your input value is ',user_int
pwr = 2
root = 0
found = 0
while pwr < 6:
	while root**pwr < user_int:
		#print 'tried ',root,'^',pwr,' = ',root**pwr
		root = root + 1
	if root**pwr == user_int:
		print "you found the ",pwr," root of",user_int," and it was ",root
		found += 1
	pwr = pwr + 1
	root = 0
if found == 0:
	print 'no root was found such that root^power = ',user_int,', where 0 < power < 6, exists'
else:
	print 'You found ',found,' combinations of powers and roots!'
'''

# Example 3.2.a - Cube Roots with a for loop
'''
x = int(raw_input('Enter an integer: '))
for ans in range(0, abs(x+1)):
	if ans**3 >= abs(x):
		break
if ans**3 != abs(x):
	print x, 'is not a perfect cube'
else:
	if x < 0:
		ans = -ans
	print 'Cube root of', x, 'is', ans
'''

# Example 3.2.b - iterating and summing the digits in a string
'''
total = 0
for c in '12345789':
	total = total + int(c)
print total
'''
# Example 3.2.c - Let s be a string that contains a sequence of decimal numbers separated by commas
# e.g., s = '1.23,2.4,3.123'. Write a program that prints the sum of the numbers in s.
'''
total = 0
c = ''
my_string = '1.1,2.2,3.3,4.4,5.5' 
for s in my_string:
	if s == ',':
		total += float(c)
		print 'hit a comma after ',c,', running total is ',total,'!!'
		c = ''
	else:
		#print 'c is ',c
		#print 's is ',s
		c += s
		#print 'c is now',c
total += float(c)
print 'hit a comma after ',c,', running total is ',total,'!!'
print 'The total of these numbers is ',total
# Things I did wrong: used float not int. Did not do final sum outside of loop.
# Took me longer than desirable to realize I need to initialize c to a blank variable
'''

# Example 3.3a - Find the square root of a target within a given epsilon based on an arbitrary guess
# 0----------guess--------------guess^2----real^2
'''
target = float(raw_input('Enter a target: '))
guess = raw_input('Enter a guess of its square root, or "auto" to work automatically: ')
if(guess == "auto"):
	guess = target/2
else:
	guess = float(guess)
epsilon = 0.01
guesses = 0
low = 0
high = target
print guess
while(abs(guess**2 - target) > epsilon):
	if(guess**2 - target < 0):
		#print 'guess is too low!'
		#exit()
		low = guess
		#high = target <-- bad because we have no new information on what the high is.  Leave it as was.
	else:
		#print 'guess is too damn high!'
		#exit()
		high = guess  #<-- here's where we get information on what the high is.
		#low = 0       <-- similarly, in this case we got no new information on what the low was so shouldn't change it.
	guesses += 1
	guess = (low + high) / 2
	print guess
	#if(guesses >= 25):
	#	exit()
print "It took ",guesses," guesses to find an acceptable answer."
print "Our answer is ",guess,", its square is ",guess**2," within ",epsilon," of ", target
exit()
'''
# Things I did wrong: didn't think to move two variables to zero in on the guess
# Tried to just move the single variable around and didn't follow intuition 
# that I'd need to remember my last guess
# Also, I at first moved both high and low simultaneously rather than converging each side at once
# That was bad because the only new information was for 1 side of the vice at a time.
# These mistakes were fixed before implementing the cube root below, but then I made them again when updating the square.
# Way to learn!!!! :(

# Example 3.3b - What would Example 3.3a do if the target were negative?
# A: The while statement would run forever.
# A: High would equal low immediately and stay that way.

# Example 3.3c - What would have to change about Example 3.3a to make it robust
# to cube roots of negative and positive numbers?
# A: Change initial low from zero or the guess to the negative target,
# That is the only change because negative numbers still meet the condition
# that if(guess**3 - target < 0) then our guess is too small
# For efficiency cap the extreme from target to 0
'''
target = float(raw_input('Enter a target: '))
guess = raw_input('Enter a guess of its cube root, or "auto" to work automatically: ')
if(guess == "auto"):
	guess = target/2
else:
	guess = float(guess)
epsilon = 0.01
guesses = 0
if(target<0):
	low = target
	high = 0
else:
	low = 0
	high = target
print guess
while(abs(guess**3 - target) > epsilon):
	if(guess**3 - target < 0):
		low = guess
	else:
		high = guess
	guesses += 1
	guess = (low + high) / 2
	print guess
	#end
print "It took ",guesses," tries to find an acceptable value."
print "(",guess,")^3 is ",guess**3,", within ",epsilon," of ",target
'''


# Section 3.4 - Floats
# Exercise 3.4a - notice that floating point numbers defy intuition
'''
x = 0.0
for i in range(10):
	x = x + 0.1
if x==1.0:
	print x,'=1.0'
else:
	print x,'is not 1.0'
'''

# Exercise 3.4b - Find the decimal representation of the binary number 10011.
'''
string = raw_input('Enter your binary number: ')
power = len(string)
total = 0
for c in string:
	total += int(c)*2**(power-1)
	power -= 1
print total
'''
# Exercise 3.5a - Implementation of Newton / Raphson for a binomial in form ax*2 + bx + c = 0
# ask for the binomial's coefficient, mononomial's coefficient, and constant
# ask for guess
# use newton-raphson to calculate a better guess

epsilon = 0.0000001
counter = 0
intBinomial = float(raw_input('Enter the coefficient to the binomial (please enter 1): '))
intMonomial = float(raw_input('Enter the coefficient to the monomial (please enter 0): '))
intConstant = float(raw_input('Enter the constant term (please enter a negative number): '))
print "Your polynomial is: ",intBinomial,"x^2 + ",intMonomial,"x + ",intConstant
guess = float(raw_input("enter your guess as to the root of the equation: "))
print "guess is ",guess,", numerator is ", intBinomial*(guess**2)+intMonomial*guess+intConstant, ", denominator is",2*(intBinomial)*guess + intMonomial
new_guess = guess
while(abs(intBinomial*(new_guess**2)+intMonomial*new_guess+intConstant) > epsilon): 
	new_guess = new_guess - (intBinomial*(new_guess**2)+intMonomial*new_guess+intConstant) / (2*(intBinomial)*new_guess + intMonomial )
	# print "better guess is ",new_guess
	counter += 1
print "\n"
print "Using Newton-Raphson, after ",counter," guesses I came up with this:"
print "Guess of root is: ",new_guess
print "value of function at the point is: ",intBinomial*(new_guess**2)+intMonomial*new_guess+intConstant

# Now just copy/paste the relevant portion of the iterative square root finder above
# This is super hacky and assumes the user has done as requested above, so we have x^2 - C = 0 and we're trying to find sqrt(C)
counter = 0
target = -1*intConstant
low = 0
high = target
# reuse the original guess above
new_guess = guess
while(abs(new_guess**2 - target) > epsilon):
	if(new_guess**2 - target < 0):
		#print 'new_guess is too low!'
		#exit()
		low = new_guess
		#high = target <-- bad because we have no new information on what the high is.  Leave it as was.
	else:
		#print 'new_guess is too damn high!'
		#exit()
		high = new_guess  #<-- here's where we get information on what the high is.
		#low = 0       <-- similarly, in this case we got no new information on what the low was so shouldn't change it.
	counter += 1
	new_guess = (low + high) / 2
	#	print new_guess
	#if(counter >= 25):
	#	exit()
print "\n"
print "Using bisection method, it took ",counter," guesses to find an acceptable answer."
print "Our answer is ",new_guess,", its square is ",new_guess**2," within ",epsilon," of ", target

