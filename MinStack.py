
from collections import deque

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        print(self.stack)

    def pop(self) -> None:
        self.stack = self.stack[1:len(self.stack)]



    def top(self) -> int:
        if len(self.stack):
            maximum = self.stack[0]
        else:
            return -1
        for i in range(len(self.stack)):
            if self.stack[i] > maximum:
                maximum = self.stack[i]
        return maximum

    def getMin(self) -> int:
        if len(self.stack):
            minimum = self.stack[0]
        else:
            return 0
        for i in range(len(self.stack)):
            if self.stack[i] < minimum:
                minimum = self.stack[i]

        return minimum




# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(42)
obj.push(8)
obj.push(7)
obj.push(2)
obj.push(-3)
obj.push(11)
obj.push(12)
obj.pop()
param_3 = obj.top()
print(param_3)
param_4 = obj.getMin()
print(param_4)