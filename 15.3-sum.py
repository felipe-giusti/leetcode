#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        triplets = set()
        
        # separate negative, zero, positive
        n, num_z, p = [], 0, []
        for num in nums:
            if num < 0:
                n.append(num)
            elif num == 0:
                num_z += 1
            else: p.append(num)
        
        # if three zeros, add zero
        if num_z >= 3:
            triplets.add((0, 0, 0))

        ns, ps = set(n), set(p)
        # if at least one zero, check n / p
        if num_z:
            for num in ps:
                if -num in ns:
                    triplets.add((-num, 0, num))
        
        def check_list(l: list, s: set):
            for i in range(len(l) - 1):
                for j in range(i+1, len(l)):
                    target = -(l[i] + l[j])
                    if target in s:
                        triplets.add(
                            tuple(sorted([l[i], l[j], target])))

        # no zeros, check if pair of negatives in p
        check_list(n, ps)

        # no zeros, check if pair of positives in n
        check_list(p, ns)

        return triplets
                    

# @lc code=end

