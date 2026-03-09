class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        
        total = sum(skill)
        teams = n // 2
        
        if total % teams != 0:
            return -1
        
        target = total // teams
        chemistry = 0
        
        left = 0
        right = n - 1
        
        while left < right:
            if skill[left] + skill[right] != target:
                return -1
            
            chemistry += skill[left] * skill[right]
            left += 1
            right -= 1
        
        return chemistry
        