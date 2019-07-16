from typing import List

class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        ans = []
        nums = [i for i in range(1, n + 1)]
        self.recur(nums, k - 1, ans)
        temp = ""
        for i in range(len(ans)):
            temp += str(ans[i])

        return temp

    def recur(self, nums: List[int], k: int, ans: List[int]):

        if len(nums) == 1:
            ans.append(nums[0])
            return
        # the place that the number will put at front
        place = k // math.factorial(len(nums) - 1)
        ans.append(nums[place])
        self.recur(nums[:place] + nums[place + 1:], k % math.factorial(len(nums) - 1), ans)


def main():
    print(Solution().getPermutation(3,3))


if __name__=='__main__':
    main()