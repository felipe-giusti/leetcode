class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        #backtracking
        res = set()
        visited = [False] * len(nums)
        
        # not optimal because adds same permutation
        def backtrack(p):
            if len(p) == len(nums):
                res.add(tuple(p))
                return

            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    p.append(nums[i])

                    backtrack(p)

                    visited[i] = False
                    p.pop()
        
        backtrack([])
        return res

