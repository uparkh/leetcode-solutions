from typing import Optional
from ListNode import ListNode

# This solution works for non-empty inputs, but I felt like there was an easier way of doing this
# that I was missing/didn't think of. To allow empty inputs, I knew that my algorithm would get
# very bloated. So I jumped to the NeetCode solution.
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = list1, list2
        while curr1:
            while curr2:
                if curr2.val <= curr1.next.val:
                    tmp1 = curr1.next
                    curr1.next = curr2

                    tmp2 = curr2.next
                    curr2.next = tmp1

                    curr1 = curr2
                    curr2 = tmp2
                else:
                    break
            curr1 = curr1.next
        return list1

# They use a dummy node and build out the list from there into a separate output list
# rather than modifying the original list. This helps avoid errors in an empty output [].
# Looking back at it now, this is so incredibly easy! I didn't go through this plan because
# I didn't know how I would deal with the remainder nodes when iterating through both lists
# with the condition |while list1 and list2|, but it's simple! Just iterate through the remaining
# ones.
# Note that this solution only creates ONE extra list node object. It just severs and rearranges
# next pointers to have a final list. This means that list1 and list2 are unusable after this call.
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next # Returns None if both were empty, or proper return list node otherwise


list1 = ListNode()
list1.build_from_list([1,2,4])
list2 = ListNode()
list2.build_from_list([1,3,4])


print(Solution().mergeTwoLists(list1, list2))


