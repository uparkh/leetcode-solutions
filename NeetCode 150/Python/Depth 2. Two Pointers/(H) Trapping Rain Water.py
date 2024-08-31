# MY ORIGINAL SOLUTION WORKED!!!!!!! First Hard problem done in 43m, 3 seconds
# Not pre-optimized at all, but the logic and problem-solving is the most important part!!!
# Hit a roadblock with the edge case (see below), but that was nice, feeling amazing!
class Solution:
    def trap(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        tallest_L, tallest_R = height[0], height[-1]
        trappedArea = 0

        while l < r:
            if tallest_L <= tallest_R:
                while height[l] <= tallest_L and l < r:
                    trappedArea += tallest_L - height[l]
                    l += 1
                tallest_L = height[l]
            else:
                while height[r] <= tallest_R and l < r:
                    trappedArea += tallest_R - height[r]
                    r -= 1
                tallest_R = height[r]
        
        return trappedArea

# NeetCode Solution, is the same logic as mine, but cleaned up more.
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         if not height:
#             return 0

#         l, r = 0, len(height) - 1
#         leftMax, rightMax = height[l], height[r]
#         res = 0
#         while l < r:
#             if leftMax < rightMax:
#                 l += 1
#                 leftMax = max(leftMax, height[l])
#                 res += leftMax - height[l]
#             else:
#                 r -= 1
#                 rightMax = max(rightMax, height[r])
#                 res += rightMax - height[r]
#         return res

print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(Solution().trap([4,2,3]))

