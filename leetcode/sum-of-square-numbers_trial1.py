class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        import math
        a = 0
        b = int(math.sqrt(c))
        while a <= b:
            sum = a**2 + b**2
            if sum == c:
                return True
            elif sum < c:
                a += 1
            else:
                b -= 1
        return False
