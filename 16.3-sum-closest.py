#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # iterate + two pointer
        nums = sorted(nums)
        res = None
        min_diff = 20001 # target between -10^4 and 10^4

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                s = (nums[i] + nums[right] + nums[left])

                diff = abs(target - s)
                if diff < min_diff:
                    min_diff = diff
                    res = s

                if s < target: # make it bigger
                    left += 1
                elif s > target: # make it smaller
                    right -= 1
                else: # sum == target
                    return res
        return res


# @lc code=end

