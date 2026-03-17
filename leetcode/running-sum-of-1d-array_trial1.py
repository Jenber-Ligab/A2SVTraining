class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = 1
        while left < n:
            nums[left] = nums[left] + nums[left - 1]
            left += 1
        return nums