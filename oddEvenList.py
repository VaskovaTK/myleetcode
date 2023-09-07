# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        count = 0
        oddHead = None
        evenHead = None
        evenStartHead = None
        oddStartHead = None
        while head !=None:
            count+=1
            if count%2 != 0:
                if oddHead == None:
                    oddHead = head
                    oddStartHead = head
                else:
                    oddHead.next = head
                    oddHead = oddHead.next
            else:
                if evenHead == None:
                    evenHead = head
                    evenStartHead = head
                else:
                    evenHead.next = head
                    evenHead = evenHead.next
            head = head.next
        if evenHead !=None:
            evenHead.next = None
            oddHead.next = evenStartHead
        return oddStartHead






def createList(newList: list):
    head = None
    savedHead = None
    for i in range(len(newList)):
        if i == 0:
            head = ListNode(newList[i])
            savedHead = head
        else:
            head.next = ListNode(newList[i])
            head = head.next
    return savedHead


sol = Solution()
print(sol.oddEvenList(createList([1,2,3,4,5])).val)