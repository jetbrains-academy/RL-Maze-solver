import unittest
from maze import Maze
from convert import Feasibility, find_reachable_neighbors
import numpy as np
from learn import Agent


def test_set_rewards(maze, feasibility):
    previous = find_reachable_neighbors(maze, maze.maze_grid[maze.end[0]][maze.end[1]])[0]
    prev_index = np.where(maze.maze_grid == previous)
    previous = feasibility.numbered_grid[prev_index[0], prev_index[1]][0]
    R = np.copy(feasibility.F_matrix)
    R = np.where(R == 1, -0.1, R)
    goal = feasibility.numbered_grid[maze.end[0], maze.end[1]]
    R[previous, goal] = 1000.0
    return goal, previous, R


class TestCase(unittest.TestCase):
    def test_0_forgot_to_call(self):
        dimension1, dimension2 = (3, 3)
        start_x, start_y = (0, 0)

        maze = Maze(dimension1, dimension2, [start_x, start_y])

        feasibility = Feasibility(maze)
        gamma = 0.5
        lrn_rate = 0.5
        agent = Agent(feasibility, gamma, lrn_rate, maze, start_x, start_y)
        # _, _, test_R = test_set_rewards(maze, feasibility)
        test_ones = np.where(feasibility.F_matrix == 1)[0]
        test_ones = test_ones.tolist()
        actual_ones = np.where(agent.R == 1)[0]
        actual_ones = actual_ones.tolist()
        if test_ones == actual_ones:
            self.fail(msg="Maybe you forgot to call the implemented set_rewards method in the init.")

    def test_agent_R(self):
        dimension1, dimension2 = (3, 3)
        start_x, start_y = (0, 0)
        maze = Maze(dimension1, dimension2, [start_x, start_y])
        feasibility = Feasibility(maze)
        gamma = 0.5
        lrn_rate = 0.5
        agent = Agent(feasibility, gamma, lrn_rate, maze, start_x, start_y)
        _, _, test_R = test_set_rewards(maze, feasibility)
        np.testing.assert_array_equal(agent.R, test_R, err_msg="Reward matrix seems off")

    def test_last_reward(self):
        dimension1, dimension2 = (3, 3)
        start_x, start_y = (0, 0)
        maze = Maze(dimension1, dimension2, [start_x, start_y])
        feasibility = Feasibility(maze)
        gamma = 0.5
        lrn_rate = 0.5
        agent = Agent(feasibility, gamma, lrn_rate, maze, start_x, start_y)
        goal, previous, test_R = test_set_rewards(maze, feasibility)
        self.assertEqual(agent.R[previous, goal], test_R[previous, goal], msg="The reward for reaching the goal cell should be 1000.0")
        self.assertTrue(0 in agent.R and -0.1 in agent.R and 1000.0 in agent.R, msg="R matrix should contain values 0, -0.1 and 1000.0.")
    #
