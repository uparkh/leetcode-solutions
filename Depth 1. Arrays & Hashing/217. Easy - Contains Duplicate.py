class Solution(object):
    def containsDuplicate(self, nums : list[int]) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        tracker = set()
        for n in nums:
            if n in tracker:
                return True
            tracker.add(n)
        return False

s = Solution()
numbers = [1,1,1,3,3,4,3,2,4,2]
print(s.containsDuplicate(numbers))

