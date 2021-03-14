from typing import List


# https://leetcode.com/problems/word-search/
class Solution79:
    def exist(self, board: List[List[str]], word: str) -> bool:  # O(m*n* 3^L)
        m, n = len(board), len(board[0])
        nw = len(word)
        seen = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(x, y, i):
            if i >= nw: return True
            if x < 0 or y < 0 or x >= m or y >= n or (x, y) in seen or board[x][y] != word[i]: return False

            seen.add((x, y))
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if dfs(nx, ny, i + 1): return True
            seen.remove((x, y))
            return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False


# https://leetcode.com/problems/unique-paths-iii/
class Solution980:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        zero_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = [i, j]
                elif grid[i][j] == 0:
                    zero_count += 1

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        seen = set()
        count = 0

        def dfs(x, y):
            nonlocal count, zero_count
            if x < 0 or y < 0 or x >= m or y >= n or (x, y) in seen or grid[x][y] == -1: return

            if grid[x][y] == 2 and zero_count == -1:  # since zero_count will increase by 1 for the starting point
                count += 1
                return

            seen.add((x, y))
            zero_count -= 1
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                dfs(nx, ny)
            zero_count += 1
            seen.remove((x, y))

        dfs(*start)
        return count


# https://leetcode.com/problems/robot-room-cleaner/
class Solution489:
    def cleanRoom(self, robot):
        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def dfs(x, y, d):
            seen.add((x, y))
            robot.clean()
            # going clockwise : 0: 'up', 1: 'right', 2: 'down', 3: 'left' Explore 4 directions : up, right,
            # down, and left (the order is important since the idea is always to turn right)
            for i in range(4):
                new_d = (d + i) % 4
                dx, dy = directions[new_d]
                nx, ny = x + dx, y + dy
                if (nx, ny) not in seen and robot.move():
                    dfs(nx, ny, new_d)
                    go_back()
                # turn the robot following chosen direction : clockwise
                robot.turnRight()

        # going clockwise : 0: 'up', 1: 'right', 2: 'down', 3: 'left'
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        seen = set()
        dfs(0, 0, 0)
