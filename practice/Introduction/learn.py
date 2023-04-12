import numpy as np
from convert import find_reachable_neighbors


def get_possible_next_states(state, F, n_states):
    # given a state s and a feasibility matrix F
    # get list of possible next states
    poss_next_states = []
    for j in range(n_states):
        if F[state, j] == 1:
            poss_next_states.append(j)
    return poss_next_states


def get_random_next_state(state, F, n_states):
    # Given a state, pick a feasible next state.
    poss_next_states = get_possible_next_states(state, F, n_states)
    next_state = poss_next_states[np.random.randint(0, len(poss_next_states))]
    return next_state


class Agent:
    def __init__(self, feasibility, gamma, lrn_rate, maze, start_x, start_y):
        self.Q = np.zeros(shape=[feasibility.F_matrix.shape[0], feasibility.F_matrix.shape[0]], dtype=np.float32)
        self.R = np.copy(feasibility.F_matrix)
        self.start = feasibility.numbered_grid[start_x, start_y]
        self.goal = feasibility.numbered_grid[maze.end[0], maze.end[1]]
        self.n_states = feasibility.cells
        self.gamma = gamma
        self.lrn_rate = lrn_rate
        self.path = []

    def set_rewards(self, maze, feasibility):
        # Find the penultimate cell to set the highest reward for reaching the end of the maze:
        previous = find_reachable_neighbors(maze, maze.maze_grid[maze.end[0]][maze.end[1]])[0]
        prev_index = np.where(maze.maze_grid == previous)
        previous = feasibility.numbered_grid[prev_index[0], prev_index[1]][0]
        # TODO: replace 1s in the template with -0.1.
        # TODO: Set the highest reward for reaching the end of the maze.

    def train(self, F, max_epochs):
        # Compute the Q matrix
        for i in range(0, max_epochs):
            curr_state = np.random.randint(0, self.n_states)  # random start state

            while True:
                next_state = get_random_next_state(curr_state, F, self.n_states)
                poss_next_next_states = get_possible_next_states(next_state, F, self.n_states)

                max_Q = -9999.99
                for j in range(len(poss_next_next_states)):
                    nn_s = poss_next_next_states[j]
                    q = self.Q[next_state, nn_s]
                    if q > max_Q:
                        max_Q = q
                # Bellman's equation: Q = [(1 - alpha) * Q]  +  [alpha * (reward + (gamma * maxQ))]
                # TODO: Update the Q matrix using the equation.

                curr_state = next_state
                if curr_state == self.goal:
                    break

    def walk(self, maze, feasibility):
        # Walk to the goal from start using Q matrix.
        curr = self.start
        self.path.append(curr)
        print(str(curr) + "->", end="")

        # Repeat until the goal is reached:
        while curr != self.goal:
            curr_position = np.where(feasibility.numbered_grid == curr)
            curr_cell = maze.maze_grid[curr_position[0], curr_position[1]][0]

            # next_ = ..... TODO: find the next cell in the path by locating
            #  the maximum Q value in the row corresponding to the current cell

            # Find the coordinates of the next cell:
            next_position = np.where(feasibility.numbered_grid == next_)
            next_cell = maze.maze_grid[next_position[0], next_position[1]][0]

            # If next_ is not reachable from the current cell the path was not found:
            reachable_neighbors = find_reachable_neighbors(maze, curr_cell)
            if next_cell not in reachable_neighbors:
                print('break. Path not found!')
                self.path.append('break')
                break

            print(str(next_) + "->", end="")
            curr = next_
            self.path.append(curr)
        print("done")