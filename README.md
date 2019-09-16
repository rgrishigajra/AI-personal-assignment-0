# a0

Finding whats wrong with the code given.It goes in an Infinite loop since the fringe acts as a stack and it keeps visiting and expanding the same two nodes. Due to this the program never moves towards the solution. Attempt no 1 to fix this is to convert the fringe to work as a queue. It maybe visit repeated nodes but it still reach an answer.
Converted the fringe to work as a queue by changing index parameter in pop(). The program arrives to solution in 16 seconds once search1 is called. There are approximately 32030 elements added to the fringe during the search before finding the solution. Output of the code
 
Started with a heuristic as with manhattan distance and changing fringe such that node with minimum value of total estimated cost = current cost+heurstic estimate higher priority and pop out that element first.
program Got much faster.Even the number of elements in the fringe got reduced.
 
Final out put
 



