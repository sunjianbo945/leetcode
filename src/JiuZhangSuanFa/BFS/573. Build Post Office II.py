class Solution:
    """
    @param grid: a 2D grid
    @return: An integer
    """

    def shortestDistance(self, grid):
        # write your code here
        houses = self.find_all_house(grid)

        # visited = set(houses)

        distance = [[0 if grid[i][j] == 0 else float('inf') for j in range(len(grid[0]))] for i in range(len(grid))]
        num_house_can_visit = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]

        for house_x, house_y in houses:
            self.bfs(grid, house_x, house_y, distance, num_house_can_visit)

        return self.find_distance(distance, num_house_can_visit, len(houses))

    def find_distance(self, distance, num_house_can_visit, required):

        total = float('inf')
        for i in range(len(distance)):
            for j in range(len(distance[0])):

                if num_house_can_visit[i][j] == required:
                    total = min(total, distance[i][j])

        return total if total < float('inf') else -1

    def bfs(self, grid, x, y, distance, num_house_can_visit):

        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        queue = [(x, y)]
        visited = {(x, y)}
        total = 1

        while queue:
            size = len(queue)

            for i in range(size):
                cur_x, cur_y = queue.pop(0)

                for d_x, d_y in direction:

                    next_x, next_y = cur_x + d_x, cur_y + d_y

                    if self.is_valid(grid, next_x, next_y) and (next_x, next_y) not in visited:
                        queue.append((next_x, next_y))
                        visited.add((next_x, next_y))
                        distance[next_x][next_y] += total
                        num_house_can_visit[next_x][next_y] += 1

            total += 1

    def is_valid(self, grid, x, y):

        return x >= 0 and y >= 0 and x < len(grid) and y < len(grid[0]) and grid[x][y] == 0

    def find_all_house(self, grid):
        house = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    house.append((i, j))
        return house