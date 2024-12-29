#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        # idea: split over slashes -> if .. pop last one
        # after looking up other solutions, instead of doing it in reverse, we can just handle it like a stack and pop items from it

        parts = path.split("/")
        res_dirs = []

        for part in parts:            
            if res_dirs and part == "..":
                res_dirs.pop()
            elif part not in ["", ".", ".."]:
                res_dirs.append(part)

        return "/" + "/".join(res_dirs)
        
# @lc code=end

