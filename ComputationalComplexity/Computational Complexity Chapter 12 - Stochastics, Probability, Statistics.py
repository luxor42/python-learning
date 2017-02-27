# Chapter 12 - Stochastic Programs, Probability, and Statistics

'''
Topics:
Randomization - "random" library
Plotting -- "pylab" library
Have to have all parameters that aren't default labeled - error message for that is strange
Histograms can be used to view the distribution of results. 
Simulations of hash tables are pretty simple if you think through them 
'''

###################################################################################################
# 12.1 - Stochastic Programs - The value of X+1 depends on the value of X and some random element
# Main library: random

# 12.1.1 - Rolling a dice
# a stochastic process where the outcome of one event has no influence on the outcome of the other

'''
import random

def rollDie():
	"""Returns a random int between 1 and 6"""
	#	print range(1,6+1)
	return random.choice(range(1,6))

def rollN(n):
	result = ''
	for i in range(n):
		result = result + str(rollDie())
	print result

n = int(raw_input("Enter how many rolls o' the dice: "))
rollN(n)

'''


###################################################################################################
# 12.2 - Inferential Statistics & Simulation
# Inferential statistics is guided by the principal that a random sample tends to exhibit
# representative (i.e. identical up to a scaling factor) properties as the population from which it is drawn

###############################
# 12.2.1 - Coin Flip Trials

'''
import random 
def flip(numFlips):
	heads = 0.0
	for i in range(numFlips):
		if random.random() < 0.5:
			heads += 1
	return heads/numFlips

def flipSim(numFlipsPerTrial, numTrials):
	fracHeads = []
	for i in range(numTrials):
		fracHeads.append(flip(numFlipsPerTrial))
	mean = sum(fracHeads)/len(fracHeads)
	print fracHeads
	return mean
'''

"""
numFlipsPerTrial = int(raw_input("Enter number of flips per trial: "))
numTrials = int(raw_input("Enter number of trials: "))
print "Percent of heads is: ",flipSim(numFlipsPerTrial, numTrials)
"""

###############################
# 12.2.2 - Flip Plot
'''

import pylab
import random

def flipPlot(minExp, maxExp, style):
	"""Assumes minExp and maxExp positive integers; minExp < maxExp
	Plots results of 2**minExp to 2**maxExp coin flips"""

	ratios = []
	diffs = []
	xAxis = []

	# trials will be defined by distinct numbers of flips
	for exp in range(minExp, maxExp + 1):
		xAxis.append(2**exp)

	# calculate a few ratios for each trial
	for numFlips in xAxis:
		numHeads = 0
		for n in range(numFlips):
			if random.random() < 0.5:
				numHeads += 1
		numTails = numFlips - numHeads
		ratios.append(numHeads/float(numTails))
		diffs.append(abs(numHeads - numTails))

	# Plot results

		# Label axes
	pylab.title('Difference Between Heads & Tails')
	pylab.xlabel('Number of Flips')
	pylab.ylabel('Abs(#Heads - #Tails)')
		# Plot the diffs in number of heads & tails as number of flips increases
	pylab.semilogx()
	pylab.semilogy()
	pylab.plot(xAxis, diffs, style)

		# Create a new figure
	pylab.figure()
		# Label axes
	pylab.semilogx()
			#	pylab.semilogy()
	pylab.title('Heads/Tails Ratios')
	pylab.xlabel('Number of Flips')
	pylab.ylabel('#Heads / #Tails')
		# Plot the ratio of heads to tails as number of flips increases
	pylab.plot(xAxis, ratios, style)

	pylab.show()

random.seed(0)
style = 'bo'
#	minExp = int(raw_input("Enter min range of exponential: "))
#	maxExp = int(raw_input("Enter max range of exponential: "))
#	flipPlot(minExp, maxExp, style)

'''

