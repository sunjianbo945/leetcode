from math import inf
from typing import List


def isBadVersion(version):
    pass


# template
def binary_search(arr, val):
    l, r = 0, len(arr) - 1  # [l, r]
    while l + 1 < r:
        m = (l + r) // 2
        if arr[m] == val: return m
        if arr[m] > val:
            r = m
        else:
            l = m

    if arr[l] == val: return l
    if arr[r] == val: return r
    return -1


def binary_search_lower_bound(arr, val):
    if not arr: return -1
    l, r = 0, len(arr) - 1  # [l, r]
    while l + 1 < r:
        m = (l + r) // 2
        if arr[m] >= val:
            r = m
        else:
            l = m

    if arr[l] == val: return l
    if arr[r] == val: return r
    return -1


def binary_search_upper_bound(arr, val):
    if not arr: return -1
    l, r = 0, len(arr) - 1  # [l, r]
    while l + 1 < r:
        m = (l + r) // 2
        if arr[m] > val:
            r = m
        else:
            l = m

    if arr[r] == val: return r
    if arr[l] == val: return l
    return -1


# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
class Solution34:
    def searchRange(self, arr: List[int], target: int) -> List[int]:
        def binary_search_lower_bound(arr, val):
            if not arr: return -1
            l, r = 0, len(arr) - 1  # [l, r]
            while l + 1 < r:
                m = (l + r) // 2
                if arr[m] >= val:
                    r = m
                else:
                    l = m

            if arr[l] == val: return l
            if arr[r] == val: return r
            return -1

        def binary_search_upper_bound(arr, val):
            if not arr: return -1
            l, r = 0, len(arr) - 1  # [l, r]
            while l + 1 < r:
                m = (l + r) // 2
                if arr[m] > val:
                    r = m
                else:
                    l = m

            if arr[r] == val: return r
            if arr[l] == val: return l
            return -1

        return [binary_search_lower_bound(arr, target), binary_search_upper_bound(arr, target)]


# https://leetcode.com/problems/first-bad-version/
class Solution278:
    def firstBadVersion(self, n):
        l, r = 0, n
        while l + 1 < r:
            m = (l + r) // 2
            if isBadVersion(m):
                r = m
            else:
                l = m

        if isBadVersion(l): return l
        if isBadVersion(r): return r

        return -1


# https://leetcode.com/problems/find-peak-element/
class Solution162:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        if l == r: return l

        while l + 1 < r:
            mid = (l + r) // 2

            if mid + 1 < n and nums[mid] < nums[mid + 1]:
                l = mid
            else:
                r = mid

        if (l > 0 and nums[l - 1] < nums[l] and nums[l] > nums[l + 1]) or (l == 0 and nums[l] > nums[l + 1]): return l
        if (r < n - 1 and nums[r - 1] < nums[r] and nums[r] > nums[r + 1]) or (
                r == n - 1 and nums[r] > nums[r - 1]): return r

        return -1


# https://leetcode.com/problems/leftmost-column-with-at-least-a-one/
class Solution1428:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        m, n = binaryMatrix.dimensions()
        res = inf

        def find_most_left(row, l, r):

            while l + 1 < r:
                mid = (l + r) // 2

                if binaryMatrix.get(row, mid) == 1:
                    r = mid
                else:
                    l = mid

            if binaryMatrix.get(row, l): return l
            if binaryMatrix.get(row, r): return r
            return inf

        for i in range(m):
            res = min(find_most_left(i, 0, n - 1), res)

        return res if res < inf else -1


# https://leetcode.com/problems/search-in-rotated-sorted-array/
class Solution33:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l + 1 < r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[l]:  # left
                if nums[l] <= target <= nums[mid]:
                    r = mid
                else:
                    l = mid
            else:  # right
                if nums[r] >= target >= nums[mid]:
                    l = mid
                else:
                    r = mid

        if nums[l] == target: return l
        if nums[r] == target: return r

        return -1


# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
class Solution81:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1

        while l + 1 < r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] == nums[l]:
                l += 1
            elif nums[mid] > nums[l]:  # left
                if nums[l] <= target <= nums[mid]:
                    r = mid
                else:
                    l = mid
            else:  # right
                if nums[r] >= target >= nums[mid]:
                    l = mid
                else:
                    r = mid

        if nums[l] == target or nums[r] == target: return True

        return False
