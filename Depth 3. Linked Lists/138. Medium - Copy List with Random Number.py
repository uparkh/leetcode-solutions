from typing import Optional

# TOTAL TIME: 00:35:11

# Because the nodes in this problem are unique in that they have this random pointer,
# I'm not really going to be able to test solutions in-house, I don't really feel like designing
# this new type of list. Just gonna use their basic class.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# Notes:
# - The fundamental challenge here is that we are making a deep copy of the list.
#   We just have to be careful there's no mixing of pointer references to the first list.

# My Original Solution - O(n) time, O(n) memory
# Pretty confident in this one, beat 96.55% time, beat 72.82% memory
class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        # Initially a dummy node
        res = Node(0)
        # Matches nodes by index
        iHeadToRes = {}

        curr = head
        currRes = res
        while curr:
            currRes.next = Node(curr.val)
            currRes = currRes.next
            iHeadToRes[curr] = currRes
            curr = curr.next

        # Remove dummy node
        res = res.next

        curr = head
        currRes = res
        while curr:
            currRes.random = iHeadToRes.get(curr.random, None)
            curr = curr.next
            currRes = currRes.next

        return res

# Neetcode Solution - O(n) time, O(n) memory
# Pretty much the exact same solution as mine fundamentally. Makes memory micro-optimizations
# on fewer variables (no |res|) and no dummy node. Because the copied list is stored
# in the values of the hash-map, we don't need to keep track of the copied list's head reference.
# Will say, this is so much easier and more pleasant to read.

# Although after running this through LeetCode, it seems that though it's more memory-efficient,
# my solution is faster, I'm assuming this is because the hash-map GET is called 4 times for each
# element. This must be a slightly slower action for the computer to do, because I only call
# my hash-map GET once -- just for wiring the |random| connections on the copy. 

class Solution:
    def copyRandomList(self, head: "Node") -> "Node":
        oldToCopy = {None: None}

        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        return oldToCopy[head]

