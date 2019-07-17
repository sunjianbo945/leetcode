
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        num = 0
        max_num = nums[0]
        for i in range(len(nums)):
            max_num = max(num + nums[i], max_num)
            num = max(0, num + nums[i])

        return max_num


class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        num = 0
        max_num = nums[0]
        for i in range(len(nums)):
            max_num = max(num + nums[i], max_num)
            num = max(0, num + nums[i])

        return max_num

def main():
    print(Solution().maxSubArray([-2, 0, 3, -5, 2, -1]))


if __name__=='__main__':
    main()