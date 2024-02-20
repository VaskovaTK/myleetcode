# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head):
        firstHead = head
        before = None
        while head is not None:
            if before != None:
                if head.val != before.val:
                    before.next = head
                    before = head
            else:
                before = head
            if head.next == None:
                if head.val == before.val:
                    before.next = None
            head= head.next



        return firstHead







    def createList(self,arr):
        head = None
        firstHead = None
        for i in range(len(arr)):
            if head == None:
                head = ListNode(arr[i])
                if firstHead== None:
                    firstHead = head
            else:
                head.next = ListNode(arr[i])
                head = head.next
        return firstHead


sol = Solution()
sol.deleteDuplicates(sol.createList([1,1,2,3,3]))