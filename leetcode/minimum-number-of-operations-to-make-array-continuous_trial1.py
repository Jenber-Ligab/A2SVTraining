class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))
        max_op = 0
        left = 0
        for right in range(len(nums)):
            while nums[right] - nums[left] >= n:
                left += 1
            max_op = max(max_op, right - left + 1)
        return n - max_op
        