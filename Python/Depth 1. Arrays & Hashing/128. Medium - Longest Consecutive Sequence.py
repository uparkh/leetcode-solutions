class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nextMap = {}
        for n in nums:
            nextMap[n] = n + 1
        highestConsecutive = 0
        for n in nextMap:
            # curr = min(nextMap) - causes O(n^2) performance,
            # I was asking myself the wrong question: "How do I jump from 1 to 3?"

            # When I should have been thinking about: "How do I know when I am at the start of
            # a new sequence?" That line of thinking would have led me to realize that I don't need
            # the min, I just need to know if the n - 1 element is in the map/set.
            curr = n
            if (curr - 1) not in nextMap:
                l = 0
                while curr in nextMap:
                    l += 1
                    curr = nextMap[curr]
                highestConsecutive = max(highestConsecutive, l)
        return highestConsecutive

# Neetcode Solution using a set (pretty much how I treated the map as a set)
# class Solution2:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         numSet = set(nums)
#         longest = 0

#         for n in nums:
#             # check if its the start of a sequence
#             if (n - 1) not in numSet:
#                 length = 1
#                 while (n + length) in numSet:
#                     length += 1
#                 longest = max(length, longest)
#         return longest

print(Solution().longestConsecutive([100,4,200,1,3]))
