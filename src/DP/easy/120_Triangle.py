from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = []
        dp.append(triangle[-1])
        for i in range(len(triangle) - 1, 0, -1):
            arr = []

            for j in range(len(triangle[i]) - 1):
                arr.append(min(dp[-1][j], dp[-1][j + 1]) + triangle[i - 1][j])

            dp.append(arr)

        return dp[-1][0]



def main():
    print(Solution().minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))


if __name__=='__main__':
    main()