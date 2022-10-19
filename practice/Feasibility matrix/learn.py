import numpy as np
from convert import find_reachable_neighbors


def get_poss_next_states(state, F, n_states):
    # given a state s and a feasibility matrix F
    # get list of possible next states
    pass


def get_rnd_next_state(state, F, n_states):
    # Given a state, pick a feasible next state.
    pass


class Agent:
    def __init__(self, feasibility, gamma, lrn_rate, maze, start_x, start_y):
        pass

    def set_rewards(self, maze, feasibility):
        # Find the penultimate cell and set the highest reward for reaching the end of the maze.
        pass

    def train(self, F, max_epochs):
        # Compute the Q matrix using the
        # Bellman's equation: Q = [(1-a) * Q]  +  [a * (rt + (g * maxQ))]
        pass

    def walk(self):
        # Walk to the goal from start using the Q matrix.
        pass