'''
#	Uncomment here to see the full dice-rolling & standard deviation exercise

# Exercise 12.2.3 - Standrad Deviation code, as an exercise

import pylab
import random

def stdDev(X):
	"""Assumes that X is a list of numbers.
	Returns the standard deviation of X"""
	mean = float(sum(X))/len(X)
	tot = 0.0
	for x in X:
		tot += (x - mean)**2
	return (tot/len(X))**0.5	# square root of mean squared difference

def makePlot(xVals, yVals, title, xLabel, yLabel, style, logX = False, logY=False):
	"""Plots xVals v. yVals with supplied title and labels.
	Created as a convenience since we'll be plotting 4 similarly formatted plots.
	"""

	pylab.figure()
	pylab.title(title)
	pylab.xlabel(xLabel)
	pylab.ylabel(yLabel)
	pylab.plot(xVals, yVals, style)
	if logX:
		pylab.semilogx()
	if logY:
		pylab.semilogy()
	#	pylab.show()

def runTrial(numFlips):
	numHeads = 0
	for i in range(numFlips):
		if random.random() < 0.5:
			numHeads += 1
	numTails = numFlips - numHeads
	return (numHeads, numTails)

def flipPlotStdDev(minExp, maxExp, numTrials, style):
	""" Proceeds through flipping coins 2*minExp to 2*maxExp number of flips.
	Repeats each coin flipping a total of numTrials of times
	"""

	ratiosMeans, diffsMeans, ratiosSDs, diffsSDs = [], [], [], []
	ratiosCVs, diffsCVs = [], []
	xAxis = []

	for exp in range(minExp, maxExp + 1):
		xAxis.append(2**exp)
	
	# Cycle through the # of flips
	for numFlips in xAxis:
		ratios = []
		diffs = []
		# Cycle over the number of trials per flip
		
		# Record the heads/tails and (heads - tails) values for each trial
		for t in range(numTrials):
			numHeads, numTails = runTrial(numFlips)
			ratios.append(numHeads/float(numTails))
			diffs.append(abs(numHeads - numTails))
		
		# Calculate summary statistics on each trial's Head v. Tail ratio & diff
		ratiosMeans.append(sum(ratios)/float(numTrials))
		diffsMeans.append(sum(diffs)/float(numTrials))
		ratiosSDs.append(stdDev(ratios))
		diffsSDs.append(stdDev(diffs))
		ratiosCVs.append(CV(ratios))
		diffsCVs.append(CV(diffs))

	# Create plots for each of those 4 values
	numTrialsString = ' (' + str(numTrials) + ' Trials)'
	
	x_label = 'Number of Flips'
	title = 'Mean Heads/Tails Ratios per Num of Flips' + numTrialsString
	makePlot(xAxis, ratiosMeans, title, xLabel = x_label, yLabel = 'Mean Heads/Tails', style=style, logX = True)

	title = 'StdDev Heads/Tails Ratios per Num of Flips' + numTrialsString
	# We use logarithmic for standard deviation because the StdDev of (heads/tails) is expected to decrease
	# as number of trials increases, unlike the ratio of heads to tails
	makePlot(xAxis, ratiosSDs, title, xLabel = x_label, yLabel = 'Standard Deviation', style=style, logX = True, logY = True)

	title = 'Mean abs(#Heads - #Tails)' + numTrialsString
	# We expect the ratio to converge to 1 but the absolute difference grows because total number of trials grows
	makePlot(xAxis, diffsMeans, title, xLabel = x_label, yLabel = 'Mean abs(#Heads - #Tails)', style=style,
	 logX = True, logY = True)

	title = 'SD abs(# Heads - # Tails)' + numTrialsString
	# The standard deviation of abs(Heads - Tails) also grows with flips leads to larger magnitude varations
	makePlot(xAxis, diffsSDs, title, xLabel = x_label, yLabel = 'Standard Deviation', style=style,
	 logX = True, logY = True)
	
	title = 'Coeff. of Var. abs(#Heads - #Tails)' + numTrialsString
	# The coefficient of variation of the absolute difference of heads & tails
	makePlot(xAxis, diffsCVs, title, xLabel = x_label, yLabel = 'Coeff. of Variation',  style=style,
	 logX = True)

	title = 'Coeff. of Var. Heads/Tails Ratio' + numTrialsString
	makePlot(xAxis, ratiosCVs, title, xLabel = x_label, yLabel = 'Coeff. of Variation', style=style,
	 logX = True, logY = True)

	pylab.show()

############################################################
# Exercise 12.2.4 - Coefficient of Variation - calibrates expected increase of standard deviation when expected value itself increases
def CV(X):	# Coefficient of Variation = stdev / mean
	mean = sum(X)/float(len(X))
	try:
		return stdDev(X) / mean
	except ZeroDivisionError:
		return float('nan')


random.seed(0)
style = 'bo'
minExp = int(raw_input("Enter min logarithm value: "))
maxExp = int(raw_input("Enter max logarithm value: "))
numTrials = int(raw_input("Enter number of trials per flip: "))

flipPlotStdDev(minExp, maxExp, numTrials, style)
'''

