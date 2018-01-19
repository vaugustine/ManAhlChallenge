import copy
import random

class RandomGen():
	"""
	Given a list of numbers and associated probabilities,
	returns a random number from the list of numbers in 
	agreement with the input probabilities.
	"""
	# value that may be returned by nextNum()
	_random_nums = []
	# probability of the occurence of random_nums
	_probabilities = []
	# cumilative probability
	_cum_probabilities = []

	def __init__(self,random_nums,probabilities):
		"""Initialize the variables"""
		self.random_nums = random_nums
		self.probabilities = probabilities
		# perform additional validations on random_nums and probabilities
		self.performValidations()
		self._cum_probabilities = copy.deepcopy(probabilities)
		for i in range(1, len(self._cum_probabilities)):
			self._cum_probabilities[i] += self._cum_probabilities[i-1]

	@property
	def random_nums(self):
		"""Return _random_nums."""
		return self._random_nums

	@random_nums.setter
	def random_nums(self,r):
		"""Validates random_nums and sets the property."""
		if not r or not isinstance(r,list):
			raise ValueError("Random Numbers have to be a non empty list")
		if not all(isinstance(num,int) for num in r):
			raise ValueError("Random Numbers have to be integers")
		self._random_nums = r

	@property
	def probabilities(self):
		"""Return _probabilities."""
		return self._probabilities

	@probabilities.setter
	def probabilities(self,p):
		"""Validates probabilities and sets the property."""
		if not p or not isinstance(p,list):
			raise ValueError("Probabilities have to be a non empty list")
		if not all(isinstance(num,(int,float)) for num in p):
			raise ValueError("Probablilities have to be real numbers")
		if not all(0 <= num <=1 for num in p):
			raise ValueError("Probablilities have to be between 0 and 1")
		if round(sum(p),5) != 1:
			raise ValueError("Sum of all Probablilities have to be 1")
		self._probabilities = p

	def performValidations(self):
		"""
		Perform additonal validations on the input lists.
		* check if both input lists are of same size
		"""
		if len(self.random_nums) != len(self.probabilities):
			raise ValueError("Random numbers and Probablilities must be the same size")

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