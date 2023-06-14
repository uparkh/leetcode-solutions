# Was struggling quite a bit. I just couldn't quite imagine a way to count how many intermediate
# # letters are swapped upon discretely realizing when the maximum number of initial swaps.
# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         l = 0
#         longest = 0
#         numSwapped = 0
#         for r in range(len(s)):


# NeetCode Solution. I understand the (r - l + 1) - maxf > k
# part comes from knowing that in a string where all characters are distinct, output is 1 + k.
# I will need to watch the video solution to more properly understand the intuition behind this,
# though.
# Ok, so the fundamental intuition is that in order to maximize the substring length in the problem,
# that substring with the highest length is going to contain the most frequent character.
# This is because if you have the most frequent character in the substring, you can use up to k
# swaps for the other characters to further extend the number of the same frequent character.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res

# s = "ABCBDBBAADC", k = 2, output: 6
# s = "ABCDE", k = 2, output: 3
