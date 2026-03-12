from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = Counter(t)
        len_t = len(count_t)
        window = {}
        result_len = float("inf")
        equal_count = 0
        result = ""
        left = 0
        for right,char in enumerate(s):
            if char in count_t:
                window[char] = window.get(char,0) + 1
                if window.get(char,0) == count_t.get(char,0):
                    equal_count += 1

            while equal_count == len_t:
                if (right - left + 1) < result_len:
                    result = s[left:right+1]
                    result_len = right - left + 1
                if s[left] in count_t:
                    window[s[left]] -= 1
                    if window[s[left]] < count_t[s[left]]:
                        equal_count -= 1
                left += 1
        return result
        