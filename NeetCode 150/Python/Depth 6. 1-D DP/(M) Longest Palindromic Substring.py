
# My Original Incorrect Solution -- 40 minutes
# I know that I needed to use tabulation, and grow each palindrome from the
# bottom up, but I couldn't quite figure out the details in time.
# I think I was on the right track, though.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Cannot divide and conquer here, I think must tabulate
        res_itvl = []  # palindromic ranges
        cur_long = 1
        for i in range(len(s)):
            if i > 0 and s[i-1] == s[i]:
                res_itvl[-1][1] += 1
                beg, end = res_itvl[-1]
                cur_long = max(cur_long, end - beg + 1)
            else:
                res_itvl.append([i, i])
        print(f'res_itvl: {res_itvl}')

        prev_long = cur_long - 1
        res = ''
        while cur_long > prev_long:  # merge and combine adjacent chars
            for interval in res_itvl:
                beg, end = interval
                l, r = beg - 1, end + 1
                if l < 0 or r >= len(s):
                    break
                if res[l] == res[r]:  # expand intvl
                    new_long = max(cur_long, r - l + 1)
                    if new_long > cur_long:
                        prev_long = cur_long
                        cur_long = new_long
                        res = s[beg: end+1]
                    interval[0] = l
                    interval[1] = r

        return res


# NeetCode Solution
# Time: O(n^3) -- creating a new string res
# Space: O(n)
# Fundamentally my idea was correct: tabulate from bottom-up starting at each
# character. My mistake was forcing the use of an array to track
# the created palindromes, I was too caught up in pre-optimizing my solution,
# when I could have just explored each palindrome starting at any letter,
# and it would be O(n^2)
class NeetCodeSolution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]  # this causes sol'n to be O(n^3)
                    resLen = r - l + 1
                l -= 1
                r += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        return res


# My Modified NC SOlution
# Time -- O(n^2)
# Space -- O(1)
class NCSolutionModded:
    def longestPalindrome(self, s: str) -> str:
        res_l, res_r = 0, 0
        resLen = 0

        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:  # only track highest resLen's
                    res_l, res_r = l, r
                    resLen = r - l + 1
                l -= 1
                r += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res_l, res_r = l, r
                    resLen = r - l + 1
                l -= 1
                r += 1

        return s[res_l : res_r + 1]

