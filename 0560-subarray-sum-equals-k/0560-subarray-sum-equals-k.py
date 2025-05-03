class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Dictionary to store cumulative sum frequencies
        freq = {0: 1}
        result = 0
        cumsum = 0
        
        for i in range(len(nums)):
            cumsum += nums[i]
            
            # Check if the complement (cumsum - k) exists in the dictionary
            if cumsum - k in freq:
                result += freq[cumsum - k]
            
            # Update the frequency of the current cumulative sum
            freq[cumsum] = freq.get(cumsum, 0) + 1
        
        return result
