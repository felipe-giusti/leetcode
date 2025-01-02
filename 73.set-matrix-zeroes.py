#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # idea 1: go through each row and save 0's column and row
        # update row, column

        rows, cols = set(), set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        
        for i in range(len(matrix)):
            if i in rows:
                matrix[i] = [0]*len(matrix[0])
                continue
            for j in range(len(matrix[0])):
                if j in cols:
                    matrix[i][j] = 0


        
# @lc code=end

