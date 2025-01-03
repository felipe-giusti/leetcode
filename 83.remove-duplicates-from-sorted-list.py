#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        cur = head
        while cur.next:
            if cur.val == cur.next.val:
                if cur.next.next:
                    cur.next = cur.next.next
                else:
                    cur.next = None
                    break
            else:
                cur = cur.next
        return head




# @lc code=end

