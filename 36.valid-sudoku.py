#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # just need to check validity, no backtracking needed
        
        seen = []

        for i in range(9):
            for j in range(9):
                char = board[i][j]
                if char != ".":
                    seen.extend([(char, i), (j, char), (char, i//3, j//3)])
        return len(seen) == len(set(seen))


# @lc code=end

