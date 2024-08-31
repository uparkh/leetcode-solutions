# My Original Solution -- 12 minutes
# Recursion with memoization.
# Time: O(n) -- repeat calculations are avoided
# Space: O(n)
# Pretty easy -- the optimal subproblem was very clearly visible.
class RecursiveSolution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def cs(n):
            if n in cache:
                return cache[n]
            if n == 1:
                return 1
            if n == 2:
                return 2

            # requires 1 step from previous, or 2 steps from previous
            cache[n] = cs(n-1) + cs(n-2)  
            return cache[n]

        return cs(n)


# Global Cache Original Solution
# Making the cache a class member speeds up all the future calculations,
# nice little hack for 99% runtime and >50% space.
class FastRecSolution:
    def __init__(self):
        self.cache = {}

    def climbStairs(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        if n == 1:
            return 1
        if n == 2:
            return 2
        self.cache[n] = self.climbStairs(n-1) + self.climbStairs(n-2)  
        return self.cache[n]


# Tabulation (bottom-up) Solution
# Not nearly as fast/efficient as globally memoized top-down, but still has
# room for improvement, but I get the idea at this point, this is just
# DP for Fibonacci numbers.
class TabulationSolution:
    def climbStairs(self, n: int) -> int:
        cache = [0] * 46
        cache[1] = 1
        cache[2] = 2
        if n <= 2:
            return cache[n]
        for num in range(3, n+1):
            cache[num] = cache[num-1] + cache[num-2]
        return cache[n]


# NeetCode Solution
# Even simpler tabulation, we don't actually need an array, since we
# only track the last two values.
# Time: O(n)
# Space: O(1)
class NeetCodeSolution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        n1, n2 = 2, 3

        for _ in range(4, n + 1):
            temp = n1 + n2
            n1 = n2
            n2 = temp
        return n2

