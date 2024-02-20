# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        array = []
        rem = 0
        while l1 and l2:
            sum = l1.val + l2.val + rem
            if sum >=10:
                rem = 1
                array.append(sum-10)
            else:
                rem = 0
                array.append(sum)
            l1 = l1.next
            l2 = l2.next
        while l1:
            sum = l1.val + rem
            if sum >=10:
                rem = 1
                array.append(sum-10)
            else:
                rem = 0
                array.append(sum)
            l1 = l1.next

        while l2:
            sum = l2.val + rem
            if sum >=10:
                rem = 1
                array.append(sum-10)
            else:
                rem = 0
                array.append(sum)
            l2 = l2.next
        if rem > 0:
            array.append(rem)
            rem = 0
        linkedList = self.createLinkedList(array)
        return linkedList






    def createLinkedList(self,array):
        head = None
        first = None
        for i in range (0, len(array)):
            if head == None:
                head = ListNode(val= array[i])
                first = head
            else:
                head.next = ListNode(val= array[i])
                head = head.next

        return first

# createLinkedList([1,2,3,4])

s = Solution()
# s.addTwoNumbers(s.createLinkedList([2,4,3]),s.createLinkedList([5,6,4]))
s.addTwoNumbers(s.createLinkedList([9,9,9,9,9,9,9]),s.createLinkedList([9,9,9,9]))