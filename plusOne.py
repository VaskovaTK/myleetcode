class Solution:
    def plusOne(self, digits: list) -> list:
        last = digits[-1] +1
        if last<=9:
            addToBefore = 0
            digits[-1] = last
        else:
            digits[-1] = last%10
            addToBefore = 1
        i = -2

        while addToBefore>0 and i > -len(digits)-1:
            digits[i] = digits[i] + addToBefore
            if digits[i] >9:
                addToBefore = digits[i] // 10
                digits[i] = digits[i] % 10
            else:
                addToBefore = 0
            i -=1
        if addToBefore >0:
            digits.insert(0,addToBefore)
        return digits
sol = Solution()
# print(sol.plusOne([1,2,3]))
# print(sol.plusOne([9]))
# print(sol.plusOne([9,9,9]))
print(sol.plusOne([5,8,7,8,8]))


