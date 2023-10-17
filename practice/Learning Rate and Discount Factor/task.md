This demonstration introduces a simple Reinforcement Learning (RL) algorithm designed to solve a 2D maze in
the shortest number of steps. The core concept of RL is learning by interaction with an environment.



<div class="hint" title="More about Reinforcement Learning">
  Unlike supervised learning, correct labels for a series of actions are not known upfront and need to be learned.
<br>
RL focuses on finding a balance between exploration (seeking future rewards) and exploitation 
(using existing knowledge). You will experiment with a Q-learning algorithm that iteratively updates a Q-table, helping 
the learning agent find the shortest path in a maze.
<br>
In Q-learning, the learning rate (&alpha;) and discount factor (&gamma;) influence the importance of future rewards. Optimal values 
for these parameters depend on the maze size, and they help achieve the optimal balance between exploration and exploitation to ensure 
successful completion.
</div>

When running `final_run.py`, the program will ask for your input, generate a maze, and use the Q-learning algorithm to find the shortest path. 

It will also create a gif of the agent moving through the maze, which you will be able to view in the next task. 

Experiment with different &alpha; (Learning Rate) and &gamma; (Discount Factor) values to find the combinations 
that work best for mazes of different sizes. If the algorithm struggles to find a path, try a different combination of the parameters (generally, for
larger mazes greater gamma and learning rate values are needed).


<div class="hint" title="Suggested Parameter Combinations">
Suggested working combinations (try others as well, these are not necessarily optimal):

- 3 x 3 maze, start anywhere, gamma = 0.6, lrn_rate = 0.5
- 5 x 5 maze, start anywhere, gamma = 0.9, lrn_rate = 0.5
- 10 x 10 maze, start anywhere, gamma = 1, lrn_rate = 0.5 (could take more than a minute)

</div>


If you would like to learn more about Reinforcement Learning, you're welcome to take [the full version of this course](https://plugins.jetbrains.com/plugin/21188)!
