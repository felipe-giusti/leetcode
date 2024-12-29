#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        # idea: split over slashes -> if .. pop last one

        parts = path.split("/")
        back_counter = 0
        res = []

        # doing it in reverse so it's easier to deal with multiple "../" in a row
        for i in range(len(parts)-1, -1, -1):
            part = parts[i]
            if not part or part == ".":
                continue                
            elif part == "..":
                back_counter += 1
            else:
                if back_counter > 0:
                    back_counter -= 1
                    continue
                res.append(part)

        return "/" + "/".join(reversed(res))



        
# @lc code=end

