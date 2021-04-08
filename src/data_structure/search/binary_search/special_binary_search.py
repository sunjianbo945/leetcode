from bisect import bisect
from functools import lru_cache
from math import inf
from typing import List


# https://leetcode.com/problems/kth-missing-positive-number/
class Solution1539:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # find the first index that has arr[index] - index - 1 == k
        l, r = 0, len(arr) - 1

        while l + 1 < r:
            m = (l + r) // 2
            missing = arr[m] - m - 1

            if missing >= k:
                r = m
            else:
                l = m

        if arr[l] - l - 1 >= k: return l + k
        if arr[r] - r - 1 >= k: return r + k

        return r + k + 1


# https://leetcode.com/problems/super-egg-drop/
class Solution887:

    @lru_cache(None)
    def superEggDrop(self, K: int, N: int) -> int:
        if K == 1: return N
        if N <= 1: return N

        l, r = 0, N
        while l + 1 < r:
            m = (l + r) // 2

            if self.superEggDrop(K - 1, m - 1) < self.superEggDrop(K, N - m):
                l = m
            else:
                r = m

        l = max(self.superEggDrop(K - 1, l - 1), self.superEggDrop(K, N - l))
        r = max(self.superEggDrop(K - 1, r - 1), self.superEggDrop(K, N - r))

        return min(l, r) + 1  # l or r is find in this case


# https://leetcode.com/problems/find-k-closest-elements/
class Solution658:
    def findClosestElements(self, A: List[int], k: int, x: int) -> List[int]:
        if k >= len(A): return A

        l, r = 0, len(A) - k
        while l + 1 < r:
            m = (l + r) // 2
            # right bound >= left bound
            if A[m + k] - x >= x - A[m]:
                r = m
            else:
                l = m

        if A[l + k] - x >= x - A[l]:
            return A[l:l + k]

        return A[r:r + k]


# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
class Solution1011:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        l, r = 0, sum(weights)

        def get_days(weight):
            day = 1
            cum = 0
            for i, w in enumerate(weights):
                if w > weight:
                    return inf

                if w + cum <= weight:
                    cum += w
                else:
                    day += 1
                    cum = w

            return day

        while l + 1 < r:
            m = (l + r) // 2

            need = get_days(m)

            if need > D:
                l = m
            else:
                r = m

        if get_days(l) <= D: return l
        if get_days(r) <= D: return r
        return -1


# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
class Solution378:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        l, r = matrix[0][0], matrix[-1][-1]

        def get_count(target):
            count = 0
            for row in matrix:
                count += bisect(row, target)

            return count

        while l + 1 < r:
            mid = (l + r) // 2

            count = get_count(mid)

            if count < k:
                l = mid
            else:
                r = mid

        if get_count(l) >= k: return l
        if get_count(r) >= k: return r

        return -1


# https://leetcode.com/problems/single-element-in-a-sorted-array/
class Solution540:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]

        l, r = 0, len(nums) - 1

        while l + 1 < r:
            m = (l + r) // 2

            if m % 2 == 1:
                if nums[m] == nums[m - 1]:
                    l = m
                else:
                    r = m
            else:
                if nums[m] == nums[m + 1]:
                    l = m
                else:
                    r = m

        if ((l > 0 and nums[l] != nums[l - 1]) or l == 0) and nums[l] != nums[l + 1]: return nums[l]
        if ((r < n - 1 and nums[r] != nums[r + 1]) or r == n - 1) and nums[r] != nums[r - 1]: return nums[r]

        return -1


# https://leetcode.com/problems/split-array-largest-sum/
class Solution410:
    def splitArray(self, nums: List[int], m: int) -> int:
        l, r = 0, sum(nums)

        def get_split(max_sum):
            split = 1
            curr_sum = 0
            for num in nums:
                if num > max_sum: return inf

                if curr_sum + num <= max_sum:
                    curr_sum += num
                else:
                    curr_sum = num
                    split += 1

            return split

        while l + 1 < r:
            mid = (l + r) // 2

            splits = get_split(mid)
            if splits > m:
                l = mid
            else:
                r = mid

        if get_split(l) <= m: return l
        if get_split(r) <= m: return r

        return -1