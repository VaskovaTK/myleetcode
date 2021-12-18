class Solution:
    def letterCombinations(self, digits: str) -> list:
        lenghtDigits = len(digits)
        if lenghtDigits <1:
            return []
        elif lenghtDigits == 1:
            firstList = self.verification(digits[0])
            retList = self.recursion([],firstList,0)
        elif lenghtDigits == 2:
            firstList = self.verification(digits[0])
            secondList = self.verification(digits[1])
            retList = self.recursion([],firstList, 0,secondList,0)
        elif lenghtDigits == 3:
            firstList = self.verification(digits[0])
            secondList = self.verification(digits[1])
            thirdList = self.verification(digits[2])
            retList = self.recursion([],firstList, 0,secondList,0, thirdList,0)
        else:
            firstList = self.verification(digits[0])
            secondList = self.verification(digits[1])
            thirdList = self.verification(digits[2])
            fourthList = self.verification(digits[3])
            retList = self.recursion([], firstList, 0, secondList, 0, thirdList, 0,fourthList,0)
        print(retList)
        return retList





    def recursion(self,retList:list, l1 = "", indexL1 = 0, l2 = "", indexL2 =0, l3 = "", indexL3 = 0, l4 = "", indexL4 =0):
        if l2 == "":
            retString = l1[indexL1]
            retList.append(retString)
            if indexL1+1<=len(l1)-1:
                self.recursion(retList,l1,indexL1+1)
            else:
                return retList
        elif l3 == "":
            retString = l1[indexL1]+l2[indexL2]
            retList.append(retString)
            if indexL2+1<=len(l2)-1:
                self.recursion(retList,l1,indexL1,l2,indexL2+1)
            else:
                if indexL1 + 1 <= len(l1) - 1:
                    self.recursion(retList, l1, indexL1 + 1,l2,0)
                else:
                    return retList
        elif l4 =="":
            retString = l1[indexL1] + l2[indexL2]+ l3[indexL3]
            retList.append(retString)
            if indexL3 + 1 <= len(l3) - 1:
                self.recursion(retList, l1, indexL1, l2, indexL2, l3,indexL3+1)
            else:
                if indexL2 + 1 <= len(l2) - 1:
                    self.recursion(retList, l1,indexL1, l2,indexL2+1,l3,0)
                else:
                    if indexL1 + 1 <= len(l1) - 1:
                        self.recursion(retList, l1, indexL1 + 1, l2, 0, l3,0)
                    else:
                        return retList
        else:
            retString = l1[indexL1] + l2[indexL2] + l3[indexL3] + l4[indexL4]
            retList.append(retString)
            if indexL4 + 1 <= len(l4) - 1:
                self.recursion(retList, l1, indexL1, l2, indexL2, l3, indexL3, l4, indexL4+1)
            else:
                if indexL3 + 1 <= len(l3) - 1:
                    self.recursion(retList, l1, indexL1, l2, indexL2, l3, indexL3+1,l4,0)
                else:
                    if indexL2 + 1 <= len(l2) - 1:
                        self.recursion(retList, l1, indexL1, l2, indexL2+1, l3, 0,l4,0)
                    else:
                        if indexL1 + 1 <= len(l1) - 1:
                            self.recursion(retList, l1, indexL1 + 1, l2, 0, l3, 0,l4,0)
                        else:
                            return retList
        return retList




    def verification(self, verNum: str):
        list2 = "abc"
        list3 = "def"
        list4 = "ghi"
        list5 = "jkl"
        list6 = "mno"
        list7 = "pqrs"
        list8 = "tuv"
        list9 = "wxyz"
        if verNum == "1" or verNum == "0":
            return None
        elif verNum == "2":
            return list2
        elif verNum == "3":
            return list3
        elif verNum == "4":
            return list4
        elif verNum == "5":
            return list5
        elif verNum == "6":
            return list6
        elif verNum == "7":
            return list7
        elif verNum == "8":
            return list8
        elif verNum == "9":
            return list9
        else:
            return None

sol = Solution()
# sol.letterCombinations("23")
sol.letterCombinations("5234")



