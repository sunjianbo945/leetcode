class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """

    def threeSum(self, numbers):
        # write your code here
        if not numbers or len(numbers) < 3: return []
        res = []
        numbers.sort()
        for i in range(len(numbers)):

            if i > 0 and numbers[i] == numbers[i - 1]:
                continue

            twoSumRess = self.twoSum(numbers, i + 1, -numbers[i])
            for twoSumRes in twoSumRess:
                res.append([numbers[i]] + twoSumRes)

        return res

    def twoSum(self, numbers, start, target):
        left = start
        if start >= len(numbers): return []
        end = len(numbers) - 1
        res = []
        while start < end:

            if numbers[start] + numbers[end] == target:
                res.append([numbers[start], numbers[end]])
                start += 1
                end -= 1
                while start < end and numbers[start] == numbers[start - 1]:
                    start += 1

                while start < end and numbers[end] == numbers[end + 1]:
                    end -= 1
            elif numbers[start] + numbers[end] < target:
                start += 1
            else:
                end -= 1



        return res