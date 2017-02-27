 # Computational Complexity Chapter 8.py

# Object Oriented Programming
'''
Objects --> collections of both data and the methods that operate on that data

"Objects are the core things that Python programs manipulate.
Every object has a type that defines the kinds of things that programs can do with objects of that type."

8.1 
Abstract data type --> set of objects and the operations on those objects

Instantiation: s = IntSet()
Attribute references: x = s.member 

The object associated with the expression preceding the dot is implicitly passed as the first parameter of the method.

data attributes associated with a class are called class variables
data attributes associated with an instance of a class are called instance variables

The concept of 'representation invariant' is that the methods of the class will enforce what valid members of the class
look like by saying what data attributes they can have. Below remove() takes advantage of insert() by only checking 
once for the presence of the string; insert() is only allowed to put the string in if it isn't already in there.
The representation invariant should be defined such that violating it means that the methods break.
I.e. "all concrete operations must preserve the representation invariant"

The def __init__(self) is what happens when you initialize a new instance of a class.
The def __str__(self) is what happens when you print an instance of a class.
..... if you don't defeine __str__self then print s will spit out some location in memory
..... as always you can call those ad hoc with print s.__str__() or print IntSet.__str__(s)

'''

#	Exercise 8.1.1

'''
class IntSet(object):	#	All class definitions begin with the word 'Class'
	"""An intSet is a set of integers"""
	# Information about the implementation (not the abstraction)
	# The value of the set is represented by a list of ints, self.vals.
	# Each int in the set occurs in self.vals exactly once.

	"""IMPORTANT: All python classes have an __init__ method called when an object of that type is instantiated.
	s = IntSet() leads to IntSet.__init__ being called, with the newly created object itself as the passed parameter.
	In this case, the __init__ method creates vals, an object of type list (in this case an empty list).
	vals is referred to as a "data attribute" of the instance s of IntSet.

	The use of the word self is a convention that is universally respected
	
	"""

	def __init__(self):
		"""Create an empty set of integers"""
		self.vals = []

	#	A function such as insert defined within a class is called a method of the class
	def insert(self, e):
		"""Assumes e is an integer and inserts e into self"""
		if not e in self.vals:
				self.vals.append(e)

	def member(self, e):
		"""Assumes e is an integer
			Returns True if e is in self, and False otherwise"""
		return e in self.vals

	def remove(self, e):
		"""Assumes e is an integer and removes e from self
			Raises ValueError if e is not in self"""
		try:
			self.vals.remove(e)
		except:
			raise ValueError(str(e) + ' not found')

	def getMembers(self):
		"""Returns a list containing the elements of self.
			Nothing can be assumed about the order of the elements."""
		return self.vals[:]

	""" The is what happens when you print an instance of the class IntSet"""
	def __str__(self):
		"""Returns a string representation of self"""
		self.vals.sort()
		result= ''
		for e in self.vals:
			result = result + str(e) + ' '
		return '{' + result[:-1] + '}' # :-1 omits the trailing comma

s = IntSet()
s.insert(3)
print s.member(3)
s.insert(5)
print s
'''


