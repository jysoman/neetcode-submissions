# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = l1
        num1 = ""
        num2 = ""

        while cur:
            num1 = num1+str(cur.val)
            cur = cur.next

        cur = l2
        while cur:
            num2 = num2+str(cur.val)
            cur = cur.next
        
        num1 = num1[::-1]
        num2 = num2[::-1]

        res = str(int(num1)+int(num2))
        res = res[::-1]
        final = ListNode()
        cur = final

        for i in range(len(res)):
            temp = ListNode(val=res[i])
            final.next = temp
            final = final.next
        return cur.next


