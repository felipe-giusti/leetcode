#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start

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
        
        combinations = [""]    

        for d in digits:
            new_combinations = []

            for c in combinations:
                for letter in phone[d]:
                    new_combinations.append(c + letter)
            combinations = new_combinations[:]
        
        return combinations

    

# @lc code=end

