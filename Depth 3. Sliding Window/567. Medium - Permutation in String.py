# Notes:
# Can check if something is a permutation by checking if they are anagrams.
# So hash map for counts.
# Iterate R until a character in the s1 map is found, then start an anagram comparison hashmap
# for that s2 substring.
# ~40 minute Solution.

# My Original Solution, O(m*n), where n = len(s1), m = len(s2) Because map equality is O(n),
# in the worst case if every character in s2 is in s1, and there is not any permutation of s1 in s2,
# then the equality check is done m times, so solution is O(m*n).
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        map_s1, map_s2 = {}, {}
        for c in s1: map_s1[c] = 1 + map_s1.get(c, 0)
        l = 0
        for r, c in enumerate(s2):
            if c in map_s1:
                if not map_s2:
                    l = r
                if (r - l + 1) > len(s1):
                    if map_s2[s2[l]] == 1: map_s2.pop(s2[l])
                    else: map_s2[s2[l]] -= 1
                    l += 1
                map_s2[c] = 1 + map_s2.get(c, 0)
                if map_s2 == map_s1: return True
            else:
                map_s2.clear()

        return False

# NeetCode Solution. O(m + n) solution where m = s2.length. The idea here is that instead of
# using a variable length hash map, since we are guaranteed that there are lowercase English
# letters in both strings, we can instead make a 26 length array for each string, that counts the
# occurrences of each letter as we process the characters. The benefit here is that we can update
# the number of equal occurrences (matches) between both arrays, as we process the s2 string.
# Instead of linear time hash map comparison with each character in s2, we know that the arrays
# are equal when the matches are equal to 26, the length of each array. Thus we have constant
# time equality testing. The first loop iterates through s1, so O(n), and the third loop
# iterates through s2 once, so O(m), thus the total time is O(m + n)

# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         if len(s1) > len(s2):
#             return False

#         s1Count, s2Count = [0] * 26, [0] * 26
#         for i in range(len(s1)):
#             s1Count[ord(s1[i]) - ord("a")] += 1
#             s2Count[ord(s2[i]) - ord("a")] += 1

#         matches = 0
#         for i in range(26):
#             matches += 1 if s1Count[i] == s2Count[i] else 0

#         l = 0
#         for r in range(len(s1), len(s2)):
#             if matches == 26:
#                 return True

#             index = ord(s2[r]) - ord("a")
#             s2Count[index] += 1
#             if s1Count[index] == s2Count[index]: # Did adding 1 make the two frequencies match?
#                 matches += 1
#             elif s1Count[index] + 1 == s2Count[index]:# Did adding 1 throw off the existing match?
#                 matches -= 1
#                                                   # If they did not match already, then no update.

#             index = ord(s2[l]) - ord("a")
#             s2Count[index] -= 1
#             if s1Count[index] == s2Count[index]: # Did shifting to right (-1) make 2 freqs match?
#                 matches += 1
#             elif s1Count[index] - 1 == s2Count[index]: # Or did it throw off the existing match?
#                 matches -= 1                           # If already did not match, no update.
#             l += 1    # Shift window
#         return matches == 26



# print(Solution().checkInclusion("abc", "eidboacaboo"))
print(Solution().checkInclusion("adc", "dcda"))
print(Solution().checkInclusion("abc", "cccccbabbbaaaa"))