##############################################################################################
##############################################################################################
# 12.3 - Distributions

# 12.3.0.1 - Histogram using pylab.hist()
'''
import random
import pylab

vals = [1, 200]	#	Establishes and min and max of the set of values.

for i in range(1000):
	num1 = random.choice(range(1, 100))
	num2 = random.choice(range(1, 100))
	vals.append(num1+num2)

pylab.hist(vals, bins=10)
pylab.show()
'''

#	12.3.0.2 - Histogram of the coin flips
#	Modifications of the flip() and flipSim() functions above.

'''
import random 
import pylab

def flip(numFlips):
	heads = 0.0
	for i in range(numFlips):
		if random.random() < 0.5:
			heads += 1
	return heads/numFlips

def flipSim(numFlipsPerTrial, numTrials):
	fracHeads = []
	for i in range(numTrials):
		fracHeads.append(flip(numFlipsPerTrial))
	mean = sum(fracHeads)/len(fracHeads)
	sd = stdDev(fracHeads)
	#	print fracHeads
	return fracHeads, mean, sd

def stdDev(X):
	"""Assumes that X is a list of numbers.
	Returns the standard deviation of X"""
	mean = float(sum(X))/len(X)
	tot = 0.0
	for x in X:
		tot += (x - mean)**2
	return (tot/len(X))**0.5	# square root of mean squared difference


#	This function assigns labels to the plots based on their numerical parameters
def labelPlot(numFlips, numTrials, mean, sd):
	pylab.title(str(numTrials) + ' trials of ' + str(numFlips) + ' flips each')
	
	#X and Y axis labeling is consistent across plots.
	pylab.xlabel('Fraction of Heads')
	pylab.ylabel('Number of Trials')

	# Find the min and max of each axis
	xmin, xmax = pylab.xlim()
	ymin, ymax = pylab.ylim()

	# pylab.text(x coordinate, y coordinate, text, [a few random non-required parameters])
	pylab.text(xmin + (xmax-xmin)*0.02, (ymax-ymin)/2, 
		# These coordinates are "2% of the distance to the right and half way up"
		'Mean = ' + str(round(mean, 4))
		+ '\nSD = ' + str(round(sd, 4)),
		size='x-large')

def makePlots(numFlips1, numFlips2, numTrials):
	val1, mean1, sd1 = flipSim(numFlips1, numTrials)
	pylab.hist(val1, bins = 20)
	xmin, xmax = pylab.xlim()
	ymin, ymax = pylab.ylim()
	labelPlot(numFlips1, numTrials, mean1, sd1)

	pylab.figure()
	val2, mean2, sd2 = flipSim(numFlips2, numTrials)
	pylab.hist(val2, bins = 20)
	pylab.xlim(xmin, xmax)
	labelPlot(numFlips2, numTrials, mean2, sd2)

def showErrorBars(minExp, maxExp, numTrials):
	"""Assumes minExp and maxExp positive ints; minExp < maxExp
		numTrials a positive integer
	Plots mean fraction of heads with error bars"""
	means, sds = [], []
	xVals = []
	for exp in range(minExp, maxExp + 1):
		xVals.append(2**exp)
		fracHeads, mean, sd = flipSim(2**exp, numTrials)
		means.append(mean)
		sds.append(sd)
	pylab.errorbar(xVals, means, yerr=2*pylab.array(sds))
	pylab.semilogx()
	pylab.title('Mean Fraction of Heads (' + str(numTrials) + ' trials)')
	pylab.xlabel('Number of flips per trial')
	pylab.ylabel('Fraction of heads & 95% confidence')

random.seed(0)

#	makePlots(10**2, 10**3, 10**5)
#	See how the error bars, which we set to the standard deviation value, get smaller
minExp = int(raw_input("Enter min x for 2^x flips: "))
maxExp = int(raw_input("Enter max x for 2^x flips: "))
numTrials = int(raw_input("Enter number of trials per flip - e.g. 2^x flips N number of times: "))
showErrorBars(minExp, maxExp, numTrials)
pylab.show() 
'''

