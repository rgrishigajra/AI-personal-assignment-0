
#!/usr/local/bin/python3
#
# hide.py : a simple friend-hider
#
# Submitted by : [PUT YOUR NAME AND USERNAME HERE]
#
# Based on skeleton code by D. Crandall and Z. Kachwala, 2019
#
# The problem to be solved is this:
# Given a campus map, find a placement of F friends so that no two can find one another.
#

import sys
import copy

# Parse the map from a given filename
def parse_map(filename):
	with open(filename, "r") as f:
		return [[char for char in line] for line in f.read().split("\n")]

# Count total # of friends on board
def count_friends(board):
    return sum([ row.count('F') for row in board ] )

# Return a string with the board rendered in a human-friendly format
def printable_board(board):
    return "\n".join([ "".join(row) for row in board])

# Add a friend to the board at the given position, and return a new board (doesn't change original)
def add_friend(board, row, col):
    return board[0:row] + [board[row][0:col] + ['F',] + board[row][col+1:]] + board[row+1:]

# Get list of successors of given board state

def successors(board,visible):
    xyz=[]
    for r in range(0, len(board)):
        for c in range(0,len(board[0])):
            visible_new=copy.deepcopy(visible)
            if board[r][c] == '.' and visible_new[r][c]=='0':
                for i in range(c,len(visible_new[0])):
                    flag=0
                    if(board[r][i]=="&")or board[r][i]=="@":
                        flag=1
                    elif(board[r][i]==".") and flag==1:
                        visible_new[r][i]='1'
                flag=0
                for i in range(c,-1,-1):
                    if(board[r][i]=="&")or board[r][i]=="@":
                        flag=1
                    elif(board[r][i]==".")and flag==0:
                        visible_new[r][i]='1'
                flag=0
                for i in range(r,len(visible_new)):
                    if(board[i][c]=="&")or board[i][c]=="@":
                        flag=1
                    elif(board[r][i]==".")and flag==0:
                        visible_new[i][c]='1'
                flag=0
                for i in range(r,-1,-1):
                    if(board[i][c]=="&")or board[i][c]=="@":
                        flag=1
                    elif(board[r][i]=="&")and flag==0:
                        visible_new[i][c]='1'
                xyz.append((add_friend(board, r, c),visible_new))
    #print(xyz)
    return (xyz)

# check if board is a goal state
def is_goal(board):
    return count_friends(board) == K 

# Solve n-rooks!
def solve(initial_board):
    visible=[]
    """for col_i in range(len(initial_board)):
        for row_i in range(len(initial_board[0])):
            colarray_i.append(0)
        visible.append(colarray_i.copy())
        colarray_i.clear()"""
    visible=[['0' for i in range(len(initial_board[0]))] for j in range(len(initial_board))]
    fringe = [(initial_board,visible)]
    while len(fringe) > 0:
        (board,visible)=fringe.pop()
        print(printable_board(board)+'\n\n'+printable_board(visible)+'\n\n\n')
        xyz=successors(board,visible)
        for s in xyz:
            if is_goal(s[0]):
                return(s[0])
           # print("new fringe")
            #print(fringe)
            fringe.append(s)
    return False

# Main Function
if __name__ == "__main__":
    IUB_map=parse_map(sys.argv[1])
    #print(visible)
    # This is K, the number of friends
    K = int(sys.argv[2])
    print ("Starting from initial board:\n" + printable_board(IUB_map) + "\n\nLooking for solution...\n")
    solution = solve(IUB_map)
    print ("Here's what we found:")
    print (printable_board(solution) if solution else "None")


