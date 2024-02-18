#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman_dict = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
             'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1
        }

        n = 0
        while s:
            try:
                n += roman_dict[s[:2]]
                s = s[2:]
            
            except KeyError:
                n += roman_dict[s[:1]]
                s = s[1:]
        return n

  
# @lc code=end
