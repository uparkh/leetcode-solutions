# Apparently this is a famously hard DP problem... so I'm not gonna force it
# too hard. Spent 32 minutes thinking about it, and I feel like I was on
# the right track, but there really is just too much complexity with having
# to consider the fact that choosing a new balloon to take on. Building
# bottom-up is challenging, maybe I should have tried top-down.

# After looking at the NeetCode Solution, I was indeed on the right track
# with thinking about holding a "pivot" index, and building bottom-up
# by "choosing" balloons to take on (inverting the problem instead of narrowing
# down from "popping"). My intuition was right that a O(n^3) runtime 
# and O(n^2) space solution was optimal. So that feels good, but no way
# was I gonna figure out the extra complexity in the next 2 hours.

# Actually, the real "inversion of the problem" is instead of the base case
# being which balloons to pop first, think of which base case to pop last.
# Popping first doesn't leave a standalone subproblem, because the two
# remaining left and right arrays are connected. Base case of popping a balloon
# last, however, does leave a clean standalone subproblem, because
# the remainders are guaranteed to be disjoint.

# This doesn't mean that it becomes easier, because that value we pop last
# still affects the subarray calculation.
# [3, 1, 5, 8], pop 5 last
# [3, 1], 5, [8] , implicit 5 affects results of [3, 1] and [8]
# Normally there's an implicit 1 there, but we replace it with an implicit 5.

# So, knowing that, the DP cache stores the results for a given range (L, R)
# representing these subarray problems. AHA, and then it becomes very easy
# to find the implicit sentinel values because those are just L-1, R+1 for any
# (L, R), so for the subproblem 1 [3, 1] 5, L=1,R=2, and then that can
# be broken up further...
# Wow that is incredibly clever, there is no chance I would have come up with
# that on my own unless I spent the next week working on it.

# NeetCode Solution
from typing import List
class NeetCodeSolution:
    def maxCoins(self, nums: List[int]) -> int:
        cache = {}
        nums = [1] + nums + [1]

        # offset simply determines the window size we are looking at
        # and iterating the pivot throughe each subarray window
        # 2 -> nums[1:2], nums[2:3], nums[3:4], etc
        # 3 -> nums[1:3], nums[2:4], nums[3:5], etc
        # ...
        for offset in range(2, len(nums)):
            for left in range(len(nums) - offset):
                right = left + offset
                for pivot in range(left + 1, right):
                    # this pivot balloon is popped last, so any elems in
                    # between this pivot and the L, R ptrs do not exist in this
                    # state, find coins
                    # also, nums[left] and nums[right] represent that implicit
                    # concept discussed earlier
                    coins = nums[left] * nums[pivot] * nums[right]

                    # now add any cached subarray calculations if they exist
                    coins += cache.get((left, pivot), 0) + cache.get((pivot, right), 0)

                    # remember we wanna maximize coins
                    cache[(left, right)] = max(coins, cache.get((left, right), 0))

        # now get the main problem (over the whole list)
        return cache.get((0, len(nums) - 1), 0)

# Wow, what a difficult problem. At least I understand and have an intuition
# for the solution. Obviously I'd love to be able to come up with this sol'n
# myself, but understanding such a complex thing it is arguably just as good.
