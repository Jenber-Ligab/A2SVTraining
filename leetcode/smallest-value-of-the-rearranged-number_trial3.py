class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        if num > 0:
            num = list(str(num))
            num.sort()
            if num[0] == '0':
                for i in range(1,len(num)):
                    if num[i] != '0':
                        num[0],num[i] = num[i],num[0]
                        break
            return int("".join(num))
        else:
            num = list(str(abs(num)))
            num.sort(reverse = True)
            return -int("".join(num))


        