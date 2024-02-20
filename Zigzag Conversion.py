class Solution:
    def convert(self, s: str, numRows: int) -> str:
        mainCol = True
        dictionary = dict()
        if numRows ==1:
            return s
        for i in range (1, numRows+1):
            dictionary[i] = ""
       # print(dictionary)
        lenght = len(s)
        countRows = 1
        index = 0
        lastRow = numRows
        while index < lenght:
            if mainCol:
                dictionary[countRows] +=s[index]
                index += 1
                countRows+=1
                if countRows>numRows:
                    mainCol = False
                    countRows = lastRow
            else:
                if countRows == lastRow:
                    countRows-=1
                    # dictionary[countRows] += " "
                    continue
                elif countRows == 1:
                    mainCol = True
                    countRows = 1
                else:
                    dictionary[countRows] += s[index]
                    index+=1
                    countRows-=1
        retStr = ""
        for i in range (1, numRows+1):
            retStr+=dictionary[i]
        #print(retStr)
        return retStr












sol = Solution()
#sol.convert(s = "PAYPALISHIRING", numRows = 3)
sol.convert("AB", 1)
