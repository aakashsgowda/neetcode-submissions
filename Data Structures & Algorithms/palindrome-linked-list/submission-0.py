# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Storing the val of the LINKED-LIST INTO an ARRAY
        # Space Complexity O(n)
        arr = []
        cur = head
        
        while cur:
            arr.append(cur.val)
            cur = cur.next
        
        l, r = 0, len(arr) - 1
        while l < r:
            if arr[l] != arr[r]:
                return False
            l = l + 1
            r = r - 1
        
        return True


        