#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #using backtracking approach

        phone = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        combinations = []

        if not digits:
            return []

        def backtrack(index, curr_comb):
            # goal
            if index == len(digits):
                combinations.append(curr_comb)
                return # next
            
            curr_digit = digits[index]

            for letter in phone[curr_digit]:
                backtrack(index+1, curr_comb + letter)

        backtrack(0, "")
        return combinations        
    

# @lc code=end

