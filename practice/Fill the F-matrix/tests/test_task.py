import unittest
from maze import Maze
from cell import Cell
from convert import Feasibility, find_reachable_neighbors
import numpy as np


def test_find_reachable_neighbors(maze_, cell_):
    neighbors = []
    for direction, (dx, dy) in maze_.delta.items():
        neighbor_x, neighbor_y = cell_.x + dx, cell_.y + dy
        if (0 <= neighbor_x < maze_.nx) and (0 <= neighbor_y < maze_.ny):
            neighbor = maze_.cell_at(neighbor_x, neighbor_y)
            # Check if the neighbor does not have the wall between it and the curr. cell
            if not neighbor.walls[Cell.wall_pairs[direction]]:
                neighbors.append(neighbor)
    return neighbors


class TestFeasibility:
    def __init__(self, maze_):
        self.cells = maze_.maze_grid.shape[0] * maze_.maze_grid.shape[1]
        self.F_matrix = np.zeros(shape=[self.cells, self.cells], dtype=int)
        self.numbered_grid = np.arange(self.cells).reshape((maze_.maze_grid.shape[0], maze_.maze_grid.shape[1]))
        self.get_neighbors(maze_)

    def get_neighbors(self, maze_):
        for cell_number in np.nditer(self.numbered_grid):
            ind1 = np.where(self.numbered_grid == cell_number)[0][0]
            ind2 = np.where(self.numbered_grid == cell_number)[1][0]
            neighbors = test_find_reachable_neighbors(maze_, maze_.maze_grid[ind1, ind2])
            if len(neighbors) > 0:
                for neighbor in neighbors:
                    # neighbor = neighbor_tuple[1]
                    neighbor_number_in_grid = self.numbered_grid[neighbor.x, neighbor.y]
                    if self.F_matrix[cell_number, neighbor_number_in_grid] == 0:
                        self.F_matrix[cell_number, neighbor_number_in_grid] = 1


class TestCase(unittest.TestCase):
    def test_0_forgot_to_call(self):
        dimension1 = 3
        dimension2 = 3
        start_x = 0
        start_y = 0

        maze = Maze(dimension1, dimension2, [start_x, start_y])

        actual_feasibility = Feasibility(maze)
        all_zeroes = not np.any(actual_feasibility.F_matrix)
        self.assertFalse(all_zeroes, msg="Maybe you forgot to call the implemented method in the init. The F_matrix "
                                         "is all zeroes.")

    def test_1_feasibility_neighbors(self):
        dimension1 = 3
        dimension2 = 3
        start_x = 0
        start_y = 0

        maze = Maze(dimension1, dimension2, [start_x, start_y])

        test_feasibility = TestFeasibility(maze)
        actual_feasibility = Feasibility(maze)
        np.testing.assert_array_equal(test_feasibility.F_matrix, actual_feasibility.F_matrix,
                                      err_msg="Your F_matrix is wrong.")
