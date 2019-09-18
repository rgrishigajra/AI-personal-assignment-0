# a0
PART ONE 

For the initial code the program had the following search abstraction
The given code tries to implement Depth first search.
Goal state:The goal state is when algorithm reaches "@" luddy hall on man
set of valid states: is every step from one sidewalk postiion to other where 
The cost funciton is one for every step that is taken.
initial state is the starting map given in argument
The successor function is the (x+1,y),(x,y+1),(x-1,y),(x,y-1) where (x,y) is current cordinates 

Finding whats wrong with the code given.It goes in an Infinite loop since the fringe acts as a stack and it keeps visiting and expanding the same two nodes. Due to this the program never moves towards the solution. Attempt no 1 to fix this is to convert the fringe to work as a queue. It maybe visit repeated nodes but it still reach an answer.
Converted the fringe to work as a queue by changing index parameter in pop(). The program arrives to solution in 16 seconds once search1 is called. There are approximately 32030 elements added to the fringe during the search before finding the solution. 
 
Started with a heuristic as manhattan distance and changing fringe such that node with minimum value of total estimated cost = current cost+heurstic estimate higher priority and pop out that element first.
program Got much faster.Even the number of elements in the fringe got reduced.
 
Created a visited nodes array so the algorithm doesnt calculate for fringes that have been visited before. Improved the efficiency of algorithm. Was able to do this since my heuristic is consistent. Program reaches solution in 100th of the initial time.

For noting down the path I traced the difference in the cordinates and appended NSEW wrt outputx

PART TWO hide.py

For this code the challenge was to avoid two friends from seeing each other. Its a lot like the n-rooks problem where pawns are the obstructions and not buildings. To solve a conflict situation I implmented a visible array in the fringe that keeps track of what all positions are visible by some friend. Then out of all the places not currently visible i place a new friend on the map. 

Goal state: when all K friends are placed on the board and no two of them see each other.

set of valid states:Is the map where some N friends are on the map and 0<=N<=K and none of the two N friends see each other.

Cost function is number of friends not placed on the board out of K.

Initial state is empty map with the buildings, luddy hall and me on the map along with empty side walks.

successor function is every sidewalk space that is not visible for any friend on the map
