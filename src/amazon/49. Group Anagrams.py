from typing import *

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memo = {}

        for s in strs:

            key = tuple(sorted(s))

            if key not in memo:
                memo[key] = [s]
            else:
                memo[key].append(s)

        return memo.values()