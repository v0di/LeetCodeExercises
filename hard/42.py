class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 1: return 0
        trapped = 0
        maxLeft = height[0] 
        maxRight = max(height[1:])
        for idx in range(1, len(height) - 1):
            if height[idx-1] > maxLeft: maxLeft = height[idx-1]
            if height[idx] == maxRight: maxRight = max(height[(idx+1):])
            y = min(maxLeft, maxRight) - height[idx]
            if y > 0:
                trapped += y
        return trapped
