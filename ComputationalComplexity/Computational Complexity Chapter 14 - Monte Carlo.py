#	Computational Complexity Chapter 14 - Monte Carlo Simulation

# 14.1 --- Roll a certain number of dice a certain number of times seeking a particular value for the dice.

'''
Topics:
Going from abstract definition of a scenario to an object oriented implementation
Realizing that objects can track their own internal variables and counters
Seeing the importance of the law of large numbers in the long run behavior of a chance outcome
'''

'''

import random
#	import sys, traceback
from inspect import currentframe, getframeinfo


class Dice(object):
	"""Create a di with a certain number of sides"""
	def __init__(self, sides):
		sideValues = []
		self.sides = sides
		for i in range(self.sides):
			sideValues.append(i+1)
		self.sideValues = sideValues

	def rollDi(self):
		"""Rolls the di"""
		return int(random.choice(self.sideValues))

	def __str__(self):
		return str(self.sides)


def makeDice(numSides, numDice):
	"""Creates dice with the specified number of sides"""
	diceSet = []
	for i in range(numDice):
		diceSet.append(Dice(numSides))
	return diceSet

def boolRolledDesiredValue(rollValues, targetValues):
	"""targetValues is a list of rolls.  rollValues is a list of rolls.
	returns True if they are the same rolls regardless of order."""
	#	print rollValues
	#	print targetValues

	#	Sort the target values so roll order doesn't matter.
	targetValues.sort()

	for i in rollValues:
		#	print "unsorted: " + str(i)

		#	Note that the sort must be run before the Boolean comparison
		i.sort()
		#	print "sorted: " + str(i)
		if i == targetValues:
			return True

	"""
	frameinfo = getframeinfo(currentframe())
	print frameinfo.filename, frameinfo.lineno
	"""

	return False

def rollDice(diceSet):
	"""Use this if we're rolling more than 1 di at a time and want to compare the output of all the roles"""
	rollValues = []

	for thisDi in  diceSet:
		#	print i
		rollValues.append(thisDi.rollDi())

	return rollValues

def checkPascal(diceSet, numRolls, numTrials, targetValues):
	"""Uses roll Dice and hitTarget to see if we hit the target in the specified number of trials"""
	diValues = []
	rollValues = []
	numSuccessful = 0

	for trial in range(numTrials):
		#	print "*** Trial # " + str(trial) + " ... "
		for i in range(numRolls):
			for thisDi in  diceSet:
			#	Roll each di in our dice set
			#	Record the value of each roll
				diValues.append(thisDi.rollDi())
			#	Record the collective dice roll
			rollValues.append(diValues)
			#	Reset the individual dice roll variable in preparation for our next roll of the dice
			diValues = []
		if boolRolledDesiredValue(rollValues, targetValues) == True:
			#	print "Success, rolled " + str(targetValues) + "!!!"
			numSuccessful = numSuccessful + 1
		#	else:
			#	print "Failure, did not roll " + str(targetValues) + " :-("

		#	Reset our track of the total roll results in preparation for the next trial
		rollValues = []

	return numSuccessful


numSidesDefault = 6
numDiceDefault = 2
numRollsDefault = 24
numTrialsDefault = 10**5

numSides = raw_input("How many sides on your di [default is " + str(numSidesDefault) + "]? ") or numSidesDefault
numSides = int(numSides)

numDice = raw_input("How many dice with " + str(numSides) + " sides [default is " + str(numDiceDefault) + "]? ") or numDiceDefault
numDice = int(numDice)

numRolls = raw_input("In many rolls do you want to see if you hit your target value [default is " + str(numRollsDefault) + "]? ") or numRollsDefault
numRolls = int(numRolls)


numTrials = raw_input("How many trials of this experiment to do want to run [default is " + "{:.2e}".format(numTrialsDefault) + "]?") or numTrialsDefault
numTrials = int(numTrials)

targetValues = [6,6]
#	numTrials = 1
print "Our roll target is: " + str(targetValues)

diceSet = makeDice(numSides, numDice)

"""
for i in range(numDice):
	print "Roll value: " + str(diceSet[i].rollDi())
"""

numSuccessful = checkPascal(diceSet, numRolls, numTrials, targetValues)
ratioSuccessful = round((float(numSuccessful) / float(numTrials)) * 100.0,8)
print "Rolled " + str(targetValues) + " in " + str(numSuccessful) + "/" + str(numTrials) + " trials, or " + str(ratioSuccessful) + "% of trials"

'''


