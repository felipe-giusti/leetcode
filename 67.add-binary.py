#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #ideas:
        # 1. transform to binary > sum > transform back
        # 2. Do string sum with carry

        num_a = int(a, 2)
        num_b = int(b, 2)

        #[2:] to remove 0b from string
        return str(bin(num_a + num_b)[2:]) 

# @lc code=end

