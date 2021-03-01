from collections import defaultdict
from typing import *


# https://leetcode.com/problems/number-of-islands/
class Solution200:
    def numIslands_bfs(self, grid: List[List[str]]) -> int:  # O(m*n), O(m*n)
        m, n = len(grid), len(grid[0])
        seen = set()  # record all island has visited
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def bfs(x, y):
            queue = [(x, y)]
            seen.add((x, y))

            while queue:
                x, y = queue.pop(0)
                for dx, dy in direction:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or ny < 0 or nx >= m or ny >= n \
                            or grid[nx][ny] == '0' or (nx, ny) in seen: continue

                    seen.add((nx, ny))
                    queue.append((nx, ny))

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in seen:
                    bfs(i, j)
                    res += 1

        return res

    def numIslands_dfs(self, grid: List[List[str]]) -> int:  # O(m*n), O(m*n)
        m, n = len(grid), len(grid[0])
        seen = set()  # record all island has visited
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(x, y):
            if x < 0 or y < 0 or x >= m or y >= n \
                    or grid[x][y] == '0' or (x, y) in seen: return

            seen.add((x, y))

            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                dfs(nx, ny)

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in seen:
                    dfs(i, j)
                    res += 1

        return res


# https://leetcode.com/problems/max-area-of-island/
class Solution695:
    def maxAreaOfIsland_bfs(self, grid: List[List[int]]) -> int:  # O(m*n), O(m*n)
        m, n = len(grid), len(grid[0])
        seen = set()  # record all island has visited
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def bfs(x, y):
            queue = [(x, y)]
            seen.add((x, y))
            count = 0

            while queue:
                x, y = queue.pop(0)
                count += 1
                for dx, dy in direction:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or ny < 0 or nx >= m or ny >= n \
                            or grid[nx][ny] == 0 or (nx, ny) in seen: continue

                    seen.add((nx, ny))
                    queue.append((nx, ny))

            return count

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in seen:
                    res = max(res, bfs(i, j))

        return res

    def maxAreaOfIsland_dfs(self, grid: List[List[int]]) -> int:  # O(m*n), O(m*n)
        m, n = len(grid), len(grid[0])
        seen = set()  # record all island has visited
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(x, y):
            if x < 0 or y < 0 or x >= m or y >= n \
                    or grid[x][y] == 0 or (x, y) in seen: return 0

            seen.add((x, y))
            count = 1  # find one island
            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                count += dfs(nx, ny)

            return count

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in seen:
                    res = max(dfs(i, j), res)

        return res


