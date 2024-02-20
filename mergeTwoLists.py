# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode):
        newList = None
        first = None
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                if newList == None:
                    newList = ListNode(list1.val)
                    first = newList
                    list1 = list1.next
                else:
                    newList.next = ListNode(list1.val)
                    list1 = list1.next
                    newList = newList.next
            else:
                if newList == None:
                    newList = ListNode(list2.val)
                    first = newList
                    list2 = list2.next
                else:
                    newList.next = ListNode(list2.val)
                    list2 = list2.next
                    newList = newList.next

        while list1 is not None:
            if newList == None:
                newList = ListNode(list1.val)
                first = newList
                list1 = list1.next
            else:
                newList.next = ListNode(list1.val)
                list1 = list1.next
                newList = newList.next


        while list2 is not None:
            if newList == None:
                newList = ListNode(list2.val)
                first = newList
                list2 = list2.next
            else:
                newList.next = ListNode(list2.val)
                list2 = list2.next
                newList = newList.next

        return first


    def create(self,array):
        linkedList = None
        first = None
        for i in range(0,len(array)):
            if linkedList == None:
                linkedList = ListNode(array[i])
                first = linkedList
            else:
                linkedList.next = ListNode(array[i])
                linkedList = linkedList.next
        return  first

sol = Solution()
print(sol.mergeTwoLists(sol.create([1,2,4]), sol.create([1,3,4])).val)
