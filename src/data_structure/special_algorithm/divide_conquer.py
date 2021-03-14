from collections import Counter
from math import inf


# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/
class Solution395:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k: return 0
        char_count = Counter(s)
        res = -inf
        for char, count in char_count.items():
            if count >= k: continue

            for part in s.split(char):
                res = max(res, self.longestSubstring(part, k))
            return res
        return len(s)