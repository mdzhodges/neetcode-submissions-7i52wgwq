# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:


        ## need to store as a string, reverse, add, reverse linked list

        l1_str = ""


        curr = l1

        while curr:
            l1_str += str(curr.val)
            curr = curr.next


        l1_reverse = l1_str[::-1]


        l2_str = ""


        curr = l2

        while curr:
            l2_str += str(curr.val)
            curr = curr.next

        l2_reverse = l2_str[::-1]

        sumOf = str(int(l1_reverse) + int(l2_reverse))
        sumOf = sumOf[::-1]


        i = 0

        dummy = ListNode(0)
        curr = dummy
            
        for char in str(sumOf):
            curr.next = ListNode(int(char))
            curr = curr.next
            
        return dummy.next
    




















