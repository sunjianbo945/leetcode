# https://leetcode.com/problems/palindrome-number/
from bisect import bisect_left, bisect
from typing import List

from math import gcd


class Solution9:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0): return False

        reverse = 0
        while x > reverse:
            reverse = 10 * reverse + x % 10
            x //= 10

        return x == reverse or x == reverse // 10


# https://leetcode.com/problems/greatest-common-divisor-of-strings/
class Solution1071:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n1 = len(str1)
        n2 = len(str2)

        if str1 == str2:
            return str1

        # check if both strings contain same repeating vals
        if str1 + str2 != str2 + str1:
            return ""

        x = gcd(n1, n2)

        if str1[:x] == str2[:x]:
            return str1[:x]
        else:
            return ""


# https://leetcode.com/problems/maximum-69-number/
class Solution1323:
    def maximum69Number(self, num: int) -> int:
        i = 0
        q = num
        six_idx = -1
        while q > 0:
            q, r = divmod(q, 10)
            if r == 6:
                six_idx = i  # refresh six_idx when found 6 at large digit.
            i += 1

        return (num + 3 * (10 ** six_idx)) if six_idx != -1 else num


# https://leetcode.com/problems/task-scheduler/
class Solution621:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # frequencies of the tasks
        frequencies = [0] * 26
        for t in tasks:
            frequencies[ord(t) - ord('A')] += 1

        # max frequency
        f_max = max(frequencies)
        # count the most frequent tasks
        n_max = frequencies.count(f_max)

        return max(len(tasks), (f_max - 1) * (n + 1) + n_max)


# https://leetcode.com/problems/score-of-parentheses/
class Solution856:
    def scoreOfParentheses(self, S: str) -> int:
        res = 0
        d = -1
        for idx, s in enumerate(S):
            d += 1 if s == "(" else -1
            if s == "(" and S[idx + 1] == ')':
                res += 2 ** d

        return res


# https://leetcode.com/problems/moving-average-from-data-stream/
class MovingAverage346:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.capacity = size
        self.total = 0
        self.arr = []

    def next(self, val: int) -> float:

        if self.size < self.capacity:
            self.total += val
            self.size += 1
            self.arr.append(val)
        else:
            self.total += val - self.arr.pop(0)
            self.arr.append(val)

        return self.total / self.size


# https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/
class Solution1287:
    def findSpecialInteger(self, arr: List[int]) -> int:
        quarter = len(arr) // 4

        if quarter == 0: return arr[0]

        for i in range(quarter, len(arr), quarter):
            if bisect(arr, arr[i]) - bisect_left(arr, arr[i]) > quarter:
                return arr[i]

        return arr[-1]


# https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/
class Solution1317:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def hasZero(num):
            if num == 0: return True
            while num:
                if num % 10 == 0:
                    return True

                num = num // 10

            return False

        for i in range(1, n):
            if not hasZero(i) and not hasZero(n - i):
                return [i, n - i]

        return [-1, -1]


# https://leetcode.com/problems/single-number-ii/
class Solution137:
    def singleNumber(self, nums: List[int]) -> int:
        return (sum(set(nums)) * 3 - sum(nums)) // 2


# https://leetcode.com/problems/statistics-from-a-large-sample/
class Solution1093:
    def sampleStats(self, count: List[int]) -> List[float]:
        n = sum(count)

        min_num, max_num, total, freq, mode = None, -1, 0, 0, 0
        first, second, idx_count = None, None, 0
        for num, frequency in enumerate(count):

            total += num * frequency

            idx_count += frequency
            # math question NOT USE "not first". 0 is also not first
            if first is None and idx_count >= n // 2:
                first = num

            if second is None and idx_count >= n // 2 + 1:
                second = num

            max_num = num if frequency > 0 else max_num
            min_num = num if min_num is None and frequency > 0 else min_num

            if frequency > freq:
                freq = frequency
                mode = num

        median = second if n % 2 == 1 else (first + second) / 2
        # print(n,first,second)
        return [min_num, max_num, total / n, median, mode]
