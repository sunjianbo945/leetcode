from typing import List

class Solution:

    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:

        counter = {}
        ret = 0
        for i in A:
            for j in B:
                counter[i + j] = counter.get(i + j, 0) + 1

        for i in C:
            for j in D:
                if -i - j in counter:
                    ret += counter[-i - j]

        return ret