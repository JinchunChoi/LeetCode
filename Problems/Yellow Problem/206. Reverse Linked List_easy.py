# up: 3952 down: 84

# T: O(n), S: O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Solution
        
        # We need to keep prev and nextTmp for reverse linked list        
        prev = None
        curr = head
        nextTmp = None
        
        while curr:
            nextTmp = curr.next # save current next 
            curr.next = prev # reverse it
            prev = curr # keep moving for next node, save curr to prev
            curr = nextTmp # pop up saved current next to curr
        
        # End of iteration, return prev 
        return prev
