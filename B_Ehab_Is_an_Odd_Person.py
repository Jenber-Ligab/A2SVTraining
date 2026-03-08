class Solution:
   
   def is_odd(self, n: int) -> bool:
       return n % 2 == 1
   
   def lexicographically(self, nums: list) -> list:
        has_odd = False
        has_even = False

        for num in nums:
            if self.is_odd(num):
                has_odd = True
            else:
                has_even = True

        if has_odd and has_even:
            nums.sort()

        return nums
if __name__ == "__main__":
   n = int(input())
   nums = list(map(int,input().split()))
   sol = Solution()
   result = sol.lexicographically(nums)
   print(*result)
