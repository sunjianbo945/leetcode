from typing import List


# https://leetcode.com/problems/remove-element/
class Solution27:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        for r, num in enumerate(nums):
            if num != val:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1

        return l


# https://leetcode.com/problems/move-zeroes/
class Solution283:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r, num in enumerate(nums):
            if num != 0:
                nums[r], nums[l] = nums[l], nums[r]
                l += 1


# https://leetcode.com/problems/partition-labels/
class Solution763:
    def partitionLabels(self, S: str) -> List[int]:
        char_pos = {}
        for i, char in enumerate(S):
            char_pos[char] = i

        res = []
        l = 0
        boundary = char_pos[S[0]]
        for r in range(len(S)):
            boundary = max(boundary, char_pos[S[r]])
            if r == boundary:
                res.append(boundary - l + 1)
                l = boundary + 1
        return res


# https://leetcode.com/problems/jump-game-ii/
class Solution45:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        r = 0
        boundary = 0
        n = len(nums)
        for l, num in enumerate(nums):
            if boundary >= n - 1: return jumps
            r = max(r, l + num)

            if l == boundary:
                boundary = r
                jumps += 1

        return jumps


# https://leetcode.com/problems/string-compression/
class Solution443:
    def compress(self, chars: List[str]) -> int:
        write, l = 0, 0
        n = len(chars)
        for r in range(n):
            if r + 1 == n or chars[r] != chars[r + 1]:
                count = r - l + 1
                chars[write] = chars[r]
                write += 1
                if count > 1:
                    for digit in str(count):
                        chars[write] = digit
                        write += 1
                l = r + 1

        return write


# https://leetcode.com/problems/longest-mountain-in-array/
class Solution845:
    def longestMountain(self, A: List[int]) -> int:
        N = len(A)
        res = r = l = 0

        while r < N:
            if r + 1 < N and A[r] < A[r + 1]:  # go up
                while r + 1 < N and A[r] < A[r + 1]:
                    r += 1

                if r + 1 < N and A[r] > A[r + 1]:  # go down
                    while r + 1 < N and A[r] > A[r + 1]:
                        r += 1

                    res = max(res, r - l + 1)
            else:
                r += 1

            l = r

        return res
