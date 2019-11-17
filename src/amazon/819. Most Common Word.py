from typing import *

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        bs = set(banned)
        ignore = set(['!', '?', "'", ',', ';', '.', ' '])
        for c in ignore:
            paragraph = paragraph.replace(c, " ")

        array = paragraph.split(' ')
        count = {}
        for i in array:
            word = i.lower()
            if word and word not in bs:
                if word not in count:
                    count[word] = 1
                else:
                    count[word] += 1

        ans, best = '', 0
        for key, val in count.items():
            if val > best:
                best = val
                ans = key
            elif val == best:
                ans = ans if ans < key else key

        return ans
