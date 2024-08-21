# My Original Solution -- 12 minutes
# Direct application of immediately learning Dijkstra's
# Time -- O(E * log(V))
# Space -- O(V * E)
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((w, v))
            
        min_heap = [(0, k)]
        travel_times = {}

        while min_heap:
            w1, n1 = heapq.heappop(min_heap)
            if n1 in travel_times:
                continue
            travel_times[n1] = w1
            for w2, n2 in adj[n1]:
                if n2 not in travel_times:
                    heapq.heappush(min_heap, (w1 + w2, n2))
        
        return max(travel_times.values()) if len(travel_times) == n else -1

# NeetCode Solution
# Clever small optimization, min heap guarantees finding the max
# travel time, can just track this info in another variable.
class NeetCodeSolution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        minHeap = [(0, k)]
        visit = set()
        t = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = w1

            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))
        return t if len(visit) == n else -1

        # O(E * logV)


