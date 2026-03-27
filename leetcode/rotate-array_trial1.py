class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse_nums(l,r):
            while l < r:
                nums[l],nums[r] = nums[r],nums[l]
                l += 1
                r -= 1
        l = 0
        r = len(nums) - 1
        k = k % len(nums)
        reverse_nums(l,r)
        reverse_nums(0, k-1)
        reverse_nums(k,len(nums)-1)
        
        