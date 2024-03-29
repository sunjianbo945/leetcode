from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while nums[i] > 0 and nums[i] <= len(nums) and nums[i] != i + 1:
                place = nums[i]-1
                temp = nums[i]
                nums[i]=nums[nums[i]-1]
                nums[place]=temp

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1

        return len(nums) + 1


if __name__ == '__main__':
    print(Solution().firstMissingPositive([3,4,-1,1]))