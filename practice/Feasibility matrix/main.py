from maze import Maze
from convert import Feasibility
from draw import draw_maze
import pandas as pd


# This function is need to print a readable representation of the feasibility matrix.
def my_print(Q):
    labels = [str(x) for x in range(Q.shape[0])]
    df = pd.DataFrame(Q, columns=labels, index=labels)
    pd.set_option('display.max_rows', None)
    print(df.to_string())


if __name__ == "__main__":
    # dimension1 = int(input('Enter x dimension: '))
    # dimension2 = int(input('Enter y dimension: '))
    # start_x = int(input('Enter x coordinate of the maze start: '))
    # start_y = int(input('Enter y coordinate of the maze start: '))

    dimension1 = 3
    dimension2 = 3
    start_x = 0
    start_y = 0

    # Create the Maze
    maze = Maze(dimension1, dimension2, [start_x, start_y])

    # Create the Feasibility Matrix
    feasibility = Feasibility(maze)
    my_print(feasibility.F_matrix)

    # These are some predefined values needed for the visualization
    margin = 80
    cell_side = 100
    width, height = (margin + cell_side * dim for dim in maze.maze_grid.shape)

    # This will draw the maze and save it to the file maze.png
    draw_maze(width, height, maze)




