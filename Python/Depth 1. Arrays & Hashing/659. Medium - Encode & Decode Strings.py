class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        res = ""
        for s in strs: res += s + "/:"
        return res


    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        res = []
        hold = ""
        startIndex, endIndex = 0, len(str)
        for i, c in enumerate(str):
            if hold and c != ":":
                hold = ""
            if c == "/" or ":":
                hold += c
            if hold == "/:":
                endIndex = i - 1
                hold = ""
                res.append(str[startIndex:endIndex])
                startIndex = i+1
                endIndex = len(str)
        return res

s = Solution()
print(s.decode(s.encode([])))

            
# Neetcode Solution is clever because it encodes the length of the string/token in the
# encoded string, allows for faster decoding via specific substrings.
# Instead of O(n*m) time, where n is number of strings, and m is average length of a string,
# this solution is in O(n) time, because each string's content is not checked.
# class Solution:
#     """
#     @param: strs: a list of strings
#     @return: encodes a list of strings to a single string.
#     """

#     def encode(self, strs):
#         res = ""
#         for s in strs:
#             res += str(len(s)) + "#" + s
#         return res

#     """
#     @param: s: A string
#     @return: decodes a single string to a list of strings
#     """

#     def decode(self, s):
#         res, i = [], 0

#         while i < len(s):
#             j = i
#             while s[j] != "#":
#                 j += 1
#             length = int(s[i:j])
#             res.append(s[j + 1 : j + 1 + length])
#             i = j + 1 + length
#         return res
