from typing import Optional
from ListNode import ListNode

# My original solution, O(n) time, and O(n) memory
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        
        r_head = None
        list_size = 0
        curr = head
        r_curr = None

        # Create a new reversed list
        while curr:
            r_head = ListNode()
            r_head.val = curr.val
            r_head.next = r_curr
            r_curr = r_head

            list_size += 1
            curr = curr.next

        curr = head
        r_curr = r_head
        prev = None
        for i in range((list_size//2)):
            tmp = curr.next
            r_tmp = r_curr.next

            curr.next = r_curr
            r_curr.next = tmp

            prev = r_curr
            curr = tmp
            r_curr = r_tmp

        if list_size % 2 == 0:
            prev.next = None
        else:
            curr.next = None


# NeetCode solution, O(n) time, O(1) memory
# This is SO smart. Like me, he also had to find the middle of the list. While I did it with
# creating a reversed list and tracking list size, he does it in a much smarter way. He advances
# two pointers, the |slow| pointer moves at a step of 1 at a time, while the |fast| pointer moves
# at a step of 2 at a time. Thus, since they occur simultaneously, when |fast| reaches the end,
# |slow| is at exactly half of the list.

# Note that even though |fast| may stop before the end of the list, it doesn't matter, because
# we only needed it to find the midpoint of the list to set |slow| to. After finding the midpoint,
# processing is only done with the |slow| pointer.

# At that point, the second half of the list can be severed, reversed, and processed via merging.
# This is so unbelievably genius I don't think I would have figured it out without seeing it.
class NeetCodeSolution:
    def reorderList(self, head: ListNode) -> None:
        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge two halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

new_list = ListNode()
new_list.build_from_list([1, 2, 3, 4, 5])
print(new_list)

Solution().reorderList(new_list)

print(new_list)
