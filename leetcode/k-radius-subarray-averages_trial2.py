class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if k == 0:
            return nums
        res = [-1]*n
        prefix = [0]*(n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        #print(prefix)
        for i in range(n):
            left = i - k
            right = i + k
            if left >= 0 and right < n:
                total = prefix[right + 1] - prefix[left]
                res[i] = total // (2*k + 1)
        return res
        '''
        window_size = 2*k + 1
        if window_size > n:
            return res
        window_sum = sum(nums[:window_size])
        for i in range(k,n-k):
            res[i] = window_sum // window_size
            if i+k+1 < n:
                window_sum += nums[i+k+1]
                window_sum -= nums[i-k]
        return res'''
        