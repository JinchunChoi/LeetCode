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
        
        # for counting the number of nodes in linked list
        while cur.next:
            count += 1
            cur = cur.next
           
        # number of shift, not rotate more
        shift = k % count
        
        # no move, return head
        if k == 0 or shift == 0:
            return head
                
        fast = slow = head
        
        # run fast pointer 
        for i in range(shift):
            fast = fast.next
        
        # run both pointer until fast.next == None
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        # keep new start node
        tmp = slow.next
        
        # cut link
        slow.next = None
        
        # connect to head
        fast.next = head
        
        # set a tmp as a head (new start node)
        head = tmp
        
        return head
            
        
        
        
