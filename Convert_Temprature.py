class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
         ans = [celsius + 273.15, celsius * 1.80 + 32]
         return ans
if __name__ == '__main__':
    sol = Solution()
    print(sol.convertTemperature(36.50))