class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelsDict = {}
        for i in range (len(jewels)):
            jewelsDict[jewels[i]] = 1
        count = 0
        for i in range (len(stones)):
            if stones[i] in jewelsDict.keys():
                count+=1
        return count
