class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        first = 0
        last = n - 1
        cur_sum = 0
        while numbers[first] + numbers[last] != target:
            cur_sum = numbers[first] + numbers[last]
            if cur_sum < target:
                first += 1
            else:
                last -= 1
        return [first+1, last+1]
        