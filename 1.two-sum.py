#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            t = target - num
            if t in nums[i+1:]:
                return [i, nums[i+1:].index(t)+ i+1]
                  
# @lc code=end

