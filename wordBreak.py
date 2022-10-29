class Solution:
    def wordBreak(self, s: str, wordDict: list) -> bool:
        i = -1
        searchFirst = self.searching(s, wordDict)
        if searchFirst:
            return True

        while i<(len(s)):
            i+=1
            searchWord = s[0:i]
            search = self.searching(searchWord, wordDict)
            if search:
                return self.wordBreak(s[len(searchWord):],wordDict)
        if len(s)>0:
            return False
        return True

    def searching (self,searchWord,wordDict):
        for j in range(len(wordDict)):
            if searchWord == wordDict[j]:
                return True
        return False


    #     result = self.recursion(s, wordDict)
    #     if result != True:
    #         result = False
    #     return result
    #
    # def recursion(self,s, wordDict):
    #     ret = True
    #     if len(s)>0:
    #         firstLater = s[0]
    #         for key in range (len(wordDict)):
    #             firstLaterOfKey = wordDict[key][0]
    #             if firstLaterOfKey == firstLater:
    #                 another = self.anotherLatters(s,wordDict[key])
    #                 if another == False:
    #                     break
    #                 else:
    #                     lenghtKey = len(wordDict[key])
    #                     newS = s[lenghtKey:]
    #                     ret = self.recursion(newS,wordDict)
    #     else:
    #         return True
    #
    # def anotherLatters (self, s, key):
    #     for i in range(len(key)):
    #         if s[i] == key[i]:
    #             continue
    #         else:
    #             return False
    #     return True


sol = Solution()
# print(sol.wordBreak( s = "catsandog", wordDict = ["cats","dog","sand","and","cat"])) #false
# print(sol.wordBreak(  s = "leetcode", wordDict = ["leet","code"])) #true
# print(sol.wordBreak(  "cars",["car","ca","rs"])) #true
# print(sol.wordBreak(  "aaaaaaa",["aaaa","aaa"])) #true
print(sol.wordBreak(  "goalspecial",["go","goal","goals","special"])) #true
