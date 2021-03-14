# https://leetcode.com/problems/leftmost-column-with-at-least-a-one/
from use_bisect import bisect
from functools import lru_cache
from math import inf
from random import random
from typing import List


# https://leetcode.com/problems/kth-missing-positive-number/
class Solution1539:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # find the first index that has arr[index] - index - 1 == k
        l, r = 0, len(arr)

        while l < r:
            m = (l + r) // 2
            missing = arr[m] - m - 1

            if missing >= k:
                r = m
            else:
                l = m + 1

        return l + k


# https://leetcode.com/problems/super-egg-drop/
class Solution887:
    @lru_cache(None)
    def superEggDrop(self, K: int, N: int) -> int:
        if K == 1: return N
        if N <= 1: return N

        l, r = 0, N + 1
        while l < r:
            m = (l + r) // 2

            lo = self.superEggDrop(K - 1, m - 1)
            up = self.superEggDrop(K, N - m)

            if lo == up:
                return lo + 1
            elif lo > up:
                r = m
            else:
                l = m + 1

        return max(self.superEggDrop(K - 1, l - 1), self.superEggDrop(K, N - l)) + 1  # l or r is find in this case



class Solution:
    def findClosestElements(self, A: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(A) - k
        while l < r:
            m = (l + r) // 2
            # right bound >= left bound
            if A[m + k] - x >= x - A[m]:
                r = m
            else:
                l = m + 1
        return A[l:l + k]