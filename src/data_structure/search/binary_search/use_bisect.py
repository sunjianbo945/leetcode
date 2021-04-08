import string
from bisect import *
from collections import defaultdict, deque
from random import random
from typing import List


# https://leetcode.com/problems/random-pick-with-weight/
class Solution528:

    def __init__(self, w: List[int]):
        self.weights = [w[0]]
        for i in range(1, len(w)):
            self.weights.append(self.weights[-1] + w[i])

    def pickIndex(self) -> int:
        w = random() * self.weights[-1]
        idx = bisect(self.weights, w)
        return idx


# https://leetcode.com/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/
class Solution1505:
    def minInteger(self, num: str, k: int) -> str:
        digits = defaultdict(deque)
        for i, c in enumerate(num):
            digits[c].append(i)  # {'4':[0], '3':[1], '2':[2],'1':[3]}

        res, moved = '', []
        for _ in range(len(num)):
            for c in string.digits:
                if not digits[c]: continue

                original_idx = digits[c][0]
                # the current index of c after a few moves. for exmaple, if 3 numbers after nums[i]
                # are removed to the front, then the index of num[i] becauses i+3 in the new array
                after_move_idx = original_idx + len(moved) - bisect(moved, original_idx)

                distance = after_move_idx - len(moved)  # the distance need to move to the right place
                # print(c, original_idx, after_move_idx, distance)
                if distance <= k:
                    k -= distance
                    res += c
                    insort(moved, digits[c].popleft())
                    break

        return res


# https://leetcode.com/problems/search-suggestions-system/
class Solution1268:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        sp = sorted(products)
        res = []
        for i in range(1, len(searchWord) + 1):
            curr = searchWord[:i]
            idx = bisect_left(sp, curr)
            res.append([s for s in sp[idx:idx + 3] if curr == s[:i]])

        return res


# https://leetcode.com/problems/range-module/
class RangeModule715:

    def __init__(self):
        self.range = []

    def addRange(self, left: int, right: int) -> None:
        l = bisect_left(self.range, left)  # has 10,20 and insert 20, 21, expect 10, 21
        r = bisect(self.range, right)

        temp = []
        if l % 2 == 0:
            temp.append(left)
        if r % 2 == 0:
            temp.append(right)

        self.range[l:r] = temp

    def queryRange(self, left: int, right: int) -> bool:
        l = bisect(self.range, left)
        r = bisect_left(self.range, right)  # has 10, 20 check 19,20
        # print(self.range, l, r)
        return l == r and r % 2 == 1

    def removeRange(self, left: int, right: int) -> None:
        l = bisect_left(self.range, left)  # has 10, 20 remove 10,11 expect 11,20
        r = bisect(self.range, right)

        temp = []
        if l % 2 == 1:
            temp.append(left)

        if r % 2 == 1:
            temp.append(right)

        self.range[l:r] = temp


# https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/
class Solution1287:
    def findSpecialInteger(self, arr: List[int]) -> int:
        quarter = len(arr) // 4

        if quarter == 0: return arr[0]

        for i in range(quarter, len(arr), quarter):
            if bisect(arr, arr[i]) - bisect_left(arr, arr[i]) > quarter:
                return arr[i]

        return arr[-1]