#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # idea: if 0, insert at 0, if 2: insert at end

        i = 0
        twos = 0
        while i+twos < len(nums):
            match nums[i]:
                case 0:
                    del nums[i]
                    nums.insert(0, 0)
                    i+=1
                case 2:
                    del nums[i]
                    nums.append(2)
                    twos += 1
                case 1:
                    i+=1


# @lc code=end

