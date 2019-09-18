from typing import List
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s = sorted(nums)

        l, r = 0, len(s) - 1

        res = []

        while l <= r:
            if len(res) % 2 == 0:
                res.append(s[r])
                r -= 1
            else:
                res.append(s[l])
                l += 1

        return res


if __name__ == '__main__':
    print(Solution().wiggleSort([1,5,1,1,6,4]))