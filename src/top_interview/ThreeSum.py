from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        s_nums = sorted(nums)
        ret = []
        pre = None
        for i in range(len(s_nums)):
            if pre == s_nums[i]:
                continue

            temp = self.twoSum(s_nums[i + 1:], -1 * s_nums[i])
            for t in temp:
                ret.append([s_nums[i]] + t)

            pre = s_nums[i]

        return ret

    def twoSum(self, nums, target):
        ret = []

        l, r = 0, len(nums) - 1

        while l < r:

            if nums[l] + nums[r] == target:
                ret.append([nums[l], nums[r]])
            elif nums[l] + nums[r] < target:
                l+=1
            else:
                r-=1

            while l < len(nums) and l >=1 and nums[l] == nums[l - 1]:
                l += 1
            while r >= 0 and r < len(nums)-1 and nums[r] == nums[r + 1]:
                r -= 1

        return ret


if __name__=='__main__':
    print(Solution().threeSum([1,-1,-1,0]))