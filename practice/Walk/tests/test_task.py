import unittest
from maze import Maze
from convert import Feasibility, find_reachable_neighbors
from learn import Agent
from tests.test_learn import TestAgent
import wrapt_timeout_decorator
import contextlib
import io

f = io.StringIO()

timeoutlimit = 20


class TestCase(unittest.TestCase):
    @wrapt_timeout_decorator.timeout(timeoutlimit)
    def test_agent_R(self):
        for x in range(10):
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
                agent.walk()
                test_agent.walk()
                self.assertEqual(agent.path, test_agent.path)

            except TimeoutError as e:
                self.fail(msg=f"TimeoutError after {timeoutlimit} seconds. Your implementation's execution does not seem "
                              f"to end in a reasonable amount of time.")