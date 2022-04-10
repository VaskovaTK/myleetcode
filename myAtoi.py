class Solution:
    def myAtoi(self, s: str) -> int:
        min = -2**31
        max = (2**31)-1
        justInt = False
        positive = True
        number = ""
        for i in range(len(s)):
            try:
                if number =="":
                    if i-1>=0:
                        if s[i-1] == "-":
                            positive = False
                            justInt = True
                            if i-2>=0:
                                if s[i-2] =="+":
                                    return 0

                        elif s[i-1] == "+":
                            positive = True
                            justInt = True
                            if i-2>=0:
                                if s[i-2] =="-":
                                    return 0


                numberInt = int (s[i])
                if numberInt:
                    justInt = False
                number+=s[i]
            except:
                if justInt == True:
                    return 0
                if number !="":
                    retNumber = int(number)
                    if positive == False:
                        retNumber = -retNumber
                    if retNumber>=min and retNumber<=max:
                        return retNumber
                    else:
                        if retNumber<min:
                            return min
                        elif retNumber>max:
                            return max

                else:
                    if s[i] ==" " or s[i] == "_" or s[i] == s[i] == "+" or s[i] == "-":
                        continue
                    else:
                        return 0


        if number !="":
            retNumber = int(number)
            if positive == False:
                retNumber = -retNumber
            if retNumber>=min and retNumber<=max:
                return retNumber
            else:
                if retNumber < min:
                    return min
                elif retNumber > max:
                    return max
        return 0


sol = Solution()
print(sol.myAtoi("4193 with words")) #4193
print(sol.myAtoi("-4193 with words")) #-4193
print(sol.myAtoi("__4193 with words")) #4193
print(sol.myAtoi("__-4193 with words")) #-4193
print(sol.myAtoi("42")) #42
print(sol.myAtoi("words and 987")) #0
print(sol.myAtoi("-91283472332")) #-2147483648
print(sol.myAtoi("+-12")) #0
print(sol.myAtoi("-+12")) #0
print(sol.myAtoi("  +  413")) #0
