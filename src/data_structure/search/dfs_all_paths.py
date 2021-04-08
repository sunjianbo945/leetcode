from functools import lru_cache
from typing import *


# https://leetcode.com/problems/generate-parentheses/
class Solution22:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(l, r, curr):
            if l == r == n:
                res.append(''.join(curr))
                return

            if l < n:
                curr.append('(')
                dfs(l + 1, r, curr)
                curr.pop()

            if r < l:
                curr.append(')')
                dfs(l, r + 1, curr)
                curr.pop()

        dfs(0, 0, [])
        return res


# https://leetcode.com/problems/n-queens/
class Solution51:
    def solveNQueens(self, n: int) -> List[List[str]]:
        column_seen = set()
        # important for a few questions
        dig_seen = set()  # assign row - column
        rdig_seen = set()  # assign row + column

        grid = [['.'] * n for _ in range(n)]
        res = []

        def dfs(r):  # row
            if r >= n:
                res.append([''.join(grid[i]) for i in range(n)])
                return

            for c in range(n):  # column
                if c in column_seen or c + r in rdig_seen or r - c in dig_seen: continue
                column_seen.add(c)
                rdig_seen.add(r + c)
                dig_seen.add(r - c)
                grid[r][c] = 'Q'

                dfs(r + 1)

                grid[r][c] = '.'
                column_seen.remove(c)
                rdig_seen.remove(r + c)
                dig_seen.remove(r - c)

        dfs(0)
        return res


# https://leetcode.com/problems/n-queens-ii/
class Solution52:
    def totalNQueens(self, n: int) -> int:
        column_seen = set()
        # important for a few questions
        dig_seen = set()  # assign row - column
        rdig_seen = set()  # assign row + column

        grid = [['.'] * n for _ in range(n)]
        count = 0

        def dfs(r):  # row
            nonlocal count
            if r >= n:
                count += 1
                return

            for c in range(n):  # column
                if c in column_seen or c + r in rdig_seen or r - c in dig_seen: continue
                column_seen.add(c)
                rdig_seen.add(r + c)
                dig_seen.add(r - c)
                grid[r][c] = 'Q'

                dfs(r + 1)

                grid[r][c] = '.'
                column_seen.remove(c)
                rdig_seen.remove(r + c)
                dig_seen.remove(r - c)

        dfs(0)
        return count


# https://leetcode.com/problems/all-paths-from-source-to-target/
class Solution797:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:  # O(2^n*n) O(n)
        seen = set()
        curr = [0]
        n = len(graph)
        res = []

        def dfs(node):
            if node == n - 1:
                res.append(list(curr))
                return

            seen.add(node)
            for neighbor in graph[node]:
                if neighbor in seen: continue

                curr.append(neighbor)
                dfs(neighbor)
                curr.pop()  # backtrack

            seen.remove(node)  # backtrack

        dfs(0)
        return res

    def allPathsSourceTarget_cache(self, graph: List[List[int]]) -> List[List[int]]:
        seen = set()
        n = len(graph)

        @lru_cache(None)
        def dfs(node):
            if node == n - 1:
                return [[node]]

            res = []
            seen.add(node)
            for neighbor in graph[node]:
                if neighbor in seen: continue

                for path in dfs(neighbor):  # path can be [1,2]
                    res += [node] + path

            seen.remove(node)  # backtrack
            return res

        return dfs(0)


# https://leetcode.com/problems/expression-add-operators/
class Solution282:
    def addOperator(self, nums, target):  # T(n) = 3T(n-1) + 3T(n-2)+... = 3 *4 (T(n-2) + T(n_3) + ...) = 3*4^n = O(4^n)

        n = len(nums)
        res = []

        def dfs(idx, prev, preEval, path):
            if idx >= n:
                if preEval == target:
                    res.append(path)
                return

            for i in range(idx, n):
                if nums[idx] == '0' and i - idx >= 1: break  # '0xxx'

                curr = int(nums[idx: i + 1])
                if idx == 0:
                    dfs(i + 1, curr, curr, str(curr))
                    continue

                dfs(i + 1, curr, preEval + curr, path + '+' + str(curr))
                dfs(i + 1, -curr, preEval - curr, path + '-' + str(curr))
                dfs(i + 1, prev * curr, preEval - prev + prev * curr, path + '*' + str(curr))

        dfs(0, 0, 0, '')
        return res


# https://leetcode.com/problems/flatten-nested-list-iterator/
class NestedIterator341:
    def __init__(self, nestedList: ['NestedInteger']):
        def dfs(nl):
            res = []
            for ni in nl:
                if ni.isInteger():
                    res.append(ni.getInteger())
                else:
                    res.extend(dfs(ni.getList()))

            return res

        self.arr = dfs(nestedList)
        self.pos = 0

    def next(self) -> int:
        self.pos += 1
        return self.arr[self.pos - 1]

    def hasNext(self) -> bool:
        return self.pos != len(self.arr)


# https://leetcode.com/problems/sudoku-solver/
class Solution37:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for i in range(10)]
        cols = [set() for i in range(10)]
        boxes = [set() for i in range(10)]

        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                curr = board[i][j]
                if curr != '.':
                    rows[i].add(int(curr))
                    cols[j].add(int(curr))
                    boxes[i // 3 * 3 + j // 3].add(int(curr))

        def dfs(r, c):
            if r >= m: return True
            if c >= n: return dfs(r + 1, 0)

            if board[r][c] != '.':
                return dfs(r, c + 1)

            b_idx = r // 3 * 3 + c // 3
            for i in range(1, 10):
                if i in rows[r] or i in cols[c] or i in boxes[b_idx]: continue

                board[r][c] = f'{i}'
                rows[r].add(i)
                cols[c].add(i)
                boxes[b_idx].add(i)

                if dfs(r, c + 1):
                    return True

                board[r][c] = '.'
                rows[r].remove(i)
                cols[c].remove(i)
                boxes[b_idx].remove(i)

            return False

        dfs(0, 0)