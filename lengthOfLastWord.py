class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word =""
        newS =""
        if s[-1] ==" ":
            for i in range(-1,-len(s)-1,-1):
                if s[i] == " ":
                    newS = s[:i]
                else:
                    break
        else:
            newS = s
        for i in range(len(newS)):
            if newS[i] == " ":
                word = ""
                continue
            word += newS[i]
        return len(word)

sol = Solution()
print(sol.lengthOfLastWord("Hello World"))
print(sol.lengthOfLastWord("   Hello   "))
print(sol.lengthOfLastWord("   fly me   to   the moon  "))

