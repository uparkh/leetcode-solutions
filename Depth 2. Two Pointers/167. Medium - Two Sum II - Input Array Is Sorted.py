# Already did this problem before as part of Data Structures class and recursive analysis.
# The "Two Pointers" problem types seem to be those that have two constant time references to the
# start and end points of a list, and iterate towards the middle.
# NeetCode solution was pretty much the same.
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            currSum = numbers[i] + numbers[j]
            if currSum < target: i += 1
            elif currSum > target: j -= 1
            else:
                return [i+1, j+1]
        return []

print(Solution().twoSum([-1, 1], -1))
