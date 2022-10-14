import numpy as np
import random


def get_poss_next_states(state, F, n_states):
    # given a state s and a feasibility matrix F
    # get list of possible next states
    poss_next_states = []
    for j in range(n_states):
        if F[state, j] == 1:
            poss_next_states.append(j)
    return poss_next_states


def get_rnd_next_state(state, F, n_states):
    # Given a state, pick a feasible next state.
    poss_next_states = get_poss_next_states(state, F, n_states)
    next_state = poss_next_states[np.random.randint(0, len(poss_next_states))]
    return next_state


class Agent:
    def __init__(self, Q, gamma, lrn_rate):
        self.Q = Q
        self.gamma = gamma
        self.lrn_rate = lrn_rate
        self.path = []

    def train(self, F, R, max_epochs, n_states, goal):
        # Compute the Q matrix
        for i in range(0, max_epochs):
            curr_state = np.random.randint(0, n_states)  # random start state

            while True:
                next_state = get_rnd_next_state(curr_state, F, n_states)
                poss_next_next_states = get_poss_next_states(next_state, F, n_states)

                max_Q = -9999.99
                for j in range(len(poss_next_next_states)):
                    nn_s = poss_next_next_states[j]
                    q = self.Q[next_state, nn_s]
                    if q > max_Q:
                        max_Q = q
                # Bellman's equation: Q = [(1-a) * Q]  +  [a * (rt + (g * maxQ))]
                # Update the Q matrix
                self.Q[curr_state][next_state] = ((1 - self.lrn_rate) * self.Q[curr_state][next_state]) + (
                            self.lrn_rate * (R[curr_state][next_state] + (self.gamma * max_Q)))

                curr_state = next_state
                if curr_state == goal:
                    break

    def walk(self, start, goal):
        # Walk to the goal from start using Q matrix.
        curr = start
        self.path.append(curr)
        print(str(curr) + "->", end="")
        while curr != goal:
            next_ = np.argmax(self.Q[curr])
            print(str(next_) + "->", end="")
            curr = next_
            self.path.append(curr)
        print("done")
