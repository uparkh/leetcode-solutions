# Original solution (could not figure out how to code it, had
# # the concept of mapping count -> list of strs right though)
# class Solution(object):
#     def groupAnagrams(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: List[List[str]]
#         """
#         counts, anagramGrouping = [], [[]]
#         countCurrent = {}
#         for str in enumerate(strs):
#             countCurrent.clear()
#             for i in range(len(str)):
#                 countCurrent[str[i]] = 1 + countCurrent.get(str[i], 0)
#             if countCurrent not in counts:
#                 counts.append(countCurrent)
#                 anagramGrouping.append([str])
#             else:
#                 anagramGrouping[counts.index(countCurrent)].append(str)
                
#         return anagramGrouping

from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = defaultdict(list) # map charCount to list of anagrams
        # defaultdict forces all values to be list types by default
        for str in strs:
            count = [0] * 26 # a ... z

            for char in str:
                count[ord(char) - ord("a")] += 1 # ascii/unicode comparison
            
            res[tuple(count)].append(str) # mutable objects (array) cannot be hashed, use tuple
            # instead (tuple is immutable)
        return list(res.values())


s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

