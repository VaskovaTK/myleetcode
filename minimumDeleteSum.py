class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dict1 = {}
        dict2 = {}
        lastDict = {}
        delDict = {}
        for i in range (0,len(s1)):
            if s1[i] not in dict1:
                dict1[s1[i]] = 1
            else:
                dict1[s1[i]] +=1


        for i in range (0,len(s2)):
            if s2[i] not in dict2:
                dict2[s2[i]] = 1
            else:
                dict2[s2[i]] +=1

        for k in dict1.keys():
            if k in dict2.keys():
                val2 = dict2[k]
                val1 = dict1[k]
                # maximum = max(val1,val2)
                remainder = 0
                if val1 > val2:
                    remainder =  val1-val2
                elif val1 < val2:
                    remainder = val2-val1
                if remainder>0:
                    delDict[k] = remainder

            else:
               delDict[k] = dict1[k]

        for k in dict2.keys():
            if k not in dict1.keys():
                delDict[k] = dict2[k]

        print(delDict)




sol = Solution()
sol.minimumDeleteSum(s1 = "sea", s2 = "eat")
sol.minimumDeleteSum(s1 = "delete", s2 = "leet")
