#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # to rotate a linked list
        # 1. save head
        # 2. use aux to change to the right
        # 3. change head to last aux

        # to define how many rotations: mod with len

        if not head or k == 0:
            return head
        
        # rotate once to get len of list
        next_node = head.next
        value = head.val
        n = 1
        while next_node:
            temp = next_node.val
            next_node.val = value
            value = temp

            next_node = next_node.next
            n += 1
        head.val = value


        for _ in range((k - 1) % n):
            next_node = head.next
            value = head.val
            while next_node:
                temp = next_node.val
                next_node.val = value
                value = temp

                next_node = next_node.next
            head.val = value
        
        return head

# @lc code=end

