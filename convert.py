class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <numRows or numRows ==1:
            return s
        lenghtS = len(s)
        columns = (lenghtS//numRows)+1
        if numRows != 2:
            # between = numRows//2
            between = numRows-2
        else:
            between = 0

        fullBetween = (columns-1)*between
        newArr = []
        numCol = columns+ fullBetween
        for i in range(numRows):
            inner = []
            for j in range(numCol):
                inner.append(None)
            newArr.append(inner)
        lastIndexRow = numRows
        lastIndexBetween = between
        indexI = 0
        indexJ = 0
        indexS = 0
        indexB = lastIndexRow-1
        betweenIndex =0
        while indexS < lenghtS:
            if indexI < lastIndexRow:
                newArr[indexI][indexJ] = s[indexS]
                indexS+=1
                indexI+=1
                betweenIndex =0
            elif betweenIndex < lastIndexBetween:
                indexJ += 1
                betweenIndex+=1
                indexB-=1
                newArr[indexB][indexJ] = s[indexS]

                indexS+=1
            else:
                indexI = 0
                indexJ +=1
                indexB = lastIndexRow-1
                continue
        retS = ""
        for i in range(numRows):
            for j in range(numCol):
                if newArr[i][j] != None:
                    retS+=newArr[i][j]

        # print(retS)
        return retS







sol = Solution()
sol.convert(s = "PAYPALISHIRING", numRows = 4) #"PINALSIGYAHRPI"
sol.convert(s = "A", numRows = 2)
sol.convert(s ="AB",numRows =3)
sol.convert(s ="ABC", numRows =2)
sol.convert(s = "PAYPALISHIRING", numRows = 3) #"PAHNAPLSIIGYIR"
sol.convert(s ="ABCD",numRows=2) #ACBD
sol.convert(s ="PAYPALISHIRING",numRows = 5) #"PHASIYIRPLIGAN"
