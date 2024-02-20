class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        else:
            res = self.rec(n)
            return res


    def rec(self,num):
        if num<4 and num !=1:
            return False
        elif num==1:
            return True
        else:
            return self.rec(num/4)


sol = Solution()
print(sol.isPowerOfFour(16))
print(sol.isPowerOfFour(5))