#	14.2 - Let's play Craps
# Pass Line bet: wins if first roll is a 7 or 11.  loses if it's 2,3,12.
#	if another number is rolled then shooter must roll that number again before rolling a 7 to win
# Don't Pass Line bet: loses if first roll is 7 or 11.  wins if it's 2,3.  gets to roll again with no consequence if it's 12.
#   if another number is rolled then shooter must roll a 7 before rolling that number again to win
#

import random
from inspect import currentframe, getframeinfo

def stdDev(X):
	"""Assumes that X is a list of numbers.
	Returns the standard deviation of X"""
	mean = float(sum(X))/len(X)
	tot = 0.0
	for x in X:
		tot += (x - mean)**2
	return (tot/len(X))**0.5	# square root of mean squared difference

class Dice(object):
	"""Create a di with a certain number of sides"""
	def __init__(self, sides=6):
		sideValues = []
		self.sides = sides
		for i in range(self.sides):
			sideValues.append(i+1)
		self.sideValues = sideValues

	def rollDi(self):
		"""Rolls the di"""
		return int(random.choice(self.sideValues))

	def __str__(self):
		return str(self.sides)


def makeDice(numSides, numDice):
	"""Creates dice with the specified number of sides"""
	diceSet = []
	for i in range(numDice):
		diceSet.append(Dice(numSides))
	return diceSet


class CrapsGame(Dice):
	def __init__(self):
		numSides = 6
		Dice.__init__(self, numSides)		 #	We want dice for Craps to be able to roll dice 

		#	Each craps game keeps track of its own wins and losses.  We can play more than once per game.
		self.passWins, self.passLosses = (0,0)
		self.dpWins, self.dpLosses, self.dpPushes = (0,0,0)

	def playHand(self):
		PassLineWin = [7,11]
		PassLineLoss = [2,3,12]

		DontPassLineWin = [2, 3]
		DontPassLineLoss = PassLineWin
		DontPassLinePush = [12]

		throw = self.rollDi() + self.rollDi()

		#	Just use the exact rules of Craps as today, don't worry about generalizing the winning numbers
		
		#	Case if we throw one of the special numbers [7,11] or [2,3,12]
		if throw in PassLineWin:
			self.passWins += 1
			self.dpLosses += 1
			#	print str(throw) + " -- The Pass Bet won! and The Don't Pass Bet Lost"
				#	exit()
		elif throw in PassLineLoss:
			self.passLosses += 1
			#	print str(throw) + " -- The Pass Bet lost!"
				#	exit()
			if throw in DontPassLinePush:
				#	print str(throw) + " -- The Don't Pass Bet pushed!"
				self.dpPushes += 1
			else:
				#	print str(throw) + " -- The Don't Pass Bet won!"				
				self.dpWins += 1

		# 	Case if we throw a different number
		else:
			# The "point" is the value that we're trying to roll again, or not, depending on our type of bet
			point = throw
			while True:
				# Throw again
				throw = self.rollDi() + self.rollDi()
				#	If our throw matches the point ...
				if throw == point:
					#	Then in a "pass" setting we've won because we haven't yet hit a 7
					#	print str(throw) + " -- later throw, the Pass Bet won and don't pass bet lost!"
					self.passWins += 1
					#	And in a "don't pass" bet we lose because we haven't yet hit a 7
					self.dpLosses += 1
					#	The game ends when we hit our former role
					break
				elif throw == 7:
					#	If we hit a 7 then we've lost a "pass" because we hit 7 
					#	print str(throw) + " -- later throw, the Pass Bet lost and Don't Pass bet won!"
					self.passLosses += 1
					self.dpWins += 1
					#	The game ends when we hit a 7
					break
				#	In the circumstance our throw doesn't match our point or a 7 then nothing happens and the shooter rolls again
				#	i.e. the loop cycles again

	def passResults(self):
		return(self.passWins, self.passLosses)

	def dpResults(self):
		return(self.dpWins, self.dpLosses, self.dpPushes)

