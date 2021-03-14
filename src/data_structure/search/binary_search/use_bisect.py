from bisect import bisect
from random import random
from typing import List


# https://leetcode.com/problems/random-pick-with-weight/
class Solution528:

    def __init__(self, w: List[int]):
        self.weights = [w[0]]
        for i in range(1, len(w)):
            self.weights.append(self.weights[-1] + w[i])

    def pickIndex(self) -> int:
        w = random() * self.weights[-1]
        idx = bisect(self.weights, w)
        return idx
