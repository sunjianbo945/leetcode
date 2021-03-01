import math
from collections import defaultdict
from functools import lru_cache
from math import factorial
from typing import List


# https://leetcode.com/problems/subsets/
class Solution78:
    def subsets(self, nums: List[int]) -> List[List[int]]:  # O(n * 2^n)
        res = []

        def dfs(idx, path):
            res.append(list(path))

            for i in range(idx, len(nums)):
                path.append(nums[i])

                dfs(i + 1, path)

                path.pop()  # backtrack

        dfs(0, [])
        return res


# https://leetcode.com/problems/subsets-ii/
class Solution90:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(idx, path):
            res.append(list(path))

            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i - 1]: continue

                path.append(nums[i])

                dfs(i + 1, path)

                path.pop()  # backtrack

        dfs(0, [])
        return res


# https://leetcode.com/problems/combinations/
class Solution77:
    def combine(self, n: int, k: int) -> List[List[int]]:  # O(2^n)
        res = []

        def dfs(idx, path):
            if len(path) == k:
                res.append(list(path))
                return

            for i in range(idx, n + 1):
                path.append(i)

                dfs(i + 1, path)

                path.pop()  # backtrack

        dfs(1, [])
        return res


# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
class Solution17:
    def letterCombinations(self, A: str) -> List[str]:
        n = len(A)
        if not n: return []
        phone_book = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"}
        res = []

        def dfs(start, path):
            if start >= n:
                res.append(''.join(path))
                return

            letters = phone_book[A[start]]
            for i in range(len(letters)):
                path.append(letters[i])
                dfs(start + 1, path)
                path.pop()

        dfs(0, [])
        return res


# https://leetcode.com/problems/factor-combinations/
class Solution254:
    def getFactors(self, n: int) -> List[List[int]]:
        if n < 2: return []
        res = []

        def dfs(start, target, path):
            if path:
                res.append(path + [target])

            for i in range(start, int(math.sqrt(target)) + 1):
                q, r = divmod(target, i)
                if r != 0: continue

                path.append(i)
                dfs(i, q, path)
                path.pop()

        dfs(2, n, [])
        return res


# https://leetcode.com/problems/palindrome-partitioning/
class Solution:
    def partition(self, s: str) -> List[List[str]]:  # O(n * 2^n), O(n^2)
        n = len(s)
        palindrome_index = defaultdict(list)
        for i in range(n):
            l, r = i, i
            while l >= 0 and r < n:
                if s[l] != s[r]: break
                palindrome_index[l].append(r + 1)
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < n:
                if s[l] != s[r]: break
                palindrome_index[l].append(r + 1)
                l -= 1
                r += 1

        res = []

        def dfs(start, path):
            if start >= n:
                res.append(list(path))
                return

            for end_idx in palindrome_index[start]:
                path.append(s[start: end_idx])
                dfs(end_idx, path)
                path.pop()

        dfs(0, [])
        return res

    def partition_cache(self, s: str) -> List[List[str]]:
        n = len(s)
        palindrome_index = defaultdict(list)
        for i in range(n):
            l, r = i, i
            while l >= 0 and r < n:
                if s[l] != s[r]: break
                palindrome_index[l].append(r + 1)
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < n:
                if s[l] != s[r]: break
                palindrome_index[l].append(r + 1)
                l -= 1
                r += 1

        @lru_cache(None)
        def dfs(start):
            if start >= n:
                return [[]]
            res = []
            for end_idx in palindrome_index[start]:
                path = [s[start: end_idx]]
                for p in dfs(end_idx):
                    res.append(path + p)
            return res

        return dfs(0)


# https://leetcode.com/problems/combination-sum/
class Solution39:
    def combinationSum(self, A: List[int], target: int) -> List[List[int]]:  # O(n^{t/m + 1})
        n = len(A)
        res = []

        def dfs(start, target, path):
            if target == 0:
                res.append(list(path))
                return

            if target < 0: return

            for i in range(start, n):
                path.append(A[i])
                dfs(i, target - A[i], path)
                path.pop()

        dfs(0, target, [])
        return res

    def combinationSum_divide_conquer(self, A: List[int], target: int) -> List[List[int]]:
        n = len(A)

        # @lru_cahce(None) not that much benefit
        def dfs(start, target):
            if target < 0: return []
            if target == 0: return [[]]

            res = []
            for i in range(start, n):
                path = [A[i]]
                for p in dfs(i, target - A[i]):
                    res.append(path + p)

            return res

        return dfs(0, target)


# https://leetcode.com/problems/combination-sum-ii/
class Solution40:
    def combinationSum2(self, A: List[int], target: int) -> List[List[int]]:  # O(2^n)
        A.sort()
        n = len(A)
        res = []

        def dfs(start, target, path):
            if target < 0: return
            if target == 0:
                res.append(list(path))
                return

            for i in range(start, n):
                if i > start and A[i] == A[i - 1]: continue

                path.append(A[i])
                dfs(i + 1, target - A[i], path)
                path.pop()

        dfs(0, target, [])
        return res


