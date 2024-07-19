from typing import List
from collections import defaultdict

# My Original Solution -- 36 minutes
# Time: O(n) -- two passes required
# Space: O(1) -- size of the alphabet is constant

# Took a bit of time, I was too stubborn to do 2 passes through the list
# but I probably shouldn't have been. I don't think there's any other way
# to do this in one pass? How else can you know the ending index of the
# range?
# Anyway I'm ultimately pretty proud that I was able to solve it, with a tiny
# bit of help from the first 5 mins of the NC video. Finally beginning to
# understand the greedy way of thinking.
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        end_map = defaultdict(int)
        for i, c in enumerate(s):
            end_map[c] = i

        # print(end_map)
        beg, end = 0, end_map[s[0]]
        res = []
        for i, c in enumerate(s):
            # print(i, c, beg, end)
            end = max(end, end_map[c])
            if i == end:
                res.append(end - beg + 1)
                beg = i + 1
        return res


# NeetCode Solution
# Wow, this is functionally the exact same solution as I had! That makes
# me even happier that I was able to do this with much cleaner code.
class NeetCodeSolution:
    def partitionLabels(self, S: str) -> List[int]:
        count = {}
        res = []
        i, length = 0, len(S)
        for j in range(length):
            c = S[j]
            count[c] = j

        curLen = 0
        goal = 0
        while i < length:
            c = S[i]
            goal = max(goal, count[c])
            curLen += 1

            if goal == i:
                res.append(curLen)
                curLen = 0
            i += 1
        return res

