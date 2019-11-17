from typing import *

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        total = 0

        visited = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i, j) not in visited:
                    self.visit(grid, i, j, visited)
                    total += 1

        return total

    def visit(self, grid, x, y, visited):

        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        queue = [[x, y]]

        while queue:
            i, j = queue.pop(0)
            for d in direction:
                new_x, new_y = i + d[0], j + d[1]
                if new_x < 0 or new_y < 0 or new_x >= len(grid) or new_y >= len(grid[0]) or grid[new_x][new_y] != '1' or (new_x, new_y) in visited:
                    continue
                else:
                    visited.add((new_x, new_y))
                    queue.append([new_x, new_y])
