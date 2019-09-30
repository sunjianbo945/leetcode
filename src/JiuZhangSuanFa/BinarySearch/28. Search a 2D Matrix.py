# https://www.lintcode.com/problem/search-a-2d-matrix/description

class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """

    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix: return False

        row_l, row_r = 0, len(matrix) - 1

        while row_l + 1 < row_r:

            mid = row_l + (row_r - row_l) // 2

            if target == matrix[mid][0]:
                return True
            elif target > matrix[mid][0]:
                row_l = mid
            else:
                row_r = mid

        if matrix[row_l][0] == target or matrix[row_r][0] == target:
            return True

        if target < matrix[row_l][0]: return False
        row = row_l
        if target > matrix[row_r][0]:
            row = row_r

        l, r = 0, len(matrix[0]) - 1

        while l + 1 < r:

            mid = (l + r) // 2

            if target == matrix[row][mid]:
                return True
            elif target >= matrix[row][mid]:
                l = mid
            else:
                r = mid

        return matrix[row][l] == target or matrix[row][r] == target

