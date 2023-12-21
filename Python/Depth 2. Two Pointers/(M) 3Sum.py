from typing import List

# My Solution:
# TwoSum is O(n), sorting is O(n log n), thus the threeSum loop is O(n^2).
# Overall it is O(n^2), I don't think O(n) is possible here.
# This solution does not work if any n in nums has more than one pair of other numbers that make
# it add to 0. Gave up at this stage because the solution probably only gets more complex from
# here if I continue the way I am. I think this is good enough, I can explain to the employer 
# everything I have done so far. Test case passing is just gonna take more time, already took
# 55 minutes here.

# class Solution:
#     def threeSum(self, nums: list[int]) -> list[list[int]]:
#         nums.sort()
#         tupleSet = set()
#         res = []
#         for i, n in enumerate(nums):
#             for2Sum = nums
#             for2Sum.pop(i)
#             twoSumToN = self.twoSum(for2Sum, -n)
#             if len(twoSumToN) != 0:
#                 t = twoSumToN + [n]
#                 t.sort()
#                 t = tuple(t)
#                 if t not in tupleSet:
#                     res.append(list(t))
#                     tupleSet.add(t)
#         return res
            
#     # TwoSum that returns the numbers, not indices, that add to get target.
#     def twoSum(self, sorted_nums: list[int], target: int) -> list[int]:
#         i, j = 0, len(sorted_nums) - 1
#         while i < j:
#             currSum = sorted_nums[i] + sorted_nums[j]
#             if currSum < target: i += 1
#             elif currSum > target: j -= 1
#             else:
#                 return [sorted_nums[i], sorted_nums[j]]
#         return []


# NeetCode Solution Notes 
# (1) Note that sorting the array means that we can just check if the number to the left of the
#   current one is the same as the current one, it means that we have already processed that number,
#   and we can skip the current one since it's a duplicate.

# (2) We can choose to skip all negative xor positive integers in our array as as the starter value a.
#   Notice that if a < 0, then for b + c = -a, b or c must be positive. Vice versa. Since we are
#   guaranteed that in each equation, one number must be positive or negative, we can only set the
#   starter value a to be negatives or positives. We choose to ignore positives, as we can more
#   intuitively break the entire loop early.

# (3) After finding the first pair of numbers that make the threeSum = 0, we have to keep running 
#   the TwoSum for more pairs, or until we are done going through the array.
#   That last while loop ensures that we don't keep going through duplicate intermediate numbers,
#   i.e. if we had [-2, 0, 1, 1, 1, 1, 1, 1, 2], that while loop ensures that we skip all the
#   unnecessary 1s.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
            res = []
            nums.sort()

            for i, a in enumerate(nums):
                # Skip positive integers
                if a > 0: # Note (2)
                    break

                if i > 0 and a == nums[i - 1]: # See note (1)
                    continue

                l, r = i + 1, len(nums) - 1
                while l < r: # Modified TwoSum
                    threeSum = a + nums[l] + nums[r]
                    if threeSum > 0:
                        r -= 1
                    elif threeSum < 0:
                        l += 1
                    else:
                        res.append([a, nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while nums[l] == nums[l - 1] and l < r: # Note (3)
                            l += 1
            return res

print(Solution().threeSum([-2,0,1,1,2]))
