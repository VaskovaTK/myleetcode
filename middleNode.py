# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: ListNode):
        savedHead = head
        count = 0
        while head.next:
            count +=1
            head = head.next
        count +=1
        middle = (count//2)+1
        newCount = 0
        while savedHead.next:
            newCount+=1
            if newCount == middle:
                return savedHead
            savedHead = savedHead.next
        return savedHead



def createList (newList:list):
    head = None
    savedHead = None
    for i in range(len(newList)):
        if i==0:
            head = ListNode(newList[i])
            savedHead = head
        else:
            head.next = ListNode(newList[i])
            head = head.next
    return savedHead

sol = Solution()
# print(sol.middleNode(createList([1,2,3,4,5])).val)
print(sol.middleNode(createList([1])).val)



