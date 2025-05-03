class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        product = 1
        result = 0
        i = 0
        
        for j in range(len(nums)):
            product *= nums[j]
            
            while product >= k and i <= j:
                product //= nums[i]
                i += 1
                
            result += j - i + 1
        
        return result
