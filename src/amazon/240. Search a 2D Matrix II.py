class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        x, y = len(matrix) - 1, 0

        while x >= 0 and y < len(matrix[0]):

            if matrix[x][y] == target:
                return True

            if matrix[x][y] < target:
                y += 1
            else:
                x -= 1

        return False

