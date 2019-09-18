from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        res = 0
        m = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                res = max(self.helper(matrix, i, j, m), res)

        return res

    def helper(self, matrix, i, j, dp):

        if (i, j) in dp:
            return dp[(i, j)]

        total = 1
        # left
        if j > 0 and matrix[i][j] < matrix[i][j - 1]:
            total = max(self.helper(matrix, i, j - 1, dp) + 1,total)
        # right
        if j < len(matrix[0]) - 1 and matrix[i][j] < matrix[i][j + 1]:
            total = max(self.helper(matrix, i, j + 1, dp) + 1,total)

        # up
        if i > 0 and matrix[i][j] < matrix[i - 1][j]:
            total =max( self.helper(matrix, i - 1, j, dp) + 1,total)

        # down
        if i < len(matrix) - 1 and matrix[i][j] < matrix[i + 1][j]:
            total = max(self.helper(matrix, i + 1, j, dp) + 1,total)

        dp[(i, j)] = total

        return dp[(i, j)]


# if __name__ == '__main__':
#     print(Solution().longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))