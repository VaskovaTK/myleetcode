class Solution():
    def twoDublicates(self, nums) :
        countDict = {}
        retList = []
        for i in range(len(nums)):
            if nums[i] not in countDict:
                countDict[nums[i]] = [i]
            else:
                countDict[nums[i]].append(i)
        for k in countDict.keys():
            if len(countDict[k]) == 2:
                firstNum = countDict[k][0]
                secondNum = countDict[k][1]
                if secondNum == firstNum+1 or secondNum == firstNum+2 or secondNum == firstNum+3 or secondNum == firstNum-1 or secondNum == firstNum-2 or secondNum == firstNum-3:
                    retList.append(k)
        print(retList)
        return retList

sol = Solution()
sol.twoDublicates([1,2,3,3,4,5]) # должен быть 3
sol.twoDublicates([1,2,3,6,4,1]) # должен быть пустой лист
sol.twoDublicates([1,2,3,6,1,5]) # должен быть пустой лист
sol.twoDublicates([1,2,3,6,4,5]) # должен быть пустой лист
sol.twoDublicates([1,2,3,3,4,4]) # должен быть 3 и 4
sol.twoDublicates([1,2,3,3,3,5]) # должен быть пустой лист


