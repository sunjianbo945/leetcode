from collections import defaultdict, deque
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

    def numIslands_dfs2(self, grid: List[List[str]]) -> int:  # O(m*n), O(m*n)
        m, n = len(grid), len(grid[0])
        seen = set()  # record all island has visited
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(x, y):
            stack = [(x, y)]
            seen.add((x, y))

            while stack:
                x, y = stack.pop()
                for dx, dy in direction:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or ny < 0 or nx >= m or ny >= n \
                            or grid[nx][ny] == '0' or (nx, ny) in seen: continue

                    seen.add((nx, ny))
                    stack.append((nx, ny))

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in seen:
                    dfs(i, j)
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


# https://leetcode.com/problems/number-of-closed-islands/
class Solution1254:
    def closedIsland_dfs(self, grid: List[List[int]]) -> int:
        seen = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        m, n = len(grid), len(grid[0])

        def dfs(x, y):
            if x < 0 or y < 0 or x >= m or y >= n or grid[x][y] == 1 or (x, y) in seen: return

            seen.add((x, y))
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                dfs(nx, ny)

        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)

        for i in range(n):
            dfs(0, i)
            dfs(m - 1, i)

        res = 0
        for i in range(m):
            for j in range(n):
                if (i, j) not in seen and grid[i][j] == 0:
                    res += 1
                    dfs(i, j)
        return res

    def closedIsland_bfs(self, grid: List[List[int]]) -> int:
        seen = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        m, n = len(grid), len(grid[0])

        def bfs(x, y):
            if grid[x][y] != 0: return
            queue = [(x, y)]
            seen.add((x, y))
            while queue:
                x, y = queue.pop(0)
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or ny < 0 or nx >= m or ny >= n or (nx, ny) in seen or grid[nx][ny] == 1: continue

                    seen.add((nx, ny))
                    queue.append((nx, ny))

        for i in range(m):
            bfs(i, 0)
            bfs(i, n - 1)

        for i in range(n):
            bfs(0, i)
            bfs(m - 1, i)

        res = 0
        for i in range(m):
            for j in range(n):
                if (i, j) not in seen and grid[i][j] == 0:
                    res += 1
                    bfs(i, j)
        return res


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


