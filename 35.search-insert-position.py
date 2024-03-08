#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # binary search

        low, high = 0, len(nums)
        while high > low:
            mid = (low + high)//2
            if target < nums[mid]:
                high = mid
            elif target > nums[mid]:
                low = mid + 1
            else:
                return mid
        # ended while and didn't return, insert in list
        nums.insert(low, target)
        return low

# @lc code=end

