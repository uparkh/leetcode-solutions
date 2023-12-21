# Notes:
# Ensuring duplicates in `t` are taken into account leads me to believe some sort of mapping
# or array match logic is needed.
# The smallest window is going to be the one that starts and ends at a letter from t.
# When the window has MORE occurrences of a character than found in `t` string, then that's
# also an invalid window, shift L.
# When shifting L to arrive at the next character in S, we are guaranteed that it's gonna stop at
# R at the very least, because R's processing steps only happen at chars that are in t.

# My Original Solution, O(m*n). I failed at the test case: s = "aaaaaaaaaaaabbbbbcdd", t = "abcdd"
# At this point I realized that this solution cannot take into account this case where a valid
# substring can contain more than one duplicate of a character found in `t` and still be valid.
# My solution is already janky, and trying to accommodate for this test case would make it
# even more complicated. If the solution I had worked well, then it would be simple to follow,
# and easy to change to accommodate for test cases.

# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         map_s, map_t = {}, {}
#         minStr = ""
#         lenMinStr = len(s) + 1
#         for c in t: map_t[c] = 1 + map_t.get(c, 0)

#         l = 0
#         for r in range(len(s)):
#             if s[r] in map_t:
#                 map_s[s[r]] = 1 + map_s.get(s[r], 0)

#                 while map_s.get(s[r], 0) > map_t[s[r]]: # counts too big, invalid window
#                     if s[l] in map_t:
#                         map_s[s[l]] -= 1
#                         if map_s[s[l]] == 0: map_s.pop(s[l])
#                     l += 1
#                 while s[l] not in map_t:
#                     l += 1
                
            
#             if map_s == map_t: # THE REALLY SLOW PART
#                 minStr = s[l:r+1] if (r - l + 1) < lenMinStr else minStr
#                 lenMinStr = len(minStr)
#                 map_s[s[l]] -= 1
#                 if map_s[s[l]] == 0: map_s.pop(s[l])

#                 while s[l] not in map_t:
#                     l += 1
#                 l += 1
        
#         return minStr


# Neetcode Solution Notes
# Mapping is required, but we can eliminate map comparisons entirely by keeping track of
# how many conditions need to be met (size of 't'), and how many conditions we currently have met
# (is count of char in s >= required count of char in t?). When `num_have` == `num_need`, it is
# a valid substring.
# After a successful window substring is found, simply just pop from the left until the
# `num_have` == `num_need` condition is no longer met.
# Every time a character is popped, reevaluate if the current window is the new min substring.
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                # update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                # pop from the left of our window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""


print(Solution().minWindow("ewcwaefgcf", "cae"))
print(Solution().minWindow("a", "a"))
            
                    

            


