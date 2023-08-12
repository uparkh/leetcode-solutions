from typing import Self
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    @staticmethod
    def build_from_list(nums: list[int]) -> Self | None:
        dummy = ListNode()
        curr = dummy
        # prev = None
        for n in nums:
            curr.next = ListNode(n)
            # curr.next = ListNode()
            # prev = curr
            curr = curr.next
        # prev.next = None
        return dummy.next
    
    def __str__(self):
        res = "["
        curr = self
        while curr is not None:
            res = res + f" {curr.val},"
            curr = curr.next
        res = res.strip(",")
        res = res + " ]"
        return res
