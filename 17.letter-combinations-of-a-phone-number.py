#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start

from collections import deque

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #using iteratively approach

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

        if not digits:
            return []

        # add c for each string
        # next iteration -> create new string for each string + add
        # 23
        # a b c
        # ad ae af bd be bf ...
        # adg adh adi ...

        i = 0
        comb_stack = deque([l for l in phone[digits[i]]])
        

        while i < len(digits)-1:
            i+=1
            for _ in range(len(comb_stack)):
                curr = comb_stack.pop()
                for l in phone[digits[i]]:                    
                    comb_stack.appendleft(curr+l)
        return list(comb_stack)    
    

# @lc code=end

