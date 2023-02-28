import unittest
from maze import Maze
from convert import Feasibility
import numpy as np
from learn import Agent


class TestCase(unittest.TestCase):
    def test_agent_Q(self):
        dimension1, dimension2 = (3, 3)
        start_x, start_y = (0, 0)
        maze = Maze(dimension1, dimension2, [start_x, start_y])
        feasibility = Feasibility(maze)
        gamma = 0.5
        lrn_rate = 0.5
        agent = Agent(feasibility, gamma, lrn_rate, maze, start_x, start_y)
        test_Q = np.zeros(shape=[feasibility.F_matrix.shape[0], feasibility.F_matrix.shape[0]], dtype=np.float32)
        try:
            np.testing.assert_array_equal(test_Q, agent.Q, err_msg="Something's wrong.")
        except AttributeError as e:
            self.fail(msg=f"AttributeError was raised. {e}. Please make sure you defined all attributes "
                          f"and they have correct names.")

    def test_agent_path(self):
        dimension1, dimension2 = (3, 3)
        start_x, start_y = (0, 0)
        maze = Maze(dimension1, dimension2, [start_x, start_y])
        feasibility = Feasibility(maze)
        gamma = 0.5
        lrn_rate = 0.5
        agent = Agent(feasibility, gamma, lrn_rate, maze, start_x, start_y)
        try:
            self.assertEqual([], agent.path, msg="sef.path should be an empty list at this stage.")
        except AttributeError as e:
            self.fail(msg=f"AttributeError was raised. {e}. Please make sure you defined all attributes "
                          f"and they have correct names.")

    def test_agent_gamma(self):
        dimension1, dimension2 = (3, 3)
        start_x, start_y = (0, 0)
        maze = Maze(dimension1, dimension2, [start_x, start_y])
        feasibility = Feasibility(maze)
        gamma = 0.5
        lrn_rate = 0.5
        agent = Agent(feasibility, gamma, lrn_rate, maze, start_x, start_y)
        try:
            self.assertEqual(gamma, agent.gamma, msg="Agent should be initialized with a self.gamma attribute.")
        except AttributeError as e:
            self.fail(msg=f"AttributeError was raised. {e}. Please make sure you defined all attributes "
                          f"and they have correct names.")


def test_agent_lrn_rate(self):
    dimension1, dimension2 = (3, 3)
    start_x, start_y = (0, 0)
    maze = Maze(dimension1, dimension2, [start_x, start_y])
    feasibility = Feasibility(maze)
    gamma = 0.5
    lrn_rate = 0.5
    agent = Agent(feasibility, gamma, lrn_rate, maze, start_x, start_y)
    try:
        self.assertEqual(lrn_rate, agent.lrn_rate, msg="Agent should be initialized with a self.lrn_rate attribute.")
    except AttributeError as e:
        self.fail(msg=f"AttributeError was raised. {e}. Please make sure you defined all attributes "
                      f"and they have correct names.")


def test_agent_start(self):
    dimension1, dimension2 = (3, 3)
    start_x, start_y = (0, 0)
    maze = Maze(dimension1, dimension2, [start_x, start_y])
    feasibility = Feasibility(maze)
    gamma = 0.5
    lrn_rate = 0.5
    agent = Agent(feasibility, gamma, lrn_rate, maze, start_x, start_y)
    test_start = feasibility.numbered_grid[start_x, start_y]
    try:
        self.assertEqual(test_start, agent.start, msg="self.start has a wrong value.")
    except AttributeError as e:
        self.fail(msg=f"AttributeError was raised. {e}. Please make sure you defined all attributes "
                      f"and they have correct names.")


def test_agent_goal(self):
    dimension1, dimension2 = (3, 3)
    start_x, start_y = (0, 0)
    maze = Maze(dimension1, dimension2, [start_x, start_y])
    feasibility = Feasibility(maze)
    gamma = 0.5
    lrn_rate = 0.5
    agent = Agent(feasibility, gamma, lrn_rate, maze, start_x, start_y)
    test_goal = feasibility.numbered_grid[maze.end[0], maze.end[1]]
    try:
        self.assertEqual(test_goal, agent.goal, msg="self.goal has a wrong value.")
    except AttributeError as e:
        self.fail(msg=f"AttributeError was raised. {e}. Please make sure you defined all attributes "
                      f"and they have correct names.")


def test_agent_n_states(self):
    dimension1, dimension2 = (3, 3)
    start_x, start_y = (0, 0)
    maze = Maze(dimension1, dimension2, [start_x, start_y])
    feasibility = Feasibility(maze)
    gamma = 0.5
    lrn_rate = 0.5
    agent = Agent(feasibility, gamma, lrn_rate, maze, start_x, start_y)
    test_n_states = feasibility.cells
    try:
        self.assertEqual(test_n_states, agent.n_states, msg="self.n_states has a wrong value.")
    except AttributeError as e:
        self.fail(msg=f"AttributeError was raised. {e}. Please make sure you defined all attributes "
                      f"and they have correct names.")


def test_agent_R(self):
    dimension1, dimension2 = (3, 3)
    start_x, start_y = (0, 0)
    maze = Maze(dimension1, dimension2, [start_x, start_y])
    feasibility = Feasibility(maze)
    gamma = 0.5
    lrn_rate = 0.5
    agent = Agent(feasibility, gamma, lrn_rate, maze, start_x, start_y)
    test_R = np.copy(feasibility.F_matrix)
    try:
        np.testing.assert_array_equal(test_R, agent.R, err_msg="self.R should be a copy of the F-matrix array.")
        self.assertFalse(agent.R is feasibility.F_matrix, msg="self.R should NOT refer to the same object as "
                                                              "feasibility.F_matrix. You need to make a copy.")
    except AttributeError as e:
        self.fail(msg=f"AttributeError was raised. {e}. Please make sure you defined all attributes "
                      f"and they have correct names.")
