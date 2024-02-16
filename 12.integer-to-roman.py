#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        # Idea
        # 40
        # divide by 10 -> 4, 0 -> if 4 or 9
        # subtract / add one + add last ...
       
        roman_dict = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }
            
        s = ""

        for digit, roman in roman_dict.items():
            s += roman * (num//digit)
            num = num%digit
        return s           


# @lc code=end

