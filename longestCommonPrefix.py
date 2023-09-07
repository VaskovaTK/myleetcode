class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        if strs[0] == "":
            return ""
        prefix =""
        indexPrefix = 0
        index = 0
        indexLast = len(strs)-1
        while index < len(strs):
            if indexPrefix< len(strs[0]):
                letterOfFirstWord = strs[0][indexPrefix]
            else:
                return prefix
            if len(strs[index])> indexPrefix:
                if strs[index][indexPrefix] == letterOfFirstWord:
                    if index == indexLast:
                        prefix += letterOfFirstWord
                        indexPrefix+=1
                        index =0
                    index+=1
                else:
                    return prefix
            else:
                return prefix
        return prefix



sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))
print(sol.longestCommonPrefix(["dog","racecar","car"]))
print(sol.longestCommonPrefix(["a"]))
print(sol.longestCommonPrefix(["ab", "a"]))
print(sol.longestCommonPrefix(["flower","flower","flower","flower"]))