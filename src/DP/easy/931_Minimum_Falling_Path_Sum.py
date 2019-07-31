from typing import List

class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        arr = A[-1]
        for i in range(len(A) - 2, -1, -1):
            temp = []
            for j in range(len(A[i])):
                temp.append(self.helper(A[i][j], j, arr))

            arr = temp

        return min(arr)

    def helper(self, number, column, arr):
        res = number + arr[column]
        if column > 0:
            res = min(res, number + arr[column - 1])

        if column < len(arr) - 1:
            res = min(res, number + arr[column + 1])

        return res

def main():
    print(Solution().minFallingPathSum([[1,3,1],[1,5,1],[4,2,1]]))


if __name__=='__main__':
    main()
