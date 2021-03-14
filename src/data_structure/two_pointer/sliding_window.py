from collections import Counter
from math import inf
from typing import List


# question for sub-problem and at least question use sliding window


# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_pos = {}
        l = 0
        n = len(s)
        res = 0
        for r, char in enumerate(s):
            if char in char_pos and char_pos[char] >= l:
                l = char_pos[char] + 1

            char_pos[char] = r

            res = max(r - l + 1, res)

        return res


# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
class Solution340:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        freq = Counter()
        l = 0
        res = 0
        for r, char in enumerate(s):
            freq[char] += 1

            while len(freq) > k:
                left_char = s[l]
                freq[left_char] -= 1
                if freq[left_char] == 0:
                    del freq[left_char]

                l += 1
            res = max(res, r - l + 1)

        return res

# https://leetcode.com/problems/arithmetic-slices/
class Solution413:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        l = 0
        n = len(nums)
        if n < 3: return 0
        prev = nums[1] - nums[0]
        count = 0
        for r in range(1, n):
            curr = nums[r] - nums[r - 1]

            if curr == prev and r - l > 1:
                count += r - l - 1
            else:
                l = r - 1
                prev = curr

        return count


# https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/
class Solution1100:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        l = 0
        char_pos = {}
        res = 0
        for r in range(len(S)):
            char = S[r]
            if char in char_pos and char_pos[char] >= l:
                l = char_pos[char] + 1

            char_pos[char] = r

            if r - l + 1 == K:
                res += 1
                l += 1

        return res


# https://leetcode.com/problems/subarray-product-less-than-k/
class Solution713:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = 0
        n = len(nums)
        pre_prod = 1
        res = 0
        for r in range(n):
            pre_prod *= nums[r]

            while pre_prod >= k and l <= r:
                pre_prod /= nums[l]
                l += 1

            res += r - l + 1  # logic outside

        return res


# https://leetcode.com/problems/minimum-size-subarray-sum/
class Solution209:
    def minSubArrayLen(self, k: int, nums: List[int]) -> int:
        pre_sum = [0]
        for num in nums:
            pre_sum.append(pre_sum[-1] + num)

        n = len(pre_sum)
        l = 0
        res = inf
        for r in range(n):
            curr = pre_sum[r] - pre_sum[l]

            while curr >= k and l < r:
                res = min(res, r - l)  # logic inside
                l += 1
                curr = pre_sum[r] - pre_sum[l]

        return res if res < inf else 0


# https://leetcode.com/problems/minimum-window-substring/
class Solution76:
    def minWindow(self, s: str, t: str) -> str:
        if s == t: return s

        t_counter = Counter(t)
        target = len(t_counter)
        s_counter = Counter()
        l = 0
        min_len, res = inf, ''
        for r, char in enumerate(s):
            s_counter[char] += 1
            if s_counter[char] == t_counter[char]:
                target -= 1

            while target == 0:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    res = s[l:r + 1]

                s_counter[s[l]] -= 1
                old = s[l]
                if s_counter[old] < t_counter[old]:
                    target += 1
                l += 1

        return res if min_len < inf else ''


# https://leetcode.com/problems/subarrays-with-k-different-integers/
class Solution992:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:

        def atLeast(k):
            num_count = {}
            res = 0
            l = 0
            for r in range(len(A)):
                num = A[r]
                if num not in num_count: num_count[num] = 0

                num_count[num] += 1

                while len(num_count) > k:
                    old = A[l]
                    num_count[old] -= 1
                    if num_count[old] == 0:
                        del num_count[old]

                    l += 1

                res += r - l + 1

            return res

        return atLeast(K) - atLeast(K - 1)
