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

        def rotate(head):
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
            return n

        if not head or k == 0:
            return head
        
        n = rotate(head)

        for _ in range((k - 1) % n):
            rotate(head)
        
        return head

# @lc code=end

