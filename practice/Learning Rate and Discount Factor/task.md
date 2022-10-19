Add the following lines to the `main` block in main.py (instead of whatever is in there at the moment)
and run the code in order to see the path of
the agent moving through the labyrinth.

```python
dimension1 = int(input('Enter x dimension: '))
dimension2 = int(input('Enter y dimension: '))
start_x = int(input('Enter x coordinate of the maze start: '))
start_y = int(input('Enter y coordinate of the maze start: '))
gamma = float(
    input('Enter the gamma value (0, 1]: '))
lrn_rate = float(input(
    'Enter the learning rate (0, 1]: '))
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
```

You will also need to import the `Agent` class.

As you might remember from the equation we discussed earlier,
Q-learning has two parameters, the learning rate ($\alpha$) and gamma ($\gamma$). Larger values 
of the learning rate increase the influence of both current rewards and future 
rewards (explore) at the expense of past rewards (exploit). The value of the discount factor 
influences the importance of future rewards. 
These values must be determined by trial and error but using 0.5 is typically a good starting place.
Optimal parameter values in this problem will differ depending on how large the maze is.
Try to find combinations that work (when the algorithm works for too long and doesn't seem to be able to 
find a path - maybe a different value combination is needed. With a large maze you might need to wait 
a little for the algorithm to solve it.