# https://leetcode.com/problems/minesweeper/
class Solution529:
    def updateBoard_dfs(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        x, y = click
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board

        directions = [(i, j) for j in range(-1, 2) for i in range(-1, 2)]

        def countMines(x, y):
            count = 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'M':
                    count += 1
            return count

        seen = set()

        def dfs(x, y):
            if x < 0 or y < 0 or x >= m or y >= n or (x, y) in seen or board[x][y] == 'M': return

            seen.add((x, y))
            count = countMines(x, y)
            board[x][y] = str(count) if count else 'B'
            if count: return

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                dfs(nx, ny)

        dfs(x, y)
        return board

    def updateBoard_bfs(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        x, y = click
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board

        directions = [(i, j) for j in range(-1, 2) for i in range(-1, 2)]

        def countMines(x, y):
            count = 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'M':
                    count += 1
            return count

        queue = [(x, y)]
        seen = {(x, y)}

        while queue:
            x, y = queue.pop(0)

            count = countMines(x, y)
            board[x][y] = str(count) if count else 'B'
            if count: continue

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if nx < 0 or ny < 0 or nx >= m or ny >= n or (nx, ny) in seen or board[nx][ny] == 'M': continue

                seen.add((nx, ny))
                queue.append((nx, ny))

        return board


# 1d example
# https://leetcode.com/problems/sequential-digits/
class Solution1291:
    def sequentialDigits_bfs(self, low: int, high: int) -> List[int]:  # O(log max)
        nums = [i for i in range(1, 10)]

        queue = [(num, num - 1) for num in nums]  # number and position
        res = []
        while queue:
            num, pos = queue.pop(0)
            if num > high: continue

            if low <= num <= high:
                res.append(num)

            if pos >= 8: continue
            num = 10 * num + nums[pos + 1]
            queue.append((num, pos + 1))

        return res

    def sequentialDigits_dfs(self, low: int, high: int) -> List[int]:
        nums = [i for i in range(1, 10)]

        res = []

        def dfs(index, number, res):
            if number > high: return
            if low <= number <= high: res.append(number)
            if index >= 8: return

            dfs(index + 1, 10 * number + nums[index + 1], res)

        for i in range(len(nums)):
            dfs(i, nums[i], res)

        return sorted(res)


# https://leetcode.com/problems/nested-list-weight-sum/
class Solution339:
    def depthSum_dfs(self, nestedList) -> int:  # O(n), O(n)

        def dfs(nest_list, depth):
            n = len(nest_list)
            res = 0
            for i in range(n):
                curr = nest_list[i]
                if curr.isInteger():
                    res += curr.getInteger() * depth
                else:
                    res += dfs(curr.getList(), depth + 1)

            return res

        return dfs(nestedList, 1)

    def depthSum_bfs(self, nestedList) -> int:  # O(n), O(n)
        queue = list(nestedList)
        level = 1
        res = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                curr = queue.pop(0)

                if curr.isInteger():
                    res += level * curr.getInteger()
                else:
                    for neighbor in curr.getList():
                        queue.append(neighbor)

            level += 1

        return res


# https://leetcode.com/problems/nested-list-weight-sum-ii/
class Solution364:
    def depthSumInverse_bfs(self, nestedList) -> int:
        queue = list(nestedList)
        level = 1
        level_num = []
        while queue:
            size = len(queue)
            for _ in range(size):
                curr = queue.pop(0)

                if curr.isInteger():
                    level_num.append((level, curr.getInteger()))
                else:
                    for neighbor in curr.getList():
                        queue.append(neighbor)

            level += 1

        res = 0
        for l, num in level_num:
            res += (level - l) * num

        return res

    def depthSumInverse_dfs(self, nestedList) -> int:
        depth_level = defaultdict(list)

        def dfs(l, depth):
            n = len(l)
            for i in range(n):
                curr = l[i]
                if curr.isInteger():
                    depth_level[depth].append(curr.getInteger())
                else:
                    dfs(curr.getList(), depth + 1)

        dfs(nestedList, 1)

        keys = depth_level.keys()
        if not keys: return 0

        max_depth = max(keys) + 1

        res = 0
        for depth, nums in depth_level.items():
            res += (max_depth - depth) * sum(nums)

        return res


# https://leetcode.com/problems/making-a-large-island/
class Solution827:
    def largestIsland_dfs(self, grid: List[List[int]]) -> int:  # O(n^2) O(n^2)
        m, n = len(grid), len(grid[0])
        grid = [[grid[i][j] for j in range(n)] for i in range(m)]
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def dfs(x, y, label):
            if x < 0 or y < 0 or x >= m or y >= n or grid[x][y] != 1: return 0

            grid[x][y] = label
            res = 1
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                res += dfs(nx, ny, label)

            return res

        label = 2
        label_area = defaultdict(int)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    label_area[label] = dfs(i, j, label)
                    label += 1

        res = max(label_area.values() or [0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    seen = set()
                    temp = 1
                    for dx, dy in directions:
                        nx, ny = i + dx, j + dy
                        if nx < 0 or ny < 0 or nx >= m or ny >= n or grid[nx][ny] in seen: continue
                        seen.add(grid[nx][ny])
                        temp += label_area[grid[nx][ny]]

                    res = max(res, temp)

        return res

    def largestIsland_bfs(self, grid: List[List[int]]) -> int:  # O(n^2) O(n^2)
        m, n = len(grid), len(grid[0])
        grid = [[grid[i][j] for j in range(n)] for i in range(m)]
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def bfs(x, y, label):
            queue = [(x, y)]
            res = 0
            seen = {(x, y)}
            while queue:
                x, y = queue.pop(0)
                res += 1
                grid[x][y] = label

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or ny < 0 or nx >= m or ny >= n or (nx, ny) in seen or grid[nx][ny] != 1: continue

                    seen.add((nx, ny))
                    queue.append((nx, ny))

            return res

        label = 2
        label_area = defaultdict(int)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    label_area[label] = bfs(i, j, label)
                    label += 1

        res = max(label_area.values() or [0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    seen = set()
                    temp = 1
                    for dx, dy in directions:
                        nx, ny = i + dx, j + dy
                        if nx < 0 or ny < 0 or nx >= m or ny >= n or grid[nx][ny] in seen: continue
                        seen.add(grid[nx][ny])
                        temp += label_area[grid[nx][ny]]

                    res = max(res, temp)

        return res


# https://leetcode.com/problems/employee-importance/
class Solution690:
    def getImportance_dfs(self, employees: List['Employee'], target_id: int) -> int:
        empid_emp = defaultdict()
        for emp in employees:
            empid_emp[emp.id] = emp

        def dfs(emp):
            if not emp: return 0

            res = emp.importance
            for sub in emp.subordinates:
                res += dfs(empid_emp[sub])

            return res

        return dfs(empid_emp[target_id])

    def getImportance_bfs(self, employees: List['Employee'], target_id: int) -> int:
        empid_emp = defaultdict()
        for emp in employees:
            empid_emp[emp.id] = emp

        target = empid_emp[target_id]
        queue = [target]
        res = 0

        while queue:
            emp = queue.pop(0)
            res += emp.importance
            for sub in emp.subordinates:
                queue.append(empid_emp[sub])

        return res


# https://leetcode.com/problems/accounts-merge/
class Solution721:
    def accountsMerge_dfs(self, accounts: List[List[str]]) -> List[List[str]]:
        email_name = defaultdict()
        email_email = defaultdict(set)
        for account in accounts:
            n = len(account)
            for i in range(1, n):
                email_name[account[i]] = account[0]
                email_email[account[i]].update(account[1:])

        seen = set()

        def dfs(email, res):
            if email in seen: return

            seen.add(email)
            res.append(email)
            for neighbor in email_email[email]:
                dfs(neighbor, res)

        res = []
        for email, _ in email_email.items():
            if email in seen: continue
            same_account = []
            dfs(email, same_account)
            same_account.sort()
            res.append([email_name[email]] + same_account)

        return res

    def accountsMerge_bfs(self, accounts: List[List[str]]) -> List[List[str]]:
        email_name = defaultdict()
        email_email = defaultdict(set)
        for account in accounts:
            n = len(account)
            for i in range(1, n):
                email_name[account[i]] = account[0]
                email_email[account[i]].update(account[1:])

        seen = set()

        def bfs(email):
            queue = [email]
            seen.add(email)
            res = []
            while queue:
                email = queue.pop(0)

                res.append(email)

                for neighbor in email_email[email]:
                    if neighbor in seen: continue

                    seen.add(neighbor)
                    queue.append(neighbor)
            return res

        res = []
        for email, _ in email_email.items():
            if email in seen: continue
            same_account = bfs(email)
            same_account.sort()
            res.append([email_name[email]] + same_account)

        return res


class Solution:
    def findRedundantConnection_dfs(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)

        def dfs(source, target):
            if source in seen: return False

            seen.add(source)
            if source == target: return True
            return any(dfs(neighbor, target) for neighbor in graph[source])

        for u, v in edges:
            seen = set()
            # this part is the key part, if both node has been seen and they can reach out each out, then retrun
            if u in graph and v in graph and dfs(u, v):
                return u, v
            graph[u].add(v)
            graph[v].add(u)

    def findRedundantConnection_bfs(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)

        def bfs(source, target):
            queue = [source]
            seen = {source}
            while queue:
                node = queue.pop(0)
                if node == target: return True

                for neighbor in graph[node]:
                    if neighbor in seen: continue

                    seen.add(neighbor)
                    queue.append(neighbor)
            return False

        for u, v in edges:
            if u in graph and v in graph and bfs(u, v):
                return u, v
            graph[u].add(v)
            graph[v].add(u)


# https://leetcode.com/problems/sentence-similarity-ii/
class Solution737:
    def areSentencesSimilarTwo_dfs(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2): return False
        graph = defaultdict(set)
        for w1, w2 in pairs:
            graph[w1].add(w2)
            graph[w2].add(w1)

        def dfs(source, target):
            if source == target: return True
            if source in seen: return False

            seen.add(source)

            return any(dfs(neighbor, target) for neighbor in graph[source])

        for w1, w2 in zip(words1, words2):
            if w1 == w2: continue
            seen = set()
            if not dfs(w1, w2):
                return False

        return True

    def areSentencesSimilarTwo_bfs(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2): return False
        graph = defaultdict(set)
        for w1, w2 in pairs:
            graph[w1].add(w2)
            graph[w2].add(w1)

        def bfs(source, target):
            queue = [source]
            seen = {source}
            while queue:
                node = queue.pop(0)
                if node == target: return True

                for neighbor in graph[node]:
                    if neighbor in seen: continue

                    seen.add(neighbor)
                    queue.append(neighbor)
            return False

        for w1, w2 in zip(words1, words2):
            if w1 == w2: continue
            if not bfs(w1, w2):
                return False

        return True


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# https://leetcode.com/problems/clone-graph/
class Solution133:
    def cloneGraph_dfs(self, node: 'Node') -> 'Node':
        seen = defaultdict()

        def dfs(node):
            if not node: return None
            if node.val in seen: return seen[node.val]

            copied = Node(node.val)
            seen[node.val] = copied
            for neighbor in node.neighbors:
                copied.neighbors.append(dfs(neighbor))

            return copied

        return dfs(node)

    def cloneGraph_bfs(self, node: 'Node') -> 'Node':
        if not node: return
        seen = {node: Node(node.val)}
        queue = [node]
        while queue:
            curr = queue.pop(0)
            for neighbor in curr.neighbors:
                if neighbor in seen:
                    seen[curr].neighbors.append(seen[neighbor])
                    continue

                seen[neighbor] = Node(neighbor.val)
                seen[curr].neighbors.append(seen[neighbor])
                queue.append(neighbor)

        return seen[node]


# https://leetcode.com/problems/knight-probability-in-chessboard/
class Solution668:
    def knightProbability_dfs(self, N: int, K: int, r: int, c: int) -> float:
        directions = {(dx, dy) for dx in (-2, -1, 1, 2) for dy in (-2, -1, 1, 2) if abs(dx) + abs(dy) == 3}

        def dfs(x, y, k):  # O(8^{N^2K}) can use cache to get O(n^2 * 8 * k)
            if x < 0 or y < 0 or x >= N or y >= N: return 0
            if k == 0: return 1

            res = 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                res += dfs(nx, ny, k - 1)

            return res

        return dfs(r, c, K) / 8 ** K

    # This is critical using dict as queue instead of queue to traversal
    def knightProbability_bfs(self, N: int, K: int, r: int, c: int) -> float:
        q = {(r, c): 1}
        level = 0
        directions = {(dx, dy) for dx in (-2, -1, 1, 2) for dy in (-2, -1, 1, 2) if abs(dx) + abs(dy) == 3}
        is_in_board = lambda r, c: 0 <= r < N and 0 <= c < N
        while level < K and q:
            next_q = defaultdict(int)
            for coord, count in q.items():
                x, y = coord
                for dx, dy in directions:
                    if is_in_board(x + dx, y + dy):
                        next_q[(x + dx, y + dy)] += count
            q = next_q
            level += 1

        return sum(q.values()) / 8 ** K


# https://leetcode.com/problems/the-maze/
class Solution490:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        m, n = len(maze), len(maze[0])
        seen = set()

        def dfs(x, y):
            if (x, y) in seen: return False
            if [x, y] == destination: return True

            seen.add((x, y))
            for dx, dy in directions:
                nx, ny = x, y
                while 0 <= nx + dx < m and 0 <= ny + dy < n and maze[nx + dx][ny + dy] != 1:
                    nx, ny = nx + dx, ny + dy

                if dfs(nx, ny): return True

            return False

        return dfs(*start)

    def hasPath_bfs(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        m, n = len(maze), len(maze[0])
        queue = [start]
        seen = set(start)
        while queue:
            x, y = queue.pop(0)
            if [x, y] == destination: return True
            for dx, dy in directions:
                nx, ny = x, y
                while 0 <= nx + dx < m and 0 <= ny + dy < n and maze[nx + dx][ny + dy] != 1:
                    nx, ny = nx + dx, ny + dy

                if (nx, ny) in seen: continue

                seen.add((nx, ny))
                queue.append((nx, ny))

        return False


# https://leetcode.com/problems/possible-bipartition/
class Solution886:
    def possibleBipartition_dfs(self, N, dislikes):
        graph = defaultdict(set)
        for a, b in dislikes:
            graph[a].add(b)
            graph[b].add(a)

        colors = [0] * N

        def dfs(i, color):
            if colors[i - 1] == 0:
                colors[i - 1] = color
            else:
                return colors[i - 1] == color

            for dislike in graph[i]:
                if not dfs(dislike, -color): return False

            return True

        for i in range(1, N + 1):
            if colors[i - 1] == 0 and not dfs(i, 1):
                return False

        return True

    def possibleBipartition_bfs(self, N, dislikes):
        graph = defaultdict(list)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        colors = [0] * N

        def bfs(i, color):
            queue = deque([i])
            while queue:
                size = len(queue)
                for _ in range(size):
                    node = queue.popleft()

                    colors[node - 1] = color

                    for neighbor in graph[node]:
                        neighbor_color = colors[neighbor - 1]
                        if neighbor_color != 0:
                            if neighbor_color == -color:
                                continue
                            else:
                                return False
                        queue.append(neighbor)

                color = -color

            return True

        for i in range(1, N + 1):
            if colors[i - 1] == 0 and not bfs(i, 1):
                return False

        return True
