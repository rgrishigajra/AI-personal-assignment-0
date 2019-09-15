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

def heuristic_generator(IUB_map,luddy_loc):
    heuristic=[]
    colarray_i=[]
    for col_i in range(len(IUB_map[0])):
        for row_i in range(len(IUB_map)):
            colarray_i.append(luddy_loc[0]-row_i+luddy_loc[1]-col_i)
        heuristic.append(colarray_i.copy())
        colarray_i.clear()
    print(heuristic)
# Perform search on the map
def search1(IUB_map):
	# Find my start position
    you_loc=[(row_i,col_i) for col_i in range(len(IUB_map[0])) for row_i in range(len(IUB_map)) if IUB_map[row_i][col_i]=="#"][0]
    fringe=[(you_loc,0)]
    fringe_counter=1
    luddy_loc=[(row_i,col_i) for col_i in range(len(IUB_map[0])) for row_i in range(len(IUB_map)) if IUB_map[row_i][col_i]=="@"][0]
    print(luddy_loc[0],luddy_loc[1])
    heuristic_generator(IUB_map,luddy_loc)
    while fringe:
        (curr_move, curr_dist)=fringe.pop(0)
        fringe_counter+=1
        for move in moves(IUB_map, *curr_move):
            if IUB_map[move[0]][move[1]]=="@":
                print("lenght of the fringe"+str(fringe_counter))
                return curr_dist+1
            else:
                fringe.append((move, curr_dist + 1))

# Main Function
if __name__ == "__main__":
    IUB_map=parse_map(sys.argv[1])
    print("Shhhh... quiet while I navigate!")
    start= timeit.default_timer()    
    solution = search1(IUB_map)
    end= timeit.default_timer()    
    print("Here's the solution I found:")
    print(solution)
    print("Time:")
    print(end-start)
    
