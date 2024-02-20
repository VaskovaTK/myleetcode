class Solution:
    def calculate(self, s: str) -> int:
        listOfValues = []
        for index in range(len(s)):
            if s[index] == " ":
                continue
            elif s[index] == "+" or s[index] == "-" or s[index] == "*" or s[index] == "/":
                listOfValues.append(s[index])
            else:
                listOfValues.append(int(s[index]))
        i = 0
        lenght = len(listOfValues)
        while i <lenght:
            if listOfValues[i] == None:
                continue
            elif listOfValues[i] == "*":
                listOfValues[i + 1] = listOfValues[i+1] * listOfValues[i-1]
                listOfValues[i] = None
                listOfValues[i-1] = None
            elif listOfValues[i] == "/":
                listOfValues[i + 1] = listOfValues[i-1] // listOfValues[i+1]
                listOfValues[i] = None
                listOfValues[i-1] = None
        for i in range(len(listOfValues)):
            if listOfValues[i] == None:
                continue
            elif listOfValues[i] == "+":
                listOfValues[i + 1] = listOfValues[i+1] + listOfValues[i-1]
                listOfValues[i] = None
                listOfValues[i-1] = None
            elif listOfValues[i] == "-":
                listOfValues[i + 1] = listOfValues[i-1] - listOfValues[i+1]
                listOfValues[i] = None
                listOfValues[i-1] = None
        lenght = len(listOfValues)
        return listOfValues[lenght-1]


sol = Solution()
print(sol.calculate("3+5/2"))
