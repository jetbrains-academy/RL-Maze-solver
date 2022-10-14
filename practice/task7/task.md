The Q-learning algorithm updates the equation below, which is based on a clever idea called the Bellman equation.
You don't need to fully understand the Bellman equation to use Q-learning, but if you're interested,
the Wikipedia article is a good place to start.

$Q(s_t,a_t)=[(1 - \alpha)*Q(s_t,a_t)]+[\alpha * (r_t + \gamma * maxQ(s_{t+1},a) \forall a)]$