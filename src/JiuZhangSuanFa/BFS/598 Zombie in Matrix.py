#  [LintCode] 598 Zombie in Matrix 解题报告
# Description
# Given a 2D grid, each cell is either a wall 2, a zombie 1 or people 0 (the number zero, one, two).
# Zombies can turn the nearest people(up/down/left/right) into zombies every day, but can not through wall.
# How long will it take to turn all people into zombies? Return -1 if can not turn all people into zombies.
#
#
# Example
# Given a matrix:
#
# 0 1 2 0 0
# 1 0 0 2 1
# 0 1 0 0 0
# return 2


class Solution:

    def zombie(self, grid):

        total =0
        direction = [[0,1],[0,-1],[1,0],[-1,0]]
        visited=set()
        pre_zero = self.num_zero(grid)
        while pre_zero:
            for i in range(len(grid)):
                for j in range(len(grid[0])):

                    if grid[i][j]==1:

                        for d in direction:
                            x,y=i+d[0],j+d[1]
                            if x<0 or y<0 or x>=len(grid) or y>= len(grid[0]) or grid[x][y]!=0:
                                continue
                            visited.add((x,y))

            for point in visited:
                grid[point[0]][point[1]] = 1

            visited.clear()
            total+=1
            cur_zero = self.num_zero(grid)
            if cur_zero==pre_zero:
                return -1
            else:
                pre_zero=cur_zero

        return total



    def num_zero(self,grid):
        num=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] ==0:
                    num+=1

        return num






