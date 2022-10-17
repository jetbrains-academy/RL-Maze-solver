import numpy as np
from maze import Maze
from convert import Feasibility, find_reachable_neighbors
from PIL import Image
from draw import make_movie
from learn import Agent
import pandas as pd


def my_print(Q):
    labels = [str(x) for x in range(Q.shape[0])]
    df = pd.DataFrame(Q, columns=labels, index=labels)
    pd.set_option('display.max_rows', None)
    print(df.to_string())


def run():
    np.random.seed(1)

    # gamma = 0.9
    # lrn_rate = 0.5
    # dimension1 = 5
    # dimension2 = 5
    dimension1 = int(input('Enter x dimension: '))
    dimension2 = int(input('Enter y dimension: '))
    start_x = int(input('Enter x coordinate of the maze start: '))
    start_y = int(input('Enter y coordinate of the maze start: '))
    gamma = float(
        input('Enter the gamma value (0, 1] (aka the discount factor, influences the importance of future rewards): '))
    lrn_rate = float(input(
        'Enter the learning rate (0, 1] (larger values increase the influence of both current rewards and future rewards (explore) at the expense of past rewards (exploit)): '))
    max_epochs = 1000

    # Create the Maze
    maze = Maze(dimension1, dimension2, [start_x, start_y])

    # Get the Feasibility Matrix
    feasibility = Feasibility(maze)

    # Initialize the agent:
    agent = Agent(feasibility, gamma, lrn_rate, maze, start_x, start_y)

    print("Analyzing maze with RL Q-learning")
    print("The F matrix:\n")
    my_print(feasibility.F_matrix)

    # Train the model:
    agent.train(feasibility.F_matrix, max_epochs)
    # train(feasibility.F_matrix, R_matrix, Q_matrix, gamma, lrn_rate, goal, n_states, max_epochs)
    print("Done ")

    print("The Q matrix is: \n ")
    my_print(agent.Q)

    print(f"Using Q to go from 0 to goal ({agent.goal})")

    agent.walk()

    # Draw the visualization
    margin = 80
    cell_side = 100
    width, height = (margin + cell_side * dim for dim in maze.maze_grid.shape)
    make_movie(width, height, maze, feasibility, agent.path)


if __name__ == "__main__":
    run()