###############################################
# 12.3.1 - Distributions

'''
#	Gaussian Distribution
random.gauss(mu, sigma)

#	Uniform Distribution
random.uniform(min, max)

#	Memoryless property of distribution: probability of an event at time t+1 is independent of the event at time t
#	Exponential Distribution
random.expovariate

#	Geometric Distribution - a discrete analog of the exponential distribution
'''

##############################################################################################
##############################################################################################
# 12.4 - p-values, null hypothesis, 

#	Null hypothesis -- result that one would get if the results were determined by chance (no skill involved)

#12.4.1 - What is the likelihood that X trials with chance of occurrence of p yields 
#	I.e. how much better do you have to be than the other team to reliably win the World Series?



#12.4.2:
# For a fixed probability > 0.5, how many trials will it take before we can reject the null hypothesis 95% of the time?
# I.e. how many experiments do we have to run to show that the team that came in with a better record wins 95% of the games?
# I.e. how long should the world series be until we can be sure the better team has won?
# The problem being faced here is that the closer events are to 50/50 the more likely that the less likely event will occur
# We have to run a lot of trials to see that the more likely event occurs significantly more times.



##############################################################################################
##############################################################################################
# 12.5 - Hashing and Collisions

import random

def collisionProb(n, k):
	"""Calculate the actual probability of a collission
	"""
	prob = 1.0
	for i in range(1, k):	#	Range is up to but not including K
		prob = prob * ((n - i)/float(n))	
							# so min value of (n - i) is (n - k - 1)
	return 1 - prob

def simInsertions(numIndices, numInsertions):
	"""Simulate insertions. 
	numIndices is the number of pigeon holes
	and numInsertions is the number of pigeons."""
	choices = range(numIndices)
	used = []
	for i in range(numInsertions):
		hashVal = random.choice(choices)	# Choices from the indices
		if hashVal in used:	#there is a collision
			return 1
		else:
			used.append(hashVal)
	return 0

def findProb(numIndices, numInsertions, numTrials):
	"""Find the actual probability based on the simulation.
	Conduct the simulation for |numTrials|.
	"""
	collisions = 0.00000
	for t in range(numTrials):
		collisions += simInsertions(numIndices, numInsertions)
	return collisions/numTrials

n = int(raw_input("Enter your the number of pigeon holes: "))
K = int(raw_input("Enter the number of pigeons: "))
trials = int(raw_input("Enter the number of simulations: "))

print "The matehamtical chance of a collision is " + str(collisionProb(n, K))
print "The estimated chance of a collision is " + str(findProb(n, K, trials))











