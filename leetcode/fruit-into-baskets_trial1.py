from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_fruit = 0
        pick = defaultdict(int)
        l = 0
        for r,v in enumerate(fruits):
            pick[v] += 1
            while len(pick) > 2:
                pick[fruits[l]] -= 1
                if pick[fruits[l]] == 0:
                    del pick[fruits[l]]
                l += 1
            max_fruit = max(max_fruit, r - l + 1)
        return max_fruit


            

        