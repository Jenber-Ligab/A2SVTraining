class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 2:
            return n    
        left = 0
        max_value = 1
        for i in range(1,n):
            prev_comp = ((arr[i] > arr[i-1]) - (arr[i] < arr[i-1]))
            if prev_comp == 0:
                left = i
            elif i == n-1 or (prev_comp * ((arr[i+1] > arr[i]) - (arr[i+1] < arr[i]))) != -1:
                max_value = max(max_value, i - left + 1)
                left = i
        return max_value
        '''up = down = 1
        res = 1
        for i in range(1,n):
            if arr[i] > arr[i-1]:
                up = down + 1
                down = 1
            elif arr[i] < arr[i-1]:
                down = up + 1
                up = 1
            else:
                up = down = 1
            res = max(res, up, down)
        return res'''
        