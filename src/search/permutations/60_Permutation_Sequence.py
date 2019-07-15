import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i for i in range(1, n + 1)]
        ans = []
        self.recur(nums, n - 1, k, ans)

    def recur(self, nums, n, k, ans):
        print(math.factorial(n))
        print(k % math.factorial(n))


def main():
    print(Solution().getPermutation(3,3))


if __name__=='__main__':
    main()