'''

""" 8.1.1., 8.1.2 - abstraction, __init__, __str__, operator overloading, 

In preparation for creating a program that keeps track of students and faculty at a university,
implement a class that allows us to instantiate people and give them some data and methods.
Both students and faculty are types of people, so we'll make use of this people class when we address them directly.

"""

import datetime

class Person(object):

	def __init__(self, name):
		"""Create a person"""
		self.name = name
		try:
			lastBlank = name.rindex(' ')
				# returns the location of the last string matching contents of ()
				# if doesn't exist, returns 0 (the first index spot)
			self.lastName = name[lastBlank+1:]
		except:
			self.lastName = name
		self.birthday = None

	def getName(self):
		"""Returns self's full name"""
		return self.name

	def getLastName(self):
		"""Returns self's last name"""
		return self.lastName

	def setBirthday(self, birthdate):
		"""Assumes birthdate is of type datetime.date
			Sets self's birthday to birthdate"""
		self.birthday = birthdate

	def getAge(self):
		"""Returns self's current age in days"""
		if self.birthday == None:
			raise ValueError
		#	return (datetime.date.today() - self.birthday).days
		return (datetime.date.today() - self.birthday).days

	# This is an example of overloading the < operator
	# We are requiring specific behavior of the < operator
	# By Python rules(?), the overload applies if the first term is type Person
	# The syntax __XX__ means we're overloading existing method XX
	"""Awesome thing: any polymorphic method that relies on the < operator will
	automatically use our specially defined __lt__ rather than the base lt.
	Remember: polymorphic methods can take arguments of different data type
	Example: sort will now work on a list of people in the way specified below"""

	def __lt__(self, other):
		"""Returns True if self's name is lexicographically less than 
			other's name, and False otherwise"""
		if self.lastName == other.lastName:
			return self.name < other.name
		return self.lastName < other.lastName

	def __str__(self):
		return self.name


"""
me = Person('Ryan Luck')
# We have to look to the __init__ function to see what to pass Person

him = Person('Barack Hussein Obama')
her = Person('Madonna')
hiswife = Person('Michelle Obama')

# print him.getLastName()
# print her.getLastName()
him.setBirthday(datetime.date(1961, 8, 4))
her.setBirthday(datetime.date(1958,8,16))
# print him.getName(), 'is', him.getAge(), 'days old'

pList = [me, him, her, hiswife]
for p in pList:
	print p
print "\n" + "now sorted: " + "\n"
pList.sort()	#	Applies to pList in-place
for p in pList:
	print p
"""


"""8.2 - Inheritance allows programmers to create type hierarchies - 
children types will inherit methods from their parent types"""

class MITPerson(Person):
	"""MIT Person is a subclass of Person
		It inherits the attributes of its superclass, Person.
		It can create new methods, such as getIdNum
		As well as override methods created in Person, such as __init__ and __lt__
	"""

	nextIdNum = 0	#identification number

	def __init__(self, name):
		Person.__init__(self, name)		 
			# We're using Person's __init__ method
		self.idNum = MITPerson.nextIdNum
			# MITPerson objects will have idNum instance variable while Person objects won't
			# This object's IdNum is set to the value of a class variable that is tracked internally to the class exclusively
			# This class variable is NOT tracked or affected by instances of the class.
		MITPerson.nextIdNum += 1 		 
			# We iterate the calss variable

	def getIdNum(self):
		return self.idNum

	# We'll use this method below.
	# Template: isinstance(<object>, <data type>)
	def isStudent(self):
		return isinstance(self, Student)

	def __lt__(self, other):	
			# Overlaods the < operator to apply to ID number for objects of MIT Person
		return self.idNum < other.idNum

"""
p1 = MITPerson('Barbara Beaver')
print p1.getIdNum()	#	A method from our MITPerson class
print str(p1) + '\'s id number is ' + str(p1.getIdNum()) + ' and name is ' + p1.getName()	
	#	A method from MITPerson's superclass, Person!
'''

