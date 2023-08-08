from ListNode import ListNode

# TOTAL TIME: 31m, 7s
# My Original Solution - O(n) time, O(1) memory
# Took some time to get right, but that's okay. It was very fun to work on. I'm happy to be
# getting into the habit of trying to get the most optimal solution. The moment I read the challenge
# of "Can you do it in O(1) memory?", I instantly went for it. This technique of having 2 different
# "acccess velocities" and doing processing based on that (first encountered in 143. Medium - 
# Reorder List.py) is so clever, I can't stop obsessing over it.
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head.next if head else None
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False

# NeetCode Solution - O(n) time, O(1) memory
# His solution is ever so slightly cleaner with the first statement. It accounts
# for a |None| type passed in by setting the |fast| ptr to the start as well.
# Then next setting is done first to avoid activation of the True return condition.

class NeetCodeSolution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
