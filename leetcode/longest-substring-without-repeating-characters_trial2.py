class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store = {}
        left = 0
        max_len = 0

        for right, char in enumerate(s):

            if char in store and store[char] >= left:
                left = store[char] + 1

            store[char] = right
            max_len = max(max_len, right - left + 1)
        return max_len

        