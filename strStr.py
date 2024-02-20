class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        listOfStartIndex = []
        firstLetter= needle[0]
        lastHaystack = len(haystack)-1
        lastNeedle = len(needle) - 1
        for i in range(len(haystack)):
            if haystack[i] == firstLetter:
                listOfStartIndex.append(i)
        for l in range (len(listOfStartIndex)):
            retSolution = self.returned(haystack, needle,lastNeedle,lastHaystack,listOfStartIndex[l])
            if retSolution >= 0:
                return retSolution
        return -1


    def returned (self, haystack, neddle, lastNeedle, lastHaystack,startIndex):
        indexNeedle =0
        for i in range (startIndex,lastHaystack+1):
            if haystack[i] == neddle[indexNeedle]:
                indexNeedle +=1
                if indexNeedle>lastNeedle:
                    return startIndex
            else:
                return -1
        return -1



sol = Solution()
print(sol.strStr(haystack = "sadbutsad", needle = "sad"))
print(sol.strStr("leetcode", needle = "leeto"))
print(sol.strStr("mississippi","issip"))