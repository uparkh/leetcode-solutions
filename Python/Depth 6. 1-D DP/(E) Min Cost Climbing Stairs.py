from typing import List
# No acceptable Solution from me here, I seriously just couldn't figure it out
# it was on the tip of my tongue the whole 24 minutes I was trying to get it,
# but no cigar.

# NeetCode Solution
# Again I am dumbfounded... he just inverted the problem and this becomes
# 20000x easier...
# Another thing, the position we're trying to reach is not the last index/floor
# but rather the position after that, there's a subtle difference, which is
# why for the test case [10, 15, 20] I kept getting min(30, 35) as a result,
# instead of 15 when I tried it myself

# Inverting also makes it so cost[0] contains the decision tree solution
# starting at index 0, and cost[1] contains the decision tree solution starting
# at index 1. Can think of it as the solution for index 0 start pos as
# having dependencies on later subsolutions of the array.
#  +---+---+
#  |   V   V
# [10, 15, 20, end]
#      ^   ^  
#      +---+


# Here is the decision tree for this problem. I have now observed that a 
# tabulation/dynamic programming solution comes from the base of the tree
# which starts at later indices. This is literally what it means to do a 
# "bottom-up" solution. I literally start at the bottom of the decision
# tree and build the solution upwards from there. The ending states
# are at index 0, and index 1.

# All dynamic programming solutions should be done only with tabulation
# and going bottom-up, I will no longer do recursive solutions.
#           0        
#           │        
#           │        
#       1◄──┴──►2    
#       │   10  │    
#       │       │    
#  3◄───┴──►2   └──►3
#      15   │   20   
#           │        
#       3◄──┘        
#          20
class NeetCodeSolution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])

