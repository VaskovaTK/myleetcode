from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        # finDict = {}
        # finDict[")"] = 0
        # finDict["]"] = 0
        # finDict["}"] = 0
        bracketsQueue = deque()

        for i in range(0, len(s)):
            if s[i] == "(":
                bracketsQueue.appendleft(")")
            elif s[i] == "[":
                bracketsQueue.appendleft("]")
            elif s[i] == "{":
                bracketsQueue.appendleft("}")
            elif s[i] == ")":
                if len(bracketsQueue)>0:
                    bracket =  bracketsQueue.popleft()
                    if bracket != ")":
                        return False
                else:
                    return False
            elif s[i] == "]":
                if len(bracketsQueue)>0:
                    bracket =  bracketsQueue.popleft()
                    if bracket != "]":
                        return False
                else:
                    return False
            elif s[i] == "}":
                if len(bracketsQueue) > 0:
                    bracket =  bracketsQueue.popleft()
                    if bracket != "}":
                        return False
                else:
                    return False
        if len(bracketsQueue)> 0:
            return False
        else:
            return True


sol = Solution()
print(sol.isValid(s = "()[]{}"))
print(sol.isValid(s = "(]"))
print(sol.isValid(s ="([)]")) #false
