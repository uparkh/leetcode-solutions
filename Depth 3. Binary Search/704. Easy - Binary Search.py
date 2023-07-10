import random

# My original solution, just a simple binary search.
# O(log n)

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            middle_index = (l+r)//2
            if target < nums[middle_index]:
                r = middle_index - 1
            elif target > nums[middle_index]:
                l = middle_index + 1
            else:
                return middle_index
        return -1
    
# NeetCode Solution
# What he means by the overflow potential is that adding 2 left and right index integers that
# are close to the integer limit will cause an integer overflow, throwing off the algorithm after 
# dividing a negative index integer by 2.
# His solution makes sure that there can be no overflow.

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         l, r = 0, len(nums) - 1

#         while l <= r:
#             m = l + ((r - l) // 2)  # (l + r) // 2 can lead to overflow
#             if nums[m] > target:
#                 r = m - 1
#             elif nums[m] < target:
#                 l = m + 1
#             else:
#                 return m
#         return -1


arr = [random.randint(-500, 500) for i in range(15)]
arr.sort()
# searchFor = random.choice(arr)
searchFor = random.randint(-500, 500)
print(arr)
print(f"Found {searchFor} at index {Solution().search(arr, searchFor)}")
# print(Solution().search([-339, -300, -256, -195, -187, -175, -112, -45, -37, 134, 284, 314, 330, 395, 427], -37))
