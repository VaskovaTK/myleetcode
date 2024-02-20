class Solution:
    def largestNumber(self, nums: list) -> str:
        dictOfNumbers = {}
        dictOfNumbers["0"] = []
        dictOfNumbers["1"] = []
        dictOfNumbers["2"] = []
        dictOfNumbers["3"] = []
        dictOfNumbers["4"] = []
        dictOfNumbers["5"] = []
        dictOfNumbers["6"] = []
        dictOfNumbers["7"] = []
        dictOfNumbers["8"] = []
        dictOfNumbers["9"] = []
        newListOfResults = []
        for i in range(len(nums)):
            nowStrNum = str(nums[i])
            firstSumbol = nowStrNum[0]
            dictOfNumbers[firstSumbol].append(nowStrNum)
        listOfKeys = ["9","8","7","6","5","4","3","2","1","0"]
        listOfResults = []
        for key in range(0,10):
            listFromDict = dictOfNumbers[listOfKeys[key]]
            if len(listFromDict)>0 and len(listOfResults) == 0:
                listOfResults = listFromDict
            elif len(listFromDict) >0:
                for i in range (len(listOfResults)):
                    newListOfResults = []
                    for j in range(len(listFromDict)):
                        newListOfResults.append((listOfResults[i] + listFromDict[j]))
                else:
                    listOfResults = newListOfResults
        print(max(listOfResults))
        return max(listOfResults)

sol = Solution()
#sol.largestNumber(nums = [10,2])
sol.largestNumber(nums = [3,30,34,5,9])








