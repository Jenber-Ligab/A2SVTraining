from collections import defaultdict
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        left = 0
        n = len(nums)
        max_sum = 0
        count = defaultdict(int)
        window_sum = 0
        for right in range(n):
            count[nums[right]] += 1
            window_sum += nums[right]
            if right - left + 1 == k:
                if len(count) == k:
                    max_sum = max(max_sum,window_sum)                
                window_sum -= nums[left]
                count[nums[left]] -= 1 
                if count[nums[left]] == 0:
                    del count[nums[left]]
                left += 1
        return max_sum
        '''
        while k <= n:
            if len(nums[left:k]) == len(set(nums[left:k])):
                max_sum = max(max_sum,sum(nums[left:k]))
            left += 1
            k += 1
                    
        return max_sum
        '''



        