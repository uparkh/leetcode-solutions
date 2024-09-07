from collections import Counter
# Tried my best to come up with a DP solution but failed. I knew of the property of
# numbers divisible by 3 having their digits summing to a multiple of 3, but couldn't
# come up with a way to implement it.


# @lee215 had a way using this property
# the idea is to just kick out any digits that are contributing to a nonzero modulo 3
# Time -- O(n logn) due to sorting
# Space -- O(n) due to counter
class Solution:
    def largestMultipleOfThree(self, A):
        total = sum(A)
        count = Counter(A)
        A.sort(reverse=1)  # trying to maximize the number

        def f(i):
            if count[i]:
                A.remove(i)
                count[i] -= 1
            if not A: return ''  # if A is empty after kickout, return empty string
            if not any(A): return '0'  # if A is all zeros, return '0'
            if sum(A) % 3 == 0: return ''.join(map(str, A))

        if total % 3 == 0:  # already good
            return f(-1)

        # for all these cases it's important we try to kick out the smallest digits first
        # so the final number is the largest possible
        # if total % 3 == 1, we need to remove one of 1, 4, 7 if they exist
        if total % 3 == 1 and count[1] + count[4] + count[7]:
            return f(1) or f(4) or f(7)
        # if total % 3 == 2, we need to remove one of 2, 5, 8 if they exist
        if total % 3 == 2 and count[2] + count[5] + count[8]:
            return f(2) or f(5) or f(8)
        # if total % 3 == 2 even after above, then there may be two of 1, 4, 7 contributing to mod == 2
        if total % 3 == 2:
            return f(1) or f(1) or f(4) or f(4) or f(7) or f(7)
        # if total % 3 == 1 even after above, then there may be two of 2, 5, 8 contributing to mod == 1
        return f(2) or f(2) or f(5) or f(5) or f(8) or f(8)


# DP solution
# Time -- O(n logn) due to sorting, but can be O(n) if we use counting sort
# I'll try coding the counting sort version for my own practice and understanding
# Space -- O(1)
class DPSolution:
    def largestMultipleOfThree(self, digits):
        dp = [-1,-1,-1]
        for a in sorted(digits)[::-1]:
            # dp[:] + [0] is used to make sure we don't modify dp while iterating over it
            # 0 is added to make sure we don't miss the case where we don't use any digit
            for x in dp[:] + [0]:
                # greedily construct new number with this new digit
                # i.e. if x = 98, a = 1, only makes sense to construct 98*10 + 1 = 981 with new digit
                y = x * 10 + a

                # only track the largest number under each modulo 3 value
                dp[y % 3] = max(dp[y % 3], y)
        return str(dp[0]) if dp[0] >= 0 else ""

# counting sort version of the above DP solution
# works but too much space usage, could have used an unstable in-place counting sort,
# but whatever, I was able to implement the counting sort version
# Time -- O(n)
# Space -- O(n)
class Solution:
    def largestMultipleOfThree(self, digits):
        dp = [-1,-1,-1]

        # counting sort
        count = [0] * 10
        csort = [0] * len(digits)
        for d in digits:
            count[d] += 1
        for i in range(1, 10):
            count[i] += count[i-1]
        for i in range(len(digits)-1, -1, -1):
            d = digits[i]
            count[d] -= 1
            csort[count[d]] = d

        for a in csort[::-1]:
            for x in dp[:] + [0]:
                y = x * 10 + a
                dp[y % 3] = max(dp[y % 3], y)
        return str(dp[0]) if dp[0] >= 0 else ""

