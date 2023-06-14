class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(t) != len(s):
            return False
        
        hashmap, hashmap2 = {}, {}

        # ORIGINAL SOLUTION
        # for char in s:
        #     if char not in hashmap:
        #         hashmap[char] = 1
        #     else:
        #         hashmap[char] += 1
        
        # for char in t:
        #     if char not in hashmap2:
        #         hashmap2[char] = 1
        #     else:
        #         hashmap2[char] += 1

        # NEETCODE SOLUTION (PYTHONIC WAY)
        for i in range(len(s)):
            hashmap[s[i]] = 1 + hashmap.get(s[i], 0)
            hashmap2[t[i]] = 1 + hashmap2.get(t[i], 0)
        # Remember that .get(key, default) does have the default functionality
        return hashmap == hashmap2


s = Solution()
print(s.isAnagram("anagram", "nagaram"))
