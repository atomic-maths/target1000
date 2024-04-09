import unittest

from grid import Grid

class TestGrid(unittest.TestCase):

	def test_initialise(self):
		""" Test the grid initialises correctly """
		grid = Grid()
		self.assertEqual(grid.number_filled_cells(), 0)

	def verify_total(self, numbers, total):
		grid = Grid()
		for num in numbers:
			grid.fill_next_empty_space(num)
		self.assertEqual(grid.score_complete_grid(), total)

	def test_total(self):
		self.verify_total([1,1,1,1,1,1,1,1,1], 667)
		self.verify_total([2,2,2,2,2,2,2,2,2], 334)
		self.verify_total([6,6,6,6,6,6,6,6,6], 998)

	def test_total_is_correct_with_specific_values(self):
		grid = Grid()
		grid.set_value(0,0,1)
		grid.set_value(1,0,2)
		grid.set_value(2,0,3)
		grid.set_value(0,1,1)
		grid.set_value(1,1,2)
		grid.set_value(2,1,3)
		grid.set_value(0,2,1)
		grid.set_value(1,2,2)
		grid.set_value(2,2,3)
		self.assertEqual(grid.score_complete_grid(), 631)

	def test_get_set_value(self):
		test_value = 2
		grid = Grid()
		grid.set_value(0,0,test_value)
		result = grid.get_value(0,0)
		self.assertEqual(result, test_value)

# This allows the test to be run from the command line
if __name__ == '__main__':
	unittest.main()