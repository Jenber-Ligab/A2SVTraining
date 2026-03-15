class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        count = 0
        res = 0
        even_count = 0
        for right in range(len(nums)):
            if nums[right] % 2 == 1:
                count += 1
                even_count = 0
            while count == k:
                even_count += 1
                if nums[left] % 2 == 1:
                    count -= 1
                left += 1
            res += even_count
        return res

        