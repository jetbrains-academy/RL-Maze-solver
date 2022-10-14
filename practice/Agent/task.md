The heart of the program is method `train()` of class `Agent`, which computes the Q matrix.
The Q stands for quality, where larger values are better. The Q matrix is built the same way as the F-matrix,
but its row indices are the "from" cells and the column indices are the "to" cells.

The Q-learning algorithm updates the equation below, which is based on the Bellman equation.
You don't need to fully understand the Bellman equation to use Q-learning, but if you're interested,
the Wikipedia article is a good place to start.

$Q(s_t,a_t)=[(1 - \alpha)*Q(s_t,a_t)]+[\alpha * (r_t + \gamma * maxQ(s_{t+1},a) \forall a)]$

where $Q(s_t,a_t)$ is the Q value of going from the current state to the next; 
$\alpha$ is learning rate; $r_t$ is the reward for the transition; $\gamma$ is the discount factor, which influences the importance of future rewards.
This largest value, $maxQ$, will be used to update the Q matrix. 


First we will need to define the Agent class. complete the `__init__` method of the class
so that it has the following attributes:
- gamma (`gamma`) - the discount factor,
- learning rate (`lrn_rate`),
- `Q` - the Q matrix
- `path` - a list that at the end of the training process will contain the optimal path - a sequence of cell numbers.
