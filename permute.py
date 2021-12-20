class Solution:
    def permute(self, nums: list) -> list:
        retList = self.recursion([],nums,0)
        return retList

    def recursion (self,retList:list,startNums,changeIndex):
        for i in range(len(startNums)):
            startNums[i],startNums[changeIndex] = startNums[changeIndex], startNums[i]
            if startNums not in retList:
                new = list(startNums)
                retList.append(new)
                self.recursion(retList, startNums, changeIndex)
        if changeIndex+1<=len(startNums)-1:
            self.recursion(retList, startNums,changeIndex+1)
        else:
            return retList
        return retList


sol = Solution()
sol.permute([1,2,3])
sol.permute([0,1])
sol.permute([1])
sol.permute([1,2,3,4])