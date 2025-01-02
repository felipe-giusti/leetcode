#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # idea Dyn Prog -> get top and left edge -> do something like dijikstra with i-1, j-1

        # calculate top row
        for i in range(1, len(grid[0])):
            grid[0][i] += grid[0][i-1]

        # calculate left column
        for j in range(1, len(grid)):
            grid[j][0] += grid[j-1][0]
            
        # calculate inner
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                grid[i][j] += min(grid[i][j-1], grid[i-1][j])
        
        return grid[-1][-1]



# @lc code=end

