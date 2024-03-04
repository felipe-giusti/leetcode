#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # window [parent, node, _, _] n = 3

        q = deque([head])
        # sliding window, with n+1 
        for _ in range(n):
            if q[-1].next is None:
                # node is first element, no parent
                if n == len(q):
                    return head.next
                # n > linked list size
                return
            q.append(q[-1].next)
        
        while q[-1].next:
            q.popleft()
            q.append(q[-1].next)

        #parent of n th node
        parent = q.popleft()
        try:
            parent.next = q[1]
        except IndexError:
            parent.next = None
        return head      

# @lc code=end

