# My Original Incorrect Solution -- 40 minutes
# I was getting somewhere. Again I realize the recurrence relation
# but just couldn't quite get it, sadly. I guess it's good that I'm recognizing
# the recurrence relation, I just gotta get better at "putting it into words
# (code)."

# I know my mistake now... in my diagram, instead of making a decision tree,
# I made a decision graph. So instead for "112", tree branches join together at
# the '2' node, instead of making the '2' node a leaf of each way branch.
# This led me down this odd solution of multiplying the branches at each
# common node, but the edge case "1123" does not have any common nodes,
# so my algorithm falls apart.
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        res = 1
        branch_mult = 1
        for i in range(len(s)):
            if i < len(s) - 1 and self.is_valid_code(s[i:i+2]):  # double char
                # need to handle '0' cases, but I'm on to something!!
                if '0' in s[i:i+2]:
                    branch_mult -= 1
                else:
                    branch_mult += 1
                continue
            if self.is_valid_code(s[i]):  # single char
                res *= branch_mult  # consume the multiplier
                branch_mult = 1

        return res

    def is_valid_code(self, strnum: str) -> bool:
        if strnum[0] == '0':
            return False
        num = int(strnum)
        if 1 <= num <= 26:
            return True
        return False


# NeetCode Solution
# Time -- O(n)
# Space -- O(n)
# Basically coded up the intuition I had, branching out properly.
# Iterating from end to start here is the only option, because it makes
# 0 invalidation very easy. Any 0 invalidates possible branches at that idx.
# Array/map "dp" tracks number of ways from that position onwards, building
# bottom up according to the decision tree.
# Also by setting dp[i+2] makes any ways possible after a double char code.
# Although I don't think they needed a map here, list does fine.
class NeetCodeSolution:
    def numDecodings(self, s: str) -> int:
        # Memoization
        # dp = {len(s): 1}

        # def dfs(i):
        #     if i in dp:
        #         return dp[i]
        #     if s[i] == "0":
        #         return 0

        #     res = dfs(i + 1)
        #     if i + 1 < len(s) and (
        #         s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
        #     ):
        #         res += dfs(i + 2)
        #     dp[i] = res
        #     return res

        # return dfs(0)

        # Dynamic Programming
        dp = {len(s): 1}
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
            ):
                dp[i] += dp[i + 2]
        return dp[0]

