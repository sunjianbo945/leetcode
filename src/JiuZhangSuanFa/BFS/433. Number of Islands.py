class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """

    def numIslands(self, grid):
        # write your code here

        queue = []
        visited = set()
        total = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] and (i, j) not in visited:
                    queue.append((i, j))
                    visited.add((i, j))
                    self.find_land(grid, queue, visited)
                    total += 1

        return total

    def find_land(self, grid, queue, visited):

        direction = [[0, 1], [-1, 0], [1, 0], [0, -1]]

        while queue:

            cur = queue.pop(0)

            for d in direction:
                x, y = cur[0] + d[0], cur[1] + d[1]
                if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or not grid[x][y] or (x, y) in visited:
                    continue

                queue.append((x, y))
                visited.add((x, y))





