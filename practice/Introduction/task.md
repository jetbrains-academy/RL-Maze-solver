
We have some predefined code that builds a Maze,
which is an object of class Maze. `Maze.maze_grid` is a Numpy array of `Cell` objects.
Some cells have walls between them, which the agent cannot go through.
Please study the code in `cell.py` and `maze.py` to figure out how the maze is built.

> If you are struggling to understand this code, we encourage you to take the AMAzing course, which will
guide you through the steps of building such a maze.

Our goal is to get the Agent from the START (which can be any cell) to the END of the maze in the fewest number of moves.
The Agent can move left, right, up, or down but not diagonally.

For our solver algorithm to work, we will need to have all the cells in the
maze numbered the way it is shown on the image below.

<img src="maze_example.png" width="300">

We will also need to build a Feasibility matrix that would
contain information about what cells can be accessed from what other cells. You can imagine it as a table where the numbers of all cells
are both column and row names, and at their intersection there's either a 0 or a 1, depending on whether one cell is accessible from the other.
For example, if you can access cell 5 from cell 0 (as in the image), in the Feasibility matrix we should have a 1 in column 0 row 5 and in column 5 row 0 and so on.
Obviously, the shape of such a matrix will be n x n, where n is the number of cells in the maze.


Feasibility matrix for a 3x3 maze shown above would look like this:

<img src="feasibility.png" width="250">

You can run `main.py` to draw a maze. It will look different every time.

<style>
img {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
</style>