This demonstration introduces a simple Reinforcement Learning (RL) algorithm designed to solve a 2D maze in
the shortest number of steps. The core concept of RL is learning by interaction with an environment to maximize a reward function. 
Unlike supervised learning, correct labels for a series of actions are not known upfront and need to be learned.
RL focuses on finding a balance between exploration (seeking future rewards) and exploitation 
(using existing knowledge). You will experiment with a Q-learning algorithm that iteratively updates a Q-table, helping 
the learning agent find the maze's shortest path.

In Q-learning, the learning rate ($\alpha$) and discount factor ($\gamma$) influence the importance of future rewards. Optimal values 
for these parameters depend on the maze size, and identifying the right combination is crucial for the algorithm's success. 
The Q-table is updated using the following equation:

$$Q(s_t,a_t)=[(1 - \alpha)*Q(s_t,a_t)]+[\alpha * (r_t + \gamma * maxQ(s_{t+1},a) \forall a)]$$

<details>

- $Q(s_t,a_t)$ represents the Q-value of a specific state-action pair at time step $t$.

- $\alpha$ is the learning rate, which determines the degree to which new information affects the current Q-value.

- $r_t$ is the immediate reward received after taking action $a_t$ in state $s_t$.

- $\gamma$ is the discount factor, which influences the importance of future rewards.

- $maxQ(s_{t+1},a)$ represents the maximum Q-value of the next state ($s_{t+1}$) over all possible actions $a$.
</details>

The learning rate and discount factor determine the balance between past information and future rewards. Adjusting these 
parameters helps the algorithm achieve the optimal balance between exploration and exploitation.

When running `final_run.py`, the program will ask for your input, generate a maze, and use the Q-learning algorithm to find the shortest path. 
It will also create a gif of the agent moving through the maze, which you will be able to view in the next task. 
Experiment with different $\alpha$ and $\gamma$ values to find the combinations 
that work best for mazes of different sizes. If the algorithm struggles to find a path, try a different combination of the parameters (generally, for
larger mazes greater gamma and learning rate values are needed).

If you would like to learn more about Reinforcement Learning, you're welcome to take [the full version of this course](https://plugins.jetbrains.com/plugin/21188)!


<div class="hint">
Suggested working combinations (try others as well, these are not necessarily optimal):

- 3 x 3 maze, start anywhere, gamma = 0.6, lrn_rate = 0.5
- 5 x 5 maze, start anywhere, gamma = 0.9, lrn_rate = 0.5
- 10 x 10 maze, start anywhere, gamma = 1, lrn_rate = 0.5 (could take more than a minute)

</div>
