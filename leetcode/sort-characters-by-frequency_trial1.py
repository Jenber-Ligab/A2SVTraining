from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        s_count = Counter(s)
        sorted_count = dict(sorted(s_count.items(),key = lambda x : x[1],reverse = True))
        sorted_str = []
        for key,value in sorted_count.items():
            sorted_str.append(key*value)

        return "".join(sorted_str)


        