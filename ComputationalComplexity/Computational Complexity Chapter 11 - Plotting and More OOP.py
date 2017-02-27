# Chapter 11 - Plotting and More About Classes

# PyLab
# Plotting
# Arrays

##################################################################################
# 11.1 - Plotting using PyLab
# A MatLab substitute - see matplotlib.sourceforge.net/users/index.html

import pylab


############# 11.1.1 - First plot
"""
pylab.figure(1) 					# create figure 1
pylab.plot([1,2,3,4], [1,7,3,5]) 	# draw on figure 1
# Two parameters of the same length.  They are the x coordinates and the matching y coordinates of a plot.
pylab.show() #  show figure on screen.  We could have also chosen to have written it to a file for example
"""


############# 11.1.2 - Two plots at once.  Writing to files.
"""
pylab.figure(1) # create figure 1
pylab.plot([1,2,3,4], [1,2,3,4])	# draw on figure 1

pylab.figure(2)	# create figure 2
pylab.plot([1,4,2,3], [5,6,7,8])	# draw on figure 2
pylab.savefig('Figure-Addie')	#save figure 2

pylab.figure(1)	# go back to working on figure 1
pylab.plot([5,6,10,3])	# draw again on figure 1
# If only 1 set of parameters are passed then those are the y values.  
# The default X values are range(len[5,6,10,3]), or range(4) to values (0,1,2,3)

pylab.savefig('Figure-Jane')	#save figure 1

####################################################
"""


############# 11.1.3 - Enriching plots with labels and plot types
'''
print "hello"
pylab.figure(1)
principal = 10000	# initial investment
interestRate = 0.05
years = 20
values = []
for i in range(years + 1):
	values.append(principal)
	principal += principal*interestRate
#	pylab.plot(values, 'ro')
pylab.plot(values,  linewidth = 30)
# The second parameter of plot is optional and is a format string that mimic's Matlab's
# The default second parameter is 'b-' which means, for some reason, a solid blue line
# 'ro' means 'red' and 'dots'

pylab.title("5% Growth, Compounded Annually", fontsize = 'xx-large')
pylab.xlabel('Years of Compounding', fontsize = 'x-small')
pylab.ylabel('Value of Principal ($)')
# Additional parameters are optional but always should be called with keyword arguments

pylab.show()

"""
To totally fuck with Python's defaults check out the dictionary-like variable pylab.rcParams
But you should probably not be using python's default renderer unless you're desperate.
"""
'''

##################################################################################
############# 11.2 - Plotting mortgages - an extended example


#############
# 11.2.1 - Arrays Digression
# In NumPy, simple expressions involving array & scalar multiplication can be used
# that matches traditional vector mathematics.

a1 = pylab.array([1,2,4])
print 'a1 = ', a1
a2 = a1*2
print 'a2 = ', a2
print 'a1 + 3 =', a1 + 3
print '3 - a1 = ', 3 - a1
print 'a1 - a2 = ', a1 - a2
print 'a1*a2 = ', a1*a2	# Term-by-term multiplication rather than the dot product
print pylab.array([1]*len(a2))	# Putting a scalar in the brackets leads to repitition

#	exit()
# The easiest way to create an array is to create a list and then convert it to an array.



def findPayment(principal, r, m):
	"""Assumes: principal and interest rate are floats
	Returns the monthly payment for a mortgage of size principal at a monthly rate of r for m months
	"""
			#	print principal, r, m
			#	exit()
	return principal*((r*(1+r)**m)/((1+r)**m - 1))

class Mortgage(object):
	"""Abstract class for building different kinds of mortgages"""

	def __init__(self, loan, annRate, months):
		"""Create a new mortgage"""
		self.loan = loan
		self.rate = annRate/12.0
		self.months = months
		self.paid = [0.0]
		self.owed = [loan]
		self.payment = findPayment(loan, self.rate, months)
		self.legend = None #description of mortgage to be used in plot

	def makePayment(self):
		"""Make a payment"""
		self.paid.append(self.payment)
		reduction = self.payment - self.owed[-1]*self.rate
			# amount reduced is equal to the payment less the interest rate based on last month's owed
		self.owed.append(self.owed[-1] - reduction)
			# new amount owed is the last amount owned less the reduction

	def getTotalPaid(self):
		"""Return the total amount paid so far"""
		return sum(self.paid)

	def __str__(self):
		return self.legend

	def plotPayments(self, style):
		pylab.plot(self.paid[1:], style, label = self.legend)
		# Show each payment from the 1st payment onwards (0th payment is initialized to $0)

	def plotBalance(self, style):
		pylab.plot(self.owed, style, label = self.legend)

	def plotTotPd(self, style):
		"""Plot the cumulative total of the payments made. Will only be called once."""
		totPd = [self.paid[0]]
		for i in range(1, len(self.paid)):
			totPd.append(totPd[-1] + self.paid[i])
		pylab.plot(totPd, style, label = self.legend)

	def plotNet(self, style):
		"""Plot an approximation to the total cost of the mortgage over time by plotting the cash
		expended minus the equity acquired by paying off part of the loan"""
		totPd = [self.paid[0]]
		for i in range(1, len(self.paid)):
			totPd.append(totPd[-1] + self.paid[i])
		
		#Equity acquired through payments is amount of original loan
		# paid to date, which is amount of loan minus what is still owed
		equityAcquired = pylab.array([self.loan]*len(self.owed))
			#print [self.loan]
			#print equityAcquired
		# self.loan is a scalar. In brackets is a list. Passing scalar list * num to pylab.array()
		# gives an array that expands the list to repeat the scalar value num times.
		equityAcquired = equityAcquired - pylab.array(self.owed)
		net = pylab.array(totPd) - equityAcquired
		pylab.plot(net, style, label = self.legend)

