As mentioned before, the Q-learning algorithm updates the equation below.

$$Q(s_t,a_t)=[(1 - \alpha)*Q(s_t,a_t)]+[\alpha * (r_t + \gamma * maxQ(s_{t+1},a) \forall a)]$$

So we will now need to implement it in code.

In this algorithm, you repeatedly start at a random position in the maze. 
Then, at every cell position, you pick a random next state and determine all possible 
states after the next state -- the "next-next states". You examine the 
current values in the Q matrix and find the largest Q value of a transition from the next state 
to any next-next state. This largest value, max_Q, is used to update the Q matrix using the equation above.

For each random starting state, you repeat this process until you reach the goal. 

The assumption here 
is that the goal is reachable, so in some problems you need to apply 
a maximum loop control variable (`max_epochs`).

As an example, suppose at some point during training, you're at cell 8 and the next random 
state is selected as cell 5. The next-next states are 8 and 2. Because moving to cell 2 
has a reward of +1000.0, the value of Q[8][5] will be increased, making that path more attractive 
than the path from cell 8 to cell 7. 

<img src="maze_example.png" width="300">