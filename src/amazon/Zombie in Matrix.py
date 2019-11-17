# Given a 2D grid, each cell is either a zombie 1 or a human 0. Zombies can turn adjacent (up/down/left/right) human beings into zombies every hour. Find out how many hours does it take to infect all humans?
#
# Example:
#
# Input:
# [[0, 1, 1, 0, 1],
#  [0, 1, 0, 1, 0],
#  [0, 0, 0, 0, 1],
#  [0, 1, 0, 0, 0]]
#
# Output: 2
#
# Explanation:
# At the end of the 1st hour, the status of the grid:
# [[1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1],
#  [0, 1, 0, 1, 1],
#  [1, 1, 1, 0, 1]]
#
# At the end of the 2nd hour, the status of the grid:
# [[1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1]]

from typing import *

def eat(matrix:List[List[int]])-> int:

    res = 0
    queue = []
    visited=set()

    n_row = len(matrix)
    n_column = len(matrix[0])
    for i in range(n_row):
        for j in range(n_column):
            if matrix[i][j] == 1:
                key = (i,j)
                queue.append(key)
                visited.add(key)



    direction = [[-1,0],[1,0],[0,1],[0,-1]]

    while queue:
        size = len(queue)

        for i in range(size):
            cur_x,cur_y = queue.pop(0)
            for d in direction:
                next_x,next_y = cur_x+d[0] , cur_y+d[1]
                if validate(matrix,next_x,next_y,visited):
                    queue.append((next_x,next_y))
                    visited.add((next_x,next_y))

        if len(visited) == n_column * n_row: return res

        res +=1

    return res

def validate(matrix, x, y , visited):

    return x>0 and y >0 and x<len(matrix) and y < len(matrix[0]) and matrix[x][y]==0 and (x,y) not in visited

print(eat(
[[0, 1, 1, 0, 1],
 [0, 1, 0, 1, 0],
 [0, 0, 0, 0, 1],
 [0, 1, 0, 0, 0]]))


