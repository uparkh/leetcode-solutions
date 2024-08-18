# My Original Solution -- 57 min
# I was really close to getting it, I just couldn't figure out the final
# bit of logic for dealing with duplicates, but oh well! I tried my best.

# New Mistake unlocked: I started with bottom-up approach....
# I have finally decided that I will no longer do this, apparently in
# interviews they won't really care which solution I do, top-down or
# bottom-up, as long as it works.
# I should practice both, but DP only after rec. memo.
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        M = len(t) + 1
        dp = [0] * M
        dp[0] = 1
        print('      ' + '  '.join(t))
        # freq = defaultdict(int)
        for i, cs in enumerate(s):
            # freq[cs] += 1
            cur = dp
            # same_num = 0
            for j, ct in enumerate(t):
                # print(j, cs, ct, cs == ct)
                if j > i:
                    break
                if cs == ct:
                    cur[j+1] = dp[j] + dp[j+1]
                    # same_num += 1
                # if same_num == freq[ct]:
                #     break
            dp = cur
            print(cs, cur)
        return dp[-1]
        

# After looking at NC solution, I was on the right track here, and almost
# had the solution, but I had the recurrence relation in the wrong direction.
# At each step in the decision tree, there are 2 options -- take the char
# or skip it, and instead of filling in the 2 DP matrix top left to bot right
# I should have started bot right and go to top left.

# That being said, after filling out the 2D DP matrix for this problem,
# it is kinda genius, I don't think I would have figured this out by myself.

# NeetCode Solution -- O(n * m) time and space, n = len(s), m = len(t)
# But space can be optimized to O(m) because only one row is needed.
class NeetCodeSolution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}

        # subproblem for t='' always = 1, bc empty string always in `s`
        # position `len(s) + 1` corresponds to s='', t='', res = 1
        for i in range(len(s) + 1):
            cache[(i, len(t))] = 1

        # subproblem for s='' always = 0 if t!='', no subseq. possible in `t`
        for j in range(len(t)):
            cache[(len(s), j)] = 0

        for i in range(len(s) - 1, -1, -1):
            for j in range(len(t) - 1, -1, -1):
                if s[i] == t[j]:
                    # (i + 1, j + 1) = take this char, advance `t` string
                    # (i + 1, j) = skip this char, don't advance `t` string
                    cache[(i, j)] = cache[(i + 1, j + 1)] + cache[(i + 1, j)]
                else:
                    # "null action" = just take previous result
                    cache[(i, j)] = cache[(i + 1, j)]
        return cache[(0, 0)]

