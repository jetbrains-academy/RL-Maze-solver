import unittest
from maze import Maze
from convert import Feasibility
import numpy as np
from learn import Agent


class TestCase(unittest.TestCase):
    def test_agent_Q(self):
        dimension1 = 3
        dimension2 = 3
        start_x = 0
        start_y = 0

        maze = Maze(dimension1, dimension2, [start_x, start_y])

        feasibility = Feasibility(maze)
        n_states = feasibility.cells
        Q_matrix = np.zeros(shape=[feasibility.F_matrix.shape[0], feasibility.F_matrix.shape[0]], dtype=np.float32)
        gamma = 0.5
        lrn_rate = 0.5
        agent = Agent(Q_matrix, gamma, lrn_rate)
        try:
            np.testing.assert_array_equal(agent.Q, Q_matrix, err_msg="Something's wrong.")
        except AttributeError:
            self.fail("AttributeError was raised.")

    def test_agent_path(self):
        dimension1 = 3
        dimension2 = 3
        start_x = 0
        start_y = 0

        maze = Maze(dimension1, dimension2, [start_x, start_y])

        feasibility = Feasibility(maze)
        n_states = feasibility.cells
        Q_matrix = np.zeros(shape=[feasibility.F_matrix.shape[0], feasibility.F_matrix.shape[0]], dtype=np.float32)
        gamma = 0.5
        lrn_rate = 0.5
        agent = Agent(Q_matrix, gamma, lrn_rate)
        try:
            self.assertEqual(agent.path, [], msg="sef.path should be an empty list at this stage.")
        except AttributeError:
            self.fail("AttributeError was raised.")

    def test_agent_gamma(self):
        dimension1 = 3
        dimension2 = 3
        start_x = 0
        start_y = 0

        maze = Maze(dimension1, dimension2, [start_x, start_y])

        feasibility = Feasibility(maze)
        n_states = feasibility.cells
        Q_matrix = np.zeros(shape=[feasibility.F_matrix.shape[0], feasibility.F_matrix.shape[0]], dtype=np.float32)
        gamma = 0.5
        lrn_rate = 0.5
        agent = Agent(Q_matrix, gamma, lrn_rate)
        try:
            self.assertEqual(agent.gamma, gamma, msg="Agent should be initialized with a self.gamma attribute.")
        except AttributeError:
            self.fail("AttributeError was raised. Agent should be initialized with a self.gamma attribute.")

    def test_agent_lrn_rate(self):
        dimension1 = 3
        dimension2 = 3
        start_x = 0
        start_y = 0

        maze = Maze(dimension1, dimension2, [start_x, start_y])

        feasibility = Feasibility(maze)
        n_states = feasibility.cells
        Q_matrix = np.zeros(shape=[feasibility.F_matrix.shape[0], feasibility.F_matrix.shape[0]], dtype=np.float32)
        gamma = 0.5
        lrn_rate = 0.5
        agent = Agent(Q_matrix, gamma, lrn_rate)
        try:
            self.assertEqual(agent.lrn_rate, lrn_rate, msg="Agent should be initialized with a self.lrn_rate attribute.")
        except AttributeError:
            self.fail("AttributeError was raised. Agent should be initialized with a self.lrn_rate attribute.")
