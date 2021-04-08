from typing import List

# https://leetcode.com/problems/happy-number/
class Solution202:
    def isHappy(self, n: int) -> bool:
        cycle = set()

        while n != 1 and n not in cycle:
            cycle.add(n)
            n = sum(pow(int(i), 2) for i in str(n))

        return n == 1


# https://leetcode.com/problems/longest-consecutive-sequence/
class Solution128:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0
        for num in nums:
            if num - 1 in nums_set:
                continue

            count = 0
            curr = num
            while curr in nums_set:
                curr += 1
                count += 1
                res = max(res, count)

        return res


# https://leetcode.com/problems/valid-sudoku/
class Solution36:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        columns = [set() for i in range(9)]
        boxes = [set() for i in range(9)]

        # validate a board
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.': continue

                num = int(num)
                box_idx = (i // 3) * 3 + j // 3

                if num in rows[i]: return False
                rows[i].add(num)

                if num in columns[j]: return False
                columns[j].add(num)

                if num in boxes[box_idx]: return False
                boxes[box_idx].add(num)

        return True