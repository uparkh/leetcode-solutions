#NeetCode Solution
# Driving intuition: check png
# For sorted order (which makes sense, because relative order stays the same)
# "If the time to hit of a previous car order-wise takes less or same time to hit target than the
# one in front, then they must combine into a fleet"
# Additionally, we are rate limited by the slowest car in the fleet, so the stack is ordered in
# car fleet speeds.

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s) # comparing times taken to get to the target
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

