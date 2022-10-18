import unittest
from maze import Maze
from convert import Feasibility, find_reachable_neighbors
import numpy as np
from learn import Agent
from tests.test_learn import TestAgent
import wrapt_timeout_decorator

timeoutlimit = 10

class TestCase(unittest.TestCase):
    @wrapt_timeout_decorator.timeout(timeoutlimit)
    def test_agent_R(self):
        dimension1, dimension2 = (3, 3)
        start_x, start_y = (0, 0)
        maze = Maze(dimension1, dimension2, [start_x, start_y])
        feasibility = Feasibility(maze)
        gamma = 0.9
        lrn_rate = 0.9
        max_epochs = 100
        agent = Agent(feasibility, gamma, lrn_rate, maze, start_x, start_y)
        test_agent = TestAgent(feasibility, gamma, lrn_rate, maze, start_x, start_y)
        try:
            agent.train(feasibility.F_matrix, max_epochs)
            test_agent.train(feasibility.F_matrix, max_epochs)
            not_zero_actual = np.where(test_agent.Q >= 10)
            not_zero_test = np.where(agent.Q >= 10)
            not_zero_feasibility = np.where(feasibility.F_matrix != 0)
            np.testing.assert_array_equal(not_zero_test, not_zero_actual, err_msg="The resulting Q matrix does not look like we expected.")
            np.testing.assert_array_equal(not_zero_feasibility, not_zero_actual, err_msg="You cannot assign "
                                                                                         "Quality values to "
                                                                                         "intersections of cells, "
                                                                                         "which are not reachable "
                                                                                         "from one another")
        except TimeoutError as e:
            self.fail(msg=f"TimeoutError after {timeoutlimit} seconds. Your method's execution does not seem to end in a "
                          "reasonable amount of time.")
