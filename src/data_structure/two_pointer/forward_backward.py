from math import inf
from typing import List


# https://leetcode.com/problems/container-with-most-water/
class Solution11:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        l = 0
        r = len(height) - 1
        while l < r:
            ans = max(ans, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return ans


# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
class Solution167:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            curr = numbers[l] + numbers[r]
            if curr == target:
                return [l + 1, r + 1]
            elif curr < target:
                l += 1
            else:
                r -= 1


# https://leetcode.com/problems/two-sum-less-than-k/
class Solution1099:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        res = -1
        while l < r:
            curr = nums[l] + nums[r]
            if (curr < k):
                res = max(res, curr)
                l += 1
            else:
                r -= 1
        return res


# https://leetcode.com/problems/palindrome-number/
class Solution9:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False

        x = str(abs(x))
        l, r = 0, len(x) - 1
        while l < r:
            if x[l] != x[r]: return False

            l += 1
            r -= 1

        return True


# https://leetcode.com/problems/valid-palindrome/
class Solution125:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        s = s.lower()

        while l < r:
            while l < r and not s[l].isalnum():  # not isalpha, isnumeric, isalnum
                l += 1

            while l < r and not s[r].isalnum():
                r -= 1

            if s[l] != s[r]: return False

            l += 1
            r -= 1

        return True


# https://leetcode.com/problems/valid-palindrome-ii/
class Solution680:
    def validPalindrome(self, s: str) -> bool:

        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]: return False
                l += 1
                r -= 1

            return True

        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return isPalindrome(l, r - 1) or isPalindrome(l + 1, r)
            l += 1
            r -= 1

        return True


# https://leetcode.com/problems/3sum/
class Solution15:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        n = len(nums)
        res = []
        for idx, num in enumerate(sorted_nums):
            if idx > 0 and sorted_nums[idx] == sorted_nums[idx - 1]: continue
            target = -num

            l, r = idx + 1, n - 1
            while l < r:
                curr = sorted_nums[l] + sorted_nums[r]

                if curr == target:
                    res.append([num, sorted_nums[l], sorted_nums[r]])
                    l += 1
                    r -= 1

                    while l < r and sorted_nums[l] == sorted_nums[l - 1]: l += 1
                    while l < r and sorted_nums[r] == sorted_nums[r + 1]: r -= 1
                elif curr < target:
                    l += 1
                else:
                    r -= 1

        return res


# https://leetcode.com/problems/3sum-closest/
class Solution16:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        sorted_nums = sorted(nums)
        n = len(nums)
        min_diff = inf
        res = 0
        for idx, num in enumerate(sorted_nums):
            if idx > 0 and sorted_nums[idx] == sorted_nums[idx - 1]: continue
            k = target - num

            l, r = idx + 1, n - 1
            while l < r:
                curr = sorted_nums[l] + sorted_nums[r]

                if (temp := abs(curr - k)) < min_diff:
                    res = curr + num
                    min_diff = temp

                if curr == k:
                    return target
                elif curr < k:
                    l += 1
                else:
                    r -= 1

        return res


# https://leetcode.com/problems/3sum-smaller/
class Solution259:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        sorted_nums = sorted(nums)
        n = len(nums)
        count = 0
        for idx, num in enumerate(sorted_nums):
            l, r = idx + 1, n - 1
            while l < r:
                curr = sorted_nums[l] + sorted_nums[r] + num
                if curr < target:
                    count += r - l
                    l += 1
                else:
                    r -= 1

        return count


# https://leetcode.com/problems/squares-of-a-sorted-array/
class Solution977:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        l, r = 0, n - 1
        for i in range(n - 1, -1, -1):
            if abs(nums[l]) < abs(nums[r]):
                square = nums[r]
                r -= 1
            else:
                square = nums[l]
                l += 1
            res[i] = square * square
        return res


# https://leetcode.com/problems/sort-transformed-array/
class Solution360:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def quadratic(x):
            return a * x * x + b * x + c

        n = len(nums)
        l, r, res = 0, n - 1, [0] * n

        index = 0 if a < 0 else n - 1  # keu part

        while l <= r:
            l_val, r_val = quadratic(nums[l]), quadratic(nums[r])
            if a >= 0:
                if l_val > r_val:
                    res[index] = l_val
                    l += 1
                else:
                    res[index] = r_val
                    r -= 1
                index -= 1
            else:
                if l_val > r_val:
                    res[index] = r_val
                    r -= 1
                else:
                    res[index] = l_val
                    l += 1
                index += 1
        return res
