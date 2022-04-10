class Solution:
    def countAndSay(self, n: int) -> str:
        saidString = "1"
        while n>1:
            n-=1
            saidString = self.say(saidString)
        return saidString

    def say(self, string):
        count = 0
        retString =""
        nowNum = ""
        for i in range(len(string)):
            if i == 0:
                nowNum = string[i]
                count +=1
            else:
                if string[i] == nowNum:
                    count+=1
                else:
                    retString+=str(count)
                    retString+=string[i-1]
                    nowNum = string[i]
                    count = 1
        retString += str(count)
        retString += string[-1]
        return retString

def test (ourInput, waitResult):
    sol = Solution()
    output = sol.countAndSay(ourInput)
    print('input was {}, output was {}, expected {}, result = {}'.format(ourInput,output,waitResult, output== waitResult))

test(4,"1211")
test(1,"1")