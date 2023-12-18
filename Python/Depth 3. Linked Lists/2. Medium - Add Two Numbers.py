from ListNode import ListNode
# TOTAL TIME: 59m, 49s
# ~37 minutes first attempt
# ~22 minutes second attempt

# This was my first attempt. I scrapped it because it felt too clunky halfway through coding it.
# I realized I was making spaghetti code just to account for edge cases (ESPECIALLY once I started
# to track |prev| pointers). I knew I wasn't thinking optimal solution, because the code didn't
# feel natural to write. That, and I saw that carry/addend processing was duplicated, and quite
# often duplicate-ish code implies there must be a better, or more elegant solution.

# So after about 37 mins of trying to make this clunky solution work, 
# class Solution:
#     def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
#         carry = 0
#         curr_l1, curr_l2 = l1, l2
#         while curr_l1 and curr_l2:
#             curr_l1.val += curr_l2.val + carry
#             carry = curr_l1.val // 10
#             curr_l1.val %= 10
#             curr_l2.val = curr_l1.val

#             curr_l1 = curr_l1.next
#             curr_l2 = curr_l2.next

#         res = l1 if curr_l1 else l2
#         curr_remaining = curr_l1 if curr_l1 else curr_l2
#         prev = curr_remaining
#         while curr_remaining and carry != 0:
#             curr_remaining.val += carry
#             carry = curr_remaining.val // 10
#             curr_remaining.val %= 10

#             prev = curr_remaining
#             curr_remaining = curr_remaining.next
#         if carry != 0: # We are guaranteed true if.o.f above loop ends due to end of list ptr
#             prev.next = ListNode(carry)

#         return res

# My Optimized Solution - O(n) time, O(1) memory, >94.07% time, >93.18% memory
# All I had to do was instead of parallel processing then individual processing that was so
# tough with the first attempt, just rewire the next pointer to the lower list.
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        if not l1:
            return l2
        carry = 0
        curr_l1, curr_l2 = l1, l2
        while curr_l1:
            addend = 0
            if curr_l2:
                addend = curr_l2.val
                curr_l2 = curr_l2.next
            curr_l1.val += addend + carry
            carry = curr_l1.val // 10
            curr_l1.val %= 10

            if not curr_l1.next:
                if curr_l2:
                    curr_l1.next = curr_l2
                    curr_l2 = None
                elif carry != 0:
                    curr_l1.next = ListNode(carry)
                    curr_l1 = curr_l1.next

            curr_l1 = curr_l1.next
        return l1

# NeetCode Solution, O(n) time, O(n) memory.
# His is much easier to understand, it's a lot more readable than mine, because he created
# an entirely new list without changing the original lists at all. Of course since he creates
# new memory and it's a simpler structure to follow (if-else max depth of 1 in the while loop),
# his solution beats 4% more of solutions, but memory-wise only beats 31.15.
class NeetCodeSolution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            # update ptrs
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

l1, l2 = ListNode(), ListNode()
l1.build_from_list([2, 3, 3, 9])
l2.build_from_list([5, 6, 7])

print(Solution().addTwoNumbers(l1, l2))
