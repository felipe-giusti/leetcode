#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d ={}
        for i, num in enumerate(nums):
            t = target - num
            if t in d:
                return [d[t], i]
            d[num] = i
                  
# @lc code=end

