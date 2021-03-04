# https://leetcode.com/problems/leftmost-column-with-at-least-a-one/
from math import inf


def isBadVersion(version):
    pass


# template
def binary_search(arr, val):
    l, r = 0, len(arr) - 1
    while l < r:
        m = (l + r) // 2
        if arr[m] == val: return m
        if arr[m] > val:
            r = m
        else:
            l = m + 1
    return l


def binary_search_lower_bound(arr, val):
    l, r = 0, len(arr) - 1
    while l < r:
        m = (l + r) // 2
        if arr[m] >= val:
            r = m
        else:
            l = m + 1
    return l


def binary_search_upper_bound(arr, val):
    l, r = 0, len(arr) - 1
    while l < r:
        m = (l + r) // 2
        if arr[m] > val:
            r = m
        else:
            l = m + 1
    return l


# https://leetcode.com/problems/first-bad-version/
class Solution278:
    def firstBadVersion(self, n):
        l, r = 0, n
        while l < r:
            m = (l + r) // 2
            if isBadVersion(m):
                r = m
            else:
                l = m + 1

        return l


# https://leetcode.com/problems/leftmost-column-with-at-least-a-one/
class Solution1428:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        m, n = binaryMatrix.dimensions()
        res = inf

        def find_most_left(row, l, r):

            while l < r:
                m = (l + r) // 2

                if binaryMatrix.get(row, m) == 1:
                    r = m
                else:
                    l = m + 1

            if binaryMatrix.get(row, l) == 1: return l
            return inf

        for i in range(m):
            res = min(find_most_left(i, 0, n - 1), res)

        return res if res < inf else -1
