class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ph = 0
        for sk in range(len(nums)):
            if nums[sk] != 0:
                nums[ph],nums[sk] = nums[sk],nums[ph]
                ph += 1
        return nums