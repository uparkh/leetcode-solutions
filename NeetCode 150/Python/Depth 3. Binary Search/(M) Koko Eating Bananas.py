# My Solution

# Order DOES NOT matter here. Sorting is on the cards, especially considering this problem
# is under Binary Search folder.
# The minimum eating speed is such that all hours h are used for eating.
# On the last pile, the last hour will be used up.

# [4, 11, 20, 41, 83] h = 6

# O(n) solution would be to sum up each element, divide by number of hours, round up, and bam,
# minimum eating speed. But this doesn't require a binary search or sorting.
# Nevermind, this does not work, because of the distinct number of piles.
# If all piles were combined, then this would work, because of averaging. But they are distinct.

# After 30 minutes I don't even have code written down, which means that in an interview I pretty
# much would be screwed. Just gonna look at the solution and get rid of my ego.

# NeetCode Solution, O(n * log n)
import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l, r = 1, max(piles)
        res = max(piles)

        # l and r are lower and upper bounds on eating speeds. Their units are bananas/hr.
        # That's why l starts at 1, to ensure that we have in our range all possible eating speeds
        # for a given piles array.
        while l <= r:
            k = (l + r) // 2 # Use of binary search I didn't think of.
            # Seems that the core idea of binary search algos is that fundamentally
            # you are comparing a target value to some median value, and shifting the next
            # range.
            # So it seems that with binary search, we don't necessarily NEED to operate on arrays,
            # we're operating on RANGES of values to find a desired TARGET that corresponds to a
            # situation.

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(p / k)

            # If the total time for this median utilizes <= the full possible hours
            # that means that it is a valid eating speed that will get all piles done before
            # hours are done.
            if totalTime <= h:
                res = min(res, k) # keep track of the lowest eating speed encountered 
                r = k - 1 # classic binary search shifting to lower range
            else:
                l = k + 1 # classic binary search shifting to upper range
            # note that there is no defined 'target' but we do get the binary search to complete
            # until the classic binary search invalidation condition of l > r, because we want
            # to explore all logical min speeds
        return res

# The main takeaway is that binary search operates on RANGES, not necessarily arrays, and the goal
# is to find a TARGET value or multiple values, using a condition to rule out which lower
# and upper ranges are desired.

print(Solution().minEatingSpeed([30,11,23,4,20], 6))
