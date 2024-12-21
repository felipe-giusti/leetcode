#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#

# @lc code=start
from collections import deque, defaultdict
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # backtracking problem

        # 1 get unique values (choices) -> rows / cols / squares (can add dict{int:[]})
        # goal: i == 81

        # get r, c from i -> if char is '.' -> for val in choice -> try backtracking (can call func on if statement and return True)
                                    # backtrack -> board[i][j] = c ; backtrack(i+1); board[i][j] = ['.']                                 

        # else (normal digit) -> continue backtrack -> if backtrack(i+1)

        row_choices, col_choices, sq_choices = defaultdict(set), defaultdict(set), defaultdict(set)
        stack = deque()

        for i in range(9):
            for j in range(9):
                char = board[i][j]

                if char != ".":
                    row_choices[i].add(char)
                    col_choices[j].add(char)
                    sq_choices[(i//3, j//3)].add(char)
                else:
                    # add positions that need to be filled
                    stack.append((i, j))
        
        def backtrack(i, j):

            #goal
            if not stack:
                # if valid, True
                


# @lc code=end

