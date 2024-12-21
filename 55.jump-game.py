#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # go through array, if current > reachable, change
        reachable = 0
        for i, num in enumerate(nums):
            if reachable < num:
                reachable = num

            # can't continue
            if reachable <= 0:
                return i == len(nums) - 1

            reachable -= 1

        return True
            


        
# @lc code=end

