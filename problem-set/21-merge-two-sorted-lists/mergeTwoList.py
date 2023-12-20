# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        node = ListNode(0)
        head = node

        while (list1 != None and list2 != None):
            newNode = None

            if (list1.val <= list2.val):
                newNode = ListNode(list1.val)
                list1 = list1.next
            else:
                newNode = ListNode(list2.val)
                list2 = list2.next
            
            node.next = newNode
            node = node.next

        if (list1 != None):
            node.next = list1
        elif (list2 != None):
            node.next = list2

        return head.next