class Solution:
    def isPalindrome(self, x: int) -> bool:
        strX = str(x)
        beginIndex = 0
        endIndex = len(strX)-1
        while beginIndex < endIndex:
            if strX[beginIndex] == strX[endIndex]:
                beginIndex=beginIndex+1
                endIndex = endIndex-1
            else:
                return False
        return True
sol = Solution()
# print(sol.isPalindrome(121))
print(sol.isPalindrome(16221))
