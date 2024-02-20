class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        beginIndex = 0
        endIndex = -1
        while beginIndex< len(s) and endIndex >= -len(s):
            ordBegin = ord(s[beginIndex])
            ordEnd = ord(s[endIndex])
            if ordBegin >122 or ordBegin <97:
                beginIndex+=1
                if ordBegin>=48 and ordBegin <=57:
                    return False
                continue
            if ordEnd > 122 or ordEnd < 97:
                endIndex -=1
                if ordEnd>=48 and ordEnd <=57:
                    return False
                continue
            if s[beginIndex] == s[endIndex]:
                beginIndex+=1
                endIndex-=1
            else:
                return False
        return True


sol = Solution()
sol.isPalindrome(s = "A man, a plan, a canal: Panama")
sol.isPalindrome(s = "race a car")
sol.isPalindrome(s = " ")
sol.isPalindrome("0P")