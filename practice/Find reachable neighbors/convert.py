import numpy as np
from cell import Cell


def find_reachable_neighbors(maze_, cell_):
    neighbors = []
    for direction, (dx, dy) in maze_.delta.items():
        neighbor_x, neighbor_y = cell_.x + dx, cell_.y + dy
        if (0 <= neighbor_x < maze_.nx) and (0 <= neighbor_y < maze_.ny):
            neighbor = maze_.cell_at(neighbor_x, neighbor_y)
            # Check if the neighbor does not have the wall between it and the curr. cell
            if not cell_.walls[direction]:
                neighbors.append(neighbor)
    return neighbors


class Feasibility:
    def __init__(self, maze_):
        self.cells = maze_.maze_grid.shape[0] * maze_.maze_grid.shape[1]
        self.F_matrix = np.zeros(shape=[self.cells, self.cells], dtype=int)
        self.numbered_grid = np.arange(self.cells).reshape((maze_.maze_grid.shape[0], maze_.maze_grid.shape[1]))
        self.get_neighbors(maze_)

    def get_neighbors(self, maze_):
        for cell_number in np.nditer(self.numbered_grid):
            ind1 = np.where(self.numbered_grid == cell_number)[0][0]
            ind2 = np.where(self.numbered_grid == cell_number)[1][0]
            neighbors = find_reachable_neighbors(maze_, maze_.maze_grid[ind1, ind2])
            if len(neighbors) > 0:
                for neighbor in neighbors:
                    neighbor_number_in_grid = self.numbered_grid[neighbor.x, neighbor.y]
                    self.F_matrix[cell_number, neighbor_number_in_grid] = 1

