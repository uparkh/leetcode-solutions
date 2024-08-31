from ListNode import ListNode
# TOTAL TIME: Unknown
# It works, but like I anticipated, it is EXTREMELY slow, with an O(k^2 * n) complexity.
# Only beats 7.96% of solutions runtime-wise.
# I am thinking now that a radix sort kind of thing could be better? Bucket-ing them sounds like
# a good idea.

class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        dummy = ListNode()
        done = False
        cur = dummy
        while not done:
            done = True
            min_i = -1
            minimum = float("inf")
            for i, head in enumerate(lists):
                if head:
                    done = False
                    if head.val < minimum:
                        minimum = head.val
                        min_i = i
            if not done:
                cur.next = ListNode(minimum)
                lists[min_i] = lists[min_i].next
                cur = cur.next
        return dummy.next

# NeetCode Solution
# Check the associated .png to see the visualization.
# Basically, you just use merge sort on any given "level" of the outer array, and then
# advance the whole level by one, run merge sort on that, then merge all component lists.
# Merging 2 sorted lists into a single list is done in the problem
# 21. Easy - Merge Two Sorted Lists
# It's so obvious now! Maybe I should have tried to look at extending that pattern, and may have
# come upon this two-by-two merging algorithm by myself.
# O(n log k)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class NeetCodeSolution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists
        return lists[0]

    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next


# Another solution involved Heap/Priority Queue, a solution that I was thinking about in the
# shower, pretty much exactly how I imagined it. Just have have a heapqueue of the lists,
# and keep reheaping once the minimum has been popped, pushing the next in that list as a
# key/priority. The linked lists in this problem can kinda be thought of as a stack of cards.
# This is quite clever, I like NeetCode's solution too, but this one is just a bit more clever
# to me, thought it does, as expected, have worse memory usage becuase of the heap.
# NeetCode's is a well-rounded solution, with runtime and memory optimized as much as possible.
from typing import List, Optional
import heapq
class HeapQueueSolution():
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        res = ListNode()
        cur = res
        for i, h in enumerate(lists):
            if h:
                heapq.heappush(heap, (h.val, i))
        while heap:
            val, i = heapq.heappop(heap)
            node = lists[i]
            cur.next = node
            cur = node
            if node.next:
                heapq.heappush(heap, (node.next.val, i))
                lists[i] = node.next
        return res.next