# https://leetcode.com/problems/surrounded-regions/
class Solution130:
    def solve_dfs(self, board: List[List[str]]) -> None:  # O(m*n), O(m*n)
        """
        Do not return anything, modify board in-place instead.
        """
        # idea is to mark the O on the boundary
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        m, n = len(board), len(board[0])
        seen = set()  # marks all x,y should not be change

        def dfs(x, y):
            if x < 0 or y < 0 or x >= m or y >= n or board[x][y] == 'X' or (x, y) in seen: return

            seen.add((x, y))

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                dfs(nx, ny)

        for i in range(n):
            dfs(0, i)
            dfs(m - 1, i)

        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)

        for i in range(m):
            for j in range(n):
                board[i][j] = 'X' if (i, j) not in seen else 'O'

    def solve_bfs(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # idea is to mark the O on the boundary
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        m, n = len(board), len(board[0])
        seen = set()  # marks all x,y should not be change

        def bfs(x, y):
            if board[x][y] == 'X': return
            queue = [(x, y)]
            seen.add((x, y))
            while queue:
                x, y = queue.pop(0)
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or ny < 0 or nx >= m or ny >= n or board[nx][ny] == 'X' or (nx, ny) in seen: continue

                    seen.add((nx, ny))
                    queue.append((nx, ny))

        for i in range(n):
            bfs(0, i)
            bfs(m - 1, i)

        for i in range(m):
            bfs(i, 0)
            bfs(i, n - 1)

        for i in range(m):
            for j in range(n):
                board[i][j] = 'X' if (i, j) not in seen else 'O'


# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
class Solution323:
    def countComponents_dfs(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        seen = set()

        def dfs(node):
            if node in seen: return

            seen.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)

        res = 0
        for i in range(n):
            if i in seen: continue

            res += 1
            dfs(i)

        return res

    def countComponents_bfs(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        seen = set()

        def bfs(node):
            queue = [node]
            seen.add(node)
            while queue:
                node = queue.pop(0)
                for neighbor in graph[node]:
                    if neighbor in seen: continue
                    queue.append(neighbor)
                    seen.add(neighbor)

        res = 0
        for i in range(n):
            if i in seen: continue

            res += 1
            bfs(i)

        return res


# https://leetcode.com/problems/flood-fill/
class Solution733:
    def floodFill_dfs(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        seen = set()
        m, n = len(image), len(image[0])
        old = image[sr][sc]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(x, y):
            if x < 0 or y < 0 or x >= m or y >= n or (x, y) in seen or image[x][y] != old:
                return

            seen.add((x, y))
            image[x][y] = newColor

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                dfs(nx, ny)

        dfs(sr, sc)
        return image

    def floodFill_bfs(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        seen = set()
        m, n = len(image), len(image[0])
        old = image[sr][sc]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def bfs(x, y):
            queue = [(x, y)]
            seen.add((x, y))
            while queue:
                x, y = queue.pop(0)
                image[x][y] = newColor

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or ny < 0 or nx >= m or ny >= n or (nx, ny) in seen or image[nx][ny] != old:
                        continue

                    seen.add((nx, ny))
                    queue.append((nx, ny))

        bfs(sr, sc)
        return image


# https://leetcode.com/problems/number-of-distinct-islands/
class Solution694:
    def numDistinctIslands_dfs(self, grid: List[List[int]]) -> int:
        seen = set()
        directions = [['r', 0, 1], ['l', 0, -1], ['u', 1, 0], ['d', -1, 0]]
        m, n = len(grid), len(grid[0])

        def dfs(x, y):  # return encoded the traversal path
            if x < 0 or y < 0 or x >= m or y >= n or (x, y) in seen or grid[x][y] == 0:
                return '#'

            path = ''
            seen.add((x, y))
            for direct, dx, dy in directions:
                nx, ny = x + dx, y + dy
                path += direct + dfs(nx, ny)

            return path

        paths = set()
        res = 0
        for i in range(m):
            for j in range(n):
                if (i, j) in seen or grid[i][j] == 0: continue

                path = dfs(i, j)
                if path in paths: continue

                res += 1
                paths.add(path)

        return res

    def numDistinctIslands_bfs(self, grid: List[List[int]]) -> int:
        seen = set()
        directions = [['r', 0, 1], ['l', 0, -1], ['u', 1, 0], ['d', -1, 0]]
        m, n = len(grid), len(grid[0])

        def bfs(x, y):  # return encoded the traversal path
            queue = [(x, y)]
            seen.add((x, y))
            path = ''
            while queue:
                x, y = queue.pop(0)

                for direct, dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or ny < 0 or nx >= m or ny >= n or (nx, ny) in seen or grid[nx][ny] == 0:
                        path += '#'
                        continue
                    path += direct
                    seen.add((nx, ny))
                    queue.append((nx, ny))

            return path

        paths = set()
        res = 0
        for i in range(m):
            for j in range(n):
                if (i, j) in seen or grid[i][j] == 0: continue

                path = bfs(i, j)
                if path in paths: continue

                res += 1
                paths.add(path)

        return res


# https://leetcode.com/problems/island-perimeter/
class Solution463:
    def islandPerimeter_bfs(self, grid: List[List[int]]) -> int:
        seen = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        m, n = len(grid), len(grid[0])

        def bfs(x, y):
            queue = [(x, y)]
            seen.add((x, y))

            count = 0
            while queue:
                x, y = queue.pop(0)

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or ny < 0 or nx >= m or ny >= n or grid[nx][ny] == 0:
                        count += 1
                        continue

                    if (nx, ny) in seen: continue

                    queue.append((nx, ny))
                    seen.add((nx, ny))

            return count

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: continue

                return bfs(i, j)

        return 0

    def islandPerimeter_dfs(self, grid: List[List[int]]) -> int:
        seen = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        m, n = len(grid), len(grid[0])

        def dfs(x, y):
            if x < 0 or y < 0 or x >= m or y >= n or grid[x][y] == 0:
                return 1

            if (x, y) in seen: return 0

            seen.add((x, y))
            count = 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                count += dfs(nx, ny)

            return count

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: continue

                return dfs(i, j)

        return 0


# https://leetcode.com/problems/number-of-provinces/
class Solution547:
    def findCircleNum_bfs(self, grid: List[List[int]]) -> int:
        graph = defaultdict(set)
        n = len(grid)
        for i in range(n):
            for j in range(1 + i, n):
                if grid[i][j] == 1:
                    graph[i].add(j)
                    graph[j].add(i)

        seen = set()

        def bfs(node):
            queue = [node]
            seen.add(node)

            while queue:
                node = queue.pop(0)
                for neighbor in graph[node]:
                    if neighbor in seen: continue

                    seen.add(neighbor)
                    queue.append(neighbor)

        count = 0
        for i in range(n):
            if i in seen: continue

            count += 1
            bfs(i)

        return count

    def findCircleNum_dfs(self, grid: List[List[int]]) -> int:
        graph = defaultdict(set)
        n = len(grid)
        for i in range(n):
            for j in range(1 + i, n):
                if grid[i][j] == 1:
                    graph[i].add(j)
                    graph[j].add(i)

        seen = set()

        def dfs(node):
            if node in seen: return

            seen.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)

        count = 0
        for i in range(n):
            if i in seen: continue

            count += 1
            dfs(i)

        return count
