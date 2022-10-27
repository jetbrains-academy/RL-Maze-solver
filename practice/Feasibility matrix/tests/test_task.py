import unittest
from maze import Maze
from convert import Feasibility
import numpy as np


class TestCase(unittest.TestCase):
    def test_feasibility_matrix(self):
        dimension1 = 3
        dimension2 = 3
        start_x = 0
        start_y = 0

        maze = Maze(dimension1, dimension2, [start_x, start_y])

        feasibility = Feasibility(maze)

        test_feasibility = np.zeros(shape=[dimension1 * dimension2, dimension1 * dimension2], dtype=int)
        try:
            np.testing.assert_array_equal(feasibility.F_matrix, test_feasibility, err_msg="Your F_matrix looks wrong.")
        except AttributeError as e:
            self.fail(msg=f"AttributeError was raised. {e}. Please make sure you defined all attributes with correct names.")

    def test_numbered_grid(self):
        dimension1 = 3
        dimension2 = 3
        start_x = 0
        start_y = 0

        maze = Maze(dimension1, dimension2, [start_x, start_y])

        feasibility = Feasibility(maze)

        test_numbered_grid = np.arange(dimension1 * dimension2).reshape((dimension1, dimension1))
        try:
            np.testing.assert_array_equal(feasibility.numbered_grid, test_numbered_grid, err_msg="Your numbered_grid looks wrong.")
        except AttributeError as e:
            self.fail(msg=f"AttributeError was raised. {e}. Please make sure you defined all attributes with correct names.")