'''
p1 = MITPerson('Richard Feynman')
p2 = MITPerson('Billy Bob Beaver')
p3 = MITPerson('Billy Bob Beaver')
p4 = Person('Billy Bob Beaver')

print 'p1 < p2 = ', p1 < p2 # MIT Person < MIT Person, so compares idNum
print 'p3 < p2 = ', p3 < p2 # MIT Person < MIT Person, so compares idNum
print 'p4 < p1 = ', p4 < p1 # Person < MIT Person, so compared strings
#	print 'p1 < p4 = ', p1 < p4 # MIT Person < Person, so compares IdNum but p4 has no idNum so error!!
"""

class Student(MITPerson):
	pass

class UG(Student):
	def __init__(self, name, classYear):
		MITPerson.__init__(self, name)
		self.year = classYear
	def getClass(self):
		return self.year

class Grad(Student):
	pass

class TransferStudent(Student):
	def __init__(self, name, fromSchool):
		MITPerson.__init__(self, name)
		self.fromSchool = fromSchool

	def getOldSchool(self):
		return self.fromSchool

# Student and Grad are intermediate types.
"""
p5 = Grad('Buzz Aldrin')
p6 = UG('Billy Beaver', 1984)
p7 = TransferStudent('Helen Wang', 'Vassar')

print p5, 'is a graduate student is', type(p5) == Grad
print p5, 'is an undergraduate student is', type(p5) == UG
print p5, 'is a student is', p5.isStudent()
print p6, 'is a student is', p6.isStudent()
print p3, 'is a student is', p3.isStudent()
print p7, 'is a transfer student from ', p7.getOldSchool()
print type(p6)
"""

class Grades(object):
	"""A mapping from students to a list of grades"""
	def __init__(self):
		"""Create empty grade book object"""
		self.students = []	 # A list
		self.grades = {}	 # A dicionary
		self.isSorted = True # This isSorted flag will get flipped as needed

	def addStudent(self, student):
		"""Assumes: student is of type Student
			Add student to the grade book"""
		if student in self.students:
			raise ValueError('Duplicate student')
		self.students.append(student)
		self.grades[student.getIdNum()] = []	#	Maps student id num to grades
		self.isSorted = False

	def addGrade(self, student, grade):
		"""Assumes: grade is a float
			Add grade to the list of grades for student"""
		try:
			self.grades[student.getIdNum()].append(grade)
		except:
			raise ValueError('Student not in grade book')

	def getGrades(self, student):
		"Returns a list of grades for student"""
		try:
			return self.grades[student.getIdNum()][:] 
								# Returns a copy of student's grades
		except:
			raise ValueError('Student not in grade book')

	#	This implementation of getStudents returns an entire list of n attributes
	def InefficientgetStudents(self):
		"""Return a list of the students in the grade book"""
		if not self.isSorted:
			self.students.sort()
			self.isSorted = True
		return self.students[:] # Returns copy of list of students
	
	"""	
		This implementation of getStudents returns a single student at a time
		Note the yield statement -- it defines a generator.
		yield will initially return the first value it encounters.
		
		When getStudents is called again, it returns the next loop iteration 
		where the yield is contained.

		The final yield is equivalent to a return
	"""
	def getStudents(self):
		"""Return the students in the grade book one at a time"""
		if not self.isSorted:
			self.students.sort()
			self.isSorted = True
		for s in self.students:
			yield s

#	allStudents = course1.getStudents()
#	allStudents.extend(course2.getStudents())

def gradeReport(course):
	"""Assumes course is of type Grades"""
	report = ''
	for s in course.getStudents():
		tot = 0.0	#	The cumulative sum of all grades received
		numGrades = 0
	
		for g in course.getGrades(s):
			tot += g
			numGrades += 1
		try:
			average = tot / numGrades
			report = report + '\n' + str(s) + '\'s mean grade is ' + str(average)
		except ZeroDivisionError:
			report = report + '\n' + str(s) + ' has no grades'
	return report

ug1 = UG('Harriet Doe', 2014)
ug2 = UG('John Doe', 2015)
ug3 = UG('David Henry', 2003)

g1 = Grad('Billy Buckner')
g2 = Grad('Bucky F. Dent')

sixHundred = Grades()
sixHundred.addStudent(ug1)
sixHundred.addStudent(ug2)
sixHundred.addStudent(g1)
sixHundred.addStudent(g2)

for s in sixHundred.getStudents():
	sixHundred.addGrade(s, 75)

sixHundred.addGrade(g1, 25)
sixHundred.addGrade(g2, 100)
sixHundred.addStudent(ug3)
print gradeReport(sixHundred)

# 8.3.1 - Generators
""" See the information on generators & yield above
Using generators, we can iterate over elements of our home made types just like lists """

book = Grades()
book.addStudent(Grad('Julie'))
book.addStudent(Grad('Charlie'))
for s in book.getStudents():
	print s

'''

# 8.4 - Mortgages Example
""" Build a program that examines the costs of three kinds of loans:
- A fixed-rate mortgage with no points
- A fixed-rate mortgage with points (1 point = 1% of the initial coast of the loan)
- A mortgage with an initial teaser rate followed by a higher rate for the duration

Structure:
A Mortgage class that includes properties shared by all mortgage types
Classes for each of the types of mortgages -- perhaps fixed rate with points a subclass of fixed rate
"""

def findPayment(r, principal, m):
	"""Assumes: principal and interest rate are floats
	Returns the monthly payment for a mortgage of size principal at a monthly rate of r for m months
	"""
	return principal*((r*(1+r)**m)/((1+r)**m - 1))

class Mortgage(object):

	def __init__(self, annInterestRate, principal, months):
		# We need to pass the initial cost and interest rate of the mortgage
		self.interestRate = annInterestRate/12	# the Monthly interest rate in this case
		self.principal = principal
		self.months = months
		
		self.monthlyPayment = findPayment(self.interestRate, principal, months)	# Do functions in the __init__ need to be globally?
		self.paid = [0.0]	#	Keep track of paid & owed in a list month-by-month
		self.owed = [principal]

		self.mortgageType = None # this class does not assume the mortgage type.
	# Remember that you don't need to return anything from the def __init__

	def getMonthlyPayment(self):
		return self.monthlyPayment

	def getMortgageType(self):
		return self.mortgageType

	def makePayment(self):	
		self.paid.append(self.monthlyPayment)	#	Tracks the amount paid each month
		#	reduction = self.monthlyPayment - self.owed[-1]*self.rate

		self.owed.append(self.owed[-1]*(1+self.interestRate)-self.monthlyPayment)
		# Each month we owe whatever was owed last month plus the interest, minus our last payment.
		"""
		Why is there no return statement in this method?  Because its only purpose
		is to be iterated over and change the value of self.paid and self.owed for
		instances of the class.  It affects instance variables directly.
		"""


	def getTotalPaid(self):
		"""Return the total amount paid so far"""
		return sum(self.paid)	#	sum() is a built-in python function.

	def __str__(self):
		return self.mortgageType

