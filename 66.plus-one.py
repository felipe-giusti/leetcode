#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # ideas: list to integer -> sum -> convert back
        # recurrence / iterate over list adding +1

        for i in range(len(digits) - 1, -1, -1):
            
            # no carry, just return
            if digits[i] + 1 != 10:
                digits[i] += 1
                return digits

            # carry
            digits[i] = 0

        # no return after loop -> still has carry
        return [1] + digits
        

# @lc code=end

