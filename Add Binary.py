class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum = int(a, 2) + int(b, 2)
        sum = bin(sum)
        return sum[2:]



sol = Solution()
print(sol.addBinary(a = "1010", b = "1011"))


