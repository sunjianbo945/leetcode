from collections import defaultdict
from typing import List


# https://leetcode.com/problems/dot-product-of-two-sparse-vectors/
class SparseVector1570:
    def __init__(self, nums: List[int]):  # O (n)
        self.idx_num = defaultdict(int)
        for idx, num in enumerate(nums):
            if num:
                self.idx_num[idx] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:  # O(min(l1,l2))
        if len(self.idx_num) < len(vec.idx_num):
            one, another = self.idx_num, vec.idx_num
        else:
            one, another = vec.idx_num, self.idx_num
        res = 0
        for idx, num in one.items():
            res += num * another[idx]

        return res


# https://leetcode.com/problems/sentence-similarity/
class Solution734:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2): return False

        dictionary = defaultdict(set)
        for w1, w2 in similarPairs:
            dictionary[w1].add(w2)
            dictionary[w2].add(w1)

        for w1, w2 in zip(sentence1, sentence2):
            if w1 == w2: continue
            if w2 not in dictionary[w1]:
                return False

        return True