def crapsSim(numHandsPerGame, numGames):

	crapsGamesOutcomes = []
	passWinsPerGame = []
	passLossesPerGame = []
	pROIPerGame = []

	dpWinsPerGame = []
	dpLossesPerGame = []
	dpPushesPerGame = []
	dpROIPerGame = []

	for i in xrange(numGames):
		if i > 0 and (i+1)%(numGames/10) == 0:
			print "Running simulation for game #: " + str(i+1)


		c = CrapsGame()
		for i in xrange(numHandsPerGame):
			c.playHand()
		crapsGamesOutcomes.append(c)


	for g in crapsGamesOutcomes:

		wins, losses = g.passResults()
		passWinsPerGame.append(wins)
		passLossesPerGame.append(losses)

		pROIPerGame.append((wins - losses) / float(numHandsPerGame))

		wins, losses, pushes = g.dpResults()
		dpWinsPerGame.append(wins)
		dpLossesPerGame.append(losses)
		dpPushesPerGame.append(pushes)

		dpROIPerGame.append((wins - losses) / float(numHandsPerGame))

		#	frameinfo = getframeinfo(currentframe())
		#	print frameinfo.filename, frameinfo.lineno
		#	exit()

	meanROI = str(round((100.0*sum(pROIPerGame)/numGames), 4)) + '%'
	sigma = str(round(100.0*stdDev(pROIPerGame), 4)) + '%'

	print 'Pass:' , 'Mean ROI = ', meanROI, 'Std. Dev. = ', sigma

	meanROI = str(round((100.0*sum(dpROIPerGame)/numGames), 4)) + '%'
	sigma = str(round(100.0*stdDev(dpROIPerGame), 4)) + '%'

	print 'Don\'t Pass:' , 'Mean ROI = ', meanROI, 'Std. Dev. = ', sigma

	print "Pass Wins: " + str(sum(passWinsPerGame)) + " and win %: " + str(float((sum(passWinsPerGame))/float(sum(passWinsPerGame+passLossesPerGame))*100))
	print "Pass Losses: " + str(sum(passLossesPerGame)) + " and lose %: " + str(float(sum(passLossesPerGame))/float(sum(passWinsPerGame+passLossesPerGame))*100)
	print "Don't Pass Wins: " + str(sum(dpWinsPerGame)) + " and win %: " + str(float(sum(dpWinsPerGame))/float(sum(dpWinsPerGame+dpLossesPerGame+dpPushesPerGame))*100)
	print "Don't Pass Losses: " + str(sum(dpLossesPerGame)) + " and lose %: " + str(float(sum(dpLossesPerGame))/float(sum(dpWinsPerGame+dpLossesPerGame+dpPushesPerGame))*100)
	print "Don't Pass Pushes: " + str(sum(dpPushesPerGame)) + " and push %: " + str(float(sum(dpPushesPerGame))/float(sum(dpWinsPerGame+dpLossesPerGame+dpPushesPerGame))*100)


#####	Main Body Start

numHandsDefault = 20
numHandsPerGame = raw_input("How many hands of Craps to do want to play today [default is " + str(numHandsDefault) + "]?") or numHandsDefault
numHandsPerGame = int(numHandsPerGame)

#	Here "games" are equivalent to "trials" previously.
numGamesDefault = 1
numGames = raw_input("How many games of " + str(numHandsPerGame) + " hands apiece do you want to play [default is " + str(numGamesDefault) + "]?") or numGamesDefault
numGames = int(numGames)

crapsSim(numHandsPerGame, numGames)




#	numSides = 6
#	numDice = 2
#	diceSet = makeDice(numSides, numDice)





