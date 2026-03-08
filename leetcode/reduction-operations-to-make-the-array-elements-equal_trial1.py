class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        operation = 0
        n = len(nums)
        for i in range(1,n):
            if nums[i] != nums[i-1]:
                operation += n - i
        return operation
        