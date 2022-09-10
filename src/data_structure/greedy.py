# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/
class Solution1963:
    def minSwaps(self, s: str) -> int:
        # Explanation : To swap optimally, we always swap First Closing and Last Open bracket so that in a single
        # swap we can make two pairs balanced []][[] We now again take out the unbalanced parenthesis after swapping ][.
        mismatch = 0
        balance = 0
        for char in s:
            if char == '[':
                balance += 1
            else:
                if balance > 0:
                    balance -= 1
                else:
                    mismatch += 1

        return (mismatch + 1) // 2
