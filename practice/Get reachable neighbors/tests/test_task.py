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


class TestCase(unittest.TestCase):

    def test_neighbors_type(self):
        dimension1 = 3
        dimension2 = 3
        start_x = 0
        start_y = 0

        maze = Maze(dimension1, dimension2, [start_x, start_y])

        neighbors = find_reachable_neighbors(maze, maze.maze_grid[1, 1])
        actual_type = type(neighbors)
        self.assertEqual(list, actual_type,
                         msg=f"The return type of the function is wrong. {actual_type} detected, expected list.")

    def test_find_neighbors(self):
        dimension1 = 3
        dimension2 = 3
        start_x = 0
        start_y = 0

        maze = Maze(dimension1, dimension2, [start_x, start_y])
        for x in range(dimension1):
            for y in range(dimension2):
                neighbors = find_reachable_neighbors(maze, maze.maze_grid[x, y])
                test_neighbors = test_find_reachable_neighbors(maze, maze.maze_grid[x, y])
                self.assertEqual(test_neighbors, neighbors, msg="Neighbors do not seem right!")
