class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        #backtracking
        res = []
        visited = [False] * len(nums)
        
        # not optimal because adds same permutation
        def backtrack(p):
            if len(p) == len(nums):
                res.append(p[:])
                return

            n_used = set()
            for i in range(len(nums)):
                if not visited[i] and nums[i] not in n_used:
                    visited[i] = True
                    p.append(nums[i])
                    n_used.add(nums[i])

                    backtrack(p)

                    visited[i] = False
                    p.pop()
        
        backtrack([])
        return res

