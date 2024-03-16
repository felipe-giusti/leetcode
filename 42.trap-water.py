class Solution:
    def trap(self, height: List[int]) -> int:
        # two pointer

        # potential ->  min ( max_left, max_right )
        # shift pointer based on which is smaller -> this way we know it will be the min

        #index left / right
        l, r = 0, len(height) - 1
        max_left, max_right = height[l], height[r]
        water = 0


        for _ in range(len(height)):
            if max_left < max_right: # move left
                if max_left - height[l] > 0:
                    water += max_left - height[l]
                
                l += 1
                max_left = max(max_left, height[l])
            else: # move right
                if max_right - height[r] > 0:
                    water += max_right - height[r]
                
                r -= 1
                max_right = max(max_right, height[r])

        return water