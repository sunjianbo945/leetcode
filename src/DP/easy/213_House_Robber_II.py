
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[1], nums[0])

        h1 = nums[0]
        h2 = max(nums[1], nums[0])

        for i in range(2, len(nums) - 1):
            h3 = max(h1 + nums[i], h2)
            h1 = h2
            h2 = h3

        f1 = max(h2, h1)

        h1 = nums[1]
        h2 = max(nums[1], nums[2])

        for i in range(3, len(nums)):
            h3 = max(h1 + nums[i], h2)
            h1 = h2
            h2 = h3
        return max(h2, h1, f1)


def main():
    print(Solution().rob([2, 0, 3, 5, 2, 1]))


if __name__=='__main__':
    main()