class Fixed(Mortgage):
	def __init__(self, loan, r, months):
		Mortgage.__init__(self, loan, r, months)
			# Uses the same init as Mortgage without adding new anything
		self.legend = 'Fixed, ' + str(r*100) + '%'

class FixedWithPts(Mortgage):
	def __init__(self, loan, r, months, pts):
		Mortgage.__init__(self, loan, r, months)	# Uses Mortgage's init
		self.pts = pts 	# ... and then adds this paramter which isn't present in Mortgage's __init__
		self.paid = [loan*(pts/100.0)]
		self.legend = 'Fixed, ' + str(r*100) + '%, '  + str(pts) + ' points'

class TwoRate(Mortgage):
	def __init__(self, loan, r, months, teaserRate, teaserMonths):
		Mortgage.__init__(self, loan, teaserRate, months)
		self.teaserMonths = teaserMonths
		self.teaserRate = teaserRate
		self.nextRate = r/12.0
		self.legend = str(teaserRate*100) + '% for ' + str(self.teaserMonths)\
			+ ' months, then ' + str(r*100) + '%'

	def makePayment(self):
		if len(self.paid) == self.teaserMonths + 1:
			self.rate = self.nextRate
			self.payment = findPayment(self.owed[-1], self.rate, self.months - self.teaserMonths)
		Mortgage.makePayment(self)

def plotMortgages(morts, amt):
	styles = ['b-','b-.','b:']
	#Give names to figure numbers
	payments = 0
	cost = 1
	balance = 2
	netCost = 3

	#Figure for the pyaments
	pylab.figure(payments)
	pylab.title('Monthly Payments of Different $' + str(amt) + ' Mortgages')
	pylab.xlabel('Months')
	pylab.ylabel('Monthly Payments')

	#Figure for the costs
	pylab.figure(cost)
	pylab.title('Cash Outlay of Different $' + str(amt) + ' Mortgages')
	pylab.xlabel('Months')
	pylab.ylabel('Total Payments')

	#Figure for balances
	pylab.figure(balance)
	pylab.title('Balance of Remaining of $' + str(amt) + ' Mortgages')
	pylab.xlabel('Months')
	pylab.ylabel('Remaining Loan Balance of $')

	#Figure for net cost
	pylab.figure(netCost)
	pylab.title('Net Cost of $' + str(amt) + ' Mortgages')
	pylab.xlabel('Months')
	pylab.ylabel('Payment - Equity $')

	# Loop through the mortgage types we're comparing
	# Finally call those plotting method in Mortgage class above
	for i in range(len(morts)):
		pylab.figure(payments)
		morts[i].plotPayments(styles[i])
		
		pylab.figure(cost)
		morts[i].plotTotPd(styles[i])

		pylab.figure(balance)
		morts[i].plotBalance(styles[i])

		pylab.figure(netCost)
		morts[i].plotNet(styles[i])

	pylab.figure(payments)
	pylab.legend(loc = 'upper center')

	pylab.figure(cost)
	pylab.legend(loc = 'best')

	pylab.figure(balance)
	pylab.legend(loc = 'best')

	pylab.show()

def compareMortgages(amt, years, fixedRate, pts, ptsRate, varRate1, varRate2, varMonths):
	totMonths = years*12
	
	# Instantiate members of each type of mortgage
	fixed1 = Fixed(amt, fixedRate, totMonths)
	fixed2 = FixedWithPts(amt, ptsRate, totMonths, pts)
	twoRate = TwoRate(amt, varRate2, totMonths, varRate1, varMonths)

	# Create a list of those mortgage types
	morts = [fixed1, fixed2, twoRate]

	for m in range(totMonths):	# cycle through each month
		for mort in morts:		# make a payment for each mortgage in that month
			mort.makePayment()

	plotMortgages(morts, amt)
	

loan = 2*10**5
years = 30

fixedRate = 7.0/100.0

pts = 3.25
ptsRate = 5.0/100.0

varRate1 = 4.5/100.0
varRate2 = 9.5/100.0
varMonths = 12*4

compareMortgages(loan, years, fixedRate, pts, ptsRate, varRate1, varRate2, varMonths)