# https://leetcode.com/problems/combination-sum-iii/
class Solution216:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:  # O(9!k/(9-k)!), O(k)
        nums = [i for i in range(1, 10)]
        res = []

        def dfs(start, k, target, path):
            if target < 0 or k < 0: return
            if target == 0 and k == 0:
                res.append(list(path))
                return

            for i in range(start, 9):
                path.append(nums[i])
                dfs(i + 1, k - 1, target - nums[i], path)
                path.pop()

        dfs(0, k, n, [])
        return res


# https://leetcode.com/problems/permutations/
class Solution46:
    def permute(self, nums: List[int]) -> List[List[int]]:  # O(n!) O(n)
        n = len(nums)
        res = []
        used = [False] * n

        def dfs(path):
            if len(path) == n:
                res.append(list(path))
                return

            for i in range(n):
                if used[i]: continue

                used[i] = True
                path.append(nums[i])

                dfs(path)

                path.pop()  # backtrack
                used[i] = False

        dfs([])
        return res


# https://leetcode.com/problems/letter-case-permutation/
class Solution784:
    def letterCasePermutation(self, S: str) -> List[str]:
        n = len(S)
        res = []

        def dfs(idx, path):
            if len(path) == n:
                res.append(''.join(path))
                return

            for i in range(idx, n):
                if S[i].isdigit():
                    path.append(S[i].lower())

                    dfs(i + 1, path)

                    path.pop()  # backtrack
                    return
                else:
                    path.append(S[i].lower())
                    dfs(i + 1, path)
                    path.pop()  # backtrack

                    path.append(S[i].upper())
                    dfs(i + 1, path)
                    path.pop()  # backtrack

        dfs(0, [])
        return res


# https://leetcode.com/problems/permutations-ii/
class Solution47:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        used = [False] * n
        nums.sort()

        def dfs(path):
            if len(path) == n:
                res.append(list(path))
                return

            for i in range(n):
                if used[i]: continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]: continue  # this line is the key part

                used[i] = True
                path.append(nums[i])

                dfs(path)

                path.pop()  # backtrack
                used[i] = False

        dfs([])
        return res


# bad question
# https://leetcode.com/problems/next-permutation/
class Solution31:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 0 or n == 1: return
        # 4 steps need to remember
        # 1. from end to beginning, find the first decrease number call 'x' and postition x_p
        x_p = n - 2
        while x_p >= 0 and nums[x_p + 1] <= nums[x_p]:
            x_p -= 1
        # 2. from end to beginning, find the first number greater than x, call y and position y_p
        if x_p > -1:  # x_p mean decreasing whole sequence
            y_p = n - 1
            while y_p >= 0 and nums[y_p] <= nums[x_p]:
                y_p -= 1
            # 3. swap x_p and y_p
            nums[x_p], nums[y_p] = nums[y_p], nums[x_p]
        # 4. reverse the partial list after x_p
        nums[x_p + 1:] = reversed(nums[x_p + 1:])


# not same but need to understand
# https://leetcode.com/problems/permutation-sequence/
class Solution60:
    def getPermutation(self, n: int, k: int) -> str:  # O(n^2)
        nums = list(map(str, (i for i in range(1, n + 1))))
        # fit k in the interval 0 ... (n! - 1)
        k -= 1
        output = []
        for i in range(n - 1, -1, -1):
            q, k = divmod(k, factorial(i))

            output.append(nums[q])
            del nums[q]  # O(n)

        return ''.join(output)

    def getPermutation_nextPermuation(self, n: int, k: int) -> str:  # O(n*k)
        def nextPermutation(nums: List[int]) -> None:

            # 4 steps need to remember
            # 1. from end to beginning, find the first decrease number call 'x' and postition x_p
            x_p = n - 2
            while x_p >= 0 and nums[x_p + 1] <= nums[x_p]:
                x_p -= 1
            # 2. from end to beginning, find the first number greater than x, call y and position y_p
            if x_p > -1:  # x_p mean decreasing whole sequence
                y_p = n - 1
                while y_p >= 0 and nums[y_p] <= nums[x_p]:
                    y_p -= 1
                # 3. swap x_p and y_p
                nums[x_p], nums[y_p] = nums[y_p], nums[x_p]
            # 4. reverse the partial list after x_p
            nums[x_p + 1:] = reversed(nums[x_p + 1:])

        k = (k - 1) % factorial(n)
        nums = [i + 1 for i in range(n)]
        for i in range(k):
            nextPermutation(nums)

        return ''.join(map(str, nums))
