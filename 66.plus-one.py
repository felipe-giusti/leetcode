#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # ideas: list to integer -> sum -> convert back
        # recurrence with +1

        n = len(digits)
        number = sum([digits[i] * (10**(n-i-1)) for i in range(n)]) + 1
        return [int(digit) for digit in str(number)]

# @lc code=end

