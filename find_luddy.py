#!/usr/local/bin/python3
#
# find_luddy.py : a simple maze solver
#
# Submitted by : Rishabh P. Gajra Username:rgajra
#
# Based on skeleton code by Z. Kachwala, 2019
#

import sys
import json
import timeit
# Parse the map from a given filename
def parse_map(filename):
	with open(filename, "r") as f:
		return [[char for char in line] for line in f.read().split("\n")]

# Check if a row,col index pair is on the map
def valid_index(pos, n, m):
	return 0 <= pos[0] < n  and 0 <= pos[1] < m

# Find the possible moves from position (row, col)
def moves(map, row, col):   
    moves=((row+1,col), (row-1,col), (row,col-1), (row,col+1))
    return [ move for move in moves if valid_index(move, len(map), len(map[0])) and (map[move[0]][move[1]] in ".@" ) ]

#creates a heuristic approx for each sidewalk position on the node
def heuristic_generator(IUB_map,luddy_loc):
    heuristic=[]
    colarray_i=[]
    for col_i in range(len(IUB_map[0])):
        for row_i in range(len(IUB_map)):
            colarray_i.append(abs(luddy_loc[0]-row_i)+abs(luddy_loc[1]-col_i))
        heuristic.append(colarray_i.copy())
        colarray_i.clear()
    #print(heuristic)
    return heuristic
#creates an empty array of size of the map
def visited_array(IUB_map):
    visited=[]
    colarray_i=[]
    for col_i in range(len(IUB_map[0])):
        for row_i in range(len(IUB_map)):
            colarray_i.append(0)
        visited.append(colarray_i.copy())
        colarray_i.clear()
    #print(visited)
    return visited
	
#Perform search on the map
def search1(IUB_map):
    # Find my start position
    you_loc=[(row_i,col_i) for col_i in range(len(IUB_map[0])) for row_i in range(len(IUB_map)) if IUB_map[row_i][col_i]=="#"][0] 
	#finding destination location
    luddy_loc=[(row_i,col_i) for col_i in range(len(IUB_map[0])) for row_i in range(len(IUB_map)) if IUB_map[row_i][col_i]=="@"][0]
	#returns an array with each element as manhattan distance from destination
    heuristic=heuristic_generator(IUB_map,luddy_loc)
    visited=visited_array(IUB_map)
    path=[]
    path.append(you_loc[0])#path is an array that stores a string of cordinates that are traversed 
    path.append(you_loc[1])
    fringe=[(you_loc,0,heuristic[you_loc[1]][you_loc[0]],0+heuristic[you_loc[1]][you_loc[0]],path)] #adding heuristic and total cost = current distance+heuristic and path in fringe
    #print(fringe)
    fringe_counter=0
    #print(fringe[0][0])
    while fringe:
        min_index=fringe.index(min(fringe, key=lambda x: x[3])) #lambda function returns minimum value from all fringe element 3 which is the total cost
        (curr_move, curr_dist,heuristic_apx,total_cost,curr_path)=fringe.pop(min_index)
        #print(curr_move, curr_dist,heuristic_apx,total_cost,curr_path[-1])
        fringe_counter+=1
        for move in moves(IUB_map, *curr_move):
            if visited[move[1]][move[0]]==0 :
                visited[move[1]][move[0]]=1
                #print(curr_path[-1],curr_path[-2],curr_move[0],curr_move[1])
                if curr_path[-2]!=(curr_move[0]) or curr_path[-1]!=(curr_move[1]) : 
                    curr_path.append(curr_move[0])
                    curr_path.append(curr_move[1])                
                if IUB_map[move[0]][move[1]]=="@": #destination condition
                    curr_path.append(move[0])
                    curr_path.append(move[1])
                    #print(fringe)
                    #print("lenght of the fringe"+str(fringe_counter))
                    return (curr_dist+1),heuristic_apx,total_cost,curr_path,True
                else:
                    #print(move, curr_dist + 1, heuristic[move[1]][move[0]], curr_dist + 1+ heuristic[move[1]][move[0]],path)
                    fringe.append((move, curr_dist + 1, heuristic[move[1]][move[0]], curr_dist + 1+ heuristic[move[1]][move[0]],curr_path.copy()))
    return 'Inf',0,0,0,False#return inf for no solution

# Main Function
if __name__ == "__main__":
    IUB_map=parse_map(sys.argv[1])
    print("Shhhh... quiet while I navigate!")
    directions=""
    start= timeit.default_timer()    
    curr_dist,heuristic_apx,total_cost,final_path,bol = search1(IUB_map)
    end= timeit.default_timer()
    print("Here's the solution I found:")
    if(bol==False):
        print(curr_dist)
    else:
        for i in range(0,(len(final_path)-2),2):
            if final_path[i]-final_path[i+2]==0:#when move is west
                if(final_path[i+1]-final_path[i+3])==1:
                    directions+="W"
                else:
                    directions+="E" #for move east
            elif final_path[i]-final_path[i+2]==1: #for north
                directions+="N"
            else:
                directions+="S" #for south
        print(curr_dist,directions)
        #print(end-start)
        
    
