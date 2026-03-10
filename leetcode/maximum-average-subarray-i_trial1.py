class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum
    
        for i in range(k, len(nums)):
            window_sum += nums[i]      # add next element
            window_sum -= nums[i-k]    # remove left element
            max_sum = max(max_sum, window_sum)
    
        return max_sum / k
        '''window_sum = 0
        max_sum = float(-inf)
        left = 0

        for right in range(len(nums)):
            window_sum += nums[right]

            if right - left + 1 > k :
                window_sum -= nums[left]
                left += 1

            max_sum = max(max_sum, window_sum)

        return max_sum / k'''

        