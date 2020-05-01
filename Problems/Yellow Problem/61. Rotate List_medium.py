# up: 1019, down: 969
# T: O(n), S: O(1)
# Two pointer (slow, fast)

# calculate the shift number with modular
# run fast pointer until shift
# and run slow, fast together until end
# at that time, slow.next is new head, keep it tmp and slow.next = None (cut link)
# fast.next is linked to previous head (fast.next = head)
# head point move to tmp (head = tmp)
# return head

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # Solution, two pointer
        if not head:
            return None
        if head.next == None:
            return head
        
        cur = head
        count = 1
        while cur.next:
            count += 1
            cur = cur.next
            
        shift = k % count
        
        if k == 0 or shift == 0:
            return head
        
        fast = slow = head
        
        for i in range(shift):
            fast = fast.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        tmp = slow.next
        
        slow.next = None
        fast.next = head
        head = tmp
        
        return head
            
        
        
        
