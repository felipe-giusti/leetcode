#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l_out = ListNode()
        curr_node = l_out
        carry = 0
        
        def sum_step(l1, l2, carry):
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            v_sum = v1+ v2 + carry
            return v_sum%10, v_sum//10
        
        while True:
            curr_node.val, carry = sum_step(l1, l2, carry)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            if l1 or l2 or carry:
                curr_node.next = ListNode() 
                curr_node = curr_node.next
            else: break
            
        return l_out

# @lc code=end

