from collections import deque
import heapq
from typing import Counter, List

# NeetCode Solution
# prioritize higher counts (it's more optimized) with a heap
# keep track of timing with a queue (natural for timekeeping)

# **PRIORITY = HEAP, TIME = QUEUE**
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()  # pairs of [-cnt, idleTime]
        while maxHeap or q:
            time += 1

            if not maxHeap:     # no need to keep looping, next time where we 
                time = q[0][1]  # do something is at front of queue
            else:
                cnt = 1 + heapq.heappop(maxHeap) # complete one task
                if cnt:
                    q.append([cnt, time + n])  # next cycle we can process next
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])  # ^counts on heap
        return time

