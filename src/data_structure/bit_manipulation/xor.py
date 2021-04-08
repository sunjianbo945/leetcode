from typing import List


# Concept
#
#     If we take XOR of zero and some bit, it will return that bit
#         a⊕0=a
#     If we take XOR of two same bits, it will return 0
#         a⊕a=0
#     a⊕b⊕a=(a⊕a)⊕b=0⊕b=b
# So we can XOR all bits together to find the unique number.


# https://leetcode.com/problems/single-number/
class Solution136:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a
