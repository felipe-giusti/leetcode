#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # go through array, if current > reachable, change
        # after looking up other solutions: we CAN have reachable be 0, what can't happen is not being able to jump AFTER reaching a spot, with this we can ignore the return conditional
        reachable = 0
        for i, num in enumerate(nums):
            # can't continue
            if reachable < 0:
                return False
            
            if reachable < num:
                reachable = num

            reachable -= 1

        return True
            
# @lc code=end

