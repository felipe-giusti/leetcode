#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
from collections import defaultdict
class Solution:
    def countAndSay(self, n: int) -> str:
        
        def say(s):
            counter = 1
            res = ""

            for i in range(len(s)-1):
                if s[i] == s[i+1]:
                    counter += 1
                else:
                    res += str(counter) + s[i]
                    counter = 1
            res += str(counter) + s[-1]
            return res


        s = "1"
        for i in range(1, n):
            print(f"{i}: {s}")
            s = say(s)
        return s
        
# @lc code=end

