class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        
        # Calculate the prefix sum and suffix sum arrays
        prefix_sum = [0] * n
        suffix_sum = [0] * n
        prefix_sum[0] = nums[0]
        suffix_sum[n - 1] = nums[n - 1]
        
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]
            suffix_sum[n - i - 1] = suffix_sum[n - i] + nums[n - i - 1]
        
        # Calculate the result array using the prefix and suffix sums
        result = [0] * n
        for i in range(n):
            left_sum = i * nums[i] - prefix_sum[i]
            right_sum = suffix_sum[i] - (n - i - 1) * nums[i]
            result[i] = left_sum + right_sum
        
        return result

