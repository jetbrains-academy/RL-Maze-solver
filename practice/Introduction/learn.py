import numpy as np
from convert import find_reachable_neighbors


def get_possible_next_states(state, F, n_states):
    # given a state s and a feasibility matrix F
    # get list of possible next states
    pass


def get_random_next_state(state, F, n_states):
    # Given a state, pick a feasible next state.
    pass


class Agent:
    def __init__(self, feasibility, gamma, lrn_rate, maze, start_x, start_y):
        self.gamma = gamma
        self.lrn_rate = lrn_rate
        self.path = []

    def set_rewards(self, maze, feasibility):
        # Find the penultimate cell and set the highest reward for reaching the end of the maze.
        pass

    def train(self, F, max_epochs):
        # Compute the Q matrix using the
        # Bellman's equation: Q = [(1 - alpha) * Q]  +  [alpha * (reward + (gamma * maxQ))]
        pass

    def walk(self, maze, feasibility):
        # Walk to the goal from start using the Q matrix.
        pass
