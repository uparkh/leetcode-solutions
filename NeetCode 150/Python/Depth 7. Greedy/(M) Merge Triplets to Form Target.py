from typing import List

# My Original Solution -- 20 min
# n == len(triplets)
# Time -- O(n)
# Space -- O(1) // technically always three guaranteed == constant
# Works, but I really don't think it is all that efficient.
# Something is wrong when I am placing consistently bottom 10% of the normal
# distribution.
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [0, 0, 0]
        # locked = set(int)  # triplet positions that are set
        for triplet in triplets:
            # print('---------------------------')
            # print(f'res: {res}')
            # print(f'triplet: {triplet}')
            this_max = [max(a, b) for (a, b) in zip(res, triplet)]
            # print(f'this_max: {this_max}')
            is_better = True
            for i, m in enumerate(this_max):
                if m > target[i]:
                    is_better = False
                    break
            if is_better:
                res = this_max
        return res == target


# NeetCode Solution
# We were pretty much thinking the same thing, he just managed to more elegantly
# code the concept of "keeping the highest possible index found without
# overshooting the target".
class NeetCodeSolution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()  # similar to the 'locked' set idea I had

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for i, v in enumerate(t):
                if v == target[i]:  # ohhh, by only using ==, not <=, he avoids
                    good.add(i)     # having to do memory updates for vals less
        return len(good) == 3       # than or equal to (unnecessary)

