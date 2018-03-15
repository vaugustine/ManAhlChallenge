import unittest

from randomgen import RandomGen


class TestRandomGen(unittest.TestCase):
	"""Tests for randomgen.py."""
	def setup(self):
		pass

	def teardown(self):
		pass

	def test_not_list(self):
		"""Test if a value error is raised if non-list types are passed to RandomGen."""
		self.assertRaises(ValueError,RandomGen,'random_num','probabilities')

	def test_Eempty_list(self):
		"""Test if a value error is raised if empty lists are passed to RandomGen"""
		self.assertRaises(ValueError,RandomGen,[],[])

	def test_randomNum_notInt(self):
		"""Test if a value error is raised when non-int value is passed to random_nums."""
		self.assertRaises(ValueError,RandomGen,[0.1,2,3,4],[0.1,0.2,0.3,0.4])

	def test_probabilities_notNumbers(self):
		"""Test if a value error is raised when a non-number is passed to probabilities"""
		self.assertRaises(ValueError,RandomGen,[1,2,3,4],[0.1,0.2,0.3,'0.4'])

	def test_probabilities_outOfRange1(self):
		"""Test if a value error is raised when a number greater than 1 is passed to probabilities"""
		self.assertRaises(ValueError,RandomGen,[1,2,3,4],[0.1,0.2,0.3,1.4])

	def test_probabilities_outOfRange2(self):
		"""Test if a value error is raised when a negative number is passed to probabilities"""
		self.assertRaises(ValueError,RandomGen,[1,2,3,4],[-0.1,0.2,0.3,0.4])

	def test_probabilities_invalidSum1(self):
		"""Test if a value error is raised when the sum of probabilities is greater than 1"""
		self.assertRaises(ValueError,RandomGen,[1,2,3,4,5],[0.1,0.2,0.3,0.4,0.5])

	def test_probabilities_invalidSum2(self):
		"""Test if a value error is raised when the sum of probabilities is less than 1"""
		self.assertRaises(ValueError,RandomGen,[1,2,3],[0.1,0.2,0.3])

	def test_differentSize_list(self):
		"""
		Test if a value error is raised when random_nums and
		probabilities lists are of different size
		"""
		self.assertRaises(ValueError,RandomGen,[1,2,3,4,5],[0.1,0.2,0.3,0.4])

	def test_probability_zero(self):
		""" Test if a random_num with 0 probability is never returned."""
		randomGenerator = RandomGen([1,2,3,4,5],[0,0.2,0.3,0,0.5])
		for i in range(100):
			nextNumber = randomGenerator.nextNum()
			self.assertTrue(nextNumber not in (1,4))

	def test_probability_one(self):
		"""Test if a random_num with probability 1 is always returned."""
		randomGenerator = RandomGen([1,2,3,4,5],[0,0,1,0,0])
		for i in range(100):
			nextNumber = randomGenerator.nextNum()
			self.assertEqual(nextNumber,3)

	def test_value_returned(self):
		"""Test if nextNum always returns a number from random_nums."""
		randomGenerator = RandomGen([1,2,3,4],[0.1,0.2,0.3,0.4])
		for i in range(100):
			nextNumber = randomGenerator.nextNum()
			self.assertTrue(nextNumber in (1,2,3,4))

	def test_value_returned_probability(self):
		"""
		Test if nextNum always returns a number from random_nums 
		in accordance with the input probability
		"""
		random_nums = [1,2,3,4]
		inputProbabilities = [0.1,0.2,0.3,0.4]
		# high number of tries to reduce the deviation in probability
		numOfTries = 10000
		errorThreshold = 0.01
		randomGenerator = RandomGen(random_nums,inputProbabilities)
		numbersReturned = {num:0 for num in random_nums}
		for i in range(numOfTries):
			numbersReturned[randomGenerator.nextNum()] += 1
		outputProbabilities = [(value/numOfTries) for value in numbersReturned.values()]
		differenceInProbabilities = [abs(i - j) for i,j in zip(inputProbabilities,outputProbabilities)]
		self.assertTrue(i < errorThreshold for i in differenceInProbabilities)

if __name__ == '__main__':
    unittest.main()