class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start = 0
        end = len(s) -1 
        for i in range(len(s)):            
            if start > end:
                break
            s[start],s[end] = s[end],s[start]
            end -= 1
            start += 1
        return s
        