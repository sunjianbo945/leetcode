from collections import defaultdict
from typing import List


# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/
class Solution1466:
    def minReorder_bfs(self, n: int, connections: List[List[int]]) -> int:
        road = defaultdict(set)
        for src, dest in connections:
            road[src].add((dest, 1))  # from 0 -> 1 is free, but it needs reverse raod 1 -> 0 and cost is 1
            road[dest].add((src, 0))

        total = 0
        queue = [0]
        seen = [0] * n
        seen[0] = 1

        while queue:
            curr = queue.pop(0)
            for neighbor, cost in road[curr]:
                if seen[neighbor] == 1: continue

                seen[neighbor] = 1
                total += cost
                queue.append(neighbor)

        return total

    def minReorder_dfs(self, n: int, connections: List[List[int]]) -> int:
        road = defaultdict(set)
        for src, dest in connections:
            road[src].add((dest, 1))  # from 0 -> 1 is free, but it needs reverse raod 1 -> 0 and cost is 1
            road[dest].add((src, 0))

        total = 0
        seen = [0] * n
        seen[0] = 1

        def dfs(city):
            nonlocal total
            seen[city] = 1
            for neighbor, cost in road[city]:
                if seen[neighbor] == 1: continue

                total += cost
                dfs(neighbor)

        dfs(0)
        return total


# https://leetcode.com/problems/sliding-puzzle/
class Solution773:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        moves = {0: (1, 3), 1: (0, 2, 4), 2: (1, 5), 3: (0, 4), 4: (1, 3, 5), 5: (2, 4)}
        m, n = len(board), len(board[0])
        state = "".join(str(board[i][j]) for i in range(m) for j in range(n))
        start = state.index('0')
        seen = set()

        queue = [(start, state)]
        steps = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                curr, state = queue.pop(0)
                if state == '123450': return steps

                for nxt in moves[curr]:
                    tmp = list(state)
                    tmp[cur], tmp[nxt] = tmp[nxt], tmp[cur]
                    tmp = ''.join(tmp)

                    if tmp in seen: continue

                    seen.add(tmp)
                    queue.append((nxt, tmp))
            steps += 1
        return -1


# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/
class Solution1293:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        queue = [(0, 0, 0)]
        seen = {(0, 0): 0}
        steps = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                x, y, obs = queue.pop(0)

                if x == m - 1 and y == n - 1: return steps

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or ny < 0 or nx >= m or ny >= n: continue

                    nobs = obs + (1 if grid[nx][ny] == 1 else 0)
                    if nobs > k: continue
                    if (nx, ny) in seen and seen[
                        nx, ny] <= nobs: continue  # has pass the position with same or lower obstacles

                    seen[nx, ny] = nobs
                    queue.append((nx, ny, nobs))

            steps += 1

        return - 1