class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLenght = 0
        maxPalindrome = ""
        if len(s) == 1:
            return s
        for i in range(len(s)):
            for j in range(i,len(s)):
                newString = s[i:j+1]
                palindromeLenght = self.searchPalindrome(newString)
                if palindromeLenght>maxLenght:
                    maxLenght = palindromeLenght
                    maxPalindrome = newString
        return maxPalindrome


    def searchPalindrome (self, string):
        startIndex = 0
        finishIndex = len(string)-1
        while startIndex < finishIndex:
            if string[startIndex] == string[finishIndex]:
                startIndex+=1
                finishIndex-=1
            else:
                return 0
        return len(string)

sol = Solution()
print(sol.longestPalindrome("babad"))
print(sol.longestPalindrome("cbbd"))
print(sol.longestPalindrome("a"))
print(sol.longestPalindrome("aa"))

