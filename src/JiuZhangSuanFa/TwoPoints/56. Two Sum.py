class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """

    def twoSum(self, numbers, target):
        # write your code here

        nums = [[numbers[i], i] for i in range(len(numbers))]

        nums = sorted(nums, key=lambda x: x[0])
        l, r = 0, len(nums) - 1

        while l < r:

            if nums[l][0] + nums[r][0] == target:
                return [nums[l][1], nums[r][1]] if nums[l][1] < nums[r][1] else [nums[r][1], nums[l][1]]
            elif nums[l][0] + nums[r][0] > target:
                r -= 1
            else:
                l += 1
        return []


class Solution1:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """

    def twoSum(self, numbers, target):
        # write your code here
        memo = {}
        for i in range(len(numbers)):

            if target - numbers[i] in memo:
                return [memo[target - numbers[i]], i]
            else:
                memo[numbers[i]] = i

        return []