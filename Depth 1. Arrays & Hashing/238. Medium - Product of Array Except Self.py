class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prod = 1
        ret = []
        for n in nums:
            ret.append(prod) # maybe? can save computation time/memory copying by declaring array size ahead of time
            prod *= n
        prod = 1
        for i in range(len(ret)-1, -1, -1):
            ret[i] *= prod
            prod *= nums[i]
        return ret

        
