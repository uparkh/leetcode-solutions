import heapq
from collections import defaultdict
from typing import List


# My Original Incorrect Solution -- 40 minutes
# I was almost there. I had the correct idea in using Dijkstra's algo, with the weights
# being the relative lexical ordering, I even got the right ordering, just some duplicates
# for the second test case, but couldn't quite do it.
# Feel much better about putting myself through the time pressure now.
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(set)
        for src, dst in tickets:
            adj[src].add(dst)

        M = len(tickets)
        min_heap = []  # (dst, src)
        res = []  # final length == M + 1
        for rdst in list(adj['JFK']):  # root
            heapq.heappush(min_heap, (rdst, 'JFK'))
            adj['JFK'].remove(rdst)
        adj.pop('JFK')

        # consume all edges -- given that valid itin exists
        while min_heap:
            print(adj, min_heap)
            dst, src = heapq.heappop(min_heap)
            # if res[-1] != src:
            res.append(src)
            if dst not in adj:  # last iter
                res.append(dst)
                continue
            for dst2 in list(adj[dst]):
                heapq.heappush(min_heap, (dst2, dst))
                adj[dst].remove(dst2)
            if not adj[dst]:
                print(f'popped {dst}')
                adj.pop(dst)
        return res


# NeetCode Solution
# O(E ** d) where E is the number of edges and d is the number of destinations
# O(E) space
class NeetCodeSolution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {src: [] for src, dst in tickets}
        res = []

        for src, dst in tickets:
            adj[src].append(dst)

        # ensures that destinations for any given src is in lexical order
        for key in adj:
            adj[key].sort()

        def dfs(adj, result, src):
            # for case ['A', 'B'], ['B', 'A'], ['A', 'C'], doesn't matter if B chosen first
            # or C chosen first from A, C will always end up being the first in `res`
            if src in adj:
                # include all destinations for src
                destinations = adj[src][:]
                while destinations:
                    # select new dest
                    dest = destinations[0]
                    adj[src].pop(0)
                    dfs(adj, res, dest)
                    # explored this dest, move onto more in the list
                    destinations = adj[src][:]

            # postorder traversal action -- add src to result
            res.append(src)

        dfs(adj, res, "JFK")
        res.reverse()

        if len(res) != len(tickets) + 1:
            return []

        return res

