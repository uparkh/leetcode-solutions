# I had the right idea of tying the iteration with a tracking of heights somehow, but couldn't tie
# it all together. I also got that while iterating, any given height cannot extend over lower ones.
# I have to realize that this is okay. I'm not meant to be solving hard problems for the next ~30
# problems.
# Keep restricting time to < 45 mins per problem. Eventually I'll start to see patterns and I can
# then begin to solve these problems more and more.

#Neetcode Solution
from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []  # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea
