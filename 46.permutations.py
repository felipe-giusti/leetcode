class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        # backtracking / dfs
        res = []

        def backtrack(cur, visited: set):
            #goal
            if len(cur) == len(nums):
                res.append(cur[:])
                return
            
            for num in nums:
                if num in visited:
                    continue
                
                visited.add(num)
                cur.append(num)

                backtrack(cur, visited)

                visited.remove(num)
                cur.pop()
                
                
        backtrack([], set())      
        return res  