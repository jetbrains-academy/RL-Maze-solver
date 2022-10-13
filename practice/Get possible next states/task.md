## Get possible next states

To train our agent, we will need to fill the Q matrix with some values (elaborate here).
we will be using the train method of the Agent class for that.
The train method will need a couple of helper functions.
The first one `get_poss_next_states` uses the F matrix to determine which states (cells) can be reached
for a given state, and returns those states as a list. 
For example, given the maze below, if s = 5, the return list is [2, 8].

<img src="maze_example.png" width="300">

### Task
Complete the implementation of the function `get_poss_next_states` in learn.py

<style>
img {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
</style>