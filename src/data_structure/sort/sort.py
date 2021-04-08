from collections import Counter
from functools import cmp_to_key
from math import inf
from typing import List


# https://leetcode.com/problems/maximum-product-of-three-numbers/
class Solution628:
    def maximumProduct(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums)

        return max(nums_sorted[-1] * nums_sorted[-2] * nums_sorted[-3],
                   nums_sorted[0] * nums_sorted[1] * nums_sorted[-1])


# https://leetcode.com/problems/task-scheduler/
class Solution621:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequencies = [0] * 26
        for t in tasks:
            frequencies[ord(t) - ord('A')] += 1

        frequencies.sort()

        # max frequency
        f_max = frequencies.pop()
        idle_time = (f_max - 1) * n

        while frequencies and idle_time > 0:
            idle_time -= min(f_max - 1, frequencies.pop())
        idle_time = max(0, idle_time)

        return idle_time + len(tasks)


# https://leetcode.com/problems/maximum-length-of-pair-chain/
class Solution646:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        res = 0
        count = 0
        sorted_pairs = sorted(pairs, key=lambda x: x[1])
        prev = -inf
        for i in range(len(sorted_pairs)):
            if sorted_pairs[i][0] > prev:
                count += 1
                prev = sorted_pairs[i][1]
                res = max(res, count)

        return res


# https://leetcode.com/problems/queue-reconstruction-by-height/
class Solution406:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        output = []
        for h, k in sorted(people, key=lambda x: (-x[0], x[1])):
            output.insert(k, [h, k])

        return output


# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
class Solution581:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums)
        l, r = inf, 0
        for i in range(len(nums)):
            if nums[i] != nums_sorted[i]:
                r = max(r, i)
                l = min(l, i)

        return r - l + 1 if r >= l else 0


# https://leetcode.com/problems/reorder-data-in-log-files/
class Solution937:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        res = []
        for i in range(len(logs)):
            log_parts = logs[i].split(' ')
            if log_parts[1].isdigit():
                res.append((1, i, logs[i]))
            else:
                res.append((0, ' '.join(log_parts[1:]), logs[i]))

        res.sort()
        return [r[2] for r in res]


# https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/
class Solution1465:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()

        horizontal_boundary, vertical_boundary = [0] + horizontalCuts + [h], [0] + verticalCuts + [w]

        h_max_diff, v_max_diff = -inf, -inf

        for i in range(len(horizontal_boundary) - 1):
            h_max_diff = max(horizontal_boundary[i + 1] - horizontal_boundary[i], h_max_diff)

        for i in range(len(vertical_boundary) - 1):
            v_max_diff = max(vertical_boundary[i + 1] - vertical_boundary[i], v_max_diff)

        return (h_max_diff * v_max_diff) % (10 ** 9 + 7)


# https://leetcode.com/problems/largest-number/
class Solution179:
    def largestNumber(self, nums: List[int]) -> str:

        def compare(x, y):
            if f'{x}{y}' > f'{y}{x}':
                return -1
            else:
                return 1

        temp = sorted(nums, key=cmp_to_key(compare))

        if temp[0] == 0: return '0'

        return ''.join(map(str, temp))


# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/
class Solution1481:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        num_count = Counter(arr)
        count = len(num_count)
        for key, v in sorted(num_count.items(), key=lambda item: item[1]):
            if v <= k:
                k -= v
                count -= 1
            else:
                return count

        return 0


# https://leetcode.com/problems/equal-sum-arrays-with-minimum-number-of-operations/
class Solution1775:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) > len(nums2) * 6 or len(nums1) * 6 < len(nums2):
            return -1
        total1, total2 = sum(nums1), sum(nums2)
        if total1 < total2:
            return self.minOperations(nums2, nums1)

        nums1.sort()
        nums2.sort()

        i, j = len(nums1) - 1, 0
        operation = 0
        while total1 > total2:
            if i < 0 or j == len(nums2) or 6 - nums2[j] > nums1[i] - 1:
                total2 += 6 - nums2[j]
                j += 1
            else:
                total1 -= nums1[i] - 1
                i -= 1

            operation += 1

        return operation
