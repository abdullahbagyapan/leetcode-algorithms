# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode(0)

        tail = head
        carry = 0


        while (l1 != None or l2 != None or carry != 0):


            if (l1 == None):
                value1 = 0
            else:
                value1 = l1.val
                l1 = l1.next

            if (l2 == None):
                value2 = 0
            else:
                value2 = l2.val
                l2 = l2.next

            sum = value1 + value2 + carry

            carry = sum // 10
            value = sum % 10

            node = ListNode(value)


            tail.next = node
            tail = tail.next

        return head.next