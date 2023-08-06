from typing import Optional
from ListNode import ListNode

# TOTAL TIME: 23 m, 31 s

# My solution, one pass, O(n), pretty straightforward. I used the dummy node technique to account
# for resultant lists that are empty (head = None).
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        # Advance |front| ptr 
        front = head
        for _ in range(n):
            front = front.next

        # Initialize lagging ptr
        back = dummy
        while front:
            front = front.next
            back = back.next
        
        # |back| ptr is at the node right before intended deletion node
        if back.next:
            tmp = back.next.next
            back.next = tmp

        return dummy.next


# Neetcode Solution - One Pass, O(n)
# Pretty much the exact same solution as mine. He decided to iterate n downwards to count
# n nodes for the |right| node instead of a range like I did. It doesn't save any memory,
# but does put it in top 9% time-wise.

# Also, I just realized that list size guaranteed to be >= 1, so my condition check is not needed.
# That, but also I can just do the node deletion in one line as he coded.

# So really all I missed was just 2 small micro-optimizations. Other than that I aced this
# in 22 minutes.

# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         dummy = ListNode(0, head)
#         left = dummy
#         right = head

#         while n > 0:
#             right = right.next
#             n -= 1

#         while right:
#             left = left.next
#             right = right.next

#         # delete
#         left.next = left.next.next
#         return dummy.next

newHead = ListNode()
# newHead.build_from_list([i for i in range(1, 5 + 1)])
newHead.build_from_list([1, 2])
print(Solution().removeNthFromEnd(newHead, 1))
