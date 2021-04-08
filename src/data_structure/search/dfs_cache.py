from bisect import bisect_left
from functools import lru_cache
from math import inf
from typing import List


# https://leetcode.com/problems/word-break/
class Solution139:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:  # O(n^3)
        wd = set(wordDict)
        n = len(s)

        @lru_cache(None)  # without lru cache it the algorithm goes to O(2^n)
        def dfs(start):
            if start >= n: return True

            for i in range(start, n):  # O(n)
                part = s[start:i + 1]
                if part not in wd: continue  # O(n)

                if dfs(i + 1): return True

            return False

        return dfs(0)


# https://leetcode.com/problems/concatenated-words/
class Solution472:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:  # O(n^4)
        wd = set(words)

        @lru_cache(None)
        def dfs(start):  # O(n^3)
            if start >= n: return True

            for i in range(start, n):  # O(n)
                part = word[start:i + 1]
                if part not in wd: continue  # O(n)

                if dfs(i + 1): return True

            return False

        res = []
        for word in words:
            n = len(word)
            if n < 1: continue

            dfs.cache_clear()
            wd.remove(word)
            if dfs(0):
                res.append(word)
            wd.add(word)

        return res


# https://leetcode.com/problems/word-break-ii/
class Solution140:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:  # O(n^4)
        wd = set(wordDict)
        n = len(s)

        @lru_cache(None)
        def dfs(start):
            if start >= n: return [[]]

            res = []
            for i in range(start, n):
                part = s[start:i + 1]
                if part not in wd: continue

                for p in dfs(i + 1):
                    res.append([part] + p)

            return res

        return [' '.join(parts) for parts in dfs(0)]


# https://leetcode.com/problems/target-sum/
class Solution494:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        n = len(nums)

        @lru_cache(None)
        def dfs(idx, preSum):
            if idx >= n:
                if preSum == S:
                    return 1
                return 0

            res = dfs(idx + 1, preSum + nums[idx])
            res += dfs(idx + 1, preSum - nums[idx])
            return res

        return dfs(0, 0)


# https://leetcode.com/problems/knight-probability-in-chessboard/
class Solution668:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        directions = {(dx, dy) for dx in (-2, -1, 1, 2) for dy in (-2, -1, 1, 2) if abs(dx) + abs(dy) == 3}

        @lru_cache(None)
        def dfs(x, y, k):
            if x < 0 or y < 0 or x >= N or y >= N: return 0
            if k == 0: return 1

            res = 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                res += dfs(nx, ny, k - 1)

            return res

        return dfs(r, c, K) / 8 ** K


# https://leetcode.com/problems/restore-ip-addresses/
class Solution93:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        if n > 12: return []

        @lru_cache(None)
        def dfs(idx, dot_count):
            if idx >= n:
                if dot_count == 0:
                    return ['']
                return []
            if dot_count < 0: return []

            res = []
            end = min(n, idx + 3)
            for i in range(idx, end):
                if s[idx] == '0' and i - idx > 0: break
                curr = s[idx:i + 1]
                if int(curr) > 255: break
                for p in dfs(i + 1, dot_count - 1):
                    if p == '':
                        res.append(curr)
                    else:
                        res.append(f'{curr}.{p}')

            return res

        return dfs(0, 4)


# https://leetcode.com/problems/distinct-subsequences/
class Solution115:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        @lru_cache(None)
        def dfs(s_i, t_i):
            if s_i >= m and t_i >= n: return 1
            if s_i >= m or t_i >= n: return 0
            if s[s_i] != t[t_i]: return 0

            res = 0
            for i in range(s_i, m):
                res += dfs(i + 1, t_i + 1)

            return res

        res = 0
        for i in range(m):
            res += dfs(i, 0)

        return res

# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
class Solution1155:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        # the number of possible ways

        @lru_cache(None)
        def dfs(d, target):
            if target <= 0: return 0
            if d == 1:
                if 0 < target <= f: return 1
                return 0

            res = 0
            for i in range(1, f + 1):
                res += dfs(d - 1, target - i)

            return res % (10 ** 9 + 7)

        return dfs(d, target)


# https://leetcode.com/problems/minimum-window-subsequence/
class Solution727:
    def minWindow(self, S: str, T: str) -> str:
        s_len, t_len = len(S), len(T)

        @lru_cache(None)
        def dfs(i, j):
            if j == t_len: return i - 1
            if i == s_len: return None

            ind = S.find(T[j], i)
            return dfs(ind + 1, j + 1) if ind != -1 else None

        res_len, res = inf, ''
        for i in range(s_len):
            if S[i] == T[0]:
                last = dfs(i + 1, 1)
                if last and res_len > last - i + 1:
                    res_len = last - i + 1
                    res = S[i:last + 1]
        return res


# https://leetcode.com/problems/maximum-profit-in-job-scheduling/
class Solution1235:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        start, end, pro = zip(*sorted(zip(startTime, endTime, profit), key=lambda x: x[0]))

        @lru_cache(None)
        def dfs(i):
            if i == len(start): return 0
            j = bisect_left(start, end[i])
            return max(pro[i] + dfs(j), dfs(i + 1))
        return dfs(0)