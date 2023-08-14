# TOTAL TIME: 35 mins

# My Original Solution - O(log n) time, O(1) space
# Hardest part here was trying to figure out the pattern to create conditions to choose the
# left half or the right half of the binary search range. This is an incredibly messy solution,
# reflected in beating 21.73% runtime wise.

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            med = (l + r) // 2
            # if target < nums[l] and target < nums[med]:
            #     l = med + 1
            # elif nums[l] > nums[med] and target < nums[med]:
            #     r = med - 1
            if target < nums[med]:
                if nums[l] > nums[med]:
                    r = med - 1
                elif target < nums[l]:
                    l = med + 1
                else:
                    r = med - 1
            elif target > nums[med]:
                if target <= nums[r] or nums[r] <= nums[med]:
                    l = med + 1
                elif target > nums[r]:
                    r = med - 1
            else:
                return med
        return -1

# NeetCode Solution - O(log n) time, O(1) space
# Cleaner, I needed to see this. I just couldn't piece together a clean solution in my head,
# got too lost in the conditionals.
# The key difference in my understanding vs. his is that he divided the outermost conditionals
# into evaluating whether or not the median value is in the left sorted portion
# or the right sorted portion, and then performed the relevant target comparisons.

# Still only beats 42.81% of solutions runtime-wise, but I cannot find a solution in the
# solutions section that is different to this one... the runtimes are 2x as fast, likely what
# happened is that perhaps the hardware was different when they ran it.
class NeetCodeSolution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            # left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
