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
