Implement the method `walk` that will walk the 
Q matrix to build the shortest path through the maze.
The method should fill `Agent.path` so that it stores the shortest path (a sequence of cell
numbers from start to goal, inclusively).

Remember that in the Q matrix row indices are "from" cells and column indices are "to" cells.
Starting from the row that corresponds to the starting cell, you need to find the next cell to move in to 
by finding the largest Q values in the given row. Repeat this until you reach the goal. The method assumes the goal state is reachable.

If you like, it could also print this sequence so that it looks something like this:

`0->1->4->3->6->7->8->5->2->done`

<div class="hint">

You can make use of the function `np.argmax()`, which returns the index of the largest 
value of an input vector. For example, if a vector vec had values (0, 10, 9, 23, 4), 
then np.argmax(vec) would return 3. 
</div>
