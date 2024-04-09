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

# This allows the test to be run from the command line
if __name__ == '__main__':
    unittest.main()