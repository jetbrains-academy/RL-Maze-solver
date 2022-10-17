import unittest
from maze import Maze
from cell import Cell
from convert import Feasibility
import numpy as np
from learn import get_poss_next_states, get_rnd_next_state
from unittest import mock

mocked_random_choice = lambda x, y: 0


def test_get_rnd_next_state(state, F, n_states):
    # Given a state, pick a feasible next state.
    poss_next_states = get_poss_next_states(state, F, n_states)
    next_state = poss_next_states[np.random.randint(0, len(poss_next_states))]
    return next_state


class TestCase(unittest.TestCase):
    def test_random_next_states(self):
        for iteration in range(10):
            dimension1 = 3
            dimension2 = 3
            start_x = 0
            start_y = 0

            maze = Maze(dimension1, dimension2, [start_x, start_y])

            feasibility = Feasibility(maze)
            n_states = feasibility.cells

            for i in range(0, n_states):
                curr_state = i
                with mock.patch('numpy.random.randint', mocked_random_choice), \
                        mock.patch('random.randint', mocked_random_choice):
                    actual_next_state = get_rnd_next_state(curr_state, feasibility.F_matrix, n_states)
                    test_next_state = test_get_rnd_next_state(curr_state, feasibility.F_matrix, n_states)
                    self.assertEqual(actual_next_state, test_next_state, msg="")