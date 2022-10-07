## Get reachable neighbors

To populate our Feasibility matrix with 0 and 1, we will first need to 
write the function that accepts a maze and a cell in that maze and returns a list of neighbors:
`Cell` objects, which are accessible from the given cell
(do not have a shared wall with it).

Complete the implementation of this function in convert.py