#  [LintCode] 611 Knight Shortest Path 解题报告
# Description
# Given a knight in a chessboard (a binary matrix with 0 as empty and 1 as barrier) with a source position, find the shortest path to a destination position, return the length of the route.
# Return -1 if knight can not reached.
#
# Notice
# source and destination must be empty.
# Knight can not enter the barrier.
#
#
# Clarification
# If the knight is at (x, y), he can get to the following positions in one step:
#
# (x + 1, y + 2)
# (x + 1, y - 2)
# (x - 1, y + 2)
# (x - 1, y - 2)
# (x + 2, y + 1)
# (x + 2, y - 1)
# (x - 2, y + 1)
# (x - 2, y - 1)
#
#
# Example
# [[0,0,0],
#  [0,0,0],
#  [0,0,0]]
# source = [2, 0] destination = [2, 2] return 2
#
# [[0,1,0],
#  [0,0,0],
#  [0,0,0]]
# source = [2, 0] destination = [2, 2] return 6
#
# [[0,1,0],
#  [0,0,1],
#  [0,0,0]]
# source = [2, 0] destination = [2, 2] return -1

class Solution:

    def knight(self, grid, source, destination):
        direction = [[1,2],[1,-2],[-1,2],[-1,-2],[2,1],[2,-1],[-2,1],[-2,-1]]
        queue = [destination]
        visited = set()
        visited.add((destination[0],destination[1]))
        total =0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:visited.add((i,j))


        while queue:
            size = len(queue)

            for _ in range(size):

                cur = queue.pop()
                if cur==source:
                    return total
                for d in direction:
                    x,y = d[0]+cur[0] , d[1]+cur[1]
                    if x<0 or y<0 or x>=len(grid) or y>=len(grid[0]) or (x,y) in visited:
                        continue
                    queue.append([x,y])
                    visited.add((x,y))

            total+=1

        return -1





