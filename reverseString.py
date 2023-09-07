class Solution:
    def reverseString(self, s: list) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        begin = 0
        end = len(s) - 1
        while begin < end:
            beginSaved = s[begin]
            s[begin] = s[end]
            s[end] = beginSaved
            end -=1
            begin+=1
        print(s)


sol = Solution()
sol.reverseString(["h","e","l","l","o"])
