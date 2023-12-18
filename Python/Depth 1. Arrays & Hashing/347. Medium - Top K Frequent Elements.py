class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freqMap = {}
        for n in nums:
            freqMap[n] = 1 + freqMap.get(n, 0)
        # counting sort
        intermediate = [[] for i in range(max(freqMap.values()) + 1)]
        for num, freq in freqMap.items():
            intermediate[freq].append(num)
        ret = []
        for elem in reversed(intermediate):
            if len(elem) != 0:
                for i in elem:
                    if len(ret) < k:
                        ret.append(i)
        return ret



s = Solution()
print(s.topKFrequent([1,1,2,2,2,3,4,4], 3))
# print(s.topKFrequent([1,2], 2))
# print(s.topKFrequent([9, 5, 5, 5 , 6, 8, 8, 4, 4], 2))
# print(s.topKFrequent([-1, -1], 1))
