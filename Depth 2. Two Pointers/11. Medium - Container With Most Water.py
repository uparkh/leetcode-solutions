# Fundamental intuition: why shift the pointer that has a bigger value, when if instead if you
# shift the one with a smaller value, you have a chance of getting a bigger area?
# It's the same decision behind TwoSum on sorted list, shift the value that gets you closer
# to the target. In TwoSum the target was a number, and you could adjust L and R pointers based on
# their sums to get closer to the solution. Here, the target is a bigger area. Shifting the larger
# of any 2 pointers 100% won't get you a bigger area, but shifting the smaller has a chance of
# getting a bigger area.

class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        maxArea = 0
        while l < r:
            minHeight = min(height[l], height[r])
            maxArea = max(maxArea, minHeight*(r-l))
            if minHeight == height[l]: l += 1
            elif minHeight == height[r]: r -= 1
        return maxArea

print(Solution().maxArea([1,1]))
