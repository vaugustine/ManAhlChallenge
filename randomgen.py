#! /usr/local/bin/python3

import copy
import random

class RandomGen:
	""" """
	# value that may be returned by nextNum()
	_random_nums = []
	# probability of the occurence of random_nums
	_probabilities = []
	# cumilative probability
	_cum_probabilities = []

	def __init__(self,random_nums,probabilities):
		""" """
		self._random_nums = random_nums
		self._probabilities = copy.deepcopy(probabilities)
		self._cum_probabilities = copy.deepcopy(probabilities)
		for i in range(1, len(self._cum_probabilities)):
			self._cum_probabilities[i] += self._cum_probabilities[i-1]

	def nextNum(self):
		"""
		Returns one of the randomNums. When this method is called
		multiple times over a long period, it should return the
		numbers roughly with the initialized probabilities.
		"""
		randomNum = random.random()
		for i in range(len(self._cum_probabilities)):
			if randomNum < self._cum_probabilities[i]:
				break
		return self._random_nums[i]

if __name__ == '__main__':

	results = {'1':0,'2':0,'3':0,'4':0,'5':0}
	randomGenerator = RandomGen([1,2,3,4,5], [0.01,0.3,0.58,0.1,0.01])
	for i in range(100):
		nextNumber = randomGenerator.nextNum()
		results[str(nextNumber)]+=1
	print (results)