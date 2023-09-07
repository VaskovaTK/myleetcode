class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 7 or n == 9:
            return False
        if n == 8:
            return True
        if n<0:
            return False
        if n % 7 == 0 or n%9 ==0 or n%8==0:
            return False
        else:
            return True
# дорешать

sol = Solution()
print(sol.isUgly(6))
print(sol.isUgly(1))
print(sol.isUgly(-2147483648))