class Solution:
    def evalRPN(self, tokens: list) -> int:
        sign = list()
        expression = ["00"]*len(tokens)
        eIndex = 0
        for i in range(len(tokens)):
            if tokens[i] == "+" or tokens[i] == "-":
                if i-1>0:
                    if tokens[i-1] !="+" and tokens[i-1] != "-" and tokens[i-1] != "*" and tokens[i-1]!="/":
                        expression[eIndex-1] = tokens[i]
                        expression[eIndex-2] ="(" + expression[eIndex-2]
                        expression[eIndex] = expression[eIndex]+")"
                    else:
                        sign.append(tokens[i])
                else:
                    sign.append(tokens[i])
            elif tokens[i] == "/" or tokens[i] == "*":
                sign.append(tokens[i])
            else:
                expression[eIndex] = tokens[i]
                eIndex+=2


