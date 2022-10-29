class Solution():
    def repeatedSubstringPattern(self,s:str, t:str):
        indexS = 0
        indexT = 0
        lenghtT = len(t)
        lenghtS = len(s)
        if lenghtT > lenghtS:
            return False
        first = -1
        while indexT < lenghtT and indexS < lenghtS:
            if t[indexT] == s[indexS]:
                if first == -1:
                    first = indexS
                indexT +=1
                indexS+=1
            else:
                first = -1
                indexT = 0
                indexS+=1
        if first == -1 or indexT < lenghtT:
            return False
        return first




sol = Solution()
print(sol.repeatedSubstringPattern("abc","bc"))
print(sol.repeatedSubstringPattern("aaa","aa"))
print(sol.repeatedSubstringPattern(s = "abcdefj", t = "cd" ))
print(sol.repeatedSubstringPattern(s = "abcd", t = "cde"))
print(sol.repeatedSubstringPattern(s = "aaa", t = "aaaa" ))