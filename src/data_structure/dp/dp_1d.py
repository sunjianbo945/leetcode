from typing import List


# https://leetcode.com/problems/longest-mountain-in-array/
class Solution845:
    def longestMountain(self, arr: List[int]) -> int:
        res, up, down = 0, 0, 0
        n = len(arr)
        for i in range(1, n):
            if arr[i] > arr[i - 1]:  # go up
                if down:  # from down to up
                    up = 0
                up += 1
                down = 0
            elif arr[i] < arr[i - 1]:  # go down
                down += 1
            else:
                up = down = 0

            if up and down:
                res = max(res, up + down + 1)

        return res
