class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        i = count = 0
        j = n - 1
        while i < j:
            s = nums[i] + nums[j]
            if s == k:                
                count += 1
                i += 1
                j -= 1
            elif s < k:
                i += 1
            else:
                j -= 1
        return count
        