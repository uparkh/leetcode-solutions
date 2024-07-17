from typing import List

# My Original Solution -- 26 minutes
# Time -- O(n)
# Space -- O(n)
# I know how to reduce the Space to O(1), easily, by not using a net
# array, and using modulus ops, but conceptually I get it, and that's what
# I care about!
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        net = [gas[i] - cost[i] for i in range(N)] * 2
        # can't ever start at negative net station
        cur_gas = net[0]
        l = 0
        # print(f'N = {N}, 2N = {2*N}')
        # print(f'net: {net}')
        for r in range(1,2*N):
            # print(l, r, cur_gas)
            if cur_gas < 0:
                l = r
                cur_gas = net[l]
            else:
                cur_gas += net[r]

            if l >= N:  # loop? no chance of completion
                return -1
            if (r - l) >= N:  # circuit completed
                return l
        return -1


# NeetCode Solution
# He just inverted the problem and went from there. I really should be
# thinking about inverting the problem...
class NeetCodeSolution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start, end = len(gas) - 1, 0
        total = gas[start] - cost[start]

        while start >= end:
            while total < 0 and start >= end:
                start -= 1
                total += gas[start] - cost[start]
            if start == end:
                return start
            total += gas[end] - cost[end]
            end += 1
        return -1

