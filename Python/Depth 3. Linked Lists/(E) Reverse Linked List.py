# head: Optional[ListNode]
# This argument means that var `head` is meant to be a ListNode, but the Optional[] indicates
# that it can be null/None. It's like Java'a @Nullable annotation, just saying the the passed
# object can be null.

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def build_from_list(self, nums: list[int]):
        curr = self
        prev = None
        for n in nums:
            curr.val = n
            curr.next = ListNode()
            prev = curr
            curr = curr.next
        prev.next = None
    
    def __str__(self):
        res = "["
        curr = self
        while curr is not None:
            res = res + f" {curr.val},"
            curr = curr.next
        res = res.strip(",")
        res = res + " ]"
        return res

# My Solution - O(n) time, O(n) memory
# I chose to do it the O(n) memory way, but I remember doing it the O(1) memory way @ Harper DSA
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        resHead = None
        temp = None
        while curr is not None:
            resHead = ListNode(curr.val)
            resHead.next = temp
            temp = resHead
            curr = curr.next

        return resHead

# NeetCode Solution - O(n) time, O(1) memory
# This works by essentially severing the .next arrows to move to the left, instead of the right
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         prev, curr = None, head

#         while curr:
#             temp = curr.next
#             curr.next = prev
#             prev = curr
#             curr = temp
#         return prev



llist = ListNode()
llist.build_from_list([1, 2, 3, 4, 5])
print(llist)

print(Solution().reverseList(llist))
