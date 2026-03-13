class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        left,right = 0, n-1
        pair_count = 0
        while left < right:
            pairs_sum = nums[left] + nums[right]
            if pairs_sum < target:
                pair_count += right - left
                left += 1
            else:
                right -= 1
        return pair_count
        

        