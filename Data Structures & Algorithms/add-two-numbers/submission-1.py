# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #   [6,5,4]
        #   [4,5,6] 
        #   [1,1,1,0]

        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            #new digit/node
            val = v1 + v2 + carry
            # 6 + 4 = 10, carry -> 1 10 // 10
            carry = val // 10
            #Let's say our node has 8 + 7 = 15, we want one's place i.e, 5
            val = val % 10
            cur.next = ListNode(val)

            # Update pointers
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next