import unittest
from pearhash import PearsonHasher



class TestPearsonHasher(unittest.TestCase):

	def test_table_is_a_permutation_of_range_256(self):
		hasher = PearsonHasher(2)
		self.assertEqual(set(hasher.table), set(range(256)))