#	For a fixed mortgage, we don't need to change anything from the default in the Mortgage
#	We just need to set the type to "Fixed"
class Fixed(Mortgage):
	def __init__(self, annInterestRate, principal, months): # Grr remember __init__ is a method
		Mortgage.__init__(self, annInterestRate, principal, months)
		self.mortgageType = 'Fixed, ' + str(annInterestRate*100) + '%'

#	For fixed with points, we pay a fraction of the initial loan principal up front
class FixedWithPts(Mortgage):
	def __init__(self, annInterestRate, principal, months, points):
		Mortgage.__init__(self, annInterestRate, principal, months)
		self.points = points
		self.paid = [principal*points/100.0]	# This will be the first amount paid in our list
		self.mortgageType = 'Fixed, ' + str(annInterestRate*100) + '%, ' + str(points) + ' points'

class TwoRate(Mortgage):
	def __init__(self, annInterestRate, principal, months, teaserRate, teaserMonths):
		Mortgage.__init__(self, teaserRate, principal, months)	#	Initialize with the teaser rate!
		self.teaserMonths = teaserMonths
		self.teaserRate = teaserRate
		self.nextRate = annInterestRate/12
		self.mortgageType = str(teaserRate*100) + '% for ' + str(self.teaserMonths) + ' months, '\
			' then ' + str(annInterestRate*100) + '%'

	def makePayment(self):	#	Payments will be different after the teaserMonths
		if len(self.paid) == self.teaserMonths + 1:
		# When we hit the teaser month, reset the payments.  Recall that payments are
		# calculated only upon call to findPayment and then are used
		# We have paid months equal to the # of teaser months, keeping in mind
		# keeping in mind self.paid starts with 0.0 so has len(1) at month 0, so we'll need
		# to add 1 to self.teaserMonths to do the comparison
			self.interestRate = self.nextRate
			self.monthlyPayment = findPayment(self.interestRate, self.owed[-1], self.months - self.teaserMonths)
			# Calculate the new payment
		Mortgage.makePayment(self)


def compareMortgage(amt, years, fixedRate, pts, ptsRate, varRate1, varRate2, varMonths):
	totMonths = years*12
	fixed1 = Fixed(fixedRate, amt, totMonths)
	fixed2 = FixedWithPts(ptsRate, amt, totMonths, pts)
	twoRate = TwoRate(varRate2, amt, totMonths, varRate1, varMonths)
	morts = [fixed1, fixed2, twoRate]

	#	Make all of the payments
	for m in range(totMonths):
		for mort in morts:
			mort.makePayment()

	#   Determine the amount paid for each type
	for m in morts:
		print m
		print ' Total payments = $' + str(int(m.getTotalPaid()))


amt = 2*(10**5)
years = 30
fixedRate = 0.07

pts = 3.25
ptsRate = 0.05
varRate1 = 0.045
varRate2 = 0.095
varMonths = 12*4


compareMortgage(amt = amt, years = years, fixedRate = fixedRate, pts = pts, ptsRate = ptsRate,
	varRate1 = varRate1, varRate2 = varRate2, varMonths = varMonths)

print "\n\n\n"

myMortgage = Fixed(fixedRate, amt, years*12)
print 'You now have a ' , myMortgage.getMortgageType()
print 'Your monthly payment is: ' , myMortgage.getMonthlyPayment()

for i in range(years*12):
	myMortgage.makePayment()

print 'Your total paid amount for this loan was: ', myMortgage.getTotalPaid()	#	Don't forget the parentheses duh


myMortgageWithPoints = FixedWithPts(ptsRate, amt, years*12, pts)
print 'You now have a ' , myMortgageWithPoints.getMortgageType()
print 'Your monthly payment is: ' , myMortgageWithPoints.getMonthlyPayment()

for i in range(years*12):
	myMortgageWithPoints.makePayment()

print 'Your total paid amount for this loan was: ', myMortgageWithPoints.getTotalPaid()	#	Don't forget the parentheses duh


myCrappyMortgage = TwoRate(varRate2, amt, years*12, varRate1, varMonths)
print 'You now have a ' , myCrappyMortgage.getMortgageType()
print 'Your initial monthly payment is: ', myCrappyMortgage.getMonthlyPayment()


for i in range(varMonths):
	myCrappyMortgage.makePayment()
print 'After ', varMonths, ' months your payment is ', myCrappyMortgage.getTotalPaid()

for i in range(years*12-varMonths):
	myCrappyMortgage.makePayment()
print 'After ', years*12, ' months you have paid ', myCrappyMortgage.getTotalPaid()











