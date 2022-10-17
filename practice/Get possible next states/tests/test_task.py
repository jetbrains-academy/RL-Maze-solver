import unittest
from maze import Maze
from cell import Cell
from convert import Feasibility
import numpy as np
from learn import get_poss_next_states


def test_get_poss_next_states(state, F, n_states):
    poss_next_states = []
    for j in range(n_states):
        if F[state, j] == 1:
            poss_next_states.append(j)
    return poss_next_states


class TestCase(unittest.TestCase):
    def test_next_states(self):
        dimension1 = 3
        dimension2 = 3
        start_x = 0
        start_y = 0

        maze = Maze(dimension1, dimension2, [start_x, start_y])

        feasibility = Feasibility(maze)
        n_states = feasibility.cells
        for cell in np.nditer(feasibility.numbered_grid):
            test_poss_next_states = test_get_poss_next_states(cell, feasibility.F_matrix, n_states)
            actual_poss_next_states = get_poss_next_states(cell, feasibility.F_matrix, n_states)
            self.assertEqual(actual_poss_next_states, test_poss_next_states, msg=f"Wrong possible next states found for cell {cell} for a test F_matrix {feasibility.F_matrix}")

