from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        if k == 0:
            return ans

        self.dfs_helper(1, k, n, [], ans)
        return ans

    def dfs_helper(self, start: int, k: int, target: int, cur: List[int], result: List[List[int]]):

        if k == 0:
            if target == 0:
                result.append(cur)
            return

        for i in range(start, 10):

            if i > target:
                continue

            self.dfs_helper(i + 1, k - 1, target - i, cur + [i], result)


def main():
    print(Solution().combinationSum3(3,8))

if __name__=='__main__':
    main()