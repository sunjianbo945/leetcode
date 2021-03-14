from math import gcd

# https://leetcode.com/problems/palindrome-number/
from typing import List


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